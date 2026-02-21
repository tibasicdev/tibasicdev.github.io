# Games Excersizes
## Review
1. What command will automatically unarchive a list and create it if it doesn't exist?
2. What data type would you use to save a highscore?
3. What is the seed and what is it useful for?
4. What type of loop is appropriate to use for a game like Yahtzee?
5. What is the code for movement?
6. How can you modify the movement code in order to make it so that when you go off the screen, you loop to the other side?
7. Can you use the sub( command to find the element in a matrix?
8. Make a formula using rand as the only random command to yield the same results as randBin( with a given seed of 0.
9. What happens when you take the inverse of a matrix with determinant 0?

## Programming
Modify the following movement code that is supposed to move two objects simultaneously according to user input.
```
:1→A
:1→B
:4→C
:4→D
:Repeat K=21
:getKey→K
:If Ans
:Output(A,B,"_")
:min(8,max(1,A+sum(ΔList(Ans={25,34}))))→A
:min(16,max(1,B+sum(ΔList(K={24,26}))))→B
:Output(A,B,"X")
:End
```
Explain the usage for this code.
```
:rand→A
:A→rand
```
Create a game where the player must make it through a maze when the arrow key movements are jumbled up.

<center>

|**[<< Summary](sk:summary-games.html)**|**[Table of Contents](starter-kit.html)**|**[Sample Program: Chase the Star >>](sk:chase-the-star.html)**|
| --- | --- | --- |

</center>
