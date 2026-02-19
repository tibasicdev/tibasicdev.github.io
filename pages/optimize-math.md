# Optimization: Math Operations and Keys
Multiplication signs are unnecessary and should be removed because the calculator does implicit multiplication. You should remember that implicit multiplication doesn't bind tighter than regular multiplication.

```
:5*A→B
can be
:5A→B
```

You don't need to put parentheses around a single variable or number by itself when doing multiplication or division.

```
:3/(A)
can be
:3/A
```

Multiplication and division have the same importance based on the order of operations (the rules that determine what order things are evaluated in), so they will be evaluated from left to right if both appear in an expression. If multiplication appears before division, you can remove the parentheses around an expression.

```
:A+(BA)/5→C
can be
:A+BA/5→C
```

Although multiplication and division have the same importance in order of operations, multiplication is in fact faster than division when doing math operations. So, you should multiply instead of dividing, especially if doing the multiplication is smaller than doing the division.

```
:(X+1)/2
:(B+C)/D
can be
:.5(X+1
:Dֿ¹(B+C
```

When adding a negative number to a positive number, switch the two numbers around and change the addition to subtraction. This allows you to get rid of the negative sign.

```
:-A+B→C
can be
:B-A→C
```

You can often times rewrite math expressions using the built-in keys and characters. When you have a number that has two or more zeros, it may be smaller to write it using the the little <sub>E</sub> character (which is designed for scientific notation). This character will multiply the number on its left (1 if no number is given) times 10 to the number given on the right.

```
:50000
can be
:5E4
```

If you want to use a variable to set the exponent of a number, you would have to use 10^X because the calculator doesn't allow ᴇX. This can be replaced with the 10^( key. This also applies to the e^( key, the <sup>2</sup> key, and the <sup>3</sup> character.

```
:10^A+e²-5²+9³
can be
:10^(A)-52+93+e^(2
```

If you have a fraction that has one as the numerator, you can replace it with multiplying the denominator by the ֿ¹ key.

```
:1/16
can be
:16ֿ¹
```

When you have a fraction that has an expression in the numerator that has parentheses around it and a variable in the denominator, you can sometimes eliminate the fraction by multiplying the variable by the ֿ¹ key and multiplying it by the expression from the numerator.

```
:If (A+B)/C
can be
:If Cֿ¹(A+B
```

If you raise a variable or value to some fractional power with one in the numerator, you can just take the denominator of the fractional power and then multiply it by the xroot character and the variable or value.

```
:A^(1/B
can be
:Bx√A
```

Always do all the operations you can ahead of time. This eliminates some of the operations that the calculator has to do.

```
:33+A(8/2→B
can be
:33+4A→B
```

Write and calculate expressions in one step instead of several steps.

```
:2BC→D
:3A→E
:D+E→F
can be
:2BC+3A→F
```

One of the basic math rules is that multiplying one times any variable is equal to the variable. So, you don't need to put the one in front of the variable.

```
:1A+3→B
can be
:A+3→B
```

When adding two variables of the same type together, you should add up the number of times the variable appears and multiply that value by the variable.

```
:A+3A→B
can be
:4A→B
```

Rewriting division with multiplication is useful when multiplying is smaller. You take the denominator and then change it to the equivalent for multiplication.

```
:(X+1)/10
can be
:.1(X+1
```

The distributive identity should be used when you have three or more variables that share a common number or variable. You take that common number or variable out and distribute it to all of the variables.

```
:CA+CB+C²→D
can be
:C(A+B+C→D
```

The multiplicative inverse identity is used when you have an expression where the same variable or value is in the numerator and denominator. You can remove the variable or value because it is canceled out.

```
:2A/(2BA
can be
:1/B
```

When you have a fraction that has a fraction as its denominator, you can sometimes use the division inverse identity. If the numerator of the first fraction is one, you can flip the second fraction causing the first fraction to disappear.

```
:1/(4/A
can be
:A/4
```
