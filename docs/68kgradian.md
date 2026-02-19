![The G Command](68k_gradian/gradian.png "The G Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts an angle to gradians, if necessary.|*angle* <sup>G</sup>|This command requires a TI-89 Titanium or Voyage 200 calculator with AMS version 3.10 or higher.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.<br>* Press 2 to enter the Angle submenu.<br>* Press C to select <sup>G</sup>.
# The G Command



The <sup>G</sup> symbol used after an angle makes sure the angle is interpreted as being in gradians (an obscure angle measure in which a full circle is equal to 400 gradians); this functionality is present only on TI-89 Titanium or Voyage 200 calculators with AMS version 3.10. If the calculator is already in gradian mode, x<sup>G</sup> is equal to x; in degree mode, x<sup>G</sup> is equal to 9*x/10; and in radian mode, x<sup>G</sup> is equal to π*x/200.

If you're using gradian angle measures extensively in a program, it's a better idea to use [68k:setMode()](68k:setmode().html) to switch to gradian mode and not worry about this. However, there are two reasons you might want to use <sup>G</sup>:
- If you need an angle in gradians only once or twice, don't bother changing the mode setting.
- In a function, you're forced to use <sup>G</sup>, since setMode() isn't valid in a function. 

In gradian mode (no conversion is necessary, so no conversion is done):
```
:cos(100)
           1
:cos(100^G)
           1
:100^G
           100
```

In degree mode:
```
:cos(100)
           cos(100)
:cos(100^G)
           1
:100^G
           90
```

## Related Commands

- [°](68k:degree.html) (degree)
- <sup>[r](68k:radian.html)</sup> (radian)
- [68k:▶Grad](68k:-grad.html)
