# Subprograms
|**This article is part of the coding stage of the [development](development.html) cycle.**|
| --- |

Imagine you're creating an [RPG](rpg.html), and the current problem you're facing is how to display all of the data for each character on the screen. Without putting too much thought into it, the easiest approach to you seems to be to simply write out the data each time. Unfortunately, when you start implementing this approach, it soon becomes apparent that it will not work in your program.

While you've only programmed in a few of the characters and their respective data, you can already see that there is simply too much data to enter in; and then when you think about the possibility of having to go through and change all of the data again if you update the program, you're now left feeling overwhelmed and wondering if there's another way. Thankfully, there is, and its name is subprograms.

A subprogram is a program called by another program to perform a particular task or function for the program. When a task needs to be performed multiple times (such as displaying character data), you can make it into a separate subprogram. The complete program is thus made up of multiple smaller, independent subprograms that work together with the main program.

There are two different general types of subprograms available:

- **External** — They exist as stand-alone programs that are listed in the program menu, and can be executed just like a regular program.
- **Internal** — They are contained inside the program itself, so that they can be called by the program whenever needed.

There are certain advantages and disadvantages to using each type of subprogram, and consequently, situations where using one type of subprogram makes more sense than using the other. This doesn't mean you can't use whichever you like, though.

## External Subprograms

External subprograms are the simplest type of subprogram, and involve executing one program from inside another program using the [prgm](prgm.html) command. You just insert the prgm command into the program where you want the subprogram to run, and then type the subprogram's name. You can also go to the program menu, and press ENTER on whichever program you want to use to paste the program's name into the program.

```
:prgmPROGNAME
```

When creating a subprogram, you take whatever code you want from the parent program and put it in its own program (see [your first program](sk:first-program.html) for more information), and then put a [Return](return.html) command whenever you want to return to the parent program. (A Return command is optional at the end of a program, and you typically leave it off as part of [program optimization](optimize.html).)

You should try to name your subprograms Zparentn or θparentn, where parent is the name of the parent program and n is the number (if you have more than one). Because subprograms are relatively unimportant by themselves, you want them to appear at the bottom of the program menu so they don't clutter it up and interfere with the user's ability to find whatever program they're looking for.

Here's a simple example where we are storing [maps](maps.html) for our maze game in a subprogram, and then retrieving the desired map from the subprogram as a string, so we can print it out on the [home screen](homescreen.html). (This example is somewhat contrived, but it should be enough to illustrate external subprograms).

```
PROGRAM:MAZE
:ClrHome
:prgmZMAZE
:Output(1,1,Ans
:Pause

PROGRAM:ZMAZE
:int(3rand→A
:"X    XX    XXXXXX    XX    XXXXXX    XX    XXXXX
:If A=1:"X X X X X X X X X X X X X X X X X X X X X X X X 
:If not(A:"X              XX              XX              X
```

![subprogram_zmaze.gif](subprogram_zmaze.gif "")

When the subprogram's name is encountered (in this case, prgmZMAZE), execution of the program will be put on hold, and program execution will transfer to the subprogram. Once the subprogram is finished running, or the Return command is executed, program execution will go back to the program, continuing right after the subprogram name. (If the [Stop](stop.html) command is used instead of Return, however, the complete program hierarchy will stop.) See the image to the right for a graphical view of program flow using subprograms. 

