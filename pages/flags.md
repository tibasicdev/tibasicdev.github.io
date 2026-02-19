# Using Variables as Flags
When programming, you may find that you want to execute a piece of code based on if another section of code has been executed. The easiest way to do this is to use a flag. What exactly is a flag? A flag is typically considered a placeholder or variable which contains a binary or Boolean value. In TI-Basic, it is typically a variable which holds a value of 0 or 1. This variable is called a flag because it is either up (1), or down (0). Flags can be very useful when used in the proper circumstance; They can help prevent double conditionals, allow for the program to behave differently based on which sections of code it has already run, or even change what a program does altogether. Let's look at an example:
```
prgmFLAG
:0→F
:Lbl 1
:Disp "Flag is"
:If F:Disp "Up"
:If not(F:Disp "Down"
:If F:Return
:1→F
:Goto 1
```
In the code above, we see a very basic flag. The flag is either up, 1, or down, 0. The program will display that the flag is down, set it to be up, then say that it is up before exiting. That's a great start, but how can flags be used in more useful ways? 

### Recycled Flags

Recycled flags are flags that are used more than once for the same purpose inside of a program. They are commonly used within loops, but can be used in other ways depending on what you are attempting to do. Consider the following: You have a variable A which you want to compare to B; If A is greater than B, you want to display a message. The only catch is, if A is greater than 50 you want to display a different message. This is a perfect place for a Recycled flag, especially if you want to repeat the comparison with different values. Take a look at the following code:
```
prgmACOMPB
:randInt(1,50→B
:Repeat A=B
:1→T
:Prompt A
:If A>50
:Then
:Disp "A is Greater than 50"
:0→T
:End
:If T(A>B):Disp "A is Greater than B"
:If A<B:Disp "A is Less than B"
:End
```
Did you understand how it worked? If not, let me walk you through it. As you may have guessed, this is a very simple guess the number game. First, we store a value to B. This value doesn't particularly matter, but we want it to be 50 or less for this game. We create a repeat loop that will run until we enter the value of B. Next, we set our flag. I put this flag setting inside the repeat loop, since we want it to reset every time we enter a new number. The program will then ask the user for a value of A to test, and now this is where the flag comes in. The program tests if A is above 50, in which case it would be out of the range of values of B. If A is greater than 50, it displays that and sets our flag to 0, or turns it off. The next conditional tests if A is greater than B. If A is greater than 50, it will always be greater than B, but since we already determined if it was greater than 50, we don't want to accidentally display a message twice. If you take a close look at the statement, we are testing "If T(A>B)" which can be rewritten as "If T and A>B" or even "If T≠0 and A>B". Lets step back and look at the values of when we compared A to 50. If A was greater than 50, T got set to 0; If A was less than or equal to 50, T was left as 1. This means that the statement we are testing will only be true if A is less than or equal to 50 based on the value in T. 

### Solitary Flags

The flag in the last example was a recycled flag, meaning we used it multiple times. This is debatably the most common form of flags. The other type of flag is a solitary flag, or a flag that is only used once. Perhaps the best example of this is a program where the author wants the user to do something before running the program. A flag may be used to allow the program to give instruction to the user before executing the code. 
```
If A
Then
ClrAllLists
Output(1,1,"Please enter data in L₁
Delvar A
Pause
Return
End
Disp mean(L₁
1→A
```
While this is another simple piece of code, it displays a solitary flag very well. This program displays the mean of L₁, however we know that if there is no data in L₁ this code will throw an error. Lists are one of the variables that cannot be directly stored to using input or prompt, and because of this we want to tell the user to enter their data into the list. This code checks to see if there is a value stored in A, and if there is it then tells the user to enter the data, sets the flag, and exits. The reason this code checks to see if there is a value in A rather than if there is not a value in A is due to the fact that there will be a value in A most of the time. This program, for the flag, sets A to 0 by deleting it once it has told the user where to enter the data. When the program is run again, presumably after they have entered their data, it will see that there is no value and will then display the mean of L₁ as intended before finally putting a value back into A so it can be run again.
