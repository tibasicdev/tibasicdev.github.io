# Review Exercises (Answers)
As a way to test your comprehension of the information, and to ensure that you actually read through the information 
instead of merely skimming over it, we have provided review exercises. These exercises provide a way of helping you apply the information, so that you get a fuller understanding of the concepts.



**1**. *True* or *False*: The ClrHome command should be used at the end of a program, to ensure that the program does not leave any leftover text on the home screen.

**Answer**: True. Although you still will have a Done message at the end. To eliminate this you can add this to the end of your code Output(1,1," 



**2**. What type of variable cannot hold a complex number?


**Answer**: Matrix.


**3**. Which of the following uses of the Disp command returns an error?
1. Disp
2. Disp ""
3. Disp "Hello World
4. Disp "Hello","World
5. None of the above.


**Answer**: None of above.


**4**. Which draw command cannot be called from a program?


**Answer**: [Pen](pen.html). It's technically not a command, but it is accessed in the draw menu like a command.


**5**. What is the difference between the iPart( and int( commands?


**Answer**: The difference between [iPart(](ipart.html) and [int(](int.html) is subtle, and many people aren't even aware of it, but it exists. Whereas iPart( always truncates its parameters, simply removing the integer part, int( always rounds down. This means that they return the same answers for positive numbers, but int( will return an answer 1 less than iPart( for (non-integer) negative numbers. For example, iPart(-5.32) is -5, while int(-5.32) is -6.


**6**. *True* or *False*:  Programs can use the home screen for everything they can do on the graph screen.


**Answer**: False. There are no graphics commands available on the home screen. 


**7**. What is the minimal modification that will allow this code to start-up?
```
:Menu("Choose One,"Menu Item",1,"Menu Item",2
:Lbl A
:Pause "Item 1
:Stop
:Lbl 2
:Pause "Item 2
```
1. Add a closing quote on the menu title.
2. Remove the Stop command.
3. Change Lbl A to Lbl 1.
4. Add a closing quote on the menu title and change Lbl A to Lbl 1.


**Answer**: Add a closing quote on the menu title.


**8**. In a statistics class, the teacher asks the students to generate a list of 100 random numbers. Unfortunately, the exercise doesn't work as intended because 22 students, in a class of 30, get the exact same numbers (using different calculators). What's a likely explanation for this surprising coincidence?


**Answer**: They all had the [rand](rand.html) command seeded to zero.


**9**. How many digits of accuracy does the TI-OS have? How many can it display on the screen?


**Answer**: It has fourteen digits of accuracy, but only ten will be displayed.


**10**. The Output( command can display text at any place on the screen, but what happens when the text goes past the end of the line?
1. Nothing. The text simply does not show up.
2. An error is returned.
3. The text will wrap around to the next line.
4. An ellipsis will be displayed at the end of the line, with the rest of the text not being displayed.


**Answer**: The text will wrap around to the next line.


**11**. *True* or *False*: You need to use a Pause command before clearing the screen, otherwise the user will only see the text on the screen for a couple seconds; it will be a blur.


**Answer**: False. There are other options available, including using the [rand](rand.html) command for a short delay or using a small Repeat getKey:End loop.


**12**. When is using the Menu command appropriate, and even desired? (Choose the best answer.)
1. If you want a generic menu.
2. Your program is going to be text-based.
3. It is the most practical menu available in your situation.
4. You want your program to stand out, so you need a fancy menu.


**Answer**: The first three answers are all good, but the best answer is if you want a generic menu.


**13**. What would be the effect of replacing a Disp command with an Output command and vice versa? Give any instances where this switch might be useful.


**Answer**: The [Output(](output.html) command doesn't scroll the screen when it gets to the bottom, like the [Disp](disp.html) command does. The main instance where this is useful is when you have lots of text that you are displaying, and the Output( command will wrap it around to the next line.


**14**. What is the maximum dimension of a list?


**Answer**: 999. Note, however, that a list that size would barely fit in RAM.


**15**. Which one statement is true about this code?
```
:Menu("","",B,"",B
:Disp "Test
:Lbl B
:Disp "Pizza
:Output(1,1,"Spaghetti
```
1. An error will be returned when the Menu( command is executed.
2. The program will execute, but there will not be any text displayed.
3. The "Test" text will be displayed along with the "Pizza" and "Spaghetti" text.
4. The "Pizza" and "Spaghetti" text will be displayed, but not the "Test".


**Answer**: The "Pizza" and "Spaghetti" text will be displayed, but not the "Test".


**16**. *True* or *False*: Before using the Menu( command, you need to clear the home screen, otherwise you will have text interrupting the menu.


**Answer**: False. The [Menu(](menu.html) command uses its own screen, which is separate from the home screen.


**17**. Consider the following code:
```
:0:Menu("Difficulty","Easy",3,"Medium",2,"Hard",1
:Lbl 1:Ans+1
:Lbl 2:Ans+1
:Lbl 3:Ans+1
```
The Ans variable keeps track of the last answer, often being used in place of more permanent variables. If the user selects the "Hard" menu item, what will Ans's value be? What effect does the label ordering have on the value, if any?


**Answer**: [Ans](ans.html)'s value will be three. The label ordering causes the value of Ans to be incremented by one for each difficulty level.


**18**. *True* or *False*: Using the home screen is faster than using the graph screen?


**Answer**: False. Both take the same time.


**19**. Which of the following cannot be used to test if a variable is any of 1, 2, 3, or 4?

1. If sum(A={1,2,3,4
2. If (A=int(A))(A>=1)(A<=4)
3. If A={1,2,3,4}
4. If A(int(A)=A)(A<5)


**Answer**: If A={1,2,3,4} because the [If](if.html) command does not work with [lists](lists.html). 


**20**. *True* or *False*: The following is an alternate to using the or operator.

```
:If (X=1)+(X=2
```


**Answer**: True.


**21**. Name a command or function that cannot be interrupted by pressing the [ON] key.


**Answer**: [randBin(](randbin.html), [SortA(](sorta.html), and [SortD(](sortd.html) all will work.


**22**. For which of the following would not(B) not equal 0?

1. .01→B
2. 0→B
3. π→B
4. -4→B


**Answer**: 0→B. Remember that [not(](not.html) negates the value, so 0 becomes 1.


**23**. *True* or *False*: The following is an alternative to using the and operator.

```
:If Anot(B
```


**Answer**: True.  Remember that [multiplication](multiply.html) is implicitly done on the TI-83 calculators.


**24**. How many bytes is an uppercase character? A lowercase character?


**Answer**: An uppercase character is one byte, while a lowercase character is two bytes.


**25**. Which of these user-created list names are actually possible on the calculator?

1. L1234
2. LBaDd
3. Lθθθθ
4. LABCD


**Answer**: Lθθθθ and LABCD. A list can't start with a number, and lowercase letters aren't allowed.


**26**. What type of variable needs a special command to store to it?


**Answer**: Picture and GDB. You use the [StorePic](storepic.html) and [StoreGDB](storegdb.html) command. 


**27**. Change this short program so it doesn't flicker and then optimize it as much as possible.

```
:4→X:4→Y:Repeat 0
:ClrHome
:Output(Y,X,"X")
:getKey→K
:If K=24:X-1→X
:If K=25:Y+1→Y
:If K=26:X+1→X
:If K=34:Y-1→Y
:End
```


**Answer**: Here is one possibility:

```
:4→X:4→Y:Repeat 0
:Output(Ans,X,"X
:Repeat Ans:getKey→K:End
:Output(Y,X,"  // 1 space
:X+(Ans=26)-(Ans=24→X
:Y+(K=34)-(K=25→Y
:End
```


**28**. *True* or *False*: You can archive another program from within a program.


**Answer**: False. You can, however, archive another program outside a program.


**29**. What is the maximum length of a string?


**Answer**: There is none. It is only limited by the amount of RAM.


**30**. Which of the following variables is it possible to archive?

1. Y<sub>1</sub>
2. prgmKEWLGAME
3. the real variable T
4. the real variable A
5. ∟RESID
6. L<sub>1</sub>


**Answer**: prgmKEWLGAME, the real variable A, and L<sub>1</sub>. Trying to archive Y<sub>1</sub>T,, and ∟RESID will give you an [ERR:VARIABLE](errors.html#variable) error.


**31**. Without trying it first, is this legal?

```
:[A]L4([A]([A](L1(1),L2(1)),L1(1(L2(2L3
```


**Answer**: No. While the syntax is correct, an error is returned when trying to get the particular element multiplied by the entire <sub>L</sub>3 list.


**32**. How would you find the fifth element from the last in a sequence of 20 elements?


**Answer**: Assuming the list is L1, you would just use:

```
:L1(15
```


**33**. What will this code do?

```
:DelVar B1→A
:If A:If B
:Disp "Hello World
```


**Answer**: Nothing. It doesn't output anything on the screen.


**34**. How do you get rid of the Done message at the end of a program?


**Answer**: You can remove the "Done" message that appears after a program is finished running by placing an expression, some text, or just a quote on the last line of your program. 


**35**. Write a program that inputs a string and outputs the letters backward, one per line.


**Answer**: Here is one possibility:

```
:Input "TEXT:",Str1
:For(X,length(Str1),1,-1
:Disp sub(Str1,X,1
:rand(10
:End
```


**36**. Will this code execute?

```
:If 0:Disp "Your turn
:Else:Disp "Guess not
```


**Answer**: No, it will give you an error.


**37**. What is the simplest program you can have that has recursion?


**Answer**: A one-liner that just calls itself:

```
PROGRAM:A
:prgmA
```


**38**. Which of these are logically equivalent?

1. not(P or Q)
2. P and Q
3. not(P and Q)
4. not(P) or not(Q)
5. not(P) and not(Q)


**Answer**: "not(P or Q)" and "not(P) and not(Q)" are logically equivalent, while "not(P and Q)" and "not(P) or not(Q)" are logically 
equivalent. This is based off of DeMorgan's Law.


**39**. *True* or *False*: There are actually 256 picture variables on the calculator, even though only 10 picture 
variables show up.


**Answer**: True. Although the other 246 must be accessed through asm.


**40**. What are the differences between assembly and TI-Basic? When would you use assembly and when would you use TI-Basic?


**Answer**: Unlike TI-Basic, which uses commands and functions that are easy to understand, assembly is programmed in the calculator's own machine language, and thus is much harder to program in and read. You would use assembly when you want your program to be fast, and you would use TI-Basic when you want to program your game fast.


**41**. How long will the program go through the loop until it stops execution?

```
:0→X
:While X
:Disp "Another Loop
:X+1→X
:If X=25
:Stop
:End
```


**Answer**: Trick question the while loop is false.So X never changes and it ends at 0.


**42**. What is wrong with this code?

```
:If X=25 Then
:Disp "X is 25
:X+1→X
:Disp "X is now", X
:End
```


**Answer**: You need to change the space between X=25 and Then to a colon, and remove the space to the left of the second X in Disp "X is now", X:

```
:If X=25:Then
:Disp "X is 25
:X+1→X
:Disp "X is now",X
:End
```


**43**. What are the only keys that will be repeated if they are held down?


**Answer**: The arrow keys and DEL.


**44**. How would you go about converting a list to a matrix? What would the code look like?


**Answer**: Just use the [List►matr(](list-matr.html) command.


**45**. *True* or *False*: There is no built-in way to convert a string to a number.


**Answer**: False. The [expr(](expr.html) command does this.
