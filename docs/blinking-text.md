# Blinking Text
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Creates a blinking effect on the home screen.|*Str1* - the text to blink on the screen<br>*A,B* - the [Output(](output.html) coordinates for the text<br>*N* - the length of the text to be displayed|None|Str1, N, A, B, Ans|[file blink.zip]|

```
:length(Str1→N:1
:Repeat getKey
:If dim(rand(15
:Output(A,B,sub(Str1+" (N spaces) ",1+NAns,N
:not(Ans
:End
```

By leaving 1 by itself on one line, we store it to [Ans](ans.html), which will be easier to work with. Then, the Repeat getKey loop will keep blinking the text until a key — any key — is pressed.

Output(A,B,sub(Str1+" (N spaces) ",1+NAns,N will display either the text or the equivalent number of spaces on the screen at coordinates (A,B). If you want to blink the text "Hello", for example, then you would need to use five spaces. We negate Ans's value with [not(](not.html), which acts as a flag to control the blinking.

If dim(rand(15 is a clever way of delaying the blinking, so that it doesn't blink too fast. rand(15 generates a list of 15 random numbers, which is a slightly time-consuming process. If dim( is just a way of wrapping this list so it doesn't change Ans. Since dim(rand(15 is always 15, the If statement will always be true, so we don't have to worry about the next line being skipped. By changing 15 to a lower or higher number, you can make the blinking go faster or slower, respectively.
