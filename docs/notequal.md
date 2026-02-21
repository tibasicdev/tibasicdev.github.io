![The ≠ Command](notequal/NOTEQUAL.PNG "The ≠ Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns true if value1 is not equal to value2.|*value1*≠*value2*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd TEST to access the test menu.
2. 2 to select ≠, or use arrows.
       
# The ≠ Command

The ≠ (not equal) operator takes two numbers, variables, or expressions, and tests to see if they are not equal to each other. It will return 1 if they are not, and 0 if they are. When determining the order of operations, ≠ will be executed after the [math](operators.html#math) operators, but it will be executed before the [logical](operators.html#logical) operators and in the order that it appears from left to right with the other [relational](operators.html#relational) operators.

```
1≠0
           1
0→X
           0
3→Y
           3
X≠Y
           1
```

## Advanced Uses

Just like the other relational operators, ≠ can take real numbers and lists for variables. In order to compare the lists, however, both must have the same dimensions; if they don't, the calculator will throw a [ERR:DIM MISMATCH](errors.html#dimmismatch) error. When comparing a real number to a list, the calculator will actually compare the number against each element in the list and return a list of 1s and 0s accordingly.

```
:{2,4,6,8}≠{1,3,5,7
           {1 1 1 1}
:5≠{1,2,3,4,5
           {1 1 1 1 0}
```

Besides real numbers and lists, ≠ also allows you compare strings, matrices, and complex numbers. However, the variables must be of the same type, otherwise the calculator will throw a [ERR:DATA TYPE](errors.html#datatype) error; and just like with lists, both matrices must have the same dimensions, otherwise you will get a [ERR:DIM MISMATCH](errors.html#dimmismatch) error.

```
:[[1,2,3]]≠[[1,2,3
           0
:"HELLO"≠"WORLD
           1
:(3+4i)≠(5-2i)    (the parentheses are added for clarity)
           1
```

## Optimization

Don't compare a variable's value to zero in a conditional expression, because the calculator treats nonzero values as true and zero as false. Instead, just write the variable by itself:

```
:If C≠0
can be
:If C
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you try to compare two different kinds of variables, such as a string and number or a list and matrix.
- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if you try to compare two lists or matrices that have different dimensions.

## Related Commands

- [=](equal.html) (equal)
- [>](greaterthan.html) (greater than)
- [≥](greaterthanequal.html) (greater than equal)
- [<](lessthan.html) (less than)
- [≤](lessthanequal.html) (less than equal)
