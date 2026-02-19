![The PlotsOn Command](plotson/PLOTSON.GIF "The PlotsOn Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Turns stat plots (all of them, or only those specified) on.|PlotsOn [*plot numbers*]|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># 2nd PLOT to access the stat plot menu.<br># 5 to select PlotsOn, or use arrows and ENTER.
# The PlotsOn Command

By itself, the command will turn on all three stat plots. 

If it is given arguments, there can be any number of them (actually, no more than 255, but this won't stop most people), but they must all be numbers 1 to 3. Then, the command will only turn on the specified plots. Unlike some commands, it is okay to give PlotsOn an expression as an argument (for example, PlotsOn X), as long as it has a value of 1, 2, or 3.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if a plot that is not 1, 2, or 3 is specified.

## Related Commands

- [Plot1(, Plot2(, Plot3(](plotn.html)
- [PlotsOff](plotsoff.html)
- [Select(](select.html)
