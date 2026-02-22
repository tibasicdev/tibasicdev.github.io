# adapted from https://github.com/IlyaOvodov/wikidot2markdown


import inspect
import json
import re
import requests
import shutil
import time
import uuid

from bs4 import BeautifulSoup
from pathlib import Path


OLD_DOMAIN = "tibasicdev.wikidot.com"
NEW_DOMAIN = "tibasicdev.github.io"
EXT = ".html"


ANCHOR = r"\[\[# +(.*?)\]\]"
URL    = r"\b((?:https?://|www\d{0,3}\.|[\w.\-]+\.[a-z]{2,4}/)[^\s()<>]+[^\s`!()\[\]{};:'\".,<>?])(#\w+)?"
UUID   = r"[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}"


BLOCKS = {}
def Block(match: re.Match) -> str:
    block_id = str(uuid.uuid4())
    BLOCKS[block_id] = match[1]
    return match[0].replace(match[1], block_id)


FOOTNOTES = []
def Footnote(match: re.Match) -> str:
    FOOTNOTES.append(match[1])
    return f"[^{len(FOOTNOTES)}]"


def unixify(url: str):
    # IDK what Wikidot actually does or what "unixify" even means but this is a pretty good guess
    return re.sub(r"[^\w.\-:/?()#]+", "-", url.lower()).rstrip("()")


def InternalLink(match: re.Match) -> str:
    page = unixify(match['page'])
    return f"[{match['text'] or match['page']}]({page}{EXT}{'#' + match['anchor'] if match['anchor'] else ''})"


def ExternalLink(match: re.Match) -> str:
    page = unixify(match['page'])
    match match.groupdict().get("interwiki"):
        case "dictionary":
            url = f"https://www.dictionary.com/browse/{page}"

        case "google":
            url = f"https://www.google.com/search?q={page}"

        case "wikipedia":
            url = f"https://en.wikipedia.org/wiki/{page}"

        case _:
            url = page

    return f"[{match['text'] or match['page']}]({url})"


def Image(match: re.Match) -> str:
    attributes = dict(re.findall(r'(?s)(\w+)="(.*?)"\s+', match["attributes"])) if match["attributes"] else {}

    return f'![{attributes.get("alt", match["source"])}]({match["source"]} "{attributes.get("title", "")}")'


class Header:
    def __init__(self, template: str, headings: dict[str, dict[str, str]]):
        self.template = inspect.cleandoc(template)
        self.headings = headings

    def format(self, **kwargs):
        header = sep = row = "|"
        for heading, names in self.headings.items():
            for name, string in names.items():
                if (value := kwargs.get(name, "").replace("@@", "")):
                    header += f"{heading}|"
                    sep += "--- |"
                    row += f"{string.format(**{name: value})}|".replace("\n", "<br>")
                    break    

        return self.template.format(**{"$header": header, "$sep": sep, "$row": row}, **kwargs)


