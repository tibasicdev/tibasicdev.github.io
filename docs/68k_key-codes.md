# Key Codes
This table contains the values returned by [getKey()](68k:getkey.html) for each (keypress, modifier) pair. Unlike the getKey found on TI-83 series calculators, the 68k calculators' getKey() returns keypresses with modifiers. 

On the TI-92, TI-92+, and Voyage 200, the key layout is different. The same effect (e.g. F8) still corresponds to the same value (e.g. 275), but is obtained differently (by pressing F8, in this example, rather than 2nd+F3). The alpha key is replaced by the "grab" button for the arrow keys.

Notice that the key codes for typing a character correspond to that characters [character code](68k:character-codes.html). For example, the key code for typing "A" is 65, and [ord(](68k:ord.html)"A") will also return 65. This even applies to the key codes for the international characters that aren't shown in this table.

| Key | || || || || || || Modifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | || None | || ⇧ (shift) | || 2nd | || ♦  (diamond) | || alpha |
| | Result | Value | Result | Value | Result | Value | Result | Value | Result | Value |
| F1 | F1 | 268 | F1 | 268 | F6 | 273 | Y= | 8460 | F1 | 268 |
| F2 | F2 | 269 | F2 | 269 | F7 | 274 | WINDOW | 8461 | F2 | 269 |
| F3 | F3 | 270 | F3 | 270 | F8 | 275 | GRAPH | 8462 | F3 | 270 |
| F4 | F4 | 271 | F4 | 271 | F4 | 271 | TblSet | 8463 | F4 | 271 |
| F5 | F5 | 272 | F5 | 272 | F5 | 272 | TABLE | 8464 | F5 | 272 |
| ♦ (diamond) | | | copy | 24576 | cut | 12288 | | | | |
| alpha | | | | | a-lock | | | | | |
| ESC | ESC | 264 | ESC | 264 | QUIT | 4360 | PASTE | 8456 | ESC | 264 |
| APPS | APPS | 265 | APPS | 265 | SWITCH | 4361 | | 8457 | APPS | 265 |
| ON[^1] | ON | 267 | | | OFF | | | | | |
| HOME | HOME | 277 | HOME | 277 | CUST | 4373 | HOME | 277 | HOME | 277 |
| MODE | MODE | 266 | MODE | 266 | [▶](68k:convert.html) | 18 | _ | 95 | MODE | 266 |
| CATALOG | CATLG | 278 | CATLG | 278 | ***[i](68k:i.html)*** | 151 | [∞](68k:infinity.html) | 190 | CATLG | 278 |
| ← (backspace) | ← | 257 | ← | 257 | INS | 4353 | DEL | 8449 | ← | 257 |
| CLEAR | CLEAR | 263 | CLEAR | 263 | CLEAR | 263 | | 8455 | CLEAR | 263 |
| X | x | 120 | X | 88 | [ln(](68k:ln.html) | 4184 | *[e](68k:e-value.html)*^( | 8280 | x | 120 |
| Y | y | 121 | Y | 89 | [sin(](68k:sin.html) | 4185 |  [sinֿ¹(](68k:arcsin.html) | 8281 | y | 121 |
| Z | z | 122 | Z | 90 | [cos(](68k:cos.html) | 4186 | [cosֿ¹(](68k:arcsin.html) | 8282 | z | 122 |
| T | t | 116 | T | 84 | [tan(](68k:tan.html) | 4180 | [tanֿ¹(](68k:arctan.html) | 8276 | t | 116 |
| ^ | [^](68k:power.html) | 94 | ^ | 94 | [π](68k:pi.html) | 140 | θ | 136 | ^ | 94 |
| | | | ([with](68k:with.html)) | 124 | F | 70 | [°](68k:degree.html) | 176 | FORMAT | 8316 | f | 102 |
| ( | ( | 40 | B | 66 | { | 123 | | | b | 98 |
| ) | ) | 41 | C | 67 | } | 125 | [©](68k:comment.html) | 169 | c | 99 |
| , | , | 44 | D | 68 | [ | 91 | | 8236 | d | 100 |
| ÷ | [/](68k:divide.html) | 47 | E | 69 | ] | 93 | [!](68k:factorial.html) | 33 | e | 101 |
| × | [*](68k:multiply.html) | 42 | J | 74 | [√(](68k:square-root.html) | 4138 | [&](68k:append.html) | 38 | j | 106 |
| - | [-](68k:subtract.html) | 45 | O | 79 | VAR-LINK | 4141 | contrast + | | o | 111 |
| + | [+](68k:add.html) | 43 | U | 85 | CHAR | 4139 | contrast - | | u | 117 |
| ENTER | ENTER | 13 | ENTER | 13 | ENTRY | 4109 | APPROX | 8205 | ENTER | 13 |
| STO▶ | [→](68k:store.html) | 258 | P | 80 | RCL | 4354 | @ | 64 | p | 112 |
| = | [=](68k:equal.html) | 61 | A | 65 | ' | 39 | [≠](68k:not-equal.html) | 157 | a | 97 |
| EE | [E](68k:e-ten.html) | 149 | K | 75 | [∠](68k:angle-symbol.html) | 159 | SYMB | 8341 | k | 107 |
| (-) | [-](68k:negative.html) | 173 | SPACE | 32 | [ans(1)](68k:ans.html) | 4372 | | 8365 | SPACE | 32 |
| . | . | 46 | W | 87 | [>](68k:greater-than.html) | 62 | [≥](68k:greater-than-or-equal.html) | 158 | w | 119 |
| 0 | 0 | 48 | V | 86 | [<](68k:less-than.html) | 60 | [≤](68k:less-than-or-equal.html) | 156 | v | 118 |
| 1 | 1 | 49 | Q | 81 | " | 34 | | 8241 | q | 113 |
| 2 | 2 | 50 | R | 82 | [\](68k:backslash.html) | 92 | | 8242 | r | 114 |
| 3 | 3 | 51 | S | 83 | UNITS | 4147 | | 8243 | s | 115 |
| 4 | 4 | 52 | L | 76 | : | 58 | | 8244 | l | 108 |
| 5 | 5 | 53 | M | 77 | MATH | 4149 | | 8245 | m | 109 |
| 6 | 6 | 54 | N | 78 | MEM | 4150 | | 8246 | n | 110 |
| 7 | 7 | 55 | G | 71 | [∫(](68k:integral.html) | 4151 | | 8247 | g | 103 |
| 8 | 8 | 56 | H | 72 | *[d(](68k:d.html)* | 4152 | | 8248 | h | 104 |
| 9 | 9 | 57 | I | 73 | ; | 59 | | 8249 | i | 105 |


| Arrow key | || || || Modifier |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | None | ⇧ (shift) | 2nd | ♦  (diamond) | alpha/@ |
| ⇐ (left) | 337 | 16721 | 4433 | 8529 | 33105 |
| ⇑ (up) | 338 | 16722 | 4434 | 8530 | 33106 |
| ⇒ (right) | 340  | 16724 | 4436 | 8532 | 33108 |
| ⇓ (down) | 344 | 16728 | 4440 | 8536 | 33112 |
| ⇖ (left+up) | 339 | 16723 | 4435 | 8531 | 33107 |
| ⇗ (right+up) | 342 | 16726 | 4438 | 8534 | 33110 |
| ⇙ (left+down) | 345 | 16729 | 4441 | 8537 | 33113 |
| ⇘ (right+down) | 348 | 16732 | 4444 | 8540 | 33116 |

An easy way to find the value of a keypress without having to consult this page is to write a short program to output key codes:
```
:Prgm
:Local k
:0→k
:While k=0
:getKey()→k
:EndWhile
:Text string(k)
:EndPrgm
```
[^1]: While ON is technically a key, it can only be caught by assembly programs or through the help of a library. Usually, this key immediately throws a "Break" exception that stops execution of the program.
