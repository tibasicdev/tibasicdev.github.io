# String to List
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Converts a string to a list of numbers.|*Str1* - The string you want to convert|*L₁* - The list that the numbers are stored to|L₁, A, Str1|[file stringtolist.zip]|

```
:1+seq(inString("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ ",sub(Str1,A,1)),A,1,length(Str1→L₁
```

With our characters stored in Str1, we loop through each character and store its position in our reference string (the uppercase alphabet) to the respective element of L₁.

This routine only allows for values from 1 to 26 in the list, since our string of characters is the uppercase alphabet, and each list value must match up to one of the string positions. If you add more characters to the string, however, you can increase the range of values in the list. This routine uses Str1, so you should [clean it up](cleanup.html) at the end of your program.


## Advanced Routine

Since a list element can store up to 14 digits, you can use int(, fPart(, and exponents to compress an additional 7 letters per element (2 digits for each letter), thus increasing your total number of characters to 6993.

```
" ABCDEFGHIJKLMNOPQRSTUVWXYZ->Str0
DelVar L1
For(A,0,dim(L1
0
For(B,1,min(7,length(Str1)-7A
Ans+.1^(2B)inString(Str0,sub(Str1,B+7A,1
End
Ans->L1(A+1
End
"
```

## Related Routines

- [Number to String](number-to-string.html)
- [List to String](list-to-string.html)
