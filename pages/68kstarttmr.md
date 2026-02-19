![The startTmr() Command](68k_starttmr/starttmr.png "The startTmr() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the value of the system clock.|startTmr()|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|3 bytes|
       
### Menu Location
N/A

# The startTmr() Command

The startTmr() command returns the number of seconds that passed since 00:00 GMT of January 1, 1997 — as far as the calculator knows, anyway, since this value is adjusted every time the current time and date changes with [68k:setTime()](68k:settime().html) or [68k:setDate()](68k:setdate().html). If the clock is running, this number is also updated every second, which is how the calculator keeps track of time.

Together with [68k:checkTmr()](68k:checktmr().html), startTmr() can be used to measure off a time interval (in seconds) while a program is running (make sure to use [68k:ClockOn](68k:clockon.html) first). the name of the commands reflects their use: you can think of a startTmr() call as creating and starting a timer:
```
:startTmr()→timer
```

The checkTmr() command will then return the number of seconds that have elapsed on the timer (without stopping it):
```
:Disp "Seconds elapsed:",checkTmr(timer)
```

This is a good abstraction and you don't need to know the details of how startTmr() and checkTmr() work to use them. In reality, checkTmr(x) returns startTmr()-x, so using it on the result of startTmr() gives a time difference.

Because both startTmr() and checkTmr() deal with whole numbers of seconds, the resulting difference in time could be off by up to a second in either direction. That is, if checkTmr() gives 15 seconds as the time, you know the time that actually passed is between 14 and 16 seconds.

## Advanced Uses

The startTmr() and checkTmr() commands can be used to figure out how much time a command or routine takes with much greater precisions by running it multiple times. For example:
```
:startTmr()→t
:For i,1,1000
: somecmd()
:EndFor
:Disp checkTmr(t)
```
Suppose that the result displayed was 100 seconds. This is accurate to 1 second, so the actual time was between 99 and 101 seconds. However, this actual time is for 1000 repetitions of somecmd() (we assume that the time the code to increment i takes is negligible, although that, too, may be taken into account). So somecmd() repeated only once takes between 99/1000 and 101/1000 seconds, so the actual time is 100 ms, measured to within 1 millisecond error.

See [68k:Timings](68k:timings.html) for more information on this, as well as the results of some common comparisons.

## Related Commands

- [68k:checkTmr()](68k:checktmr().html)
- [68k:ClockOn](68k:clockon.html)
- [68k:ClockOff](68k:clockoff.html)
- [68k:getTime()](68k:gettime().html)

## See Also

- [68k:Timings](68k:timings.html)
