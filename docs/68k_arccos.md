![The Arccos (cos^-1) command](68k_arccos/arccos.png "The Arccos (cos^-1) command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Takes the inverse cosine of a number (usually, an integer or fraction).|cos<sup>-1</sup>(*angle*)|This command works on all calculators.|1 byte|
       
### Menu Location
Press [2nd] COS button to enter cos<sup>-1</sup>(.
       
# The Arccos (cos^-1) command


The `cos<sup>-1</sup>()` command returns the [inverse cosine](https://mathworld.wolfram.com/inversecosine.html) of an angle measure. Naturally, the result depends on the angle [mode](68k:setmode.html) the calculator is in: radian, degree, or (in AMS version 3.10) gradian. You can also use one of the <sup>[`r`](68k:radian.html)</sup>, [`°`](68k:degree.html), <sup>[`G`](68k:gradian.html)</sup> marks to specify an angle mode.

For many common angles, `cos<sup>-1</sup>()` can compute an exact result. Other angles, the calculator will leave alone unless it's in approximate mode (or unless you make it approximate), and then it will give a decimal approximation. As long as the calculator is in radian [mode](68k:mode-settings.html), `cos<sup>-1</sup>()` can be used with complex numbers as well.

```
:cos⁻¹(1/2)
           π/3
:cos⁻¹(-1/2)
           2π/3
:cos(cos⁻¹(x))
           x
```

If `cos<sup>-1</sup>()` is applied to a list, it will take the inverse cosine of every element in the list.

## Advanced Uses

The `cos<sup>-1</sup>()` of a matrix is not (in general) the same as taking the cosine of every element of the matrix. I hope that someone more qualified to talk about this updates this part of the page.

## Error Conditions

- Please update this part too

## Related Commands

- [`68k:sin()`](68k:sin().html)
- [`68k:tan()`](68k:tan().html)
- [`68k:cos()`](68k:cos().html)
