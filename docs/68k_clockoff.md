![The ClockOff Command](68k_clockoff/clockoff.png "The ClockOff Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Turns off the hardware clock.|ClockOff|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|2 bytes|
       
### Menu Location
N/A

       
# The ClockOff Command

The `ClockOff` Command turns off the calculator's clock as far as the [68k:time and date](68k:time-and-date.html) commands are concerned: that is, the timer used by [`68k:startTmr()`](68k:starttmr.html), [`68k:getTime()`](68k:gettime.html), and other commands will not keep updating every second, but will stay the same until the clock is turned on again.

It's not usually a good idea to use this in a program: there's no real benefit to doing so (it doesn't make the calculator run faster or anything like that) but there's the real drawback that it throws off the calculator's time. However, the mere existence of this command means that you should probably use [`68k:ClockOn`](68k:clockon.html) anytime you need to use the time and date commands.

Since it modifies the global status of the calculator, `ClockOff` can't be used in a function. 

## Error Conditions



## Related Commands

- [`68k:ClockOn`](68k:clockon.html)
- [`68k:isClkOn()`](68k:isclkon.html)
- [`68k:startTmr()`](68k:starttmr.html)
