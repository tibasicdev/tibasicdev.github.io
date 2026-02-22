![The mid() Command](68k_mid/mid.png "The mid() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Selects a substring from a string, or a sublist from a list.|mid(*string-or-list*,*start*[,*count*])|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press D to enter the String submenu.
- Press 5 to paste mid(.
       
# The mid() Command

The mid() command can be used in two ways: to select a sublist from a list, or a substring from a string. In both cases, the syntax is similar:
- the first argument is the list or string to start with.
- the second argument is the number of the first element or character to include, 
- the third argument is how long the sublist or substring should be.

That is, mid(*list*,*x*,*y*) will give a list of the *x*<sup>th</sup> element, (*x*+1)<sup>th</sup> element, and so on up to the (*x*+*y*-1)<sup>th</sup> element of *list*. If *x*=2 and *y*=3, this will give a 3-element list starting from the 2<sup>nd</sup> element.
```
:mid({1,2,3,4,5},2,3)
	{2 3 4}
```
For strings, mid(*string*,*x*,*y*) will give a *y*-character-long string starting from the *x*<sup>th</sup> character of *string*:
```
:mid("TI-Basic",2,5)
	"I-Bas"
```

In practice, the mid() command is rarely useful for lists, although it might occasionally come in handy. It really shines with strings, since there is no other way to select a character from within a string. Whereas you might use list[5] to select the 5<sup>th</sup> element of a list, with a string you have to write mid(string,5,1) to get that single character.

A noteworthy feature of mid() is that out-of-bounds indices don't cause an error. If the length you give for the substring or sublist is more than the number of remaining characters or elements, then it will give you as many as there are, instead. If the value of *start*  happens to be past the end, then the output will be a null value: the empty list {} for a list, and the empty string "" for a string.

## Optimization

The third argument — the length of the sublist or substring — is optional if you want to include everything past the first element or character. For example:
```
:mid({1,2,3,4,5},3)
	{3 4 5}
:mid("TI-Basic",4)
	"Basic"
```
In this case, the result is the same as the result of [68k:right()](68k:right.html), but the input is different.

Furthermore, if you're always going to start at the beginning of the string, [68k:left()](68k:left.html) is a better alternative to mid(): left(var,x) is equivalent to mid(var,1,x), and saves you a total of 3 bytes.
```
:mid(str,1,5)
	can be
:left(str,5)
```

## Error Conditions

**[260 - Domain error](68k:errors.html#e260)** happens when *start* isn't positive, or *count* is negative.

## Related Commands

- [68k:left()](68k:left.html)
- [68k:right()](68k:right.html)
- [68k:inString()](68k:instring.html)
