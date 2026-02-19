![The checkTmr() Command](68k_checktmr/checktmr.png "The checkTmr() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Checks the value of the system clock.|checkTmr(*time*)|This command requires a calculator with AMS version 2.07 or higher (it will also work on any TI-89 Titanium or Voyage 200 calculator)|2 bytes|
       
### Menu Location
N/A

# The checkTmr() Command

The `checkTmr()` command, together with [`68k:startTmr()`](68k:starttmr().html) uses the built-in system clock to measure the time (in seconds) that passed between two points of the program. Make sure that the clock is on (with [`68k:ClockOn`](68k:clockon.html) before using these).

The name of the commands reflects their use: you can think of a `startTmr()` call as creating and starting a timer:
```
:startTmr()→timer
```

The `checkTmr()` command will then return the number of seconds that have elapsed on the timer (without stopping it):
```
:Disp "Seconds elapsed:",checkTmr(timer)
```

This is a good abstraction and you don't need to know the details of how `startTmr()` and `checkTmr()` work to use them. In reality, what `startTmr()` actually returns is the current value of a system timer (which increases by 1 every second). The `checkTmr()` command does the same thing, but subtracts its parameter: so `checkTmr(x)` is equivalent to `startTmr()`-x. 

Because both `startTmr()` and `checkTmr()` deal with whole numbers of seconds, the resulting difference in time could be off by up to a second in either direction. That is, if `checkTmr()` gives 15 seconds as the time, you know the time that actually passed is between 14 and 16 seconds.

## Advanced Uses

The `startTmr()` and `checkTmr()` commands can be used to figure out how much time a command or routine takes with much greater precisions by running it multiple times. For example:
```
:startTmr()→t
:For i,1,1000
: somecmd()
:Disp checkTmr(t)
```
Suppose that the result displayed was 100 seconds. This is accurate to 1 second, so the actual time was between 99 and 101 seconds. However, this actual time is for 1000 repetitions of `somecmd()` (we assume that the time the code takes to increment i is negligible, although that may also be taken into account). So `somecmd()` repeated only once takes between 99/1000 and 101/1000 seconds, so the actual time is 100 ms, measured to within 1 millisecond error.

See [68k:Timings](68k:timings.html) for more information on this, as well as the results of some common comparisons.

## Related Commands

- [`68k:ClockOn`](68k:clockon.html)
- [`68k:ClockOff`](68k:clockoff.html)
- [`68k:getTime()`](68k:gettime().html)
- [`68k:starttmr()`](68k:starttmr().html)

## See Also

- [68k:Timings](68k:timings.html)
