![The TimeCnv command](68k_timecnv/timecnv.png "The TimeCnv command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Converts seconds into a list containing days, hours, minutes, and seconds.|dayOfWk(*seconds*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|
       
### Menu Location

       
# The TimeCnv command

This command converts a number of seconds into a list containing {days, hours, minutes, seconds}.

```
:timeCnv(152442117)
:      {1764 9 1 57}
```

The above example has converted 152,442,117 seconds into 1764 days, 9 hours, 1 minute, and 57 seconds.

## Advanced Uses

This command can be used to easily convert the output of the [68k:startTmr()](68k:starttmr().html) or the [68k:checkTmr()](68k:checktmr().html) commands to a more readable and understandable format.

## Related Commands

- [68k:startTmr()](68k:starttmr().html)
- [68k:checkTmr()](68k:checktmr().html)
- [68k:dayOfWk()](68k:dayofwk().html)
