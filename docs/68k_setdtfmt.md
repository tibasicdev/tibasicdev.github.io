![The setDtFmt() Command](68k_setdtfmt/setdtfmt.png "The setDtFmt() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Sets the default date format.|setDtFmt(*format-number*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

       
# The setDtFmt() Command

The setDtFmt() sets the default format for dates: this format is used in the top right corner of the Apps Desktop, and also as the format for the output of [68k:getDtStr()](68k:getdtstr.html) (when it's used without a parameter to override this setting).

The eight possible formats each have a number associated to them, which is the number you should pass to setDtFmt(). It will return the number of the previous setting, which is convenient if you want to restore it later.

The eight formats are as follows (dd, mm, and yy are the date, month, and year respectively, in two digits)

| Format Number | Date Format |
| --- | --- |
| 1 | "mm/dd/yy" |
| 2 | "dd/mm/yy" |
| 3 | "mm.dd.yy" |
| 4 | "dd.mm.yy" |
| 5 | "yy.mm.dd" |
| 6 | "mm-dd-yy" |
| 7 | "dd-mm-yy" |
| 8 | "yy-mm-dd" |

Typically, you'd only use this command in a program if you needed to use getDtStr() many times with the same format. In that case, save the return value of setDtFmt(), and use it to restore the date format at the end of the program.

## Error Conditions



## Related Commands

- [68k:getDtFmt()](68k:getdtfmt.html)
- [68k:getDtStr()](68k:getdtstr.html)
