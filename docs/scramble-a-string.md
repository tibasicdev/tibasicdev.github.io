# Scramble a String
|Routine Summary|Inputs|Outputs|Variables Used|Authors|Download|
|--- |--- |--- |--- |--- |--- |
|Scrambles a string|*Str1* - The string you want to scramble|*Ans* - The scrambled string|Ans, Str1, L, N, L₁, L₂|seb83, Edward H, Timothy Foster|[file scramble_prgm.zip]|

This routine takes a string stored in Str1 and scramble it. The results is contained in Ans. For example, "ABCDE12345" could be scrambled to "B34AC1DE25".

```
:rand(length(Str1→L₁
:cumSum(1 or Ans→L₂
:SortA(L₁,L₂
:sub(Str1,L₂(1),1
:For(N,2,length(Str1
:Ans+sub(Str1,L₂(N),1
:End
```

With your string stored in Str1, it creates L₁={1,2,3,4,...,length(Str1)}. After that, L₂ is created randomly to sort L₁ in function of L₂. L₁ now could look like {5,3,4,1,2} if you entered a 5 character string. In the [For(](for.html) loop, it takes one by one the character of Str1 accordingly to L₁ to store it to Ans. Your scrambled string is now in Ans.

For the TI-84+ and higher with a MathPrint or color OS, use this code instead:

```
:randIntNoRep(1,length(Str1→L₁
:sub(Str1,Ans(1),1
:For(N,2,length(Str1
:Ans+sub(Str1,L₁(N),1
:End
```
## Related Routines

- [Reverse a String](reverse-a-string.html)
