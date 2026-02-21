# Number to String
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Converts a real number to a string.|*N* - the number you want to convert|*Str1* - the number N in string form|L₁, L₂, Y₁, Str1, N|[file numbertostring.zip]|

**Note:** If you have a TI-84+ CE with OS 5.2 or higher, you can ignore this entire routine and just use the [`toString(`](tostring.html) command.

```
:{0,1→L₁
:NAns→L₂
:LinReg(ax+b) Y₁
:Equ►String(Y₁,Str1
:sub(Str1,1,length(Str1)-3→Str1
```

This code works because it creates two points with a known best fit line: the best fit line through (0,0) and (1,N) is y=Nx+0. [`LinReg(ax+b)`](linreg(ax-b.html) calculates this best fit line, and stores its equation to `Y₁`.

Then, we use [`Equ►String(`](equ-string.html) to store this equation to `Str1`, which now contains "NX+0" with N replaced by the numerical value of N. After that, the [sub(](sub.html) command get rids of the "X+0" at the end, leaving only the string representation of N.

This routine uses `L₁`, `L₂`, and `Y₁`, so you should [clean up](cleanup.html) those variables at the end of your program. If you're working with the graph screen in [function](graphing-mode.html#function) mode, storing to `Y₁` can be a problem since it will draw an unwanted line through your graphics. Use `r₁` instead but make sure the calculator isn't in [polar](graphing-mode.html#polar) mode.

**Note:** This only works for real numbers. With complex numbers, such as imaginary numbers, you can use this code at the end of the first to get the same effect with *i* in it. This routine will also only work for N<10^50. To convert larger N, see the alternate below.

```
:Str1+"i→Str1
```

## Alternate Routine

The following routine will perform the same function for converting N to a string as shown above. This routine, however, allows N to be as large as the TI-84+ overflow limit (10^100) by utilizing [`Med-Med`](med-med.html) regression.

```
:{0,.5,1→L₁
:NAns→L₂
:Med-Med Y₁
:Equ►String(Y₁,Str1
:sub(Str1,1,length(Str1)-3→Str1
```

## Related Routines

- [List to String](list-to-string.html)
- [Matrix to String](matrix-to-string.html)
- [Number to String (Alternate)](number-to-string2.html)
