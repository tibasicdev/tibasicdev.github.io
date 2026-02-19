# Typewriter Routine
|Routine Summary|Inputs|Variables Used|
|--- |--- |--- |
|Makes text appear letter by letter|*Str1* - Text to be displayed.<br>*A,B* - Row and colum to display text.|*A, B, T, Str1*|

```
:For(T,1,length(Str1
:Text(A,B,sub(Str1,1,T
:rand(5
:End
```

We use a [For(](for.html) loop over the length of the string to go through the string letter by letter. In order to make the spacing come out right, instead of figuring out the right coordinate to display each character at, we display the first T characters of the string starting from the beginning. The rand(5) provides a split-second delay to achieve the typewriter effect.

For multiple lines with the typewriter effect, you can combine this routine with the one to [wordwrap text](wordwrap-text.html).

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if the string doesn't fit entirely on the screen.

## Related Routines

- [Wordwrapping Text](wordwrap-text.html)
