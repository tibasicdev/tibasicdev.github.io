![The Select( Command](select/SELECT.GIF "The Select( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Allows the user to select a subinterval of any enabled Scatter or xyLine plots.|Select(*x-list name*, *y-list name*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2nd LIST to access the list menu.
1. RIGHT to access the OPS submenu.
1. 8 to select Select(, or use arrows and ENTER.
       
# The Select( Command

When Select( is called, if it has any [Scatter](plotn.html#scatter) or [xyLine](plotn.html#xyline) plots to work with, it displays the graph screen and allows the user to pick a left bound and then a right bound on one of the plots (the left and right keys move from point to point, while the up and down keys switch plots). Then, it stores all the points between those bounds to *x-list name* and *y-list name*. Finally, it sets the chosen plot to use *x-list name* and *y-list name* as its X and Y lists.

## Optimization

It isn't necessary to add the ∟ symbol before list names:

```
:Select(∟X,∟Y)
can be
:Select(X,Y)
```

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if there are no enabled Scatter or xyLine plots for the command to work with.
 
## Related Commands

- [Plot1(](plotn.html), [Plot2(](plotn.html), [Plot3(](plotn.html)
- [Input](input.html)
