# Matrix to String
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Converts a matrix to a string.|*[A]* - The matrix you want to convert|*Str1* - The string that the text is stored to|[A], L₁, A, B, Ans, Str1|[file matrixtostring.zip]|

**Note:** If you have a TI-84+ CE with OS 5.2 or higher, you can ignore this entire routine and just use the [toString(](tostring.html) command.

```
:dim([A]→L₁:"?
:For(A,1,L₁(1
:For(B,1,L₁(2
:Ans+sub("ABCDEFGHIJKLMNOPQRSTUVWXYZ",[A](A,B),1
:End:End
:sub(Ans,2,length(Ans)-1→Str1
```

With our values stored in [A], we get the dimensions (row x column) of the matrix, which are stored in a list. We then loop through each row and column, and store the character at the respective element to our string that is at the matching position in our substring. In order to construct a string with all of the characters from [A], we first need to create a dummy string. This is what the "? is used for.

Each time through the [For(](for.html) loops, we concatenate the string from before (which is still stored in the Ans variable) to the next character that is found in the matrix. Using [Ans](ans.html) allows us to not have to use another string variable, since Ans can act like a string and it gets updated accordingly, and Ans is also faster than a string variable.

By the time we are done with the For( loops, all of our characters are put together in Ans. However, because we stored the dummy character as the first character at the beginning of the string, we now need to remove it, which we do by simply getting the substring from the second character to the end of the string. Finally, we store the string to a more permanent variable (in this case, Str1) for future use.

This routine only allows for values from 1 to 26 in the matrix, since our string of characters is the uppercase alphabet, and each matrix value must match up to one of the string positions. If you add more characters to the string, however, you can increase the range of values in the matrix. This routine uses [A] and L₁, so you should [clean them up](cleanup.html) at the end of your program.

## Related Routines

- [Number to String](number-to-string.html)
- [List to String](list-to-string.html)
