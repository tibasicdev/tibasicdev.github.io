![The setTime() Command](68k_settime/settime.png "The setTime() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Sets the current time on the calculator's clock, returning the previous time setting.|setTime(*hours*,*minutes*,*seconds*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

# The setTime() Command

The setTime() command changes the time of day on the calculator's clock (give it the new time in hours, minutes, and seconds, in that order). The value it returns is the previous time setting, as a list of {*hours*,*minutes*,*seconds*}.

setTime() respects the current [time zone](68k:settmzn.html): if you set the time to 8 AM, it will change the time to 8 AM in the time zone you're using, not necessarily to 8 AM GMT. Make sure to change the time zone before you set the time, if you plan to do both, or you'll get the wrong result.

The calculator measures time starting from 00:00 GMT on January 1, 1997. Although [68k:setDate()](68k:setdate().html) will reject any date earlier than that, with a combination of setTime() and setTmZn() you might actually end up with an earlier time than that. If this happens, the calculator keep counting the time correctly, but return a time of 00:00 GMT until it reaches a normally valid time.

A final quirk of setTime() is that it affects the output of [68k:startTmr()](68k:starttmr().html) and [68k:checkTmr()](68k:checktmr().html). So if you're timing a section of your program, and use setTime() in the middle of that section, the time lapse will get thrown off.

## Error Conditions




## Related Commands

- [68k:setDate()](68k:setdate().html)
- [68k:getTime()](68k:gettime().html)
- [68k:getTmStr()](68k:gettmstr().html)
