# List to String
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Converts a list of numbers to a string.|*L₁* - The list you want to convert|*Str1* - The string that the text is stored to|L₁, A, Ans, Str1|[file listtostring.zip]|

**Note:** If you have a TI-84+ CE with OS 5.2 or higher, you can ignore this entire routine and just use the [toString(](tostring.html) command.

```
:"?
:For(A,1,dim(L₁
:Ans+sub("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ ",1+L₁(A),1
:End
:sub(Ans,2,length(Ans)-1→Str1
```

With our list of values stored in L₁, we loop through each element of L₁ and store the character to our string that is at the matching position in our substring. In order to construct a string with all of the characters from L₁, we first need to create a dummy string. This is what the "? is used for.

Each time through the [For(](for.html) loop, we concatenate the string from before (which is still stored in the Ans variable) to the next character that is found in the list. Using [Ans](ans.html) allows us to not have to use another string variable, since Ans can act like a string and it gets updated accordingly, and Ans is also faster than a string variable.

By the time we are done with the For( loop, all of our characters are put together in Ans. However, because we stored the dummy character as the first character at the beginning of the string, we now need to remove it, which we do by simply getting the substring from the second character to the end of the string. Finally, we store the string to a more permanent variable (in this case, Str1) for future use.

This routine allows for values from 0 to 36 in the list, since our string of characters is the ten digits and 26 uppercase letters, plus a space, and each list value must match up to one of the string positions. If you add more characters to the string, such as [lowercase letters,](hexcodes.html#toc4) however, you can increase the range of values in the list; if you need fewer characters you can simply remove them. This routine uses L₁, so you should [clean it up](cleanup.html) at the end of your program.

## Related Routines

- [Number to String](number-to-string.html)
- [Matrix to String](matrix-to-string.html)
- [String to List](string-to-list.html)
