![The End Command](end/for/FOR_ANIMATED.gif "The End Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Indicates the end of a block of statements.|If *condition*<br>Then<br>*statement(s)*<br>End<br><br>While *condition*<br>*statement(s)*<br>End<br><br>Repeat *condition*<br>*statement(s)*<br>End<br><br>For(*variable*,*start*,*end*[,*step*])<br>*statement(s)*<br>End|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program, press:
1. PRGM to enter the PRGM menu
1. 7 to choose End, or use arrows
       
# The End Command

The `End` command is used together with the different control structures, including the [`If`](if.html) conditional, [`While`](while.html) loop, [`Repeat`](repeat.html) loop, and [`For(`](for.html) loop, to indicate the *end* of the code block for the respective control structure. In the case of the `If` conditional, you also need to add a [`Then`](if.html) command, which is used to indicate the beginning of the control structure.

## Advanced Uses

You can prematurely end a control structure by using a single `If` conditional and then having `End` be its executed command. Because the calculator stores the positions of the `End` commands, it will take this `End` command to be the `End` command of the control structure.

```
:If <condition>
:End
```

One of the most important features of the `End` command is putting multiple control structures inside of each other (known as nesting). While you typically nest `If` conditionals inside of loops, you can actually nest any control structure inside of any other control structure — this even works when using the same control structure, such as a `While` loop inside of another `While` loop.

When nesting control structures, you need to remember to put the appropriate number of `End` commands to close the appropriate structure. The easiest way to keep track of lots of nested control structures is to code the first part, add an `End` immediately after the beginning, and then hit 2nd DEL on the line with the `End`, then hit ENTER a lot of times.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this statement is used outside a program.
- **[ERR:SYNTAX](errors.html#invalid)** occurs if this statement is used before a logic block has been initiated.

## Related Commands

- [`If`](if.html)
- [`Then`](then.html)
- [`While`](while.html)
- [`Repeat`](repeat.html)
- [`For(`](for.html)
