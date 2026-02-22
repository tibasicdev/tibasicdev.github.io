# Text Sprites Reference
## Horizontal Sprites

### Explanation

In order to create a [text sprite](graphics.html), one must have a series of characters and each character returns a certain number of pixels in certain arrangement on the graphscreen. Each character, when displayed on the graphscreen will return certain pixels in its first column of text. For example, if one displayed the letter "J" to the graphscreen it would look like this: (0 = empty pixel, 1 = filled pixel)
```
001
001
001
101
111
```
The first column of text is therefore "00011." The value, 00011b, (in [binary](binandhex.html)) is equivalent to the decimal value 3. Each character, when displayed on the graphscreen will such a number associated with it. Therefore it is easy to organize all the possible text sprites numerically.

You can create rows of text spites this way.  You could then stack these rows up from bottom to top to fill large portions of the screen.  An important thing to remember though, is that vertical text sprites are much faster for larger images.  They can fill the entire screen in just 4 seconds on an 84!

### Chart

This chart contains the best characters to use for each pixel combination when drawing a text sprite:
1. Each is at most three pixels wide (not counting the 1-pixel margin to the left of each character).
2. When possible, they are 1-byte characters, or if not, at least commonly accessible.


| Char. | Binary | Decimal | Char. | Binary | Decimal |
| --- | --- | --- | --- | --- | --- |
| space | 00000b | 0 | ? | 10000b | 16 |
| . | 00001b | 1 | ] | 10001b | 17 |
| ![83lgfont/0Bh_LcrossIcon.gif](83lgfont/0Bh_LcrossIcon.gif "") mark | 00010b | 2 | <sup>2</sup> | 10010b | 18 |
| J | 00011b | 3 | 2 | 10011b | 19 |
| + | 00100b | 4 | <sup>x</sup> | 10100b | 20 |
|  í | 00101b | 5 | $\definecolor{darkgreen}{rgb}{0.90,0.91,0.859}\pagecolor{darkgreen} \overline{\mathrm{x}}$ | 10101b | 21 |
| e | 00110b | 6 | û | 10110b | 22 |
| ![83lgfont/0Ah_LboxIcon.gif](83lgfont/0Ah_LboxIcon.gif "") mark | 00111b | 7 | $\definecolor{darkgreen}{rgb}{0.90,0.91,0.859}\pagecolor{darkgreen} i$ | 10111b | 23 |
| ^ | 01000b | 8 | Y | 11000b | 24 |
| 1 | 01001b | 9 | Î | 11001b | 25|
| : | 01010b | 10 | $\definecolor{darkgreen}{rgb}{0.90,0.91,0.859}\pagecolor{darkgreen} \chi$ | 11010b | 26 |
| *none* | *01011b* | *11* | X | 11011b | 27 |
| º | 01100b | 12 | '  | 11100b | 28 |
| s | 01101b | 13 | ! | 11101b | 29 |
| ( | 01110b | 14 | Q | 11110b | 30 |
| u | 01111b | 15 | [ | 11111b | 31 |

## Vertical Sprites

### Differences with horizontal sprites

The main difference for a vertical sprite is that you need only one [text(](text.html) command to fill an entire horizontal line. It has a noticeable advantage on horizontal sprites when sprites are larger. It is not only faster but you are not limited to a 5x5 sprite or a 7x7 sprite. Also, you don't use a picture variable which can be more convenient in some situations. You don't need to group Pics and your program in order to send it to someone.
In order to draw a sprite, you must draw from bottom to top in order to not erase what is already written. The main disadvantage is that only ∟ , **N** and … don't end with a 0. But it really doesn't matter, because you can make any vertical sprite using only the ., [, and the ∟.  In conclusion, if you need to draw large sprites or even to fill the graphscreen, you should use vertical sprites, otherwise horizontal sprites are for you.

```
:Text(9,1,"1
:Text(8,1,"Δ
:Text(7,1,"Ω
:Text(6,1,"Δ
:Text(5,1," 1
:Text(4,1,"     //5 spaces
```

### Chart

This chart contains characters from 1 to 6 pixels wide. A 0 represents an empty pixel while a 1 is for a black pixel. If you need a character larger than 6 pixels wide, you can search in Weregoose database [here](http://weregoose.unitedti.org/bottomrow/).

| Char. | Binary | Char. | Binary | Char. | Binary | Char. | Binary |
| --- | --- | --- | --- | --- | --- | --- | --- |
| space | 0 | - | 0000 | ![83lgfont/07h_LsqDown.gif](83lgfont/07h_LsqDown.gif "") | 00100 | * | 001000 |
| : | 00 | 4 | 0010 | σ | 01000 | ≠ | 010000 |
| . | 10 | 0 | 0100 | û | 01010 | w | 010100 |
| ` | 000 | { | 0110 | É | 01110 | @ | 011100 |
| ( | 010 | F | 1000 | μ | 10000| m | 100010 |
| ) | 100 | A | 1010 | ñ | 10010 | *n* | 100100 |
| **N** | 101 | } | 1100 | ß | 10100 | <sub>10</sub> | 101110 |
| [ | 110 | 1 | 1110 | È | 11100 | Ω | 110110 |
| ∟ | 111 | ° | 00000 | z | 11110 | $ | 111100 |
| | | | | | | Δ | 111110 |


## Also see
[Text Sprite Finder](http://www.unitedti.org/index.php?download-273) - this program is a compact version of what is on this page, this page simply explains how this program fundamentally works.
[Vertical Sprites Bottom Row](http://weregoose.unitedti.org/bottomrow/) - to have a complete database with the bottom row of all TI-83/84/+/SE characters.
[Graphics](graphics.html) - for information on using text sprites.
[Binary and Hexidecimal](binandhex.html) - to understand how to read the binary format.
[TI-83 Plus Large Font](83lgfont.html) - for clarification on which characters are being referred to.
[CHARS.8xp](archives:chars.html) - A program that contains many otherwise unobtainable characters.
[Text Sprite Generator](https://www.cemetech.net/programs/index.php?mode-file-path-/83plus/basic/media/txtsprt.zip) - A drawing program that outputs the text sprite code to display the sprite.
