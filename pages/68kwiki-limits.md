# Wiki Markup Limitations
Unfortunately, the rich vocabulary of wiki syntax doesn't allow to properly display a command in titles and code blocks. When this happens, the offending page will link here so we can properly apologize, clarify what is meant, and give the syntax that displays them correctly where it is possible to do so.

Here are the commands and symbols that suffer from this problem:

- The <sup>[r](68k:radian.html)</sup> command
 - Use ^^r^^ to render it correctly where possible.
 - Use ^^[r](68k:radian.html)^^ to render it in a link.
 - Replace it with ^r in code blocks.
- The <sup>[G](68k:gradian.html)</sup> command
 - Use ^^G^^ to render it correctly where possible.
 - Use ^^[G](68k:gradian.html)^^ to render it in a link.
 - Replace it with ^G in code blocks.
- The *[68k:d](68k:d.html)*[()](68k:d.html) command
 - Use //d//() to render it correctly where possible.
 - Use //[68k:d](68k:d.html)//[()](68k:d.html) to render it in a link.
 - Use [68k:d](68k:d.html)[[/span]][()](68k:d.html) if the above fails to work properly.
 - Replace it with d() in code blocks.
- The [E](68k:e-ten.html)[[/size]] command
 - Use E[[/size]] to render it correctly where possible.
 - Use [E](68k:e-ten.html)[[/size]] to render it in a link.
 - Replace it with E in code blocks.
- The <sup>[T](68k:transpose.html)</sup> command
 - Use ^^T^^ to render it correctly where possible.
 - Use ^^[T](68k:transpose.html)^^ to render it in a link.
 - Replace it with ^T in code blocks.
- The $\bar{x}$ and $\bar{y}$ symbols.
 - Use [[$ \bar{x} $]] to render $\bar{x}$ correctly.
 - Use [[$ \bar{y} $]] to render $\bar{y}$ correctly.
 - Avoid using these in code blocks, or replace with xbar and ybar.

On a related note, there are two operators that don't have any trouble being displayed, but can't be used in a link, so every page that refers to them has to dance around the issue much like this page does in the next sentence. They are: # ([68k:indirection](68k:indirection.html)) and | ([68k:with](68k:with.html)).

## See Also
- The [wiki syntax description](http://www.wikidot.com/doc:wiki-syntax) on www.wikidot.com.
