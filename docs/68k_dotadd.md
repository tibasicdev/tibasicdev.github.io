![The .+ Command](68k_dotadd/dotadd.png "The .+ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Adds two values, using element-by-element addition when adding a matrix and a number.|*value1* .+ *value2*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.<br>* Press 4 to enter the Matrix submenu.<br>* Press K to enter the Element ops submenu.<br>* Press 1 to select .+.<br>...frankly, just typing it is way easier.
# The .+ Command

The .+ command works like plain [+](68k:add.html) in most cases, adding two values together. It's distinguished by its application to matrices: in particular, when adding a matrix and a scalar. Normal addition of a matrix and a single value will add that value along the main diagonal only: as though the value were multiplied by the identity matrix. However, .+ does the more intuitive thing (for anyone but an algebraist, anyway) and adds the value to every element of the matrix.

```
:[a,b;c,d]+x
        [x+a  b  ]
        [c    x+d]
:[a,b;c,d].+x
        [x+a  x+b]
        [x+c  x+d]
```

It doesn't really make much sense to use .+ to add other kinds of values, but you can do it if you like.

Although the order of the matrix and the scalar doesn't matter, be warned that in some cases, the . will be interpreted as a decimal point. You can put spaces to help the calculator figure out what you mean.
```
:5.+[a,b;c,d]
        [a+5.  b   ]
        [c     d+5.]
:5 .+ [a,b;c,d]
        [a+5  b+5]
        [c+5  d+5]
```

## Related Commands

- [+](68k:add.html) (add)
- [.-](68k:dotsubtract.html)
