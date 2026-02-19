![The setDate( Command](setdate/SETDATE.PNG "The setDate( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets the date of the clock on the TI-84+/SE.|setDate(*year*,*month*,*day*)|TI-84+/SE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:
1. 2nd CATALOG to enter the command catalog
1. s to skip to commands starting with S
1. Scroll down to setDate( and select it
       
# The setDate( Command

The setDate( command sets the date of the clock on the TI-84+/SE calculators. It takes three arguments: the year, the month, and the day. All three of these must be integers; in particular, year must be four digits, and month and day can be one or two digits. They represent the associated value that goes with a respective date. For example, this would set the date to January 1, 2008:

```
:setDate(2008,1,1
```

Once you have set the date, you can display it in three different formats on the [mode screen](settings.html) using the [setDtFmt(](setdtfmt.html) command: Month/Day/Year, Day/Month/Year, or Year/Month/Day. Of course, the date will only show up if the clock is on; if you need to turn the clock on, use the [ClockOn](clockon.html) command or select 'TURN CLOCK ON' , displayed in place of the clock on the mode screen.



## Related Commands

- [getDate](getdate.html)
- [getDtFmt](getdtfmt.html)
- [getDtStr(](getdtstr.html)
- [setDtFmt(](setdtfmt.html)
