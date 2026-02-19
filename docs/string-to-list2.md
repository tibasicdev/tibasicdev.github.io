# String To List2
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Converts a String into a List|Str1|L₁|A,B, Str0, Str1, L₁|Toothless the Dragon|

```
" ABCDEFGHIJKLMNOPQRSTUVWXYZ->Str0
DelVar L1
int(length(Str1)/7->dim(L1
For(A,0,dim(L1
0
For(B,1,min(7,length(Str1)-7A
Ans+.1^(2B)inString(Str0,sub(Str1,B+7A,1
End
Ans->L1(A+1
End
"
```

This code was made as an alternative to the [string-to-list](string-to-list.html) code. it works in conjunction with the [list to string alternative](list-to-string2.html).

## Related Routines

- [List to String](list-to-string.html)
- [String to List](string-to-list.html)
- [List to String Alternative](list-to-string2.html)
