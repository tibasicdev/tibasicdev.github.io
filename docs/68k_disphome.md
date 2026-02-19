![The DispHome Command](68k_disphome/DispHome.gif "The DispHome Command")
           
|Command Summary|Command Syntax|[Token Size](tokens.html)|
|--- |--- |--- |
|Returns the user to the homescreen|Main command, no special syntax|2 bytes|

### Menu Location
Press [CATALOG] [D] then scroll down until you see it.
       
# The DispHome Command
The DispHome command returns the user to the homescreen. This is very useful in a program that uses the I/O screen since ending a program with a command like [68k:Stop](68k:stop.html) will not automatically return the user to the homescreen. Take this example:
```
Prompt a
Pause
DispHome
```
This code will ask for a value for "a", then go to the homescreen. Had you not put the DispHome command there, you would have stayed at the I/O screen, which in some cases can be confusing.

## Optimization

The DispHome command also combines the functionality of the [68k:Stop](68k:stop.html) command. For example
```
DispHome
Stop

can be

DispHome
```

## Related Commands

- [68k:Disp](68k:disp.html)
- [68k:DispG](68k:dispg.html)
- [68k:DispTbl](68k:disptbl.html)
