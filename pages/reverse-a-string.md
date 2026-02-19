# Reverse a String
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Reverses the characters in a string.|*Str1* - The string you want to reverse|*Str1* - The reversed string|Str1, I, Ans|[file reversestring.zip]|

```
:Str1
:For(I,1,length(Ans)-1
:sub(Ans,2I,1)+Ans
:End
:sub(Ans,1,I→Str1
```

With our string stored in Str1 and [Ans](ans.html), we loop through each character, starting from the beginning to the end, and add it to the beginning of the string, building the reversed string up at the beginning as we go:

```
12345    (original string - the first character is the first reversed character)
212345   (add then second character before the first, reversing the string)
3212345  (continue adding characters in reverse)
543212345 (this is what the end result looks like)
```

Since adding to the beginning of the string alters the indices, we must take that into account — this is where the 2I in the formula comes from. It adds the 2nd character the first time, the 4th character (which was originally the 3rd) next, the 6th character (originally the 4th) after that, and so on.

Using Ans allows us to not have to use another string variable, since Ans can act like a string and it gets updated accordingly, and Ans is also faster than a string variable.

By the time we are done with the [For(](for.html) loop, all of our characters are put together in Ans in reverse order, before the original string. To finish, we take the first (reversed) half as a [substring](sub.html) and store it back in Str1 for further use. We can use I for this purpose because it looped from 1 to length(Str1)-1, so its value will be length(Str1) when exiting. 

If you want to preserve the original string, store it to a different string variable in the first line of the code.

When you are done using Str1, you should [clean it up](cleanup.html) at the end of your program.
