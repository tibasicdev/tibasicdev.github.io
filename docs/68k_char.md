![The char() Command](68k_char/char.png "The char() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a character given its ASCII code.|char(*code*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press D to enter the String submenu.
- Press A to paste char(.
       
# The char() Command

The `char()` command converts an integer between 0 and 255 to the corresponding character in the calculator's [internal code](68k:character-codes.html) (which is a modification of ASCII). It can also operate on a list or matrix by converting each of their elements to a character.

This command, and its inverse [`68k:ord()`](68k:ord.html), can be useful for programs that deal with arbitrary strings (which could, potentially, contain any character), but they can come up in other cases as well. For example, since the letters A..Z are consecutive characters in the calculator's internal code, with A being `char(65)`, you can calculate the n<sup>th</sup> letter in the alphabet with the expression  `char(n+64)`.

There are two special values of `char()` to be aware of. The character given by `char(0)` is actually the empty string, which you usually want to avoid using; the character given by `char(13)` is a newline "enter" character, which is replaced by ":" when you type it somewhere. If you actually want to store `char(13)` to a string, you have to use the `char()` command.

## Advanced Uses

TI-Basic does not allow lists to contain picture variables, and in many cases (such as [tilemaps](68k:sprites.html#toc6)) you want to get around this limitation. One way to do so is to name the variables "tile1", "tile2", "tile3", and so on, with only the number changing — then #("tile"&string(n)) gives the n<sup>th</sup> picture variable.

A more efficient way is to assign the pictures numbers in a different range, such as 65-90, and name the variables "tilea", "tileb", "tilec", etc. Then, #("tile"&char(n)), which is faster, converts a number to the corresponding picture variable. This allows for a maximum of 146 different tiles, if you use all the characters that could conceivably be part of a variable name.

## Error Conditions

**[260 - Domain error](68k:errors.html#e260)** happens when the character code isn't in the range 0..255.

## Related Commands

- [`68k:ord()`](68k:ord.html)

## See Also

- [68k:Character Codes](68k:character-codes.html)
