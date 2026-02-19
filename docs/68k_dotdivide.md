![The ./ Command](68k_dotdivide/dotdivide.png "The ./ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Divides two values, doing so element-by-element for two matrices.|*value* ./ *value*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press 4 to enter the Matrix submenu.
- Press K to enter the Element ops submenu.
- Press 4 to select ./.
...frankly, just typing it is way easier.
       
# The ./ Command

The ./ operator works just like [/](68k:divide.html) in most cases. The only exception is with matrices. The / command can't do anything with then (except for dividing a matrix by a value), but ./ will just apply the operation element-by-element. Obviously, when this is done for two matrices, their dimensions have to match up.
```
:[a,b;c,d] ./ [e,f;g,h]
           [a/e  b/f]
           [c/g  d/h]
```

When dividing a constant number by a matrix with ./, you may need to space it out so that there's no confusion between ./ and a decimal point.
```
:1./[a,b;c,d]
           Error: Data type
:1 ./ [a,b;c,d]
           [1/a  1/b]
           [1/c  1/d]
```

## Error Conditions



## Related Commands

- [.+](68k:dotadd.html)
- [.-](68k:dotsubtract.html)
- [.*](68k:dotmultiply.html)
- [.^](68k:dotpower.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