class Converter:
    conversions = {
        # Modules
        rf'\[\[module Redirect destination="{URL}".*?\]\]':
        r'<!DOCTYPE html>\n<meta http-equiv="refresh" content="0; URL=\1">\n<link rel="canonical" href="\1">',

        # Links
        rf'\[\[\[\*?(?P<page>{URL})(?:\s*\|\s*(?P<text>.*?))?\]\]\]': ExternalLink,
        r'\[\[\[\*?(?P<page>.*?)(?:#(?P<anchor>.+?))?(?:\s*\|\s*(?P<text>.*?))?\]\]\]': InternalLink,

        rf'(?s)\[\[a href="(?P<page>{URL})"\]\](?P<text>.*?)\[\[/a\]\]': ExternalLink,

        rf'\[\*?(?P<interwiki>dictionary|google|wikipedia):(?P<page>.*?)(\s+(?P<text>.*?))?\]': ExternalLink,
        rf'\[\*?(?P<page>{URL})(?:\s+(?P<text>.*?))?\]': ExternalLink,

        # Blocks
        r'(?s)^\[\[code(?: +type="(?:[\S]+)")?\]\](.*?)\[\[/code\]\]\s*?$': Block,  # block code
        r'(?s)^\[\[math(?: *\w*)\]\](.*?)^\[\[/math\]\]\s*?$': Block,  # block math
        rf'\[.*?\]\(({URL})\)': Block,  # links
        r'@@(.*?)@@': Block, # unparsed text

        # Discarded tags
        r'(?s)[<\[]!--.*?--[>\]]': r'',  # comments
        r'_$': r'',  # line continuation

        r'(?s)\[\[div .*?\]\](.*?)\[\[/div\]\]': r'\1',  # divs

        # Formatting
        r'~~|(?<!-)--(?!-)': r'—',  # em dash ~~ -> —
        r'(?<=[^:])//(.*?\S.*?)//': r'*\1*',  # italics
        r'__(.*?\w.*?)__': r'<u>\1</u>',  # underlining
        r'(?<!-)--(.*?\w.*?)--(?!-)': r'~~\1~~',  # strikeout
        r'{{(.*?\S.*?)}}': r'`\1`',  # monospace
        rf'`\[(.*?)\]\((.*?)\)`': r'[`\1`](\2)', # monospaced links
        r'\^\^(.*?\S.*?)\^\^': r'<sup>\1</sup>',  # superscript
        r',,(.*?\S.*?),,': r'<sub>\1</sub>',  # subscript

        # Lists
        r'^(\s)*\*\s': r'\1- ',  # unordered lists
        r'^(\s)*#\s': r'\g<1>1. ',  # ordered lists (spec abuse)

        # Headings
        r'^!\+': "#",
        rf'(?:{ANCHOR}\s*)?^\+ (.*?\S.*?)(?: *{ANCHOR})?$': r"## \2 {#\1\3}",
        rf'(?:{ANCHOR}\s*)?^\+\+ (.*?\S.*?)(?: *{ANCHOR})?$': r"### \2 {#\1\3}",
        rf'(?:{ANCHOR}\s*)?^\+\+\+ (.*?\S.*?)(?: *{ANCHOR})?$': r"#### \2 {#\1\3}",
        r' ?\{#\}': r'',

        rf' *{ANCHOR} *': r'',
        r'\[#(.+?)(?:\s+(.*?))?\]': r'[\2](#\1)',

        # Collapsibles
        r'\[\[collapsible.*?\]\]': r'<details style="display: inline;"><summary>show</summary>',
        r'\[\[/collapsible\]\]': r'</details>',

        # Code
        rf'^\[\[code(?: +type="(\S+)")?\]\]({UUID})\[\[/code\]\]\s*?$': r'```\1\n\2\n```',
        rf'^\[\[include inc:prgm-code\s*\|\s*code\s*=({UUID})\]\]\s*?$': r'```\1\n```',

        # Math
        r'\[\[\$\s*([\S\t ]*?)\s*\$\]\]': r'$\1$',  # inline math [[$ ... $]] -> $...$
        rf'^\[\[math\]\]({UUID})\[\[/math\]\]\s*?$': r'$$\1$$',  # block math
        rf'(?s)^\[\[include inc:math\s*(?:\|eqn\s*=\s*)?({UUID})\]\]': r'$$\1$$', # include math

        # Tables
        r'\|\|(\|)?': lambda match: "|" + (" |" if match[1] else ""),
        r'^\s*\|~.*?$': lambda match: match[0].replace("~", "") + "\n" + "| --- " * (match[0].count("|") - 1) + "|",
        r'\[\[/?(table|cell|row).*?\]\]': r'', # just flatten 'em

        # Images
        r'\[\[(?:=|<|>|f<|f>)?image\s+(?P<source>.*?)(?P<attributes>(\s+\w+=".*?")+)?\]\]': Image,

        # Footnotes
        r'\[\[footnote\]\]\s*(.*?)\s*\[\[/footnote\]\]': Footnote,
    }

    includes = {
        "68k-command":
            Header("""![{$title}]({$filename}/{$picture} "{$title}")
                   
            {$header}
            {$sep}
            {$row}
                   
            ++ Menu Location
            {$location}
                   
            !+ {$title}
            """,
            {
                "Command Summary": {"$summary": "{$summary}"},
                "Command Syntax": {"$syntax": "{$syntax}"},
                f"[Calculator Compatibility](68k:cross-compatibility{EXT})": {
                    "$ams2xx": "This command requires a calculator with AMS version 2.{$ams2xx} or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)",
                    "$ams3xx": "This command requires a TI-89 Titanium or Voyage 200 calculator with AMS version 3.{$ams3xx} or higher.",
                    "$flashrom": "This command requires a calculator with Flash memory (that is, it will not work on a TI-92).",
                    "default": "This command works on all calculators."
                    },
                f"[Token Size](6k:tokenization{EXT})": {"$size": "{$size}"}
            }),

        "68k-error":
            "**[[[68k:errors#e{$num}|{$num} - {$error}]]]** happens when {$cause}.",

        "cid":
            inspect.cleandoc("""
            |This article is currently in development. You can help TI-Basic Developer by expanding it. {$extra}|
            | --- |
            """),

        "command":
            Header("""![{$title}]({$filename}/{$picture} "{$title}")
                       
            {$header}
            {$sep}
            {$row}

            ++ Menu Location
            {$location}
                   
            !+ {$title}
            """,
            {
                "Command Summary": {"$summary": "{$summary}"},
                "Command Syntax": {"$syntax": "{$syntax}"},
                f"[Calculator Compatibility](compatibility{EXT})": {"$compatibility": "{$compatibility}"},
                f"[Token Size](tokens{EXT})": {"$size": "{$size}"}
            }),

        "development":
            inspect.cleandoc("""
            |**This article is part of the {$stage} stage of the [development](development%s) cycle.**|
            | --- |
            """ % EXT),

        "math":
            "$$ {$eqn} $$",

        "next-prev":
            inspect.cleandoc("""
            <center>

            |**[<< {$prevtitle}]({$prevpage}%s)**|**[{$toctitle}]({$tocpage}%s)**|**[{$nexttitle} >>]({$nextpage}%s)**|
            | --- | --- | --- |

            </center>
            """ % (EXT, EXT, EXT)),

        "nspire-command":
            Header("""![{$title}]({$filename}/{$picture} "{$title}")
                       
            {$header}
            {$sep}
            {$row}

            ++ Menu Location
            {$location}
            
            !+ {$title}
            """,
            {
                "Command Summary": {"$summary": "{$summary}"},
                "Command Syntax": {"$syntax": "{$syntax}"},
                f"[Calculator Compatibility](compatibility{EXT})": {"$compatibility": "{$compatibility}"},
            }),

        "prgm-code":
            inspect.cleandoc("""
            ```
            {$code}
            ```
            """),

        "routine":
            Header("""
            {$header}
            {$sep}
            {$row}
            """,
            {
                "Routine Summary": {"$summary": "{$summary}"},
                "Inputs": {"$input": "{$input}"},
                "Outputs": {"$output": "{$output}"},
                "Variables Used": {"$variable": "{$variable}",
                                   "$variables": "{$variables}",
                                   "$variables used": "{$variables used}"},
                "Author": {"$author": "{$author}"},
                "Authors": {"$authors": "{$authors}"},
                "Download": {"$download": "{$download}", "$url": "{$url}"}
            }),

        "stub":
            inspect.cleandoc("""
            |This article is a stub. You can help TI-Basic Developer by expanding it.|
            | --- |
            """),

        "unfinished":
            inspect.cleandoc("""
            |This article is under construction and needs to be completed. You can help by expanding it.|
            | --- |
            """),
    }

    def convert_include(self, filename: str, title: str):
        def inner(match: re.Match) -> str:
            name = match[1]
            entries = {"$" + key.strip(): value[0].strip()
                       for key, *value in map(lambda s: s.split("=", maxsplit=1), (match[2] or "").split("|")) if value}

            return self.includes[name].format(default="DEFAULT",
                                                               **({"$location": "N/A\n"} | entries),
                                                               **{"$filename": filename, "$title": title})

        return inner

    def table_of_contents(self, page: str):
        def inner(match: re.Match) -> str:
            return "\n".join((len(depth) - 2) * "\t" + f"- [{anchor or heading}](#{unixify(heading)})"
                             for depth, heading, anchor in re.findall(r"^(##+) (.*?) (\{#.*?\})?$", page,
                                                                      flags=re.MULTILINE))

        return inner


    def convert(self, page: str, filename: str, title: str):
        BLOCKS.clear()
        FOOTNOTES.clear()

        # Convert include boxes
        page = re.sub(r"(?s)\[\[include inc:([^\s\]]+)\s*(?:\|?(.*?))?\n*\]\]\s*?$",
                      self.convert_include(filename, title),
                      page,
                      flags=re.MULTILINE)

        # Convert everything else
        for pattern, repl in self.conversions.items():
            page = re.sub(re.compile(pattern, flags=re.MULTILINE), repl, page)

        # Add footnotes
        for index, footnote in enumerate(FOOTNOTES):
            page += f"\n[^{index + 1}]: {footnote.replace('\n', '\n\t')}"

        # Replace blocks
        for block_id, block in BLOCKS.items():
            page = page.replace(block_id, block.rstrip().lstrip("\n"))

        # Fix ordered lists
        for n in range(1, 100):
            page = re.sub(rf"^(\s*{n}\. .*?\s+)^(\s*)\d+\. ",
                          lambda match: f"{match[1]}{match[2]}{n + 1}. ",
                          page,
                          flags=re.MULTILINE)

        # Table of contents
        page = re.sub(r"\[\[toc\]\]", self.table_of_contents(page), page)

        # Leftovers
        page = page.replace("@@", "")
        page, n = re.subn(r"(?s)\[\[([a-z]+)\s+.*?\]\]", lambda m: print(f"Found {m[1]} in {filename}") or "", page)

        page = re.sub(r"\n{4,}", r"\n\n\n", page)

        if n >= 5:
            raise KeyError("too many tags")

        return page.replace(OLD_DOMAIN, NEW_DOMAIN)
    

