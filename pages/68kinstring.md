![The inString() Command](68k_instring/instring.png "The inString() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Finds a search string in another string.|inString(*string*, *search-string*,[)|This command works on all calculators.|3 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.<br>* Press D to enter the Strings submenu.<br>* Press 6 to select inString(.
# The inString() Command

The inString() command searches for one string inside another, starting from the beginning and going forward. If it finds the string, it returns the position where it finds it. If it doesn't find the string, it returns 0. If the string is there multiple times, it will only find the first one.

Optionally, you can also give inString() a starting position. In that case, it won't find any occurrences of the strings earlier than that position.

```
:inString("Chop shops stock chops.","hops")
           7
:inString("Chop shops stock chops.","hops",8)
           20
:inString("Chop shops stock chops.","stocks")
           0
```

## Related Commands

- [68k:mid(](68k:mid.html)
- [68k:ord(](68k:ord.html)
- [68k:string(](68k:string.html)
