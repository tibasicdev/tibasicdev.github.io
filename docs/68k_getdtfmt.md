![The getDtFmt() Command](68k_getdtfmt/getdtfmt.png "The getDtFmt() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the current default date format.|getDtFmt()|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

       
# The getDtFmt() Command

The getDtFmt() returns the number of the current default date format for [68k:getDtStr()](68k:getdtstr.html) (that is, the format that getDtStr() with no parameters will use). This same format is also used to display the time in the corner of the Apps Desktop.

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

In a program, it's usually unnecessary to use getDtFmt(). Most of the time, you'll just use getDtStr() with a format already specified; in the rare exceptions where you need to use getDtStr() a lot with the same format, you'd use [68k:setDtFmt()](68k:setdtfmt.html) to pick the format you want, save the result, and use it to restore the date format at the end of the program.

## Related Commands

- [68k:getDtStr()](68k:getdtstr.html)
- [68k:setDtFmt()](68k:setdtfmt.html)
