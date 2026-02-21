![The isClkOn() Command](68k_isclkon/isclkon.png "The isClkOn() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Checks if the hardware clock is turned on.|isClkOn()|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

       
# The isClkOn() Command

The isClkOn() command checks if the calculator's clock (which is used by most [68k:time and date](68k:time-and-date.html) commands) is running or stopped. The result of isClkOn() is a truth value — true if the clock is on, and false if the clock is off — which makes it perfect for a condition in commands such as [68k:If](68k:if.html):
```
:If isClkOn() Then
: Disp "Clock is running."
:Else
: Disp "Clock is stopped."
:EndIf
```

The isClkOn() command, though useful, isn't often called for. For instance, there's no need to check if the clock is on if you're planning to turn it on anyway:
```
:If not isClkOn()
: ClockOn

should just be

:ClockOn
```
One use for [68k:isClkOn()](68k:isclkon.html) is in functions, which aren't allowed to change the global status of the calculator with commands like [68k:ClockOn](68k:clockon.html) or [68k:ClockOff](68k:clockoff.html). Instead, you might do the next best thing, and return an error message if the clock is turned off.

## Related Commands

- [68k:ClockOn](68k:clockon.html)
- [68k:ClockOff](68k:clockoff.html)
- [68k:startTmr()](68k:starttmr.html)
