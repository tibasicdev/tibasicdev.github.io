![The FnOff Command](68k_fnoff/fnoff.png "The FnOff Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|This command turns off all or a group of functions.|FnOff *[optional function numbers]*|This command works on all calculators.|
       
### Menu Location
- Press F4 from the Homescreen to enter the OTHER menu.
- Press 8 to select the FnOff command.
       
# The FnOff Command

The FnOff Command turns Graph functions off. The FnOff Command command can be used to clear the graph of any functions that the user has created before running any programs that might require the graph screen. The FnOff command can also be used to turn just one or a few functions off by stating the function number after the command FnOff:

```
:FnOn
:FnOff 2,3,4
```

The above code will turn on all functions, and then it will turn off only functions 2, 3, and 4. You can use this if you only want one or two functions to display, but you want all the functions entered so that they can be quickly graphed.

## Error Conditions

**[260 - Domain error](68k:errors.html#e260)** happens when the optional function argument is not in the range 1-99.

## Related Commands

- [68k:FnOn](68k:fnon.html)
