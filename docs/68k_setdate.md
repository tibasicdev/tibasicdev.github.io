![The SetDate command](68k_setdate/setdate.png "The SetDate command")
       
|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |
|setDate(*year, month, day*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|
       
### Menu Location

       
# The SetDate command

This command sets the calculator's date to whatever is specified in the command. The year must fall in the range 1997 to 2132 for this command to work.

```
:setDate(2001, 10, 31)
:      {2001, 11, 1}
```

The above example has set the calculator's date to October 31<sup>st</sup>, 2001, and the date it was set at originally was November 1<sup>st</sup>, 2001.

## Error Conditions

**[40 - Domain error](68k:errors.html#e40)** happens when the year is outside of the range of 1997 to 2132, or the month is above or below 0 to 12, or the date is above or below 0 to 31.

## Related Commands

- [68k:getDate()](68k:getdate.html)
- [68k:getDtStr()](68k:getdtstr.html)
- [68k:setDtFmt()](68k:setdtfmt.html)
- [68k:getDtFmt()](68k:getdtfmt.html)
