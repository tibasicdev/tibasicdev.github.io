# Wordwrapping Text on the Graphscreen
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Displays text on several lines on the graph screen.|*Str1* - text to display<br>*A* - starting row<br>*B* - starting column|None|Str1, A, B, C, Ans|[file wordwrap.zip]|

```
:1→C
:For(A,A,57,6
:inString(Str1,"/",Ans
:Text(A,B,sub(Str1,C,Ans-C
:If Ans=length(Str1:57→A
:Ans+1→C
:End
```

This routine displays a string on the graph screen, with line breaks after every slash "/" character. The routine requires there to be a slash at the end of the string (so, a sample string would be "THIS TEXT IS TOO LONG TO/DISPLAY ON ONE LINE/").

The row and column (A and B) inputs determine the upper and left boundaries of the text. You determine the right boundary by where you put the slash characters. The lower boundary is 57, hardcoded into the routine (this is the lowest that text can be displayed), but you could change this if you wanted a different boundary.

The variable C is used for an index inside Str1, that tells us which character we're currently on. We're starting at the beginning of the string, so we store 1 to C.

The [For(](for.html) loop will increment A by 6 each time we display a line (small font characters are 6 pixels tall). We start at the current value of A, and end at 57 because beyond that, [Text(](text.html) will throw a domain error.

Now, we search for the next slash "/" character using the [inString(](instring.html) command. Then, using [Text(](text.html), we display the line between C and the "/", not including the slash itself. Ans+1→C will move the C index to the next character after the slash.

The line If Ans=length(Str1:57→A will end the loop early as soon as we reach the end of the string. This command can modify [Ans](ans.html), which would be bad, but it only does so when we're ready to exit anyway — at that point, we won't be needing Ans anymore.

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if Str1 is improperly formatted (check for the backslash at the end).
- **[ERR:DOMAIN](errors.html#domain)** is thrown if text goes off the screen. This shouldn't happen unless B is very close to the right edge, if A or B are negative, or if the calculator is in [Horiz](horiz.html) mode (in which case, replace 57 with 25).

## Related Routines

- [Highlighting Text](highlighting-text.html)
