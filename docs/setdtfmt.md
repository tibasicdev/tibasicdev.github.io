![The setDtFmt( Command](setdtfmt/SETDTFMT.PNG "The setDtFmt( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets the date format of the clock on the TI-84+/SE.|setDtFmt(*value*)|TI-84+/SE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:
1. 2nd CATALOG to enter the command catalog
1. s to skip to commands starting with S
1. Scroll down to setDtFmt( and select it
       
# The setDtFmt( Command

The setDtFmt( command sets the date format of the clock on the TI-84+/SE calculators when displaying the date on the [mode screen](settings.html). There are three different formats available, and you simply use the respective value (can be either a literal number or a variable) to display the desired one: 1 (M/D/Y), 2 (D/M/Y), or 3 (Y/M/D). For example, this would set the date format to Month/Day/Year:

```
:setDtFmt(1
```
  
In order for the date format to work, you need to set the date using either the [setDate(](setdate.html) command, or by going into the set clock menu (accessible by pressing ENTER on the 'SET CLOCK' message that is displayed at the bottom of the mode screen). Of course, the date will only show up if the clock is on; if you need to turn the clock on, use the [ClockOn](clockon.html) command, or scroll down to the 'TURN CLOCK ON' message that is displayed in place of the clock on the mode screen and press ENTER twice.

## Related Commands

- [getDate](getdate.html)
- [setDate(](setdate.html)
- [getDtFmt](getdtfmt.html)
- [getDtStr(](getdtstr.html)
