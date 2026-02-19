![The string() Command](68k_string/string.png "The string() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts any expression to a string.|string(*expression*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press D to enter the String submenu.
- Press 1 to select string(.
       
# The string() Command

The string() command converts any expression to its string form. This applies to numbers, but also to lists, matrices, symbolic expressions, and equations. The result depends on all the mode settings that are typically involved with displaying a number: base, exact/approx setting, etc.

```
:string(50)
           "50"
:string({1,2,3,4,5})
           "{1,2,3,4,5}"
:string(1/(1-x))
           "-1/(x-1)"
```

The main use of string() is with output commands like [68k:PtText](68k:pttext.html), [68k:PxlText](68k:pxltext.html), [68k:Text](68k:text.html), [68k:Title](68k:title.html), etc. These commands only work with strings, so for any other data type, you'll have to use string() first — [&](68k:append.html) will also come in handy. For example:

```
:Text "The value of x is: "&string(x)
```

If you're just converting numbers, you might also want to look into [68k:format()](68k:format().html), which only applies to numbers and also puts them in a specific form.

## Advanced Uses

Together with the # ([68k:indirection](68k:indirection.html)) operator, string() can be used to access variables like a1, a2, a3, ..., in order:
```
:#("a"&string(n))
```

## Related Commands

- [68k:expr()](68k:expr().html)
- [68k:format()](68k:format().html)
- [68k:char()](68k:char().html)
