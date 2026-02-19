# Commenting Your Code
|**This article is part of the coding stage of the [development](development.html) cycle.**|
| --- |

When you are in the process of writing a program, everything about the program (i.e., variables, program structure, branching labels, etc.) is fresh in your mind and it's easy to remember. But what would happen if you stopped working on the program for a year, and then decided to start working on it again?

All or most of your previous knowledge of the program would be gone, and you would have to spend some time (or lots of time, depending on the program) to figure out how the program works again. While this is only a hypothetical example, this problem is a real concern for lots of people who have multiple projects going at any one time.

Thankfully, this problem can be easily prevented by simply adding comments to your code. A comment is a brief note that describes some functionality or feature of your code. You don't need to comment everything, but the two main things that you should comment are:

- **Program Structure** — Loops and branching with appropriate label names
- **Variables** — What their purpose is and any possible values

The amount of free RAM is the only limit on comment size, but you should generally try to keep your comments clear and concise. In addition, if your comment is more than a couple lines in length, you should split it up into multiple lines. This makes it easier to read and update, if needed.

## Text Comments

There are a couple different ways that you can add text comments to your code, with each having their own advantages and disadvantages. The first way is to make the comment a string literal (i.e., place a quote before the comment text), and then just place it on its own line.

```
:"Comment here
```

The advantage of this comment method is that it is extremely simple to use and update. You can make your comment almost anything you want (the two characters you can't use are the store command and a quote), and the calculator just reads it as a string.

The disadvantage of this method is that it prevents you from using the [Ans](ans.html) variable, since the comment will be stored to Ans when the calculator reads it. The comment also slows the program down because the calculator has to execute it each time.

The second way to add a text comment to your code is by placing the comment in a [conditional](if.html) or [loop](while.html), and using zero as the condition. Based on Boolean logic, the condition will always be false, which causes the calculator to not execute the conditional or loop, and subsequently skip right over the comment nested inside of it.

```
:While 0
:Comment here
:End
```

The advantage of this comment method is that it doesn't mess with any of the variables, and you can use the store command and quote character. The disadvantage is that it takes up some additional memory to use the conditional or loop, and this problem only worsens the more comments you use.

## Indenting Code

Another way to comment code is by indenting it, which allows you to easily identify control structures and blocks of code. Just like how there is a built-in colon that denotes the beginning of each new line, you can place your own colons before any statements on a line.

```
:While 1
::Disp "Hello
::Disp "Goodbye
:End
```

Although there is no restriction on how many colons you can place at the beginning of a line, one colon is generally sufficient. However, if adding two or three colons helps you better visualize the code, then that's what you should go with.

It is usually discouraged to use this method. Not only does it take up additional memory by adding bytes to the program, it also affects some commands. For example, the following method will not work. The intention of the code is to display only "FALSE".

```
:2→A
:If A=1
::Disp "TRUE"
:Disp "FALSE"
```

By adding the extra colon, an extra line is added. This specific line is skipped due to the If statement being false. However, Disp "TRUE" is run as well as Disp "FALSE".

## Descriptive Variables

Yet another way to comment code is by using descriptive variables that reflect where and how they are used. This is primarily related to using the real variables (A-Z and θ), since they are the most commonly used variables, and are much smaller and faster than other variables.

Of the real variables, the standard variables and situations are:

- I and J for the looping variable in [For(](for.html) loops
- X and Y for the X and Y screen coordinates respectively.
- K for storing the keypress with the [getKey](getkey.html) command.

Each of these variables is mnemonic — for example, K is the first letter in keypress — making them fairly easy to remember.

## Advanced Uses

You can modify the text comments so that you can turn them on or off. You just use a conditional with a variable as the condition, and then change its value from false (i.e., the comments are off) to true (i.e., the comments are on). Based on Boolean logic, the easiest system for the variable value is one for true and zero for false.

You also need to display the comments on the screen, so that you can read them during program execution. If you are using the [home screen](homescreen.html), you should use the [Pause](pause.html) command and its optional argument. While program execution is halted until the user presses ENTER, the Pause command allows you to display the entire comment on one line, and you can even scroll the comment left or right to read it, if necessary.

```
:If A:Pause "Comment here
```

You should use the same variable for all of the comments, so that the comments work in unison. The variable can be whatever you want, but the simplest variable to use is a real variable (A-Z and θ). You just need to remember to set the variable to zero at the beginning of the program, so that the comments are turned off by default.

<center>

|**[<< Techniques](techniques.html)**|**[Overview](development.html)**|**[Subprograms >>](subprograms.html)**|
| --- | --- | --- |

</center>
