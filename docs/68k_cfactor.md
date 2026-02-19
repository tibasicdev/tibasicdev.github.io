![Cfactor](68k_cfactor/sample.png "Cfactor")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|factors the first argument for all its variables or for var.|cFactor(expression1[,var])<br>cFactor(list1[,var])<br>cFactor(matrix1[,var])|This command works on all calculators.|X byte(s)|
       
### Menu Location
MATH/Algebra/Complex
       
# Cfactor

cFactor(expression1) returns expression1 factored with respect to all of its variables over a common denominator.

expression1 is factored as much as possible toward linear rational factors even if this introduces new non-real numbers. This alternative is appropriate if you want factorization with respect to more than one variable.

When a list or matrix is provided, cFactor() will iterate over the list or matrix. 

```
:cFactor(a^3*x^2+a*x^2+a^3+a)
          a*(a+⁻i)*(a+i)*(x+⁻i)*(x+i)
:cFactor(x^2+4/9)
          (3*x + -2*i)*(3*x + 2*i)
:cFactor(x^2+3)
          x²+3
:cFactor(x^2+a)
          x²+a
```

## Related Commands

- Command 1
- Command 2
- Command 3 

## See Also

- Design Concept 1
- Design Concept 2
- Technique 1
