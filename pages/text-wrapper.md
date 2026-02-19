# Text Wrapper
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Wraps text on the screen whenever you want. (Preserves space functionality.)|*Str1**/Ans* — String to wrap|*Text on screen*|R, C, I, Str1, Ans|BlakPilar|
## Code (Graph Screen)
```
:"YAY, I MADE A LINEºWRAPPER FOR (ALMOST)ºANY LENGTH OF TEXT!º =D→Str1
:ClrDraw
:DispGraph
:DelVar RDelVar CFor(I,1,length(Str1
:If C<91 and "º"≠sub(Str1,I,1
:Then
:If " "≠sub(Str1,I,1
:Text(R,C,sub(Str1,I,1
:C+4→C
:If I<length(Str1)-1:Ans-2(" "≠sub(Str1,I,1→C
:Else
:DelVar CR+6→R
:End
:C+4(C>89→C
:I-(C>89→I
:End
```
## Explanation (Graph Screen)
**NOTE:** The string declaration can easily be changed to "Ans→Str1" as long as you are **100% certain** that Ans will be a string.

The first two lines after the string are self-explanatory (I hope). We first need to store zero to R and C (this is done by using DelVar), which will be used as our row and column variables. We then start a loop which will only execute while in the string.

The first If statement that we encounter checks for our new line character, which in this case is used as the degree sign (2ND+APPS>1). If the current character is **not** our new line character, and it is **not** a space, we display it and add 4 to our column variable.

With our third If statement, we check to see if we are still in the string. If we are, and the next character is a space, we subtract two from the column variable. The number 2 can be changed to whatever you want the word spacing to be (TI-OS default is 1).

Finally, we reach our Else, which is what will happen if the current character **is** the new line character. All we do is reset the column, and add six to the row (again, the number 6 can be easily changed for line spacing). Simple as that!

Note, this will also wrap text in case you forget the new line character.

## Code (Home Screen)
```
:"WOOT, NOW IT'S A LINEºWRAPPER FOR THE HOMEºSCREEN! =]→Str1
:ClrHome
:1→R:1→C
:For(I,1,length(Str1
:If C≠17 and "º"≠sub(Str1,I,1
:Then
:Output(R,C,sub(Str1,I,1
:C+1→C
:Else
:I-(C=17→I
:1→C:R+1→R
:End
:If R=9:Stop
:End
```

## Explanation (Home Screen)
**NOTE:** As with the graph screen version, the string declaration can easily be changed to "Ans→Str1" as long as you are **100% certain** that Ans will be a string.

This isn't that different from the graph screen version. We just have to keep in mind that the home screen *only* has an 8x16 dimension and is monospaced (each character is the same width and height), so we need to adjust our variables accordingly. The row can have a max of 8, and the column can have a max of 16. Each's minimum is 1.

As we display text, we check to see if the current character is our new line character. If it isn't, then we go through our displaying. If it is, then we change our variables.
