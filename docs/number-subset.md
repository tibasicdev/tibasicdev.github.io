# Number Subset
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Returns a subset of a number.|*A* - the number to get the subset from<br>*B* - the starting position of the subset<br>*C* - the length of the subset|*Ans* - the subset of the number|A, B, C, Ans|Weregoose|[file numbersubset.zip]|

```
:10^(2-B+int(log(A
:int((A-int(A/Ans)Ans)/Ans10^(C
```

With our number stored in A, and the staring position and length of the subset stored in B and C respectively, we get the subset of the number by first subtracting the number divided by 10 to the power of 2-B+int(log(A (which is used to get how many digits are in the number), and then dividing that result by multiplying 10 to the power of 2-B+int(log(A and 10 to the power of C (which is the length of the subset).

A simple example should help you understand this routine. Say you input the number 123, with a starting position of 2 and a length of 2, it will return a result of 23. You can also use negative and decimal numbers with the routine, and it will still work correctly: a number of 13579.02468 with a starting position of 4 and length 4 will return 7902.

This routine is comparable to the [sub(](sub.html) command that works with [strings](strings.html).
