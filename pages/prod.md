![The prod( Command](prod/PROD.GIF "The prod( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the product of all or part of a list.|prod(*list*[,*start*,[*end*]])|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># 2nd LIST to access the list menu.<br># LEFT to access the MATH submenu.<br># 6 to select prod(, or use arrows and ENTER.
# The prod( Command

The prod( command calculates the product of all or part of a list. 

When you use it with only one argument, the list, it multiplies all the elements of the list. You can also give it a bound of *start* and *end* and it will only multiply the elements starting and ending at those indices (inclusive).

```
prod({1,2,3,4,5})
    120
prod({1,2,3,4,5},2,4)
    24
prod({1,2,3,4,5},3)
    60
```

## Optimization

If the value of *end* is the last element of the list, it can be omitted: 
```
prod({1,2,3,4,5},3,5)
can be
prod({1,2,3,4,5},3)
```

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** if the starting or ending value aren't positive integers.
- **[ERR:INVALID DIM](errors.html#invaliddim)** if the starting or ending value exceed the size of the list, or are in the wrong order.

## Related Commands

- [sum(](sum.html)
- [dim(](dim.html)
- [seq(](seq-list.html)
