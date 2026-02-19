# Easter Calculation
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Calculates the day that Easter Sunday falls on any given year.|*Y* - The year (any year at all)|*Ans* - The day in March of Easter Sunday (plus 31 if the month is April)|Y, Ans|John Horton Conway|[file eastercalculation.zip]|

```
:int(Y/ᴇ2
:50-30fPart((11(1+19fPart(Y/19))-Ans+int(Ans/4)+int(8(Ans+11)/25))/30
:If Ans=50 or Ans=49 and 11≤19fPart(Y/19
:Ans-1
:round(Ans+7-7fPart((int(23(3+(Ans>31))/9)+Ans-31(Ans>31)+2+Y+int(Y/4)-int(Y/ᴇ2)+int(Y/400))/7),0
```

This is the TI-BASIC version of an Easter Calculation algorithm by John Horton Conway (famous for creating the cellular automata "The Game of Life"). After implementation of this program, `3+(Ans>31)` is the month it occurs in, and `Ans-31(Ans>31)` is the day.

## Date Identification
This code, as it stands right now, displays the day of March it falls on (if it's over 31, then the day in April+31).

Append the following code to display the actual day:
```
:ClrHome
:Disp sub("MARCHAPRIL",1+5(Ans>31),5
:Output(1,7,Ans-31(Ans>31
```

## Why it Works

Easter is the first Sunday strictly after the Paschal Full Moon, which is an approximation of the real full moon (the 14th day of a lunar month, specifically), although it may be off by as much as two days.

The formula is

![http://latex.codecogs.com/gif.latex?%28April%5C%3B19%3DMarch%5C%3B50%29-%28%2811G&plus;C%29%5Cmod30%29](http://latex.codecogs.com/gif.latex?%28April%5C%3B19%3DMarch%5C%3B50%29-%28%2811G&plus;C%29%5Cmod30%29 "")

except if the formula gives April 19, take April 18, and if the formula gives you April 18 and **G**≥12, take April 17.

Here is the value of **G**:

![http://latex.codecogs.com/gif.latex?G%3D%28Y%5Cmod19%29&plus;1](http://latex.codecogs.com/gif.latex?G%3D%28Y%5Cmod19%29&plus;1 "")

Here is the value of **C** (with **H**=`int(Y/100)`, and [H]=`int(H)`):

![http://latex.codecogs.com/gif.latex?C%3D-H&plus;%5BH/4%5D&plus;%5B8%28H&plus;11%29/25%5D](http://latex.codecogs.com/gif.latex?C%3D-H&plus;%5BH/4%5D&plus;%5B8%28H&plus;11%29/25%5D "")

The first four lines of code implement this algorithm.

Lastly, the last line of code adjusts the date to the next Sunday using a modified version of the [Day of Week routine.](day-of-week-alternative.html)[[footnote]] If you have an 84+ or 84+SE, this may as well be `Ans+7-dayOfWk(Y,3+(Ans>31),Ans31(Ans>31))`. [[/footnote]]

## Alternate Routine

This routine is a modified version of the Easter20Ops function on [this page](https://web.archive.org/web/20150227133210/http://www.merlyn.demon.co.uk/estralgs.txt).

```
:2613+1483int(.01Y)-2225int(Y/400→A
:round(29fPart(int((66690fPart(Y/19)+319int(Ans/25))/330)/29
:56-Ans-7fPart((int(5Y/4)+A-Ans)/7
```

This returns the date of Easter as day-of-March, just like the previous routine. Retrieving the actual date is the exact same.

## Error Conditions

- None known.

## Related Routines

- [Day of Week (Alternative)](day-of-week-alternative.html)
