# Number One-Liners
This page is dedicated to showcasing small snippets of code that may be useful. These small routines are designed to accomplish tasks involving numbers and their attributes. Unless specified, the output is in Ans.

------
**Rounding** - [lirtosiast](http://www.wikidot.com/user:info/lirtosiast), [Trenly](http://www.wikidot.com/user:info/Trenly) 

The int( command always rounds towards -∞, and iPart( rounds towards 0. Here are the other two directions:
```
-int(-X                   //rounds towards +∞
```
```
iPart(X+not(not(fPart(X   //rounds away from 0
```

For natural rounding, where a number rounds up if the decimal part is greater than one half and down otherwise, use this:
```
iPart(X+(fPart(X)≥.5
```

To round towards the nearest N or multiple of N, the code would be:
```
X/N->X
NiPart(X+(fPart(X)≥.5
```
------
**Number Concatenation** – [DarkerLine](http://www.wikidot.com/user:info/DarkerLine)

Returns the number formed by concatenating positive integers M and N.
```
N+M10^(1+int(log(N
```

------
**Number of Digits in Nonzero Integer**

If X is always positive, remove the "abs(".
```
1+int(log(abs(X
```

------
**Number of Digits in Decimal Number** – [Weregoose](http://www.wikidot.com/user:info/Weregoose), [lirtosiast](http://www.wikidot.com/user:info/lirtosiast)
```
not(X)+sum(0 or fPart(abs(X10^(cumSum(binomcdf(13,0))-2-int(log(abs(X+not(X
```

------
**Sum of Digits of Integer** – [DarkerLine](http://www.wikidot.com/user:info/DarkerLine), [lirtosiast](http://www.wikidot.com/user:info/lirtosiast)

If X is always nonnegative, remove the "abs(".
```
sum(int(10fPart(abs(X10^(-cumSum(binomcdf(13,0
```

------
**Sum of Digits of Decimal Number** – [DarkerLine](http://www.wikidot.com/user:info/DarkerLine), [lirtosiast](http://www.wikidot.com/user:info/lirtosiast)

If X is always nonnegative, remove both "abs(". If nonzero, remove the "+not(X".
```
sum(int(10fPart(abs(X10^(cumSum(binomcdf(13,0))-2-int(log(abs(X+not(X
```

------
**Fraction Simplifier** – [Battlesquid](http://www.wikidot.com/user:info/Battlesquid)

Simplifies fractions where A is the numerator and B is the denominator.

With [Disp](disp.html)

```
"A/B▶Frac"→Str1
Disp expr(Str1
```

With [Output(](output.html)

```
"A/B▶Frac"→Str1
Output(1,1,expr(Str1
```

Alternatively, there is [Xeda Elnara](http://www.wikidot.com/user:info/Xeda Elnara)'s method, but an [abs](abs.html) command would have to be used to ensure that there is not a negative input.

```
gcd(A,B→C
A/C→A
B/C→B
```

------
**Base<sub>10</sub> to Base<sub>2</sub> (Decimal to Binary)** – [coltonj96](http://www.wikidot.com/user:info/coltonj96)

Takes any whole positive number and converts it to binary.

```
Σ(int(2fPart(2ֿֿ¹Ans/(2^A)))10^A,A,0,iPart(round(log(Ans)/log(2),1
```

Input must be a whole positive integer and be less than 1024 due to limit of 10 digits
