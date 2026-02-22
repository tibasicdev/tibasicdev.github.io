# Math Functions
Calculators are built with one primary purpose: math. Programming, game playing, and everything else is secondary. Thus, you will find a number of powerful math commands. Although it may seem that they are of no use to a programmer, programs sometimes need math functions, and many math functions can be used in clever ways. In this guide we'll group the commands into the following five categories:

##Algebra

Symbolic manipulation is the primary cool factor of the 68k (TI-89, TI-92, TI-92+, and V200) calculators. With the [68k:solve()](68k:solve.html) command, the calculator can give *exact* solutions to a fair number of equations (of course, approximate solutions are even easier to get). Along with a dozen variations on solve(), there are a few commands for extracting various parts of an expression, which should be useful for writing your own algebraic tools.

As on earlier calculator models, there's also logs and complex number operations, which are even better with symbolic math.

Here is the complete list of algebraic commands:

- | ([68k:with](68k:with.html))
- [68k:abs()](68k:abs.html)
- [68k:angle()](68k:angle.html)
- [68k:cFactor()](68k:cfactor.html)
- [68k:comDenom()](68k:comdenom.html)
- [68k:conj()](68k:conj.html)
- [68k:cSolve()](68k:csolve.html)
- [68k:cZeros()](68k:czeros.html)
- [68k:exp▶list()](68k:exp-list.html)
- [68k:expand()](68k:expand.html)


- [68k:factor()](68k:factor.html)
- [68k:getNum()](68k:getnum.html)
- [68k:getDenom()](68k:getdenom.html)
- [68k:imag()](68k:imag.html)
- [68k:ln()](68k:ln.html)
- [▶ln](68k:to-ln.html) <sup>3.10</sup>
- [68k:log()](68k:log.html)
- [68k:▶logbase()](68k:-logbase.html) <sup>3.10</sup>
- [68k:nSolve()](68k:nsolve.html)


- [68k:part()](68k:part.html)
- [68k:▶Polar](68k:-polar.html)
- [68k:polyEval()](68k:polyeval.html)
- [68k:randPoly()](68k:randpoly.html)
- [68k:real()](68k:real.html)
- [68k:▶Rect](68k:-rect.html)
- [68k:root()](68k:root.html) <sup>3.10</sup>
- [68k:solve()](68k:solve.html)
- [68k:zeros()](68k:zeros.html)


##Arithmetic

For basic arithmetic, the 68k calculators' advantage is that it can do exact calculations with integers up to 256<sup>255</sup>-1 (and approximate floating-point decimal calculations up to 10<sup>1000</sup>-1). Here is the complete list of arithmetic commands:


- [+](68k:add.html), [-](68k:subtract.html), [*](68k:multiply.html), [/](68k:divide.html), [‾](68k:negative.html), [^](68k:power.html)
- [√()](68k:square-root.html), [!](68k:factorial.html), [%](68k:percent.html), [▶](68k:convert.html), [0b](68k:0b.html), [0h](68k:0h.html)
- [68k:abs()](68k:abs.html)
- [68k:approx()](68k:approx.html)
- [68k:▶Bin](68k:-bin.html)
- [68k:ceiling()](68k:ceiling.html)
- [68k:comDenom()](68k:comdenom.html)
- [68k:▶Dec](68k:-dec.html)
- [E](68k:e-ten.html)
- [68k:exact()](68k:exact.html)
- [68k:floor()](68k:floor.html)
- [68k:fPart()](68k:fpart.html)


- [68k:gcd()](68k:gcd.html)
- [68k:getNum()](68k:getnum.html)
- [68k:getDenom()](68k:getdenom.html)
- [68k:getUnits()](68k:getunits.html)
- [68k:▶Hex](68k:-hex.html)
- [68k:int()](68k:int.html)
- [68k:intDiv()](68k:intdiv.html)
- [68k:iPart()](68k:ipart.html)
- [68k:isPrime()](68k:isprime.html)
- [68k:lcm()](68k:lcm.html)
- [68k:max()](68k:max.html)
- [68k:min()](68k:min.html)


- [68k:mod()](68k:mod.html)
- [68k:nCr()](68k:ncr.html)
- [68k:nPr()](68k:npr.html)
- [68k:propFrac()](68k:propfrac.html)
- [68k:remain()](68k:remain.html)
- [68k:rotate()](68k:rotate.html)
- [68k:round()](68k:round.html)
- [68k:shift()](68k:shift.html)
- [68k:sign()](68k:sign.html)
- [68k:tmpCnv()](68k:tmpcnv.html)
- [ΔtmpCnv()](68k:deltatmpcnv.html)


##Calculus

What with the ability for symbolic calculation, the 68k calculators are much more useful for calculus than other models; they can do symbolic differentiation and integration, as well as calculate infinite sums and products. There are some numeric functions as well carried over from earlier calculator models.

Here is the complete list of calculus commands:


- [∫()](68k:integral.html), [∏()](68k:product-pi.html), [∑()](68k:sum-sigma.html)
- [68k:arcLen()](68k:arclen.html)
- [68k:avgRC()](68k:avgrc.html)
- *[d()](68k:d.html)*


- [68k:deSolve()](68k:desolve.html)
- [68k:fMax()](68k:fmax.html)
- [68k:fMin()](68k:fmin.html)
- [68k:impDif()](68k:impdif.html) <sup>3.10</sup>


