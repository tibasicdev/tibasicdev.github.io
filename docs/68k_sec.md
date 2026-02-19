![The sec() Command](68k_sec/sec.png "The sec() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the secant of a number (usually, an angle).|sec(*angle*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press A to enter the Trig submenu.
- Press 5 to select sec(.
       
# The sec() Command

The `sec()` command returns the secant (the reciprocal of the [cosine](68k:cos.html)) of an angle measure. Naturally, the result depends on the angle [mode](68k:setmode.html) the calculator is in: radian, degree, or (in AMS version 3.10) gradian. You can also use one of the <sup>[r](68k:radian.html)</sup>, [°](68k:degree.html), <sup>[G](68k:gradian.html)</sup> marks to specify an angle mode.

The `sec()` command, along with 11 other trig and hyperbolic functions, was added with AMS version 2.07. It can be easily replaced on earlier versions with 1/cos(x), which is what it simplifies to anyway.

For many common angles, `sec()` can compute an exact result. Other angles, the calculator will leave alone unless it's in approximate mode (or unless you make it approximate), and then it will give a decimal approximation. As long as the calculator is in radian [mode](68k:mode-settings.html), `sec()` can be used with complex numbers as well.


```
:sec(60°)
           2
:sec(x)
          1/cos(x)
:sec(π/2)
          undef
```

If `sec()` is applied to a list, it will take the secant of every element in the list. However, it can't be applied to matrices the way [`cos()`](68k:cos.html) can (this is probably an oversight; all the trig and hyperbolic functions that were present in all AMS versions work with matrices, but the ones added in version 2.07 do not).

## Error Conditions



## Related Commands

- [`68k:csc()`](68k:csc().html)
- [`68k:cot()`](68k:cot().html)
- [`secֿ¹()`](68k:arcsec.html)
