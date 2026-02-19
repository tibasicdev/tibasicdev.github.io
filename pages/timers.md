# Timers
|Routine Summary|Outputs|Variables Used|Author|
|--- |--- |--- |--- |
|Calculates amount of time that passes.|Ans|H, M, S, T| TI-BD Community|

```
ClrHome
AxesOff
ZStandard
ZInteger
FnOff
PlotsOff
Text(0,0,"0h 0m 0s
Pause
startTmr→T
Repeat max(K={105,21,45
getKey→K
checkTmr(T
Text(0,0,int(Ans/3600),"h ",remainder(int(Ans/60),60),"m ",remainder(Ans,60),"s           //11 spaces
End
```

This simple routine counts up from when you press `Enter` and stops when you press `Enter`, `Clear`, or `Del`.  This program calculates the amount of time that passes between key presses in minutes, and it displays the passing time in seconds as it is counting.

First, the clock makes sure you are ready to start the timer; it awaits you to press enter.  Immediately afterward, the [startTmr](starttmr.html) command is activated into the variable T.  [checkTmr(](checktmr.html)T tells how many seconds from the startTmr activation has gone by.  When a key is pressed, a small calculation is performed to determined to find how many minutes have gone by.

This program is a basic example of how startTmr and checkTmr( can be used to count time.  Unfortunately, this only works for the TI-84 series that have time compatibility.
----
|Routine Summary|Inputs|Variables Used|Author|
|--- |--- |--- |--- |
|Counts down from a given time.|M, S|T, M, S,—A—| TI-BD Community|
```
:Input "Minutes:",M
:Input "Seconds:",S
:60M+S→S
:AxesOff
:startTmr→T
:Repeat K or S=checkTmr(T
:getKey→K
:Text(-1,0,0,S-checkTmr(T)+"     //3 spaces
:End
:ClrDraw
:ClrHome
```

This timer, instead of counting up, counts down from a given starting point.  First, the program asks for minutes and seconds.  Unfortunately, the [checkTmr(](checktmr.html) command deals with seconds, so we must convert the minutes to seconds in order to make the program work.  According to the code, the timer will stop when either a key is pressed or the amount of time which has passed is equal to the given amount of seconds.

We turn the axes off so they won't be in the way. We then add 3 spaces after the [Text(](text.html) and [checkTmr(](checktmr.html) commands. The T variable represents the number of seconds that pass by after the [startTmr](starttmr.html) command is executed. If we did not input the spaces, the seconds will look like 990 instead of 99 when counting down from numbers larger than 100.
