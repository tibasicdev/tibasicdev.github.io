# Binary/Decimal Conversion
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|These two routines convert binary to decimal and vice versa.|D / Str1|Ans / D|Str1, D, I|Michael2_3B / BlackPilar|
Bin▶Dec
```
:Input "BIN: ",Str1
:Delvar DFor(I,length(Str1),1,-1
:If "1"=sub(Str1,I,1
:D+2^(length(Str1)-I→D
:End
```
Dec▶Bin
```
" →Str1   //1 space character
Repeat not(D
D/2→D
sub("01",1+not(not(fPart(Ans))),1)+Str1→Str1
iPart(D→D
End
expr(sub(Str1,1,length(Str1)-1
DelVar Str1   //if you want to keep your binary number in the string, skip this
```

## Bin▶Dec
The way that this function works is pretty simple, actually. First we get the user to tell us what the binary value they wish to convert is. Then we clear the variable D (making it zero by default), and being our loop, working backwards through the string. If the character is a "1", then that means that 2 (binary's base), is raised to that positions power, beginning with zero at the far left. We add the resulting power of two to our decimal value, and continue through the binary value.

## Dec▶Bin
Here, we first initialize our string, which will hold the binary number until the end. D is the decimal number you want to convert. Our loop repeats itself until D=0, that way all values over 2 can be covered. Inside the loop, we divide D by 2 first. We then take the substring of "01" and add str1 after it, updating str1. The 0 in the string is selected to add if there is no remainder from D/2, and the 1 is selected if there is. After that, the integer part of D/2 is stored into D. Once everything is all done, we take the expr() of str1, excluding the last character which is the space character, putting the binary number into Ans. And of course, to clean up, we delete variable Str1.

## Error Conditions

- **[ERR:OVERFLOW](errors.html#overflow)** is thrown in Bin▶Dec if the resulting decimal will be greater than 9e99.

## Related Pages

- [Binary & Hexadecimal](binandhex.html)
