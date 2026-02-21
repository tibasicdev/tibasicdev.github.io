# Estimated Time Remaining
|Routine Summary|Inputs|Outputs|Variables Used|Author|Authors|
|--- |--- |--- |--- |--- |--- |
|A program to calculate the ETA in seconds in a For loop.|None|None|T, Z, E, I|Bio_Hazard1282| Only include this if you aren't the author of the routine.|

```
600->E
ClrHome
Output(1,1,"N:
Output(2,1,"E:
Output(2,3,E
Output(3,1,"ETA:
startTmr->Z
Repeat checkTmr(Z:End
startTmr->T
For(I,1,E
Output(1,3,I
100I/E
If Ans and checkTmr(Z:Then
Output(3,5,"    	//4 spaces
Output(3,5,int(checkTmr(T)/(.01Ans))-checkTmr(T
startTmr->Z
End:End
```

An explanation of the routine, including how it works, how you can modify it, what variables it uses, and anything else that is important to know when using the routine. The explanation should be thorough enough so that a person can use the routine without requiring help from somebody else.

### What is it?
This program calculates the ETA in a [For()](for.html) loop.

### How does it work?
At the beginning of the program, a sample value of 600 is stored to the variable E for the ending value. The four output commands show a bit of text for the current value (N), ending value (E), and (ETA) for the time in *seconds* left for the loop to execute.

Before the [For()](for.html) loop begins, we start timer Z and wait until one second has passed. Then we start timer T right before the loop to increase accuracy for the ETA.

Now the For() loop starts, and we show an output on the screen to indicate where we are in the loop.

```
Output(1,3,I
```

The next part of the program is to divide the increment variable *I* by *E* so we know how far we are in the loop.

```
100I/E
```

We then check if [Ans](ans.html) is greater than 0, to prevent an error. We also check if timer Z is greater than 0 as well to make the ETA smoother and make the program run faster to minimize the amount of times it has to update the ETA. In most operating systems, the ETA for common tasks is usually updated every second, so we'll apply that same concept to this program.

```
If Ans and checkTmr(Z:Then
```

We now will calculate the ETA (estimated time of arrival, except we're not going anywhere. So we're calculating the estimated time remaining.). We will make sure the time left in seconds is whole number (so not a decimal). We will divide timer T from the answer of `100I/E`, and subtract it from Timer T. We add four spaces before we output the ETA so it doesn't look like a mess.

```
Output(3,5,"    //4 spaces
Output(3,5,int(checkTmr(T)/(.01Ans))-checkTmr(T
```

After that, we will restart timer Z and finish the [If()](if.html) condition with an [End](end.html) command. We will end the For() loop with another End command.

## Error Conditions

- **[ERR:DIVIDE BY 0](errors.html#divideby0)** is thrown if E is 0.

## Related Commands

- [startTmr](starttmr.html)
- [checkTmr(](checktmr.html)
- [For()](for.html)
- [If](if.html)
- [End](end.html)
