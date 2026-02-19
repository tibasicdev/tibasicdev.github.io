![The cot() Command](68k_cot/cot.png "The cot() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the cotangent of a number (usually, an angle).|cot(*angle*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press A to enter the Trig submenu.
- Press 6 to select cot(.
       
# The cot() Command

The `cot()` command returns the cotangent (the reciprocal of the [`tangent`](68k:tan.html)) of an angle measure. Naturally, the result depends on the angle [mode](68k:setmode.html) the calculator is in: radian, degree, or (in AMS version 3.10) gradian. You can also use one of the `<sup>[r](68k:radian.html)</sup>`, [`°`](68k:degree.html), `<sup>[G](68k:gradian.html)</sup>` marks to specify an angle mode.

The `cot()` command, along with 11 other trig and hyperbolic functions, was added with AMS version 2.07. It can be easily replaced on earlier versions with `1/tan(x)`, which is what it simplifies to anyway.

For many common angles, `cot()` can compute an exact result. Other angles, the calculator will leave alone unless it's in approximate mode (or unless you make it approximate), and then it will give a decimal approximation. As long as the calculator is in radian [mode](68k:mode-settings.html), `cot()` can be used with complex numbers as well.


```
:cot(60°)
           √3/3
:cot(x)
          1/tan(x)
:cot(0)
          undef
```

If `cot()` is applied to a list, it will take the cotangent of every element in the list. However, it can't be applied to matrices the way `cos()` can (this is probably an oversight; all the trig and hyperbolic functions that were present in all AMS versions work with matrices, but the ones added in version 2.07 do not).

## Error Conditions



## Related Commands

- [`68k:sec()`](68k:sec().html)
- [`68k:csc()`](68k:csc().html)
- [`cotֿ¹()`](68k:arccot.html)
