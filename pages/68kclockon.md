![The ClockOn Command](68k_clockon/clockon.png "The ClockOn Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Turns on the hardware clock.|ClockOn|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|2 bytes|
       
### Menu Location
N/A

# The ClockOn Command

The `ClockOn` command turns on the calculator's clock, used by most [68k:time and date](68k:time-and-date.html) commands. Only when the clock is on, will the value returned by [`68k:startTmr()`](68k:starttmr().html), [`68k:getTime()`](68k:gettime().html), and other commands actually change with the passage of time. If you write a program that uses any of these commands, be sure to include this command at the beginning of the program.

Since it modifies the global status of the calculator, `ClockOn` can't be used inside a function. If you're writing a function that depends on measuring time (so you need the clock to be on), the best thing you can do is use the [`68k:isClkOn()`](68k:isclkon().html) command to check if the clock is on or off, and return an error message if it's off.

## Error Conditions



## Related Commands

- [`68k:ClockOff`](68k:clockoff.html)
- [`68k:isClkOn()`](68k:isclkon().html)
- [`68k:startTmr()`](68k:starttmr().html)
