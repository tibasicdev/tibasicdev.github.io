![The FnOn Command](68k_fnon/fnon.png "The FnOn Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|This command turns on all or a group of functions.|FnOn *[optional function numbers]*|This command works on all calculators.|
       
### Menu Location
- Press F4 from the Homescreen to enter the OTHER menu.<br>* Press 7 to select the FnOn command.
# The FnOn Command

The FnOn command turns on one or a group of functions. The optional argument specifies which functions are to be turned on, and if there is no argument, then all the functions are turned on, not just the specified functions. This is used mostly to turn back on functions after they are turned off by the similar FnOff command, or it is used to turn back on functions after a program that has used the graphscreen.

```
:FnOff
:FnOn 4,7,9,20
```

The above code will turn off all functions, and then it will turn on only functions 4, 7, 9, and 20. This is useful if you want to graph only a few functions, but still have the rest of the functions stored in the calculator.

## Error Conditions



## Related Commands

- [68k:FnOff](68k:fnoff.html)
