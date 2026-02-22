# Order of Operations
//"Please excuse my dear Aunt Sally" —Anonymous//

To figure out order of operations, the calculator divides all the operations into 15 priority levels. When evaluating an expression, everything on one priority level is simplified (usually, going from left to right) before moving on to the next.

Of course, everything inside parentheses, brackets, and braces is simplified first.


**Priority Level**
**Operations on that level**


**1**
 Everything inside parentheses **( )**, brackets **[ ]**, and braces **{ }** 


**2**
 Indirection (**#**)[^1]


**3**
 Function calls: everything with its own parenthesis, e.g. **[68k:sin()](68k:sin.html)** 


**4**
 Operators that go after their operand, e.g. **<sup>[T](68k:transpose.html)</sup>**
This also includes taking elements from lists and matrices with **[ ]**


**5**
 Exponentiation (**[^](68k:power.html)**, **[.^](68k:dotpower.html)**)[^2]


**6**
 Negation (**[-](68k:negative.html)**) 


**7**
 String concatenation (**[&](68k:append.html)**) 


**8**
 Multiplication and division (**[*](68k:multiply.html)**, **[/](68k:divide.html)**, **[.*](68k:dotmultiply.html)**, **[./](68k:dotdivide.html)**) 


**9**
 Addition and Subtraction (**[+](68k:add.html)**, **[-](68k:subtract.html)**, **[.+](68k:dotadd.html)**, **[.-](68k:dotsubtract.html)**)


**10**
 Equality relations: (**[=](68k:equal.html)**, **[≠](68k:not-equal.html)**, **[>](68k:greater-than.html)**, **[≥](68k:greater-than-or-equal.html)**, **[<](68k:less-than.html)**, **[≤](68k:less-than-or-equal.html)**) 


**11**
 Logical and arithmetic **[68k:not](68k:not.html)** [^3]


**12**
 Logical and arithmetic **[68k:and](68k:and.html)** 


**13**
 Logical and arithmetic **[68k:or](68k:or.html)**, **[68k:xor](68k:xor.html)** 


**14**
 Constraint "[68k:with](68k:with.html)" operator (**|**) 


**15**
 Store ([→](68k:store.html)) 


[[footnoteblock]]
[^1]: Note that this means #x[n] will take the n<sup>th</sup> element of #x, not # of x[n]
[^2]: Unlike other priority levels, this one is evaluated right to left. For instance, x^y^z is interpreted as x^(y^z) not (x^y)^z.
[^3]: This order may seem unintuitive when and, or, xor, not are arithmetic operations. For instance, not 5+6 will be not(5+6) as opposed to not(5)+6.
