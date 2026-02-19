![The dayOfWk command](68k_dayofwk/dayofwk.png "The dayOfWk command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Returns an integer from 1-7 that shows what day of week it is for a specific date.|dayOfWk(*year, month, day*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|
       
### Menu Location

# The dayOfWk command

The `dayOfWk` command returns an integer from 1 through 7 which shows what day of the week it was on a certain date. The Ti-89 Titanium manual says that this function may not give accurate results for years prior to 1583 (pre-Gregorian calendar).

| Integer value: | Day of the week: |
| --- | --- |
| 1 | Sunday |
| 2 | Monday |
| 3 | Tuesday |
| 4 | Wednesday|
| 5 | Thursday|
| 6 | Friday |
| 7 | Saturday |

```
:dayOfWk(1948,9,6)
:      2
:dayOfWk(1600,1,15)
:      7
```

The above examples find that September 6<sup>th</sup>,1948 was a Monday and that January 15<sup>th</sup>, 1600 was a Saturday. It also works with future dates, in case you want to use that in a program.

## Related Commands

- [`68k:getDate()`](68k:getdate().html)
- [`68k:setDate()`](68k:setdate().html)
- [`68k:timeCnv()`](68k:timecnv().html)