with open("titles.json", "r+", encoding="utf8") as file:
    TITLES = json.load(file)
    

def fetch_title(filename: str):
    if filename in TITLES:
        return TITLES[filename]

    time.sleep(0.5)
    response = requests.get(f"http://{OLD_DOMAIN}/{filename.replace('_', ':')}")

    match response.status_code:
        case 200:
            pass

        case 404:
            print(f"{filename}: Not Found")

        case code:
            print(f"{filename}:", code)
            raise requests.HTTPError

    tag = BeautifulSoup(response.content, "html.parser").find("title")
    TITLES[filename] = title = tag.text.removesuffix(" - TI-Basic Developer") if tag else ""

    with open("titles.json", "w+", encoding="utf8") as file:
        json.dump(TITLES, file, ensure_ascii=False, indent=4)

    return title
    

INCLUDE_PREFIXES = [
    "",
    "68k",
    "asm",
    "nspire",
    "sk"
]

EXCLUDE_FILES = [
    "did-you-know",

    "68k:did-you-know",
    "add-news",
    "all-did-you-know",
    "archives",
    "dyk",
    "empty-page",
    "live-chat",
    "mstram1",
    "nav",
    "noahbaby94",
    "number-of-pages",
    "pages",
    "pages-3",
    "pages-not-command-tag",
    "to-do",
    "upload",
    "uploading-help"
]


