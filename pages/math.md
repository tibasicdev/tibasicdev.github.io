# Math Functions
Calculators are built with one primary purpose: math. Programming, game playing, and everything else is secondary. Thus, you will find a number of powerful math commands. Although it may seem that they are of no use to a programmer, programs sometimes need math functions, and many math functions can be used in clever ways. In this guide we'll group the commands into the following general groups:



### Number Operations

These commands deal with different ways you can manipulate the integer and fraction parts of a number, and are mostly found in the MATH-NUM menu.

- [►Frac](frac.html), [►Dec](dec.html) — display a number as either a *frac*tion or a *dec*imal.
- [iPart(](ipart.html), [int(](int.html), [fPart(](fpart.html), [round(](round.html)  — take the integer or fractional part of a number in various ways.

### Probability and Combinatorics

These commands are generally found in the MATH-PRB menu (except for [randM(](randm.html), which is in the MATRIX-MATH menu). They include commands for generating random numbers, and commands that are useful for solving problems in combinatorics and probability theory.

- [rand](rand.html), [randInt(](randint.html), [randNorm(](randnorm.html), [randBin(](randbin.html), [randM(](randm.html) — pseudorandom number generation.
- [nPr](npr.html), [nCr](ncr.html), [!](factorial.html) — combinatorical quantities.

### Calculus

Although the TI-83 series calculators don't, by themselves, have the capability for symbolic calculations, these commands (found in the main MATH menu) can provide numerical approximations for some commonly computed quantities in calculus.

- [fMin(](fmin.html), [fMax(](fmax.html) — numerical function optimization in one variable.
- [nDeriv(](nderiv.html), [fnInt(](fnint.html) — derivatives and integrals.
- [solve(](solve.html) — numerical solution of an equation in one variable.

### Trigonometry

These commands allow you to manipulate angles, and are generally affected by [Radian mode](radian-mode.html) and [Degree mode](degree-mode.html) (so you should check those pages out). Some of these commands live in the 2nd ANGLE menu, some are on the keyboard, and some can only be found in the 2nd CATALOG menu:

- [sin(](sin.html), [sinֿ¹(](arcsin.html), [cos(](cos.html), [cosֿ¹(](arccos.html), [tan(](tan.html), [tanֿ¹(](arctan.html) — trigonometric or circular functions.
- [sinh(](sinh.html), [sinhֿ¹(](arsinh.html), [cosh(](cosh.html), [coshֿ¹(](arcosh.html), [tanh(](tanh.html), [tanhֿ¹(](artanh.html) — hyperbolic functions.
- [°](degree-symbol.html) and <sup>[r](radian-symbol.html)</sup> — for converting between various angular units.
- [P►Rx(](p-rx.html), [P►Ry(](p-ry.html), [R►Pr(](r-pr.html), [R►Pθ(](r-ptheta.html) — for converting between rectangular and polar coordinates.
- [►DMS](-dms.html) — Formatting command for degrees-minute-second notation.





### Complex Number Operations

These commands are used for dealing with complex numbers, and are found in the MATH-CPX menu. Many other math commands work on complex numbers too, and complex numbers are fairly strongly connected to trigonometry.

- *[i](i.html)* — the basis of complex number theory.
- [conj(](conj.html), [real(](real-func.html), [imag(](imag.html), [angle(](angle.html), [abs(](abs.html) — manipulate complex numbers.
- [►Rect](-rect.html), [►Polar](polar-display.html) — display complex numbers in either rectangular or polar form.

### [Operators](operators.html)

These commands are found on the keyboard and in the 2nd TEST menu, and deal with basic mathematical and logical commands.

- [+](add.html), [-](subtract.html), [*](multiply.html), [/](divide.html), [^](power.html), [‾](negative.html) — math operators.
- [=](equal.html), [≠](notequal.html), [<](lessthan.html), [>](greaterthan.html), [≤](lessthanequal.html), [≥](greaterthanequal.html) — relational operators.
- [and](and.html), [or](or.html), [xor](xor.html), [not(](not.html) — logical operators.

### Powers, Inverses, Exponentials, and Logarithms

These commands are found all over the place, many on the keyboard itself, and deal with raising some value to a power, or raising a number to some value, or the inverses of those operations.

- [ֿ¹](inverse.html), [²](2.html), [³](3.html), [√(](square-root.html), [³√(](cube-root.html), [×√](xroot.html) — returns the number raised to the respective power.
- [10^(](ten-exponent.html), [e^(](e-exponent.html), [E](e-ten.html), [ln(](ln.html), [log(](log.html) — commands for dealing with exponentials.

### Miscellaneous 

These commands have nothing to do with each other, but don't really belong to other categories either.

- [π](pi.html), *[e](e-value.html)* — famous (and occasionally, even useful) math constants.
- [min(](min.html), [max(](max.html) — returns the smaller number(s) or the larger number(s).
- [lcm(](lcm.html), [gcd(](gcd.html) — returns the least common multiple or the greatest common denominator of two numbers.





## Comments

Note that the [statistics](statistics.html) commands are not included here. That is because statistics is not math. There is also the [finance](finance.html) commands and variables, which are another topic unto themselves.

In addition, all of the above commands, except for the calculus and random number generating commands, can be applied to [lists](lists.html) as well. For single-argument commands, this just means that the command is applied to each element of the list separately.

For multiple-argument commands, there are two ways to do it: with a number and a list (then, the command is applied with that number to each element of a list), and with two lists (then, it's done pairwise, and the lists must be the same size, otherwise the calculator will throw a [ERR:DIM MISMATCH](errors.html#dimmismatch) error).
