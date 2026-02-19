# Optimization: Logic and Relational Operators
Because the calculator treats every nonzero value as true and zero as false, you don't need to compare if a variable's value is nonzero. Instead, you can just put the variable by itself.

```
:If C≠0
can be
:If C
```

Instead of comparing a variable to zero, use the [`not(`](not.html) logical operator. Because not( returns the opposite value of the variable, true will become false and false will become true.

```
:While A=0
can be
:While not(A
```

When making expressions that combine the [`and`](and.html) and [`or`](or.html) operators where the and operator comes first, you don't need to include parentheses around the and operator. The `and` operator has a higher precedence than `or`, so it is evaluated first. This can become complicated with complex expressions, so you might want to leave some of the parentheses for clarity.

```
:If (A=1 and B=2) or (A=2 and B=1)
can be
:If A=1 and B=2 or A=2 and B=1
```

If you are comparing two unary expressions (expressions with no comparison operator) with the `and` operator, you don't need the `and` operator. For `and` to be true, both values must be nonzero. So, multiplying them will produce the same effect because if either one of the values is zero, the product of both values will also be zero.

```
:If A and B
can be
:If AB
```

A similar technique can be applied to expressions with comparison operators, except some restrictions are required.
With unary expressions, to test [`If`](if.html) A and B is true you multiply them.  With equations, you can multiply the left sides of each together and you can do the same for the right sides.  However, a value being 0 could return a different result than anticipated, so it is best to use this technique when the values are not 0.

```
:If A=B and C=D
can be
:If AC=BD
```

As `and` is similar to multiplying, the `or` operator is similar to addition.  Adding two values together yields a non-zero result if one of the conditions is true.  When you are comparing equations using the `or` operator, you can add the two together (This is not used for unary expressions because the plus symbol and or symbols are both one-byte tokens).  For this the only restriction is that all values must have the same sign (or be 0), or you can circumvent this by using [`abs(`](abs.html).  This is necessary because if two variables have the same value except one is negative, this expression could return false.

```
:If A=B or C=D
can be
:If A+C=B+D
```

The most unused logical operator is [`xor`](xor.html) (exclusive `or`). The `xor` operator is useful when comparing two expressions and checking if one but not both are true. In fact, `xor` is specifically designed for this purpose.

```
:If A=2 and B≠2 or A≠2 and B=2
can be
:If A=2 xor B=2
```

Many times a compound expression can be shortened by combining expressions that have the same meaning or replacing expressions that can be written another way. Think about what the expression means and then think about how to make a shorter equivalent expression. There are many ways of writing an expression, so there are usually ways to rewrite it.

```
:If A>B or A<B
can be
:If A≠B
```

If you have the `not(` operator around an expression, you can usually change the logical operator to the math opposite. This allows you to remove the `not(` operator.

```
:If not(B=C and A=D
can be
:If B≠C or A≠D
```

[DeMorgan's Law](https://en.wikipedia.org/wiki/de_morgan-27s_laws) can be used for expressions in which the not operator is around two separate unary expressions joined by the `and` or `or` operators. It allows you to remove the second not operator and then change the `and` to `or` and vice versa.

```
:If not(A) and not(B
can be
:If not(A or B
```

Min is useful when you are comparing one variable or value to several other variables to see if they are all equal to the variable or value. To use [`min(`](min.html) you just create an expression with the `min(` function and put the common variable or value inside it followed by an equal sign and a left curly brace. You then list out the variables that you are comparing the variable or value to, separating each one with a comma.

```
:If A=10 and B=10 and C=10
can be
:If min(10={A,B,C
```

[`Max(`](max.html) is useful when you are comparing one variable or value to several other variables to see if at least one is equal to the variable or value. You do the same thing as the `min(` function, just replacing min with max.

```
:If A=10 or B=10 or C=10
can be
:If max(10={A,B,C
```

You can put a comparison operator inside the `min(` or `max(` functions to compare when several values or variables are equal to one variable and several values or variables are equal to another variable. This works especially well with three or more variables.

```
:If A=X and B=U or A=Y and B=V
can be
:If max(A={X,Y} and B={U,V
```

`Abs(` is useful when you are comparing a variable to two even or odd values using the `or` operator. You subtract the larger value from the smaller value, divide the result by two, and then put it on the left side of the equal sign. Next, you subtract the larger value by the result on the left side of the equal sign, and then take the variable being tested and subtract it by that value. You then put the `abs(` function around the result and place the expression on the right side of the equal sign.

```
:If A=45 or A=105
can be
:If 30=abs(A-75
```

`X=n<sub>1</sub> or X=n<sub>2</sub>` should become `abs(n<sub>1</sub>-mean({n<sub>1</sub>,n<sub>2</sub>}))=abs(X-mean({n<sub>1</sub>,n<sub>2</sub>}))` (simplified) if `n<sub>1</sub>` and `n<sub>2</sub>` are positive integers and `n<sub>1</sub>+n<sub>2</sub>` is even. If there are three terms, then see if you can simplify two of them according to this rule. If you can't, then a string of `or`'s will be faster than the `max(X={n<sub>1</sub>,n<sub>2</sub>,…` approach. If there are four terms or more, then use `max()`.
