![The Tangent( Command](tangent/TANGENT.GIF "The Tangent( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Draws a line tangent to an expression at the specified value.|Tangent(*expression*,*value*)|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd PRGM to access the draw menu.
2. 5 to select Tangent(, or use arrows and ENTER.
       
# The Tangent( Command

The Tangent( command draws a graph of an expression and then draws a line tangent to that expression, with the line touching the graph at the point of the specified value. You can either use a [equation variable](system-variables.html#equation) (such as Y<sub>1</sub>) or an expression in terms of X (such as X²). Though you can use equation variables from any [graphing mode](graphing-mode.html), they will be treated as functions in terms of X. Tangent( also ignores the graphing mode currently selected.

Here is a simple example, where we are graphing the [parabola](https://en.wikipedia.org/wiki/parabola) X<sup>2</sup> and then drawing a tangent line at the value X=2.

```
:"X²→Y₁
:Tangent(Y₁,2
```
or
```
:Tangent(X²,2
```

## Advanced Uses

Whether the graph shows up or not is dependent on the window dimensions of the graph screen, and you should use a [friendly window](friendly-window.html) to ensure it shows up as you intended.

------

Tangent( will update X and Y for each coordinate drawn (like [DrawF](drawf.html) and [DrawInv](drawinv.html)), and exit with the last coordinate still stored.

------

When evaluating the expression using Tangent(, the calculator will ignore the following errors: [ERR:DATA TYPE](errors.html#datatype), [ERR:DIVIDE BY 0](errors.html#divideby0), [ERR:DOMAIN](errors.html#domain), [ERR:INCREMENT](errors.html#increment), [ERR:NONREAL ANS](errors.html#nonrealans), [ERR:OVERFLOW](errors.html#overflow), and [ERR:SINGULAR MAT](errors.html#singularmat). If one of these errors occurs, the data point will be omitted. However, the errors will still be thrown if they occur when evaluating the function *at* the point of tangency.

------

Using [Ans](ans.html) as an optimization for storing to an equation will not work. For example, the following code returns [ERR:DATA TYPE](errors.html#datatype) because Ans is a string, not an equation variable.

```
:"X²
:Tangent(Ans,2
```

Of course, you *can* use Ans in the equation, if it's a real number, but that's usually not as useful.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if you try to use an equation variable that is undefined.

## Related Commands

- [DrawF](drawf.html)
- [DrawInv](drawinv.html)
