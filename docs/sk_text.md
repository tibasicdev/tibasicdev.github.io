# Text and Text Sprites
|This article is currently in development. You can help TI-Basic Developer by expanding it. |
| --- |


The Text( command is very helpful for graphics on the graph screen. It can be use to make Text Sprites, and to display information that can be more customized than the home screen. To use this, you use the syntax: Text(*X Position*,*Y Position*, *Variable*).  The variable can be any data type.


## Displaying Text

Let's say you want to tell the user that they're score was 10. you would use this code:

```
:Text(1,1,"Your Score Was:10")
```
Since this is on the graph screen, you don't have to worry about a limit as much.  The horizontal limit is 94 pixels, and the characters are smaller. 

However, games usually have variating scores.  You can use this code to display the player's score, A.
```
:Text(1,1,"Your Score Was:",A)
```

## Larger Text

There is an additional argument ,-1, that goes at the beginning of the command. -1 is the difference between 5*3 Graph screen text and 8*5 Home screen text. So lets say your making a title page, and you want it to say "My Home Page" at the top in big letters, and beneath that the information in small letters, you would use this:

```
:ClrDraw
:Text(-1,0,0,"My Home Page")
:Text(10,1,"This is my testing homepage.")
```

## Text Sprites

**Note:** If you are using a TI-84+CSE or TI-84+CE, the increased resolution makes working with Text Sprites very challenging. Many of the techniques described in this section *may not function properly*.

Text sprites are a way of showing a character or piece of background. They are mainly used for puzzle games, that draw the playing field once, like [Donut Quest](http://tibasicdev.github.io/archives:donut-quest) by Mikhail Lavrov.

A text sprite uses `Text(` in order to display a little icon.  Here is the general code.
```
:For(A,1,7)
:Text(0,A,sub(string,A,1))
:End
```
The *string* is a 7 character string with the first five characters representing the object and the last two being spaces.  What happens is every time the [For(](for.html) loop is executed, the text moves one to the right and the next character in the string is displayed.  It ends up overwriting the previous text except for its first row. If you don't understand this yet, you may want to throw a [Pause](pause.html) in the code to see the sprites drawn step by step.

```
:For(A,1,7)
:Text(0,A,sub(string,A,1))
:Pause
:End
```

So, let's say you want to draw a donut.  What would the string be?  First, draw a five by five grid and outlay your donut.
```
0 1 1 1 0
1 1 1 1 1
1 1 0 1 1
1 1 1 1 1
0 1 1 1 0
```
Now, take notice on where the ones are.  Look at the first column.  The middle three pixels are on.  What character has its first row in the same pattern?  Let's try (.
```
0 1 0
1 0 0
1 0 0
1 0 0
0 1 0
```
Look!  Same first rows!  So, a ( would be the first character.  For the donut, you want the string to be "( [ X [ ( _ _".  When this is put into the code, you make a donut shape.  This can be done with most five by five designs.

Try making this one.
```
0 0 1 0 0
0 1 1 1 0
1 1 0 1 1
0 1 1 1 0
0 0 1 0 0
```
Can you make the appropriate string?
<details style="display: inline;"><summary>show</summary>
```
:For(A,1,7)
:Text(0,A,sub("-(X(-  ",A,1))
:End
```
</details>

<center>

|**[<< Drawing More Shapes](sk:more-shapes.html)**|**[Table of Contents](starter-kit.html)**|**[Using Pictures >>](sk:pictures.html)**|
| --- | --- | --- |

</center>
