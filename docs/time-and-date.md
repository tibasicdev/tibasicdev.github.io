# Time And Date Commands
The TI-84 Plus and TI-84 Plus SE, which have a built-in hardware clock, introduce several commands for dealing with time. Some of these rely on the built-in clock, while others are used for formatting times and dates and could technically have been introduced on earlier calculators. However, the only time/date command that is available on the pre-84 calculators is [dbd(](dbd.html).

All of these commands except dbd( can be found only through the command catalog (2nd CATALOG). [dbd(](dbd.html) can also be found in the Finance menu — 2nd FINANCE on the TI-83, and APPS 1:Finance... on the TI-83+ or higher.

Despite its name, the [Time](time.html) command has nothing to do with the clock. It is a mode setting for sequence graphs.


### Low-Level Commands

- **[startTmr](starttmr.html)** — This command returns the current value of a timer that is updated every second when the clock is enabled. This value doesn't correspond to any actual time, but can be used with [checkTmr(](checktmr.html) to get a time difference.
- **[checkTmr(](checktmr.html)** — checkTmr(X) is equivalent to [startTmr](starttmr.html)-X. This can be used to get the time elapsed since startTmr was used.
- **[ClockOn](clockon.html)**, **[ClockOff](clockoff.html)** — Enables or disables the hardware clock.
- **[isClockOn](isclockon.html)** — Tests if the clock is enabled or not.

### Time Commands

- **[setTime(](settime.html)** — Sets the current time, in hours, minutes, and seconds. If the clock is enabled, this time will be updated every second.
- **[getTime](gettime.html)** — Returns the current time as the list {hours, minutes, seconds}. This command is unaffected by time format.
- **[setTmFmt(](settmfmt.html)** — Sets the time format - 12 hour, or 24 hour.
- **[getTmFmt](gettmfmt.html)** — Returns this time format setting.
- **[getTmStr(](gettmstr.html)** — Returns the current time as a string, affected by time format (though you can override it with an optional argument).


### Date Commands 

- **[setDate(](setdate.html)** — Sets the current date (year, month, and day). If the clock is enabled, this date will be updated as needed.
- **[getDate](getdate.html)** — Returns the current date as the list {year, month, day}. This command is unaffected by date format.
- **[setDtFmt(](setdtfmt.html)** — Sets the date format - 1 for month/day/year, 2 for day/month/year, or 3 for year/month/day.
- **[getDtFmt(](getdtfmt.html)** — Returns this date format setting.
- **[getDtStr(](getdtstr.html)** — Returns the current date as a string, affected by date format (though you can override it with an optional argument).

### Time/Date Manipulation

- **[timeCnv(](timecnv.html)** — Converts a number of seconds into a list of {days, hours, minutes, seconds} representing the same time lapse.
- **[dayOfWk(](dayofwk.html)** — Returns the day of week (Sunday through Saturday encoded as 1 through 7) of a specified date.
- **[dbd(](dbd.html)** — Returns the number of days between two dates — this command is available on all calculators, not just the 84+/SE.
