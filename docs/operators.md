# Operators
Just like other programming languages, TI-Basic has the standard set of core operators built-in (math, relational, and logical), although they each have their own syntax and rules. 

- [{#math}](#math-operators)
- [{#relational}](#relational-operators)
- [{#logical}](#logical-operators)
	- [{#order-of-operations}](#order-of-operations)

## Math Operators {#math}

There are five math operators: [+](add.html), [-](subtract.html), [*](multiply.html), [/](divide.html), and [^](power.html). Anybody who has ever done even basic math should know and recognize at least the first four operators, but for those who don't, their meaning is pretty straightforward:

: **+** : Adds two numbers together
: **-** : Subtracts one number from another
: ***** : Multiplies two numbers together
: **/** : Divides one number by another
: **^** : Raises a number to a power

There are two similar negative symbols on the TI-83 calculators — the [subtraction](subtract.html) symbol (the - key) and the [negation](negative.html) symbol (the (-) key). These aren't interchangeable. However, it's almost always clear from an expression which one is being used, so the - symbol will be used to represent both throughout most of this guide.

## Relational Operators {#relational}

There are six relational operators: [=](equal.html), [≠](notequal.html), [>](greaterthan.html), [≥](greaterthanequal.html), [<](lessthan.html), and [≤](lessthanequal.html). Just like with the math operators, these operators are used in almost every math class, and thus most people should know them.

: **=** : X=Y is true if X is equal to Y
: **≠** : X≠Y is true if X is not equal to Y
: **>** : X>Y is true if X is greater than Y
: **≥** : X≥Y is true if X is greater than or equal to Y
: **<** : X<Y is true if X is less than Y
: **≤** : X≤Y is true if X is less than or equal to Y

Because the calculator does not have a separate time for logical values (true and false), they are represented by the numbers 1 and 0. This becomes important when dealing with [piecewise expressions](piecewise-expressions.html).

## Logical Operators {#logical}

There are four logical operators: [and](and.html), [or](or.html), [not(](not.html), and [xor](xor.html). Their interpretations are mostly intuitive when thinking about the meaning of the English word:

: **and** : X and Y is true if both X and Y are true
: **or** : X or Y is true if at least one of X and Y is true
: **xor** : X xor Y is true if only one of X and Y is true
: **not(** : not(X) is true if X is false

Again, as with the relational operators, 1 is used to for 'true', and 0 is used for 'false'. It so happens that the logical operators treat all nonzero values as though they were 1 (true), so the expression '2 and 3' will be true just as '1 and 1'.

Here is a truth table of the various values:

| A | B | A and B | A or B | A xor B | not(A) |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

### Order of Operations {#order-of-operations}

The TI-83 series of calculators has nine priority levels for evaluating expressions. All the functions on a priority level will be calculated from left to right before moving on to the next priority level. Of course, calculations within parentheses are done first. Here is a table of the priority levels:

| Priority Level | Functions |
| --- | --- |
| 1 | Functions that precede their argument (such as [√(](square-root.html) or [sin(](sin.html)), except for negation |
| 2 | Functions that follow their argument (such as <sup>[2](2.html)</sup> or [!](factorial.html)) |
| 3 | [^](power.html) and [×√](xroot.html) |
| 3.5 | [Negation](negative.html) |
| 4 | [nPr](npr.html) and [nCr](ncr.html) |
| 5 | [Multiplication](multiply.html), [division](divide.html), and implied multiplication |
| 6 | [Addition](add.html) and [subtraction](subtract.html) |
| 7 | The relational operators [=](equal.html), [≠](notequal.html), [<](lessthan.html), [>](greaterthan.html), [≤](lessthanequal.html), [≥](greaterthanequal.html) |
| 8 | The logic operator [and](and.html) |
| 9 | The logic operators [or](or.html) and [xor](xor.html) |
| 10 | Conversions such as [►Frac](-frac.html) |

TI refers to the routine that determines order of operations as the Equation Operating System (EOS<sup>TM</sup>). Unfortunately, this cool name hasn't become common usage.

### Test your knowledge

Here are some sample problems on logical operators, in order of complexity.  For the more difficult ones, it may be best to break them up into smaller parts and work in steps.

| # | Question |
| --- | --- |
| 1 | **0 and 1 or 1** |
| 2 | **0 and (1 or 1)** |
| 3 | **4 and -4 xor (.6 and 0)** |
| 4 | **not(1) xor (1 and 1 xor 1)** |
| 5 | **1 and 0 xor (6*4 and 0) or not(0 and 6)** |
| 6 | **1 and (1 xor not(5 xor 1 and 0)) xor not(1 xor not(1 or not(1)))** |

[[=]]
<details style="display: inline;"><summary>show</summary>
| # | Answer |
| --- | --- |
| 1 | 1 |
| 2 | 0 |
| 3 | 1 |
| 4 | 0 |
| 5 | 1 |
| 6 | 1|
</details>
[[/=]]
