# Review Exercises
As a way to test your comprehension of the information, and to ensure that you actually read through the information instead of merely skimming over it, we have provided review exercises. These exercises provide a way of helping you apply the information, so that you get a fuller understanding of the concepts.  Highlight the area next to the word answer for the answer.[[/span]]




**1**. *True* or *False*: The ClrHome command should be used at the end of a program, to ensure that the program does not leave any leftover text on the home screen.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
True. Although you still will have a Done message at the end. To eliminate this you can add this to the end of your code Output(1,1,"
```
</details>

**2**. What type of variable cannot hold a complex number?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Matrix.
```
</details>

**3**. Which of the following uses of the Disp command returns an error?
1. Disp
2. Disp ""
3. Disp "Hello World
4. Disp "Hello","World
5. None of the above

**Answer:**<details style="display: inline;"><summary>show</summary>
```
None of above.
```
</details>

**4**. Which draw command cannot be called from a program?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Pen. It's technically not a command, but it is accessed in the draw menu like a command.
```
</details>

**5**. What is the difference between the iPart( and int( commands?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
The difference between iPart( and int( is subtle, and many people aren't even aware of it, but it exists. Whereas iPart( always truncates its parameters, simply removing the integer part, int( always rounds down. This means that they return the same answers for positive numbers, but int( will return an answer 1 less than iPart( for (non-integer) negative numbers. For example, iPart(-5.32) is -5, while int(-5.32) is -6.
```
</details>

**6**. *True* or *False*:  Programs can use the home screen for everything they can do on the graph screen.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False. There are no graphics commands available on the home screen.
```
</details>

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

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Add a closing quote on the menu title.
```
</details>

**8**. In a statistics class, the teacher asks the students to generate a list of 100 random numbers. Unfortunately, the exercise doesn't work as intended because 22 students, in a class of 30, get the exact same numbers (using different calculators). What's a likely explanation for this surprising coincidence?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
They all had the rand command seeded to zero.
```
</details>

**9**. How many digits of accuracy does the TI-OS have? How many can it display on the screen?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
It has fourteen digits of accuracy, but only ten will be displayed.
```
</details>

**10**. The Output( command can display text at any place on the screen, but what happens when the text goes past the end of the line?
1. Nothing. The text simply does not show up.
2. An error is returned.
3. The text will wrap around to the next line.
4. An ellipsis will be displayed at the end of the line, with the rest of the text not being displayed.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
The text will wrap around to the next line.
```
</details>

**11**. *True* or *False*: You need to use a Pause command before clearing the screen, otherwise the user will only see the text on the screen for a couple seconds; it will be a blur.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False. There are other options available, including using the rand command for a short delay or using a small Repeat getKey:End loop.
```
</details>

**12**. When is using the Menu( command appropriate, and even desired? (Choose the best answer.)
1. If you want a generic menu.
2. Your program is going to be text-based.
3. It is the most practical menu available in your situation.
4. You want your program to stand out, so you need a fancy menu.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
The first three answers are all good, but the best answer is if you want a generic menu.
```
</details>

**13**. What would be the effect of replacing a Disp command with an Output( command and vice verse? Give any instances where this switch might be useful. Also, when would you use Disp in conjunction with Output?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
|The Output( command doesn't scroll the screen when it gets to the bottom, like the Disp command does. The main instance where this is useful is when you have lots of text that you are displaying, and the Output( command will wrap it around to the next line. Output( is also faster than Disp .
```
</details>

**14**. What is the maximum dimension of a list?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
999. Note, however, that a list that size would barely fit in RAM.
```
</details>

**15**. Which one statement is true about this code?
```
:Menu("","",B,"",B
:Disp "Test
:Lbl B
:Disp "Pizza
:Output(1,1,"Spaghetti
```
1. An error will be returned when the Menu command is executed.
2. The program will execute, but there will not be any text displayed.
3. The "Test" text will be displayed along with the "Pizza" and "Spaghetti" text.
4. The "Pizza" and "Spaghetti" text will be displayed, but not the "Test".

**Answer:**<details style="display: inline;"><summary>show</summary>
```
The "Pizza" and "Spaghetti" text will be displayed, but not the "Test"
```
</details>

**16**. *True* or *False*: Before using the Menu( command, you need to clear the home screen, otherwise you will have text interrupting the menu.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False. The Menu( command uses its own screen, which is separate from the home screen.
```
</details>

**17**. Consider the following code:
```
:0:Menu("Difficulty","Easy",3,"Medium",2,"Hard",1
:Lbl 1:Ans+1
:Lbl 2:Ans+1
:Lbl 3:Ans+1
```
The Ans variable keeps track of the last answer, often being used in place of more permanent variables. If the user selects the "Hard" menu item, what will Ans's value be? What effect does the label ordering have on the value, if any? Why?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Ans's value will be three. The label ordering causes the value of Ans to be incremented by one for each difficulty level.
```
</details>

**18**. *True* or *False*: Using the home screen is faster than using the graph screen?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False. Both take the same time.
```
</details>

**19**. Which of the following cannot be used to test if a variable is any of 1, 2, 3, or 4?

1. If sum(A={1,2,3,4
2. If (A=int(A))(A>=1)(A<=4)
3. If A={1,2,3,4}
4. If A(int(A)=A)(A<5)

**Answer:**<details style="display: inline;"><summary>show</summary>
```
If A={1,2,3,4} because the If command does not work with lists.  However, #4 would also trigger, for all integers less then 5 except for 0.
```
</details>

**20**. *True* or *False*: The following is an alternate to using the or operator.

```
:If (X=1)+(X=2
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
True.
```
</details>

**21**. Name a command or function that cannot be interrupted by pressing the [ON] key.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
randBin(, SortA(, and SortD( all will work.
```
</details>

**22**. For which of the following would not(B) not equal 0?

1. .01→B
2. 0→B
3. π→B
4. -4→B

**Answer:**<details style="display: inline;"><summary>show</summary>
```
0→B. Remember that not( negates the value, so 0 becomes 1.
```
</details>

**23**. *True* or *False*: The following is an alternative to using the and operator.

```
:If Anot(B
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False.  Actually, in that code, the not(B is done first, so the only thing that returns true with that is if A is 1, and B is 0.  Not a replacement of and.
```
</details>

**24**. How many bytes is an uppercase character? A lowercase character?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
An uppercase character is one byte, while a lowercase character is two bytes.
```
</details>

**25**. Which of these user-created list names are actually possible on the calculator?

1. L1234
2. LBaDd
3. Lθθθθ
4. LABCD

**Answer:**<details style="display: inline;"><summary>show</summary>
```
|Lθθθθ and LABCD. A list can't start with a number, and lowercase letters aren't allowed.
```
</details>

**26**. What type of variable needs a special command to store to it?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Picture and GDB. You use the StorePic and StoreGDB command.
```
</details>

**27**. Change this short program so it doesn't flicker and then optimize it as much as possible.

```
:0→X:0→Y:Repeat 0
:ClrHome
:Output(Y,X,"X")
:getKey→K
:If K=24:X-1→X
:If K=25:Y+1→Y
:If K=26:X+1→X
:If K=34:Y-1→Y
:End
```

**Answer:**<details style="display: inline;"><summary>show</summary>Here is one possibility:
```
:4→X:4→Y:Repeat 0
:Output(Ans,X,"X
:Repeat Ans:getKey→K:End
:Output(Y,X,"  // 1 space
:X+(Ans=26)-(Ans=24→X
:Y+(K=34)-(K=25→Y
:End
```
</details>

**28**. *True* or *False*: You can archive another program from within a program.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
False. You can, however, archive another program outside a program.
```
</details>

**29**. What is the maximum length of a string?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
There is none. It is only limited by the amount of RAM.
```
</details>

**30**. Which of the following variables is it possible to archive?

1. Y<sub>1</sub>
2. prgmKEWLGAME
3. the real variable T
4. the real variable A
5. L_RESID
6. L<sub>1</sub>

**Answer:**<details style="display: inline;"><summary>show</summary>
```
prgmKEWLGAME, the real variable A, and L1. Trying to archive Y1T,, and ∟RESID will give you an ERR:VARIABLE error.
```
</details>

**31**. Without trying it first, is this legal?

```
:[A]L4([A]([A](L1(1),L2(1)),L1(1(L2(2L3
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
|No. While the syntax is correct, an error is returned when trying to get the particular element multiplied by the entire L3 list.
```
</details>

**32**. How would you find the fifth element from the last in a sequence of 20 elements?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Assuming the list is L1, you would just use::L1(15
```
</details>

**33**. What will this code do?

```
:DelVar B1→A
:If A:If B
:Disp "Hello World
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Nothing. It doesn't output anything on the screen.
```
</details>

**34**. How do you get rid of the Done message at the end of a program?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
You can remove the "Done" message that appears after a program is finished running by placing an expression, some text, or just a quote on the last line of your program.
```
</details>

**35**. Write a program that inputs a string and outputs the letters backward, one per line.

**Answer:**<details style="display: inline;"><summary>show</summary>Here is one possibility:
```
:Input "TEXT:",Str1
:For(X,length(Str1),1,-1
:Disp sub(Str1,X,1
:rand(10
:End
```
</details>

**36**. Will this code execute?

```
:If 0:Disp "Your turn
:Else:Disp "Guess not
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
No, it will give you an error.
```
</details>

**37**. What is the simplest program you can have that has recursion?

**Answer:**<details style="display: inline;"><summary>show</summary>A one-liner that just calls itself:
```
PROGRAM:A
:prgmA
```
</details>

**38**. Which of these are logically equivalent?

1. not(P or Q)
2. P and Q
3. not(P and Q)
4. not(P) or not(Q)
5. not(P) and not(Q)

**Answer:**<details style="display: inline;"><summary>show</summary>
```
"not(P or Q)" and "not(P) and not(Q)" are logically equivalent, while "not(P and Q)" and "not(P) or not(Q)" are logically equivalent. This is based off of DeMorgan's Law.
```
</details>

**39**. *True* or *False*: There are actually 256 picture variables on the calculator, even though only 10 picture variables show up.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
True. Although the other 246 must be accessed through assembly.
```
</details>

**40**. What are the differences between Assembly and TI-Basic? When would you use Assembly and when would you use TI-Basic?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Unlike TI-Basic, which uses commands and functions that are easy to understand, assembly is programmed in the calculator's own machine language, and thus is much harder to program in and read. You would use assembly when you want your program to be fast, and you would use TI-Basic when you want to program your game fast.
```
</details>

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

**Answer:**<details style="display: inline;"><summary>show</summary>
```
This is a trick question. The while loop is false, so X never changes and it ends at 0.
```
</details>

**42**. What is wrong with this code?

```
:If X=25 Then
:Disp "X is 25
:X+1→X
:Disp "X is now", X
:End
```

**Answer:**<details style="display: inline;"><summary>show</summary>
```
You need to change the space between X=25 and Then to a colon, and remove the space to the left of the second X in Disp "X is now", X:
```
</details>

**43**. What are the only keys that can actually be held down, causing them to be repeated?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
The arrow keys and DEL.
```
</details>

**44**. How would you go about converting a list to a matrix? What would the code look like?

**Answer:**<details style="display: inline;"><summary>show</summary>
```
Just use the List►matr( command.
```
</details>

**45**. *True* or *False*: There is no built-in way to convert a string to a number.

**Answer:**<details style="display: inline;"><summary>show</summary>
```
True. The expr( command does this.
```
</details>

[[html]]
<br><br>
[[/html]]
