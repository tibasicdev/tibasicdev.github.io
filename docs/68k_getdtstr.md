![The getDtStr() Command](68k_getdtstr/getdtstr.png "The getDtStr() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the current date in a string.|getDtStr([*format*])|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

# The getDtStr() Command

The getDtStr() command returns the current date in a string. The date can be in one of eight formats, numbered from 1 to 8. This format can be given to getDtStr() directly: for instance, getDtStr(5) will return the date in the fifth format. Or, you can set a default format with the [68k:setDtFmt()](68k:setdtfmt().html) command, and getDtStr() will use that format when it's not given a specific format to use.

The eight formats are as follows (dd, mm, and yy are the date, month, and year respectively, in two digits)

| Format Number | Result of getDtStr() |
| --- | --- |
| 1 | "mm/dd/yy" |
| 2 | "dd/mm/yy" |
| 3 | "mm.dd.yy" |
| 4 | "dd.mm.yy" |
| 5 | "yy.mm.dd" |
| 6 | "mm-dd-yy" |
| 7 | "dd-mm-yy" |
| 8 | "yy-mm-dd" |

Formats 5 and 8 are useful in that if you store dates in either of those format, sorting the strings will sort the dates in chronological order.

## Error Conditions



## Related Commands

- [68k:getDate()](68k:getdate().html)
- [68k:getDtFmt()](68k:getdtfmt().html)
- [68k:setDate()](68k:setdate().html)
- [68k:setDtFmt()](68k:setdtfmt().html)
