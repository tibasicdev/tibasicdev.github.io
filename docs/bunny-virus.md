# Bunny Virus
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Creates a virus-like effect which locks up the calculator.|None|None|None|[file bunny_virus.zip]|


> **Disclaimer**: We are not responsible for any damage that this routine causes to your calculator or anybody else's calculator. If you decide to try it out on somebody else's calculator, you should give them some warning ahead of time.


```
:999→dim(∟BUNNY
:While 1
:SortA(∟BUNNY
:End
```

While it isn't possible to create a true virus in TI-Basic, you can create a virus-like effect which locks up the calculator, and forces the user to have to remove the batteries to get out of the program. Removing the batteries causes the calculator to shut off, and when the calculator is turned back on, the RAM will be cleared. This is where the virus aspect comes from.

The idea behind the code is actually pretty simple. The calculator has a few commands (in particular, [SortA(](sorta.html) and [SortD(](sortd.html)) which cannot be interrupted by the ON key while they are executing. If you give one of these commands a large list (in the case of SortA( and SortD( ), they will be very time-consuming, which gives the illusion that the calculator has stalled.

Because these commands will eventually finish executing given enough time, an infinite [While](while.html) loop is placed around them so that they will be repeated indefinitely until the person removes their batteries. In addition to these two commands, the [Fill(](fill.html) and [randBin(](randbin.html) commands also work on the older TI-83 and TI-82 calculators, although it doesn't work on the newer TI-83+ and higher calculators.