if __name__ == "__main__":
    converter = Converter()
    for file in Path("2025-08-01/source").glob("*.txt"):
        filename = file.stem
        prefix, name = filename.split("_", maxsplit=1) if "_" in filename else ("", filename)

        # Fetch title
        title = fetch_title(filename)

        # Convert (some) pages
        if prefix not in INCLUDE_PREFIXES or filename.startswith("_"):
            continue

        if any(filename.startswith(start) for start in ["admin", "member", "sandbox", "test"]):
            continue

        if filename.startswith("chat") and filename != "chatbot":
            continue

        if filename in EXCLUDE_FILES:
            continue

        try:
            text = converter.convert(file.read_text(encoding="utf8"), filename, title).strip()

        # These must not be files we care about
        except KeyError as e:
            print(f"Skipped {filename}: {e.args}")
            continue

        if not text:
            print(f"Skipped {filename}: empty")
            continue

        # Write converted sources
        out = Path(f"docs/{filename}.md")
        out.parent.mkdir(parents=True, exist_ok=True)

        with open(out, "w+", encoding="utf8") as outfile:
            # Ensure title
            if not re.search("^# .", text, flags=re.MULTILINE):
                text = f"# {title}\n" + text

            outfile.write(text + "\n")
            print(f"Wrote {filename}")

        # Copy attached files
        attachments = out.parent / out.stem
        attachments.mkdir(parents=True, exist_ok=True)
        for attachment in Path(f"2025-08-01/files/{filename}").glob("*"):
            shutil.copy(attachment, attachments)

    print()

    # Compile DYKs
    dyks = '# "Did You Know..." Archive\n\n### Did you know...\n'
    for dyk in Path(f"2025-08-01/source").glob("dyk_*.txt"):
        text = converter.convert(dyk.read_text(encoding="utf8"), "", "")
        dyks += f"- {text}\n"

    with open(Path("docs/did-you-know.md"), "w+", encoding="utf8") as outfile:
        outfile.write(dyks)
        print("Wrote DYKs")