- [68k:limit()](68k:limit.html)
- [68k:nDeriv()](68k:nderiv.html)
- [68k:nInt()](68k:nint.html)
- [68k:taylor()](68k:taylor.html)


##Statistics

Statistics is the one field in which the 68k calculators don't stand out compared to other TI models. In fact, there are considerably less statistical tools than, say, on the TI-83 series calculators (compare their page on [statistics](statistics.html)). What there is left is mostly a variety of regression models: 
- [68k:LinReg](68k:linreg.html) and [68k:MedMed](68k:medmed.html) — two different linear models.
- [68k:QuadReg](68k:quadreg.html), [68k:CubicReg](68k:cubicreg.html), [68k:QuartReg](68k:quartreg.html), [68k:PowerReg](68k:powerreg.html) — polynomial models.
- [68k:ExpReg](68k:expreg.html), [68k:LnReg](68k:lnreg.html), [68k:Logistic](68k:logistic.html), [68k:SinReg](68k:sinreg.html) — the other models.
For all of these, use the [68k:ShowStat](68k:showstat.html) command to display the results in a dialog box, and look at the statistical [68k:system variables](68k:system-variables.html) for more information.

There are also some general-purpose commands for sample statistics:
- [68k:mean()](68k:mean.html), [68k:median()](68k:median.html), [68k:stdDev()](68k:stddev.html), [68k:variance()](68k:variance.html), and with OS 3.10, [68k:stDevPop()](68k:stdevpop.html)
- [68k:OneVar](68k:onevar.html) and [68k:TwoVar](68k:twovar.html) for getting a bunch of statistics at once.
- [68k:rand()](68k:rand.html),  [68k:randMat()](68k:randmat.html), [68k:randNorm()](68k:randnorm.html), [68k:randPoly()](68k:randpoly.html), and [68k:RandSeed](68k:randseed.html) to generate random numbers.

Finally, you can plot data with the [68k:NewPlot](68k:newplot.html) command (see also [68k:PlotsOn](68k:plotson.html) and [68k:PlotsOff](68k:plotsoff.html)).

##Trigonometry

The main thing to remember when doing trig is to be aware of what angle mode you're in. By default, you're using radians, where a full circle measures 2π. The other two angle modes are degrees, where a full circle is 360, and (on the newest OS versions for the TI-89 Titanium and Voyage 200) "gradians" where a full circle measures 400.

The commands that actually work with these include the usual trig functions (half of which — the mostly useless half — were added in OS version 2.07) and their inverses, as well as commands to convert rectangular coordinates (x,y) into polar coordinates (r,θ). There's also the hyperbolic functions (there's a hyperbolic equivalent for each of the normal trig functions).

As far as symbolic math is concerned, you can use [68k:tExpand()](68k:texpand.html) and [68k:tCollect()](68k:tcollect.html) to rearrange complicated expressions using sin() and cos(), and hope to simplify them somewhat by doing so.

The entire list of trig commands is:


- <sup>[r](68k:radian.html)</sup>, [°](68k:degree.html), <sup>[G](68k:gradian.html)</sup> <sup>3.10</sup>
- [∠](68k:angle-symbol.html)
- [68k:cos()](68k:cos.html)
- [cosֿ¹()](68k:arccos.html)
- [68k:cosh()](68k:cosh.html)
- [coshֿ¹()](68k:arccosh.html)
- [68k:cot()](68k:cot.html) <sup>2.07</sup>
- [cotֿ¹()](68k:arccot.html) <sup>2.07</sup>
- [68k:coth()](68k:coth.html) <sup>2.07</sup>
- [cothֿ¹()](68k:arccoth.html) <sup>2.07</sup>
- [68k:csc()](68k:csc.html) <sup>2.07</sup>
- [cscֿ¹()](68k:arccsc.html) <sup>2.07</sup>


- [68k:csch()](68k:csch.html) <sup>2.07</sup>
- [cschֿ¹()](68k:arccsch.html) <sup>2.07</sup>
- [68k:▶DD](68k:-dd.html)
- [68k:▶DMS](68k:-dms.html)
- [68k:▶Grad](68k:-grad.html) <sup>3.10</sup>
- [68k:P▶Rx()](68k:p-rx.html)
- [68k:P▶Ry()](68k:p-ry.html)
- [R▶Pθ()](68k:r-ptheta.html)
- [68k:R▶Pr()](68k:r-pr.html)
- [68k:▶Rad](68k:-rad.html) <sup>3.00?</sup>
- [68k:sec()](68k:sec.html) <sup>2.07</sup>
- [secֿ¹()](68k:arcsec.html) <sup>2.07</sup>


- [68k:sech()](68k:sech.html) <sup>2.07</sup>
- [sechֿ¹()](68k:arcsech.html) <sup>2.07</sup>
- [68k:sin()](68k:sin.html)
- [sinֿ¹()](68k:arcsin.html)
- [68k:sinh()](68k:sinh.html)
- [sinhֿ¹()](68k:arcsinh.html)
- [68k:tan()](68k:tan.html)
- [tanֿ¹()](68k:arctan.html)
- [68k:tanh()](68k:tanh.html)
- [tanhֿ¹()](68k:arctanh.html)
- [68k:tCollect()](68k:tcollect.html)
- [68k:tExpand()](68k:texpand.html)
