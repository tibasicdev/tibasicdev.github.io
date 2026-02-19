# Day Of Week (Alternative)
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Calculates the day of week of a date, without using [dayOfWk(](dayofwk.html) (because it's only available on the 84+ and 84+SE)|*D* - The day<br>*M* - The month<br>*Y* - The year (Any year at all)|*Ans* - 0-6 = the day of week (Sunday - Saturday)|D, M, Y, Ans|Michael Keith|[file weekday2.zip]|

```
:Y-(M<3
:round(7fPart((int(23M/9)+D+4+Y+int(Ans/4)-int(Ans/ᴇ2)+int(Ans/400)-2(M≥3))/7
```

This is the TI-BASIC version of a Day of Week formula in C by Michael Keith, found at the beginning of [this page](http://cadaeic.net/calendar.htm). The formula is `(d+=m<3?y—:y-2,23*m/9+d+4+y/4-y/100+y/400)%7`, a mere 45 characters. In comparison with the other Day of the Week routine, this handles not just the years between 1950 and 2049.[[footnote]] If you have a TI-84+/SE or a TI-8+ OS 1.15 (at least), replace `int(Ans/ᴇ2)` with `int(sub(Ans))`. [[/footnote]]

There is also a human-readable version on the site, as follows.
> dayofweek = ( [23m/9] + d + 4 + y + [z/4] - [z/100] + [z/400] - 2 (if m ≥ 3) ) mod 7
> 
> where 
> [x] means to truncate downward to the nearest integer, and
> z = y - 1 if m < 3,
> z = y otherwise.

## Why it Works

Directly from [this website](http://cadaeic.net/calendar.htm):
> Assume for the moment that February has 30 days (we'll correct for this later). Then the number of days in each of month is 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, which modulo 7 is 3, 2, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3. Now stick a 2 before this sequence and a 2 3 2 3 3 after it, and you get (2) 3 2 3 2 3 2 3 3 2 3 2 3 (2 3 2 3 3), which is just 2,3,2,3,2,3,2,3,3 repeated twice. But - this is the key - these numbers are the first differences of the sequence [23m/9] = (2,5,7,10,12,15,17,20,23). Therefore, the term [23m/9] adds the sum (mod 7) of the total number of days in months 1 to m-1 to the day of the week, thus correctly adjusting the formula for the months that have passed prior to m.
> 
> The next term, d, simply adjusts the sum based on the day of the month. The constant term, 4, shifts the result to correctly align with the calendar.[[footnote]] Note: You can change the constant to 5 in the formula for returning Monday as 0, Tuesday as 1, etc. [[/footnote]] The next term, y, adds 1 for each passing year, since 365 = 1 mod 7. The next three terms add 1 (the leap day) for each leap year that's passed since the "base date", including this year. To complete the correct formula requires handling two exceptions:
> 
> # If m ≥ 3 (we are later than February), then we must subtract 2 because February actually has 28 days rather than the 30 we assumed.
> # If m < 3 (the opposite case), then we must use z = y-1 rather than z = y. This causes the leap-day correction term to not include the leap day for the given year, since in this case it hasn't yet occured.

## Display Day

Just as the other formula, append the following code to display the day of the week,
```
:Disp sub("SUNDAY***MONDAY***TUESDAY**WEDNESDAYTHURSDAY*FRIDAY***SATURDAY*",9Ans+1,9      //replace *s with spaces
```
Or you can use the alternative code, which is smaller and space-pads it.
```
Disp sub("***SUN***MON**TUESWEDNES*THURS***FRI*SATUR",6Ans+1,6)+"DAY       //replace *s with spaces
```
## Error Conditions

- None known.

## Related Routines

- [Day of Week](day-of-week.html)
- [Day, Date & Time](extended-clock-script.html)
- [Easter Calculation](easter-calculation.html)
