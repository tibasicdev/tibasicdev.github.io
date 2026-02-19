![The ord() Command](68k_ord/ord.png "The ord() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Gives the ASCII code of a character.|ord(*string*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press D to enter the string submenu.
- Press B to select ord(.
       
# The ord() Command

The ord() command gives the ASCII code of a character (that is, its [character code](68k:character-codes.html), which is a modification of standard ASCII). The input is meant to be a single character, but the command doesn't actually check for that — so in practice, it gives the ASCII code of the first character in a string. You can convert multiple characters at once by giving ord() a list (or matrix) of characters.

The inverse of ord() is [68k:char()](68k:char().html), which converts a character code to a character.

```
:ord("America")
           65
:ord({"A","b","c"})
           {65  98  99}
:ord("")
           0
```

## Optimization

Code such as
```
:inString("ABCDEFGHIJKLMNOPQRSTUVWXYZ",str)
```
should be replaced by appropriate use of ord(); in this case,
```
:ord(str)-64
```

## Related Commands

- [68k:char()](68k:char().html)

## See Also

- [68k:character-codes](68k:character-codes.html)
