![The Get( Command](get/GET.GIF "The Get( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Gets a variable's value from a connected calculator or CBL device.|Get(*variable*)|TI-83/84/+/SE/CSE/CE*|1 byte<br><br><br><sub>*OS 5.1.5 or later</sub>|

### Menu Location
While editing a program, press:
1. PRGM to access the program menu.
1. RIGHT to access the I/O menu.
1. ALPHA A to select Get(.
       
# The Get( Command

The `Get(` command is meant for use with the CBL (Calculator Based Laboratory) device, or other compatible devices. When the calculator is connected by a link cable to such a device, `Get(*variable*)` will read data from the device and store it to *variable*. Usually, this data is a list, and so you want to `Get(L₁)` or some other list variable.

## Advanced Uses

In fact, the `Get(` command can also be used for linking two calculators, in which case it functions precisely like [`GetCalc(`](getcalc.html). This is probably for compatibility with the TI-82, which used `Get(` rather than `GetCalc(` for linking two calculators. However, since this isn't a documented feature (in fact, your TI-83+ manual will insist that `Get(` **cannot** be used in this way), it isn't guaranteed to work with future calculator versions.

## Optimization

Nevertheless, using `Get(` instead of `GetCalc(` will make your program smaller, and probably preserve functionality.

## Norland Robot
The `Get(` command is usually used after a [`Send`](send.html) command to confirm its transmission like this: `Get(*var*)`. The variable in the parentheses is where the time of the robot's movement is stored. You can display the time moved with a [`Disp`](disp.html) command.


## Related Commands

- [`GetCalc(`](getcalc.html)
- [`Send(`](send.html)
