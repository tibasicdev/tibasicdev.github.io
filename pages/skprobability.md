# Probability
Probability functions are helpful for generating random numbers, and provide an element of variability in many calculator games.  Examples include an asteroid game where you avoid a random map of asteroids with your ship while crossing the screen, and RPGs where opponents need to have slightly unpredictable power in their attacks.
## Key Commands
The main commands to use in random number generation are [rand](rand.html) and [randInt(](randint.html).  By itself, rand generates a decimal number between 0 and 1.  This number can be manipulated like any other number, making it very easy to set up a random event.  Lets say you want to randomize the description of a character's death in an RPG.  You want to say that the dragon ate him half the time, and that the dragon burnt him to a crisp the other half.  This is how you could do that with rand.

```
:"The dragon ate him
:If int(2rand
:"The dragon burned him
:Output(1,1,Ans
```
This works because doubling the rand command gives you a number between 0 and 2.  If rand is less than .5, it will be doubled to between 0 and 1 and converted to 0 as the integer side is empty.  If the number is greater than .5, it will be converted to 1 by int(.  Notice that because there is only one possible outcome where the random number is a positive integer, you don't need to check if it is exactly one. We'll show you in a minute how to generate lists with rand as well.

randInt( is useful for doing the same thing as above but in a more visually simple manner.  Instead of needing to convert a random decimal to integers, the calculator does the work for you.  It takes either 2 or 3 arguments.  The first two are the minimum and maximum, and optionally you can add a third to create a list of integers.  To create a list of 20 dice rolls, the code would be like this:
```
:randInt(1,6,20
```
The same can be accomplished with rand, albeit in a more complex manner. The rand command can create lists when you add parenthesis and an argument for the size of the list.
```
:1+int(6rand(20
```
<center>

|**[<< Powers and Exponentials](sk:powers-exponentials.html)**|**[Table of Contents](starter-kit.html)**|**[Trigonometry >>](sk:trigonometry.html)**|
| --- | --- | --- |

</center>
