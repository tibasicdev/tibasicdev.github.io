# Day of Week
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Calculates the day of week of a date, without using [dayOfWk(](dayofwk.html) (because it's only available on the 84+ and 84+SE)|*D* - The day<br>*M* - The month<br>*Y* - The year (1950 through 2049)|*Ans* - 0-6 = the day of week (Sunday - Saturday)|D, M, Y, Ans|[file weekday.zip]|

```
:round(7fPart(dbd(101.5,DE2+M+fPart(.01Y))/7
```

Using the [dbd(](dbd.html) command, we return the number of days between the given date and January 1, 1950, our base date. dbd('s argument, in this case, is of the form DDMM.YY, so we put the date we're given in that form with D[E](e-ten.html)[[/size]]2+M+fPart(.01Y. Once we have the number of days between the two dates, we divide it by seven (as there are seven days in a week) to get the number of weeks.

However, we are not interested in the number of weeks between two dates, we are interested in how far into the week we are. That would be the fractional part of the number of weeks. For example, if there was fourteen days between two dates (the first date being a Sunday) and we divide that by seven, we would have the equation 14/7=2.00. The .00 means that the week hasn't yet begun (and so, the day is Sunday).

If there was 15 days between two dates, the equation would give 15/7=2.1428571. The .1428571 means that we are .1428571 into the week, and if we multiply that by seven, we get the equation .1428571*7=1. This means that we are one day into the week (and so, the day is Monday). So in our formula, after finding out the number of days between two dates, we find the fractional part of it, and multiply that by seven. Finally, [round(](round.html) gets rid of any minor rounding errors.

As the 1<sup>st</sup> of January, 1950 was a Sunday (which is the date we have inputed into the above routine), so the number of days into the week will always be relative to Sunday. That is, the output 0 through 6 is relative to the days Sunday through Saturday respectively. If you want 0 to be Monday instead, make the base date January 2 instead by changing 101.5 to 201.5.

This routine can handle dates from January 1, 1950 to December 31, 2049. For other dates, it will assume the year is in that range instead. There is also an [alternative routine](day-of-week-(alternative).html) that handles dates in an unlimited range.

## Display Day

Append the following code to display the day of the week:

```
:Disp sub("SUNDAY***MONDAY***TUESDAY**WEDNESDAYTHURSDAY*FRIDAY***SATURDAY*",9Ans+1,9      //replace *s with spaces
```
Or this code, which should display the day of the week, only the display method takes less space and space pads it.
```
Disp sub("***SUN***MON**TUESWEDNES*THURS***FRI*SATUR",6Ans+1,6)+"DAY       //replace *s with spaces
```
## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** if the date is invalid.

## Related Routines
- [Day of the Week (Alternative)](day-of-week-(alternative).html)
