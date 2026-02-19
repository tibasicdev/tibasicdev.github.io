![The # Command](68k_indirection/indirection.png "The # Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Gets a variable given its name as a string.|#*var-name*|This command works on all calculators.|2 bytes|
       
### Menu Location
On a widescreen calculator, press 2nd # to paste #.<br><br>Or, on any calculator model, press:<br>* 2nd CHAR to enter the CHAR popup menu.<br>* 3 to enter the Punctuation submenu.<br>* 3 again to paste #.
# The # Command

The # operator takes a string containing a variable name, such as "x", and gives you the variable itself. This can be used to get the value of that variable (kind of like a weaker version of [expr()](68k:expr.html)), but the # operator really shines when you need to refer to the variable itself: storing to it, for example. 5→expr("var") will give you an error. 5→#"var", however, will work.

```
:"x"→str
:5→#str
           5
:x
           5
:DelVar #str
:x
           x
```

You'll see # called the "indirection" operator (for instance, in the command catalog). This is because using # is an indirect way of accessing a variable's value: you don't have the variable itself to work with, just its name. 

## Advanced Uses

The # command is particularly useful for dealing with picture variables, if you don't know the exact name of the picture ahead of time. For example, you might have two pictures, called 'cat' and 'dog', that you need to display depending on whether x=1 or x=2. This can be done with an [68k:If](68k:if.html) command, but that gets more and more complicated as you add pictures. On the other hand, you can always do this:
```
:{"cat","dog"}→pics
:RclPic #(pics[x])
```

The # command is necessary here because [68k:RclPic](68k:rclpic.html) and commands like it want the actual picture variable as an argument, not a string with its name; [68k:expr()](68k:expr().html) wouldn't work either because it would try to find the value of 'cat', and get an error.

------

Whenever you're dealing with external files created by someone else (such as external levels for a game), you don't know the variable names ahead of time, so you'll need the # operator. For the example of an external level, you would first input the variable name of the level into a string variable (say, the variable 'level'). Then you can use '#level', just as you would a regular variable, to refer to it.

## Optimization

In many cases, both # and [68k:expr()](68k:expr().html) will do the same thing. In these cases, it's still better to use #, because it's faster.

## Error Conditions



## Related Commands

- [68k:expr()](68k:expr().html)
- [→](68k:store.html)
- [68k:DelVar](68k:delvar.html)
