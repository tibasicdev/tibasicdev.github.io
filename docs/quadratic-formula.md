# Quadratic Formula
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Solves for the complex roots of a quadratic equation.|*A, B, C* - the constants in Ax<sup>2</sup>+Bx+C=0|*Ans* - a 2-element list of the two roots (or the one repeated root)|A, B, C|thornahawk|[file Quad_Routines.zip]|

```
-2C/(B+{-1,1}√(B²+4ACi²
```

For optimization purposes, an alternate form of the quadratic formula is used (see below for the formulas). The {-1,1} list is used to replace the ± symbol — lists can be used just as well as numbers in expressions, making the result a list as well. By using *i*² in the expression in place of subtraction, the routine avoids having to activate [a+bi](a-bi.html) mode to allow complex roots.

The output is a complex list in [Ans](ans.html) of the two roots. If there is only one root, it will be returned twice. If both roots are real, they will still be returned correctly, but stored internally as complex numbers — so use the [real(](real-func.html) command on them if you want to pass them to commands that don't accept complex arguments.

## Advanced

The ordinary formula above can give poor results if B is much larger than A and/or C. In that case, an alternate routine can be used:

```√(B²+4ACi²
If 0>real(Ansconj(B
-Ans
-.5(B+Ans
{Ans/A,C/Ans
```

## Formulas

The ordinary quadratic formula, and its alternate form are used:

$$
\begin{align}
\mathrm{For} \hspace{5pt} ax^2+bx+c = 0, \\ \\
x = \frac{-b\pm\sqrt{b^2-4ac}}{2a} \\ \\
x = \frac{2c}{-b\pm\sqrt{b^2-4ac}}
\end{align}$$
