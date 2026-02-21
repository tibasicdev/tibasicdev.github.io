![The r Command](68k_radian/radian.png "The r Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts an angle to radians, if necessary.|*angle* <sup>r</sup>|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 2 to enter the Angle submenu.
- Press 2 to select <sup>r</sup>.
       
# The r Command



The <sup>r</sup> symbol used after an angle makes sure the angle is interpreted as being in radians. If the calculator is already in radian mode, x<sup>r</sup> is equal to x; in degree mode, x<sup>r</sup> is equal to 180*x/π; and in gradian mode, x<sup>r</sup> is equal to 200*x/π.

If you're using radian angle measures extensively in a program, it's a better idea to use [68k:setMode()](68k:setmode.html) to switch to radian mode and not worry about this. However, there are two reasons you might want to use <sup>r</sup>:
- If you need an angle in radians only once or twice, don't bother changing the mode setting.
- In a function, you're forced to use <sup>r</sup>, since setMode() isn't valid in a function. 

Make sure to use parentheses around an expression like (π/3)<sup>r</sup>, since π/3<sup>r</sup> will be interpreted as π/(3<sup>r</sup>), and the conversion will be done incorrectly.

In radian mode (no conversion is necessary, so no conversion is done):
```
:sin(π/6)
           1/2
:sin((π/6)^r)
           1/2
:π^r
           π
```

In degree mode:
```
:sin(π/6)
           sin(π/6)
:sin((π/6)^r)
           1/2
:π^r
           180
```

## Related Commands

- [°](68k:degree.html) (degree)
- <sup>[G](68k:gradian.html)</sup> (gradian)
- [68k:▶Rad](68k:-rad.html)
