# Pad a String
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Pad a string with spaces on the left and right.|*Ans* - The string you want to pad<br>*N* - How many spaces you want|*Str1* - The padded string|X, N, Ans, Str1|[file padstring.zip]|

```
:For(X,1,N
:" "+Ans+" 
:End
:Ans→Str1
```

With our string stored in [Ans](ans.html), we concatenate (add) a space to the beginning and end of the string. At the same time, the new string is stored to Ans, which is what we use next time through the For( loop. The loop gets repeated over and over again until we have added however many spaces we wanted.  If you only want spaces on one side of the string, edit the second line accordingly.

Using Ans allows us to not have to use another string variable, since Ans can act like a string and it gets updated accordingly, and Ans is also faster than a string variable.

We store the string to a more permanent variable (in this case, Str1) for future use. When you are done using Str1, you should [clean it up](cleanup.html) at the end of your program.

## Related Routines

- [Strip a String](strip-a-string.html)
- [Scramble a String](scramble-a-string.html)
