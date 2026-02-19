# Marquee
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Scrolls a string across one line, in marquee fashion, on the home screen.|*Str1* - the text to be scrolled<br>*A,B* - the [Output(](output.html) coordinates for the text<br>*N* - the number of characters to display at a time|None|Str1, A, B, N, Ans|Weregoose|[file marquee.zip]|

```
:Str1
:Repeat getKey
:Output(A,B,sub(Ans,1,N
:sub(Ans,2,length(Ans)-1)+sub(Ans,1,1
:If dim(rand(4
:End
```

By leaving Str1 by itself on one line, we store it to [Ans](ans.html), which will be easier to work with. Then, the Repeat [getKey](getkey.html) loop will display the marquee until a key — any key — is pressed.

Output(A,B,sub(Ans,1,N will display N characters of Str1 at A,B. Then, the next line will rotate Str1, so that the next time we're at this point in the loop, the string shifts one character.

Finally, If dim(rand(4 is a clever way of delaying the marquee, so it doesn't scroll too fast. rand(4 generates a list of 4 random numbers, which is a slightly time-consuming process. If dim( is just a way of wrapping this list so it doesn't change Ans. Since dim(rand(4 is always 4, the If statement will always be true, so we don't have to worry about the next line being skipped. By changing 4 to a lower or higher number, you can make the marquee go faster or slower, respectively.

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if the length N is longer than the number of characters in Str1.
