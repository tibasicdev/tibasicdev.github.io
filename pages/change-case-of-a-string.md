# Change Case of a String
|Routine Summary|Inputs|Outputs|Variables Used|Authors|Download|
|--- |--- |--- |--- |--- |--- |
|Converts a string to lower/upper case.|*Str1* - The string to convert<br>*A* - The case to convert to: 0 for lower, 1 for upper|*Ans* or *Str1*- The converted string|Str1, Str2, A, B, N|Electromagnet8|http://www.cemetech.net/forum/viewtopic.php?p=235430#235430 Cemetech|

```
" "+Str1+" →Str1 
length(Ans→B 
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz→Str2 
For(N,2,B 
inString(sub(Str2,1+A26,26),sub(Str1,N,1 
If Ans 
sub(Str1,1,N-1)+sub(Str2,Ans+not(A)26,1)+sub(Str1,N+1,B-N→Str1 
End 
sub(Str1,2,B-2→Str1
```

We pad the string with spaces to prevent a domain error.

With our string stored in Str1, we loop through each character in order.

To convert to lowercase, we search for the uppercase characters in Str2.
To convert to uppercase, we search for the lowercase characters in Str2.

If it finds the other case character, we replace that character with the other case character. Otherwise, we skip the code to replace.

Example use:
```
"helLO wOrld"
converted to lowercase is
"hello world"

"H^:'[]{}/ello* world"
converted to uppercase is
"H^:'[]{}/ELLO* WORLD"
```
