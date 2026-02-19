![The ∠ Command](68k_angle-symbol/angle-symbol.png "The ∠ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Used in entering a vector in polar, cylindrical, or spherical format, or a complex number in polar form.|[*r*,∠*θ*]<br>[*r*,∠*θ*,*z*]<br>[*r*,∠*θ*,∠*φ*]<br>(*r*∠*θ*)|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH menu.
- Press 2 to enter the Angle submenu.
- Press 7 to select ∠.
       
# The ∠ Command

The ∠ operator is used for alternate forms of entering vectors or complex numbers. It will be used for output depending on the Complex Format and Vector Format [68k:mode settings](68k:mode-settings.html), but you can always use it in an expression.

For vectors (which are just 1x2 or 1x3 matrices, as far as ∠ is concerned):
- [r,∠θ] is equivalent to [r*cos(θ),r*sin(θ)]
- [r,∠θ,z] is equivalent to [r*cos(θ),r*sin(θ),z]
- [r,∠θ,∠φ] is equivalent to [r*cos(θ)*sin(φ),r*sin(θ)*sin(φ),r*cos(φ)]
These have to be row vectors — you can't use column vectors with ∠.

For complex numbers, (r∠θ) is equivalent to r*(cos(θ)+***i****sin(θ)). You have to have the parentheses there, and both r and θ must be real numbers or expressions.

## Error Conditions





## Related Commands

- [68k:angle()](68k:angle().html)
- [68k:abs()](68k:abs().html)
- [68k:norm()](68k:norm().html)