Although subprograms can call themselves (i.e., [recursion](recursion.html)) or other subprograms, each subprogram should return to the parent program and let it handle all the program calling. A structured program hierarchy is easier to understand and update (in fact, it's actually a [code convention](code-conventions.html)), and helps cut down the potential for [memory leaks](errors.html).

Each program call is sixteen bytes, and gets put on a stack in RAM by the calculator. This is fine as long as its size isn't larger than the free RAM available, but each additional program call takes more memory until the program Returns.  Having many nested program calls can run out of memory and crash the calculator (giving you a [ERR:MEMORY](errors.html#memory) error).

External subprograms often are made to increase the speed of a program and decrease the size of the program overall by executing often used code at one place, where it can be called quickly. (as opposed to Labels)

To make subprograms even faster, a Return may be used in the subprogram, but only is useful in subprograms with several methods, and only after a method has been completed. The problem with using a Return in such a method is that it isn't very easy to prevent memory leaks by using a Return before an End command should have been called.

Because the same thing happens with Goto's before End commands as Returns before End commands, we can use this to our advantage, to quickly return from a subprogram. By using a Goto to a label with one or possibly more End commands, you can quickly return from a program, or quickly reset a While, Repeat, or For( loop without having to execute the rest of the code in the subprogram or loop.

```
Goto ST
Lbl E1
End
Lbl E0
Return
Lbl ST
[code]
If [condition]
Goto E0
[code]
If [condition]
Then
[code]
Goto E1
End
For(A,1,10
[code]
If [condition]
Goto E1
[code]
End
```

This can significantly increase the speed of subprograms or loops, by using Labels without worry of [ERR:MEMORY](errors.html#memory).

### Passing Arguments

The main problem associated with trying to use external subprograms is that there is no built-in support for passing arguments to subprograms. This feature is important because it allows the subprogram to act differently based on what values are given to it for processing.

Fortunately, you can mimic this functionality by using [variables](variables.html). Because all variables are global (variables used by one program can be used by another), changing a variable in one program affects that variable everywhere else. While you can use almost any variable that you want, there are three main types of variables that you should choose from:

- **Pre-Defined Variables** — Includes reals, strings, matrices, built-in lists, etc. These variables are frequently used by most programs, so you don't have to worry very much about whether the user cares if your mess with them.
- **User-Defined Lists** — Uses the individual list elements to store different values. These variables have a certain sense of security that comes with using them because they are the only variable that you can actually create, so a program can have its own custom list to use.
- **Ans** — It can take on whatever value and variable you want, so the program doesn't have a specific variable hard-coded in. Its value changes whenever you store something or simply place an expression or string on a line by itself.

When using a pre-defined variable or user-defined list, you simply have to set the variable to the value that you want and then call the subprogram. The subprogram should be able to use that variable without problems, but if you don't properly setup the variable, the subprogram won't work correctly.

```
:{2,3,5,7,9→PRIME
:prgmZPRIME
```

Using the Ans variable is essentially the same, except you need to add some additional code to the subprogram. Because the value of Ans changes whenever there is a new variable storage, you should have the first line inside the subprogram save Ans to another, more stable variable.

```
:{2,3,5,7,9
:prgmZPRIME

PROGRAM:ZPRIME
:Ans→PRIME
```

This change saves some memory in the main program (in our example, we were able to get rid of the →PRIME statement), but the subprogram size is larger, since we really just shifted the variable storage code to the subprogram. However, if the subprogram is called multiple times this extra memory is only used once instead of once per call.

This does create a problem, though, because now when you store Ans to another variable, it will crash the program if Ans isn't the same type of variable. There is only one case where you can avoid crashing when the subprogram receives the wrong variable type.  If the subprogram is expecting a real variable (such as A or X) and it is passed a list, it can prevent a crash by using the fact that a parenthesis ("(") has multiple functions.

```
PROGRAM:ZSUB
:Ans(1→A
```

The reason that this works is because a user-defined list doesn't need the ∟ prefixed character at the beginning when referring to the list. While you may be only asking the user to input a simple real variable, a list would also be allowed. There is nothing you can really do to fix this problem with other types, so just be careful.

### Advanced Uses

The main consideration when using external subprograms is how many subprograms your program should have. While you're still putting your program together, it's good to keep it in many small, separate subprograms; but when you're done, all those subprograms become a liability and make your program unwieldy to use. This is because you have to remember all those subprograms in order to use your program.

There are two different ways to resolve this problem. The first way is to put the subprograms back in your program. This should only be done if a subprogram was only called once or twice, and putting it back in won't slow down the program. All you have to do is paste the code from the subprogram in place of the subprogram call. When you're done, you can delete the now unnecessary subprograms.

(The more detailed explanation is to go through your main program, and whenever you see a prgm call for a subprogram, clear that line and press 2nd STO. The Recall option will come up. Press the PRGM key and select the appropriate subprogram from the EXEC menu. The calculator will paste that subprogram's code into the main program.)

This is the same subprogram example from before, but now we've gotten rid of the ZMAZE subprogram and simply placed the subprogram code in the MAZE program itself:

```
PROGRAM:MAZE
:ClrHome
:int(3rand→A
:"X    XX    XXXXXX    XX    XXXXXX    XX    XXXXX
:If A=1:"X X X X X X X X X X X X X X X X X X X X X X X X 
:If not(A:"X              XX              XX              X
:Output(1,1,Ans
:Pause
```

The second way to resolve the problem is by simply combining your subprograms together, so that there are fewer subprograms needed. Of course, how many subprograms you decide to use is up to you, but you should try to limit it to three or four subprograms at most, and just one subprogram ideally. This might take some effort on your part, but it will most certainly make your users happy.

When you start combining your subprograms together, you should place the subprograms one after the other, giving each subprogram a unique branching label (note that labels are local, so you can't use Goto in one program to jump to a label in another program). Instead of having to search through each individual subprogram, branching allows you to simply jump to the desired subprogram. You then just use the subprogram's variable argument to determine which subprogram to access.

```
:If A=e:Goto A  // jump to first subprogram
:If A=π:Goto B  // jump to second subprogram
:Stop  // the subprogram was accidentally called
:Lbl A
: // subprogram code
:Return
:Lbl B
: // subprogram code
: // No Return needed here
```

Looking at the example, the first thing you should notice is the variable values that are used to determine which subprogram to jump to. While you could use something simple like one or two, those values have a high probability of being accidentally entered in by the user or being set by another unrelated program. What works better is to use random decimals (like .193 or 1.857) or math symbols (like e or π).

If none of the variable values for the subprograms match, then none of the subprograms will be executed; instead, program execution will go to the Stop command on the next line, which will  immediately stop the entire program. The reason for adding this [program protection](protection.html) is to prevent the user from running the subprogram separate from our main program.

This is a real concern since external subprograms are listed in the program menu, and the user most likely at some point will try to run the subprogram just out of pure curiosity. Unless the user is a competent TI-Basic programmer who knows what they are doing, however, you normally don't want to let the user mess with your subprograms. If they change something, or delete some lines of code, then your program might stop working correctly.

The second thing you should notice about the example is the Return command at the end of each subprogram. If you have lots of subprograms, and you're accessing a subprogram near the bottom, it takes a considerable amount of time for program execution to go back to the main program. This happens because program execution doesn't return to the main program until after it reaches the end of the program, or it executes a Return command. So, just remember to include the Return commands as needed.

### Using Assembly
Although using assembly programs can limit the [compatibility](compatibility.html) of your program, they can be helpful in reducing the memory your program occupies, and allow for easier calling of subprograms. To use an assembly program for calling subprograms, have your subprograms named using some very simple pattern (e.g. "ZZ10", "ZZ11", "ZZ12", "ZZ13", etc). Then create a program such as the following called ZEXEC (or something similar):

```
:"ZZ"+Ans→StrX
://Assembly program to run program name in StrX
```

Then you can call this program through the line:

```
:"13
:prgmZEXEC
```

This will create a string with the contents "ZZ13" which will then run the program ZZ13. Depending on the assembly program you are using, you could have "ZZ13" archived (along with the rest of the subroutines) and when ZEXEC is called, it copies it to an unarchived program, runs the copy, and then deletes the copy, thus only one subroutine at a time is unarchived. This is useful for programs with lots of subroutines. One way of doing this is using [xLIB](xlib.html), for which the ZEXEC code would look like this:

```
"ZZ"+Ans
real(10,0,0
prgmXTEMP000
real(10,1,0
```

In order to make this concept more efficient, a number to string routine would come in handy. If one were using such a routine one could have various actions in a program return number values. These numbers would be converted into strings and the program would run the corresponding subprogram. This would become useful with a custom menu, one could have the program return the location of the cursor, convert that into a string and run the subprogram that corresponds to that cursor location. Some assembly programs that can be used may be found on the [assembly libraries](asmlibs.html) page.

### Advantages

There are several advantages of using external subprograms. First, and foremost, they reduce program size by eliminating redundant code. Instead of having to type the code multiple times for a task that occurs more than once in a program, you just type it once and put it in a subprogram. You then call the subprogram whenever you want to perform the task in your program.

Second, external subprograms increase program speed by making programs as compact as possible. You separate conditional tasks from the program (they either happen every time or they are skipped over), and put them in a subprogram; you then call the subprogram instead. This improves program speed because the calculator doesn't have to go through all of the conditional code anymore.

Third, external subprograms make editing, debugging, and optimizing easier. Instead of going through the entire program, looking for the code you want to change, you can focus on one subprogram at a time. This makes the code more manageable, allowing you to more thoroughly look at each subprogram and to better keep track of which subprograms you have looked at. It also prevents you from accidentally changing other parts of the program.

Lastly, subprograms are reusable, allowing multiple programs to share and use the same code. Breaking a program into smaller, individual subprograms, which each do a basic function or task, allows other programs to use those subprograms. Consequently, this reduces program size.

## Internal Subprograms {#internal}

Internal subprograms are the most complicated type of subprogram, and involve putting the subprograms in the main program itself. This is not the same thing as pasting the code from the subprogram in place of the subprogram call, like you do with external subprograms; rather, it is designing your main program so that it can take advantage of subprograms, but all the code is self-contained.

There are several different ways that you can make internal subprograms, but the three most common ways are:

1. Append to the beginning of the program
2. Structured loops or branching
3. Branching out of broken loops

### Append to Program Beginning

If you remember how we used external programs, then this should be very familiar. Instead of placing the subprograms in their own separate program, we are now just placing the subprograms at the beginning of our main program.

The standard way to make a subprogram is to use an If-Then conditional:

```
:If A=1.234:Then
: // subprogram code
:DelVar A
:Return
:End
```

Then to call the subprogram, you just set the variable to the desired value:

```
:1.234→A
:prgmPROGNAME
```

Of course, there are some important considerations that you need to be aware of. You can use whatever random value for the variable that you want, just as long as it isn't something that the user would typically use. This is to ensure that the subprogram isn't accidentally run when it shouldn't be, which is why you need to reset the variable's value inside the subprogram before exiting.

While you could use any variable that you want (including Ans), the best variables to use are the simple real variables (A-Z and θ). This is because they are small in size and they are constantly being used by other programs, so you don't have to really worry very much about your subprograms being accidentally run. (Ans is not a very good variable to use for the reasons listed above.)

You should always remember to include the [Return](return.html) command at the end of the subprogram. Once the subprogram is finished, the Return command will cause the subprogram to stop and return to the previous place in the program from where it was called. The other reason for the Return command is to prevent any memory errors that can occur if a program recursively calls itself too much.

#### Advanced Uses

You can have multiple subprograms at the beginning listed one after the other by simply using different values for the the variable:

```
:If A=1.234:Then
: // subprogram 1
:End
:If A=2.246:Then
: // subprogram 2
:End
```

While this works quite well when you only have three or four subprograms, with more subprograms it can actually slow down the main program. This happens because the calculator has to go through all the subprograms to get to the main program code.

You could fix this problem in a couple different ways, but the easiest way is to simply place all the subprograms in an If-Then conditional and then make that part of the subprograms. If this conditional is false, all of the subprograms will be skipped over.

A real number has an integer (accessed with the [iPart(](ipart.html) command) and fraction (accessed with the [fPart(](fpart.html) command) part, and you can use both of those for the subprograms: the integer will be the subprogram access check on the outside If-Then conditional and the fraction will be the respective subprogram we want to run.

```
:If 123456=iPart(A:Then  // get integer part of number
:10fPart(A  // get fraction part of number
:If Ans=1:Then
: // subprogram 1
:End
:If Ans=2:Then
: // subprogram 2
:End
: // rest of subprograms
:End
```

For calling the subprograms, you then just set the variable to the desired value like before:

```
:123456.1→A  // run subprogram 1
:prgmPROGNAME
```

### Structured Loops or Branching

If you don't like placing subprograms at the beginning of a program, the next approach that you can try is placing subprograms in the actual program code. While it would appear easy to simply place the subprograms wherever you feel like in your program, you can't readily do this since it would almost certainly cause your program to stop working correctly. Instead, you need to modify your program and subprograms so they can be put together.

What this modification entails is reorganizing your program so that the code works in a modular fashion as individual subprograms. This may not seem like it would be worth the effort, depending on the amount of code in your program, but modularization makes the program easier to understand and update (see [planning programs](plan.html) for more information).

While there are several different ways you can structure the code in a modular fashion, the simplest way is to give each subprogram its own individual loop with a respective variable value as the loop condition. You can then access and exit the desired loop by simply changing the value of the variable. Of course, you have to determine which loop and variable you are going to use.

There are three different loops you can choose from ([While](while.html), [Repeat](repeat.html), and [For(](for.html)), but the best loop to use in this circumstance is While. This is because the condition is tested at the top of the loop, so if it's false already before the loop, then the loop will actually be skipped over (which is what allows us to use the loops as subprograms).

Once you have decided upon a particular loop, now you need to choose which variable you want to use. Like with the first way to make internal subprograms, the best variable to use is one of the real variables (A-Z and θ). This is because we just need a single value, and real variables only take up 15 bytes of memory (other variables are just as small, but they take up more memory when you're accessing them).

Now that the loop and variable have been chosen, we need to setup the system of loops to act as the subprograms. What works best is to have a main program loop and then place the subprogram loops inside of it. Putting the variable and loops together, here is what the program skeleton looks like:

```
:Repeat not(A  // main program loop
:1→A
:While A=1
: // subprogram 1
:2→A  // enter loop for second subprogram
:End
:While A=2
: // subprogram 2
:DelVar A  // exit main program loop
:End
: // rest of subprograms
:End
```

You just set the value of the variable in the loop to use the desired subprogram. Then when you are done with the subprogram, you just change the value of the variable to something different to exit the loop. You do the same thing to exit the main program loop. You can use whatever system of values for the variable that you want, but just remember to keep it simple enough so that you can come back to it later and it still makes sense to you.

The one drawback of using this approach is that the calculator has to go through all the subprograms to exit the main program loop, which can really be slow depending on the size of the subprograms. At the same time, this approach is very easy to understand and follow because the loops are organized in a straight forward manner, so it's kind of an even trade off.

Related to using structured loops, the alternative you can use is branching. While using branching by itself to structure a program is generally frowned upon (see [planning programs](plan.html) for more information), you can actually use it quite effectively for making internal subprograms that only need to be called a few times. Here is a simple example:

```
:0→A:Goto A
:Lbl B
: // main program code
:1→A:Goto A
:Lbl C
: // main program code
:Stop
:Lbl A
: // subprogram code
:If A:Goto C
:Goto B
```

The A variable is used for determining when to stop the program: a zero value will simply cause the subprogram to jump back to the main program, but a value of one will cause the subprogram to jump to the exit of the program (the C label). Because the calculator doesn't store the label positions, there is no way to get memory leaks using this approach, which is especially important when exiting the program. However, it does get hard to follow and maintain the code the more branching there is.

### Branching out of Loops

The last way to make internal subprograms is arguably the most difficult to understand, but once you have it setup in your program, it provides an easy framework for adding additional subprograms. The best time to use these kind of subprograms is when you have a main program loop that you're running and you want to be able to jump out of it and then back into it whenever you want.

The basis of these subprograms is using branching ([Goto](goto.html) and [Lbl](lbl.html)) with loops and [conditionals](if.html) (anything that uses an [End](end.html) command). Branching by itself allows the calculator to jump from one point in a program to another, skipping over whatever code you don't want executed. When you use branching to exit loops and conditionals, however, it has the unwanted effect of causing memory leaks.

Memory leaks happen because the calculator doesn't get to reach the End command for the associated loop or conditional, and the calculator just keeps on storing the End commands in its stack until there is eventually no free memory left. (Memory leaks can also occur with excessive program [recursion](recursion.html).) Here is a simple example that has a memory leak:

```
:Lbl A
:While 1
:Goto A
:End
```

If you notice, when the Goto A command is executed, it jumps to the matching label A that is on the line before the loop. The While 1 loop is never allowed to finish because the End command never gets reached, and the branching occurs over and over again until the calculator finally slows down to a stop (because there is less and less free memory available) and returns a memory error.

This type of programming is common with beginners, and its use is generally frowned upon; instead you should try to use proper program structure (see [planning programs](plan.html) for more information). However, if you know what you are doing, you can actually use these broken loops and conditionals for internal subprograms, and you won't have to worry about memory leaks or the dreaded memory error.

There are two different approaches that you can use. The first approach is to use another Goto and matching label to jump back into the loop. Because the calculator doesn't store the labels, you can freely use whatever branching in the loop that you want, and the calculator will act like it had never even left the loop:

```
:Repeat getKey
:Goto A
:Lbl B
:End
:Stop
:Lbl A
: // subprogram code
:Goto B
```

The key here is that the Goto A command jumps to the matching label A outside the loop, and then the Goto B jumps to the matching label B back inside the loop. The calculator still has the loop's associated End command on its stack, so the loop will just keep looping without problems until you eventually press a key to stop it and it executes the Stop command.

While this first approach works rather nicely in small programs, it is not very practical for use in large programs because all the branching starts to slow the program down. Unlike loops and conditionals, the calculator doesn't keep track of the label positions, so it must start from the beginning of the program to find the matching label to jump to. The further down the label is in the program code, the more time the calculator must spend looking for it.

The second approach solves this problem by using a duplicate End command for the loop or conditional. Since the calculator keeps track of the number of unfinished loops and conditionals by storing the associated End commands in its stack, we can make the calculator believe that our different End command is actually the End command that belongs to the loop. Here is a simple example to illustrate:

```
:Repeat getKey
:Goto A
:End
:Stop
:Lbl A
: // subprogram code
:End
```

Like with the first approach, when Goto A is executed the program will jump to the matching label A, and then the subprogram code will be executed. This time, however, the calculator will read the End command after the subprogram code, which it believes is the end of the loop, and then immediately jump back to the beginning of the loop. This process will be repeated over and over again until the user presses a key, at which time the Stop command will be executed and the program will stop.

The subprogram code for both approaches can be whatever you want, including other loops and conditionals. You just need to remember to close the loops and conditionals before returning to the original loop, otherwise the calculator will have the wrong End command on its stack. You also want to have a matching number of End commands for your loops and conditionals, or you will get a memory leak.

#### Advanced Uses

There are a couple different ways you can enhance the duplicate End subprogram approach so that you get the most use out of it. The first way is relatively simple, and just involves using a For( loop as the looping structure, instead of a While loop or Repeat loop (which is what we had in our previous examples).

A For( loop is basically a specialized form of a While loop, with the main differences being that it is executed a specific number of times and it has the variable setup and ending condition built-in. You just choose a variable, the range of values, and the increment (it is optional, with one as the default); and then the loop will start the variable at the initial value and increment it each time until it reaches the ending value.

Now when you start using the For( loop for internal subprograms, you need to make sure the For( loop executes at least twice. This is so that the End command of the For( loop gets used along with the End command of the subprogram, otherwise it will simply fall through after the first time through the loop. You can select different subprograms based on the variable's value. Here is our example from above, now using a For( loop instead:

```
:For(A,0,1
:If not(A:Goto A
:End
: // main program code
:Stop
:Lbl A
: // subprogram code
:End
```

When the For( loop is executed, the A variable is set to zero. The not(A condition is true, so the calculator executes the Goto A command and then jumps to the matching label A. The calculator then jumps back to the beginning of the For( loop and increments the A variable to one. This time, however, there is no subprogram jump taking place, and the calculator simply finishes the For( loop like normal.

The second way to enhance the duplicate End subprogram approach is by using a simple trick. Because a While loop loops only when the condition is true, when the calculator comes across a While loop with a false condition, it will simply skip over the entire loop (and everything inside the loop). The easiest way to make a false condition is to use zero, since zero will never be true (based on Boolean logic). Here is a simple example to demonstrate:

```
:While 0
:Lbl A
: // subprogram code
:End
: // main program code
:If getKey:Then
: // program code
:Goto A
:End
```

When the calculator encounters the While 0 loop, it won't execute it because 0 is false. After the calculator enters the subprogram conditional, it executes some program code and then hits the Goto A command and jumps to the matching label A inside the While 0 loop. The calculator takes the End command of the loop as the End command of the conditional, and thus no memory leak occurs.

The reason that this trick is so valuable is because it allows you to place your subprograms at the beginning of the program, and you don't ever have to worry about them being accidentally executed (they will always be skipped over). In addition, now that the labels are at the beginning of the program, there is no more speed problem to deal with, since the calculator doesn't have to search through the entire program to find the labels.

### Advantages

The main advantage of using internal subprograms is that there is only one program needed to make your program run. When you give someone your program, you don't have to worry about forgetting to include any subprograms; or somebody deleting your subprograms afterwards, causing your program to stop working correctly. These things are mostly out of your hands, but users will think your program is at fault. 

Related to the first advantage, the other advantage is that the user's program menu doesn't get  cluttered up with insignificant subprograms. This problem is relative to how many subprograms a program has, but it can become tiresome to have to sort through the program menu in order to find the program that you want. If anything, this is just a nice courtesy to the users of your programs.

## References

- Arthur O'Dwyer and his guide [The Complete TI-83 Basic Optimization Guide](http://tibasicdev.github.io/local--files/downloads/83trix.zip)
- Brad Wentz and his guide [Loop Trick for z80 Calcs](http://tibasicdev.github.io/local--files/downloads/looptrick.zip)

<center>

|**[<< Commenting Code](comments.html)**|**[Overview](development.html)**|**[Program Cleanup >>](cleanup.html)**|
| --- | --- | --- |

</center>
