# Number Or String
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Determines whether an input is a number or string.|*Ans* - the number or string to examine|*Ans* - 1 if the input is a number, 0 if it is a string|A, B [,∟A, ∟B if input is a string]|bfr|http://tibasicdev.github.io/local—files/routine-page/routine.zip routine.zip|

```
:DelVar AFor(B,1,1
:Ans->A
:Ans->B
:A=B
```

If Ans is a string, it is stored to ∟A and ∟B. A remains 0, B remains 1, and A=B returns false. If Ans is a number, it is stored into both A and B, thus A=B returns true.

The For( command is used to avoid updating Ans. If this routine is used in a larger program and the input can be stored into a more permanent variable, For(B,1,1 can become 1->B. If this is not possible, the For( statement should have an End added.
