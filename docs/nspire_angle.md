![Angle](nspire_angle/ "Angle")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|
|--- |--- |--- |
|Computes the angle of a complex number or a set of complex numbers.|**angle(***Expr1***)** → *expression*<br>**angle(***List1***)** → *list*<br>**angle(***Matrix1***)** → *matrix*|If this is only available on certain versions of the nspire|

### Menu Location


# Angle

The **angle(** command computes the angle of a complex number, which corresponds to the rotation of a vector whose length is equivalent to the **[abs(](nspire:abs.html)** of the number. The angle is returned in degrees, gradians, or radians, depending on the mode the calculator is in.

```
Degree mode
:angle(1+i) = 45
Radian mode
:angle(1+i) = π/4
```

**angle(** can also return the angles for a list or matrix of complex numbers, returning the outputs in a list or matrix respectively. **angle(** will attempt to return a closed-form expression for the value rather than a decimal expression when utilizing the CAS, and can also return a symbolic evaluation of an angle.

```
:angle(z) = π(sign(z)-1)/2
```

## Formulas

The general formula for the angle of complex number *x+iy* is given by



Often denoted as θ, the angle of a complex number is used in its polar representation



where *r* is the absolute value of the number.

## Related Commands

- **[nspire:abs(](nspire:abs.html)**
- **[nspire:sign(](nspire:sign.html)**
- **[nspire:imag(](nspire:imag.html)**
