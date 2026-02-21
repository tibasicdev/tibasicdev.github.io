# Time And Date Commands
The OS version 2.07 update introduced several commands for dealing with times and dates. Some of these rely on the built-in clock, while others are used for formatting. 

TI-84+ programmers will not find many differences in function here — these commands were added to both calculator series at the same time, and are almost exactly the same. The only difference is the addition of the [68k:getTmZn()](68k:gettmzn.html) and [68k:setTmZn()](68k:settmzn.html) commands, and the absence of a days-between-dates command.



### Low-Level Commands

- **[68k:startTmr()](68k:starttmr.html)** — This command returns the current value of a timer that is updated every second when the clock is enabled. This value doesn't correspond to any actual time, but can be used with [68k:checkTmr()](68k:checktmr.html) to get a time difference.
- **[68k:checkTmr()](68k:checktmr.html)** — checkTmr(t) is equivalent to [68k:startTmr()](68k:starttmr.html)-t. This can be used to get the time elapsed since startTmr was used.
- **[68k:ClockOn](68k:clockon.html)**, **[68k:ClockOff](68k:clockoff.html)** — Enables or disables the hardware clock.
- **[68k:isClkOn()](68k:isclkon.html)** — Tests if the clock is enabled or not.

### Time Commands

- **[68k:setTime()](68k:settime.html)** — Sets the current time, in hours, minutes, and seconds. If the clock is enabled, this time will be updated every second.
- **[68k:getTime()](68k:gettime.html)** — Returns the current time as the list {hours, minutes, seconds}. This command is unaffected by time format.
- **[68k:setTmFmt()](68k:settmfmt.html)** — Sets the time format - 12 hour, or 24 hour.
- **[68k:getTmFmt()](68k:gettmfmt.html)** — Returns this time format setting.
- **[68k:getTmStr()](68k:gettmstr.html)** — Returns the current time as a string, affected by time format (though you can override it with an optional argument).
- **[68k:setTmZn()](68k:settmzn.html)** — Sets the current time zone, as an offset (in minutes) from GMT.
- **[68k:getTmZn()](68k:gettmzn.html)** — Returns the current time zone.





### Date Commands 

- **[68k:setDate()](68k:setdate.html)** — Sets the current date (year, month, and day). If the clock is enabled, this date will be updated as needed.
- **[68k:getDate()](68k:getdate.html)** — Returns the current date as the list {year, month, day}. This command is unaffected by date format.
- **[68k:setDtFmt()](68k:setdtfmt.html)** — Sets the date format - 1 for month/day/year, 2 for day/month/year, or 3 for year/month/day.
- **[68k:getDtFmt()](68k:getdtfmt.html)** — Returns this date format setting.
- **[68k:getDtStr()](68k:getdtstr.html)** — Returns the current date as a string, affected by date format (though you can override it with an optional argument).

### Time/Date Manipulation

- **[68k:timeCnv()](68k:timecnv.html)** — Converts a number of seconds into a list of {days, hours, minutes, seconds} representing the same time lapse.
- **[68k:dayOfWk()](68k:dayofwk.html)** — Returns the day of week (Sunday through Saturday encoded as 1 through 7) of a specified date.
