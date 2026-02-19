![The ▶Rad Command](68k_rad/rad.png "The ▶Rad Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Converts an angle measure to radians, if necessary.|*angle*▶Rad|This command requires a TI-89 Titanium or Voyage 200 calculator with AMS version 3.00 or higher.|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 2 to enter the Angle submenu.
- Press B to select ▶Rad.
       
# The ▶Rad Command

The ▶Rad command is used to convert both degrees and gradians into radians. (If the command is given a value in radians it returns that value unchanged).

If you do not specify what unit you want to be used (using either the [r command](68k:radian.html), the [° command](68k:degree.html), or the [G command](68k:gradian.html)), whatever default the calculator's mode is set to will be used. Here are some examples:

```
:setMode("ANGLE", "DEGREE")
:90▶Rad
           1
:90^r▶Rad
           90
```

It appears to be equivalent to the <sup>[r](68k:radian.html)</sup> command, but only on the TI-89 Titanium or Voyage 200.

## Related Commands

- [▶Deg](68k:deg.html)
- [▶Grad](68k:grad.html)
- <sup>[r](68k:radian.html)</sup> (radian)
