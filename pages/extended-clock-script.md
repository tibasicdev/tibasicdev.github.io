# Day, Date & Time
|Routine Summary|Author|
|--- |--- |
|Shows the time, date, and day of week.|2Tie|

```
:getDate
:dayOfWk(Ans(1),Ans(2),Ans(3
:Disp sub("***SUN***MON**TUESWEDNES*THURS***FRI*SATUR",6Ans-5,6)+"DAY      //replace *s with spaces
:Disp getDtStr(getDtFmt
:Disp getTmStr(getTmFmt
```

First, the program acquires the date stored on your TI-84. Then it stores it and manipulates it to get the day of week. It then checks that and displays the result. Then it collects the formats to display the time and date.

## Optimization

Although the program is already very small (about 122 bytes), you can make it smaller by shortening the day names to three letters each.  This optimization would probably only benefit if you are including this in a larger program that you want as small as possible.

```
:Disp sub("SUNMONTUEWEDTHUFRISAT",3Ans-2,3
```

## Error Conditions

This program should not generate any errors if coded right.  It might display incorrect time if the clock is off.  Use [ClockOn](clockon.html) if it is.

## Related Routines

- [Day of the Week](day-of-week.html)
