![The getDate() command](68k_getdate/getDate.png "The getDate() command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the current date set on the calculator and returns it in list format.|getDate()|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

       
# The getDate() command

The getDate() command checks the date that the calculator is set to, and then returns it in a list format. The list will always be in the format {year, month, day}. To change this list to another format, you can use the closely related [68k:getDtStr()](68k:getdtstr.html) option, which just returns the date in a string format, not as a list. The [68k:setDtFmt()](68k:setdtfmt.html) command does not work on this command, but it will change the format that the calculator returns the [68k:getDtStr()](68k:getdtstr.html) command as.

For example, if the calculator's date was set to March 14th, 2011, the getDate() command would return the following:
```
:getDate()
:     {2011 3 14}
```

## Related Commands

- [68k:getDtStr()](68k:getdtstr.html)
- [68k:getDtFmt()](68k:getdtfmt.html)
- [68k:setDate()](68k:setdate.html)
- [68k:setDtFmt()](68k:setdtfmt.html)
