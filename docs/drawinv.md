![The DrawInv Command](drawinv/DRAWINV.GIF "The DrawInv Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Draws the inverse of a curve in terms of X.|DrawInv *curve*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd DRAW to access the draw menu.
2. 8 to select DrawInv, or use arrows and ENTER.
       
# The DrawInv Command

The `DrawInv` command draws the inverse of a curve in terms of X. Its single argument is an expression in terms of X.

For example, `DrawInv X²` will draw the inverse of the equation Y=X<sup>2</sup>. The inverse reverses the variables X and Y, so that the curve X=Y<sup>2</sup> will be graphed. In this case, the inverse of the function has a simple form: Y=√(X) and Y=-√(X); most functions, however, do not have an inverse expressible as Y= equation, making this command particularly useful.

You can also think of this as graphing the expression but with X representing the vertical direction, and Y representing the horizontal.

`DrawInv` requires the calculator to be in [`Func`](func.html) mode, and is affected by the [`Connected`](connected.html)/[`Dot`](dot.html) setting.

## Advanced Uses

`DrawInv` will update X and Y for each coordinate drawn (like [`Tangent(`](tangent.html) and [`DrawF`](drawf.html)), and exit with the last coordinate still stored.

When evaluating the expression using `DrawInv`, the calculator will ignore the following errors: [ERR:DATA TYPE](errors.html#datatype), [ERR:DIVIDE BY 0](errors.html#divideby0), [ERR:DOMAIN](errors.html#domain), [ERR:INCREMENT](errors.html#increment), [ERR:NONREAL ANS](errors.html#nonrealans), [ERR:OVERFLOW](errors.html#overflow), and [ERR:SINGULAR MAT](errors.html#singularmat). If one of these errors occurs, the data point will be omitted.

For this reason, `DrawInv` can sometimes behave in an unexpected fashion: for example, it doesn't throw an error for list or matrix expressions (it won't graph anything, either).

## Error Conditions

- **[ERR:MODE](errors.html#mode)** is thrown if the calculator is not in [`Func`](func.html) mode when using `DrawInv`.

## Related Commands

- [`DrawF`](drawf.html)
- [`Tangent(`](tangent.html)
