# Decimal to Fraction
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Converts a decimal number to a fraction.|*Ans* - the number you want to convert to a fraction|*Ans* - the fraction in list format|Ans, X|Weregoose|[file decimaltofraction.zip]|

```
:Ans→X:{1,abs(Ans
:Repeat E‾9>Ans(2
:abs(Ans(2){1,fPart(Ans(1)/Ans(2
:End
:round({X,1}/Ans(1),0
:Ans/gcd(Ans(1),Ans(2
```

Although there is a [►Frac](frac.html) command available for converting a decimal number to a fraction, this is only a formatting command and doesn't actually give you the numerator and denominator as separate numbers. This limits your choices for using fractions, especially since ►Frac only works with the [Disp](disp.html) and [Pause](pause.html) commands. In addition, it does not work very well, and fails for several inputs that you would think are within its ability to figure out (such as -1.3427625). Fortunately, you can improve upon the ►Frac command by using your own routine.

The basic algorithm that you use when converting a number to a fraction is commonly known as the [Euclidean algorithm](https://en.wikipedia.org/wiki/euclidean_algorithm). While it has been around for literally millennia, it is still one of the best algorithms because of its sheer simplicity (it doesn't require any factoring or other complex math operations).

The way it works is that you have two numbers (in our routine, it's one and the decimal number you input), and you divide the first number by the second number, and check to see if there is a remainder. If there is a remainder, you then repeat the process again, except this time you swap the numbers. This process is repeated over and over again until the second number is equal to zero, at which point you will have your desired fraction.

One thing you will probably notice is that we aren't actually checking for zero in the Repeat loop. Because of the way that TI designed the TI-Basic language, each number has a limited amount of precision. As a result, any math calculations that involve extremely small or large numbers will produce rounding errors that don't return the right number. The easiest way to deal with this problem is by checking for a really small number (in this case, <sub>E</sub>‾9).
