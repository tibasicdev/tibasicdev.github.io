# Homescreen
Whee! You got through the first part of the starter kit! Now, we come to the second part, which will get into the finer points of the homescreen and data types.
We will start off the second part of the kit by discussing more of the homescreen. Let's begin, shall we?



## Letting the User See Something
Back in the first part, you only learned of one command that can display information, the Disp command. We will learn two more commands that deal with output, starting with the ClrHome command.

### ClrHome
The [ClrHome](clrhome.html) command clears the homescreen, giving you an empty space to work with. No arguments are needed, just select it from the I/O menu of the PRGM button (only accessible this way while editing).

**Two Notes**
1. Output( will write over anything on the homescreen
1. Disp, Input, and Prompt will not recognize Output( commands, so if you have some text printed at 1,1 and then use Input, you will write over the Output(


### Output
The [Output(](output.html) command lets you print text, just like the Disp command. There are two differences, though: You can choose where to start the text, and strings that go off the end of the screen will wrap around to the next line!
To use it, you need three arguments: the row where the first character appears, the column, and the text.
You use it like so:
```:Output(8,1,"PRESS ENTER")
```
This text starts at the bottom-left corner of the screen, and prints PRESS ENTER.
The most useful application for Output( is to dynamically update the home screen. If you had money in the top left corner and life in the bottom left for a game, using Disp to update those would be a pain. You would have the un-updated text blink, because you had to ClrHome first. Output allows you to avoid the flicker.

## Making the Program Smart
In the past, you only knew of the Input command for input. Now we will cover two more input methods, the first being Prompt.

### Prompt
[Prompt](prompt.html) is a much more primitive command than Input, but it gets the job done. It only needs one argument: the variable. You can add more variables to one Prompt statement, as long as they are separated by commas. Here is a basic use:
```Prompt A
```
The code will show A=?, which means, "What do you want A to equal?". Prompt has limitations, and quality programs are unlikely to use it because the A=? thing doesn't look very professional.
The limitations are outlined below:
- Cryptic - Prompt doesn't allow custom text to be displayed, unlike Input. The casual calculator user can be intimated by the cryptic look that is forced.
- No Exception - If you want someone to enter a string using Prompt, the user **must** put quotation marks around the string or risk error. Input doesn't care.

## Final Notes

These are the last of the commands that can directly influence the home screen. The furthest from direct influence is getKey, which you will discover in detail in the next lesson.  More on the commands you just learned can be found on their respective pages.  Try searching for them in the upper right hand corner of the site!
Hopefully you can use the homescreen commands well.  Next up we explore the hidden elements of input: data types, and the getKey command.

<center>

|**[<< Sample Program: Guessing Game](sk:guessing-game.html)**|**[Table of Contents](starter-kit.html)**|**[Using getKey >>](sk:getkey.html)**|
| --- | --- | --- |

</center>
