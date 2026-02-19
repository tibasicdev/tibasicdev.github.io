![The .- Command](68k_dotsubtract/dotsubtract.png "The .- Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Subtracts two values, using element-by-element subtraction when subtracting a matrix and a number.|*value1* .- *value2*|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.<br>* Press 4 to enter the Matrix submenu.<br>* Press K to enter the Element ops submenu.<br>* Press 2 to select .-.<br>...frankly, just typing it is way easier.
# The .- Command

The .- command works like plain [-](68k:add.html) in most cases, taking the difference of two values. It's distinguished by its application to matrices: in particular, when subtracting a matrix and a scalar (in either order). Normally, the operation will be done along the main diagonal only: as though the value were multiplied by the identity matrix. However, .- does the more intuitive thing (for anyone but an algebraist, anyway) and subtracts the value from every element of the matrix (or, if the matrix is being subtracted, subtracts every element from the scalar value).

```
:[a,b;c,d]-x
        [-x+a  b   ]
        [c     -x+d]
:[a,b;c,d].-x
        [-x+a  -x+b]
        [-x+c  -x+d]
```

It doesn't really make much sense to use .- to add other kinds of values, but you can do it if you like.

When subtracting a matrix from a constant number, be warned that the . may be interpreted as a decimal point. You can put spaces to help the calculator figure out what you mean.
```
:5.-[a,b;c,d]
        [-a+5.  -b   ]
        [-c     -d+5.]
:5 .+ [a,b;c,d]
        [-a+5  -b+5]
        [-c+5  -d+5]
```

## Related Commands

- [-](68k:subtract.html) (subtract)
- [.+](68k:dotadd.html)
