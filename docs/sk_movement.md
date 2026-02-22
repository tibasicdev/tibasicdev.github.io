# Movement
Movement is commonly used in programs as a way to add user interaction. It is part of [user input](userinput.html) as it relies exclusively upon the [getKey](getkey.html) command to work. You can use movement in many programs and for many different things, including moving a cursor in a menu or moving a character around the screen. It is the latter case that we are going to explain and show here.


## The Code

To achieve the function of movement, we need to use some intense code and combine that with the attribute of getKey.  First of all, the object that is being moved must have an identification.  In two-dimensional space, the object needs two numbers to represent its position: the *x* coordinate, and the *y* coordinate.  Those can be represented by a couple of real variables, for example, A and B.  The next key for movement is to change the object's position.  This can be done by adding or subtracting 1 to A or B, which will inevitably change the object's position.  The next thing is outputting the result.

### Home Screen

On the home screen, movement is quite easy.  The *x*-axis uses numbers 1-16, and the *y* axis uses numbers 1-8.  We'll provide a simple description of the code here.  First, we must identify the position of the object.  Our object is an X, and we want it to be at the center of the screen.  So, it needs to be at the coordinates (8,4).  However, remember that the position on the home screen is inverted to (*y*,*x*), so the actual coordinates are (4,8).  We want to store these coordinates.  Ok, easy enough...
```
:4→A
:8→B
```
Next, we need to make a loop so that the user can move the object multiple times.  We will use a [Repeat](repeat.html) loop so that the code will repeat until the condition is met.
```
:Repeat K=21
```
Now, we need to retrieve input from the user.  We need to use getKey to identify which arrow key was pressed.  So, we will simply install the command and store it into K.  Note that we could also use other keys for movement in place of the arrows (like the number pad for using 8 directions), but the arrow keys are simplest here.
```
:getKey→K
```
Now, we need to make sure that the user pressed a key.  We don't want to erase the object's current position on every loop, so we use a conditional to make sure the key is pressed.  Otherwise, the object blinks repeatedly.
```
:If Ans
```
The next step is to output the space.  If a key is pressed, we need to erase the X so that when we output its new position, the object isn't duplicated.  To erase something on the home screen, we simply output a space.
```
:Output(A,B," ")
```
The next part is one of the more confusing things we'll be teaching you in this guide, so listen closely.  We'll need to look at the code in reverse to analyze it.  Here is what it looks like:
```
:min(8,max(1,A+sum(ΔList(Ans={25,34→A
:min(16,max(1,B+sum(ΔList(K={24,26→B
```
A quick and dirty explanation.  We know K is the value of a keypress.  The point is to test which key exactly was pressed.  We compare the variable K to a list containing the left and right key values.  If left was pressed, the list becomes {1,0}.  If right was pressed, the list becomes {0,1}.  If neither, {0,0}.  Next is the [ΔList(](deltalist.html) command.  That command will calculate the difference between the second and first elements in the list.  So, if the list was {1,0}, then ΔList({1,0}) becomes {-1}.  ΔList({0,1}) is {1}, and ΔList({0,0}) is {0}.  [sum](sum.html)( is used to convert the list into a real number that can be added to B.  So, if the input was left, the operation becomes B+(-1).  Next up are the [max](max.html)( and [min](min.html)( commands.  The max( and min( commands are used to create a boundary for the object so that it does not fly off the screen, causing an error in the program.  max( compares 1 and the new value of B to make sure it is not too far to the left.  If it is, B is reset to 1.  The min( command compares the new value of B to 16 to make sure the object doesn't fly off to the right.  If it is, B automatically becomes 16.  This is done with both A and B, adjusting for the different boundaries and getKey values associated with the horiontal and vertical planes.

Finally, we need to output X at its new position.  Simply use the [Output](output.html)( command, and end the loop.
```
:Output(A,Ans,"X")
:End
```
(**Note!:** Ans is used because it is faster than using B.  Because we just calculated the value of B, its contents are already stored in Ans!)

Putting all this together, we can now create out program!
```
PROGRAM:MOVE
:4→A
:8→B
:Repeat K=21
:getKey→K
:If Ans
:Output(A,B," ")
:min(8,max(1,A+sum(ΔList(Ans={25,34→A
:min(16,max(1,B+sum(ΔList(K={24,26→B
:Output(A,Ans,"X")
:End
```
That's how movement works!  There are a few more things to consider though, and those are discussed below.  Remember that you don't need end brackets on the end of a line or in special situations like before the store command.  We use them here on the outputs to make it clearer that there is a space in the first one.

For an in depth explanation of the code, you can visit [this](movement-explanation.html) page.

## Simultaneous Movement

Movement is not limited to those two codes.  The next step is to add enhancements to make the code work everywhere.  For example, what if you have two things moving at the same time?  What does that code look like?  Unfortunately, the calculator can only output separate objects one at a time.  True simultaneous movement is hard to accomplish.  However, it can be simulated.

First of all, since you have multiple objects, you need multiple pairs of coordinates.  The easiest way would be to use a bunch of real variables, but that isn't always the best way.  For a small amount of objects, like from 2-3, real variables can be used.  However, for large amounts of objects, like 4-10 or even more, a [list](list.html) might be needed because of the limited amount of reals.  Now, another thing to consider is speed.  The more objects moving, the slower the program will be.  Make sure you define what you are wanting before writing a code.

Now, let's say you only want two things moving at a time.  You want the calculator to randomly move an X and an O.  First, you need to initialize their positions.  The X will start at the top left corner and the O will start at the bottom right.  Since we are moving only two objects, we can use real variables.  A and B will be X, and C and D will be O.
```
:1→A
:1→B
:8→C
:16→D
```
The next step is to start the loop.  The loop ends when the objects collide or a button is pressed.
```
:Repeat getKey or (A=C and B=D)
```
Now, since the two objects are just moving randomly, you don't need to ask for input.  Thus, no little getKey command is needed to determine movement.  So, the next step is to simply erase the current positions of the objects since we know they are going to move anyway.  Just output a space for each coordinate, remembering the form (*x*,*y*).
```
:Output(A,B,"_")
:Output(C,D,"_")
```
Now, the coordinates have to be redefined to represent movement.  Since the movement is random, we will use [randInt](randint.html)(. (You will learn random commands later).  We can create a variant of the code used for normal movement, but since we don't need to test a getKey, we don't need ΔList( or anything.  However, min( and max( are still needed to test the boundaries.  So, here is the code.
```
:min(8,max(1,A+randInt(-1,1)))→A
:min(16,max(1,B+randInt(-1,1)))→B
:min(8,max(1,C+randInt(-1,1)))→C
:min(16,max(1,D+randInt(-1,1)))→D
```
The final part is the output.  Simply output each character with the new values.
```
:Output(A,B,"X")
:Output(C,D,"O")
:End
```
Putting the code together, we get the following:
```
PROGRAM:MOVE3
:1→A
:1→B
:8→C
:16→D
:Repeat getKey or (A=C and B=D)
:Output(A,B,"_")
:Output(C,D,"_")
:min(8,max(1,A+randInt(-1,1)))→A
:min(16,max(1,B+randInt(-1,1)))→B
:min(8,max(1,C+randInt(-1,1)))→C
:min(16,max(1,D+randInt(-1,1)))→D
:Output(A,B,"X")
:Output(C,D,"O")
:End
```
So, now you can create movement emulations for user interaction and create calculator generated motion along with simultaneous elements.

Unfortunately, when trying to move 5 or more objects, real variables become a hassle.  When you juggle a ton of objects, you must use a list to keep track of all the coordinates and to make a speedy program.  You won't need to know this now though, for as you progress with further lessons, you will gradually gain that knowledge.

## Collision detection

The next step is pertains to this question: How can I create walls where the object can't go through them?  With the previous codes, if you create a random boundary, the object can still go through it.  What if you want to make a maze?  Well, fortunately, there is a way.  To make boundaries, you have to add some sort of conditional testing for if there is a wall there or not.  The way you do that is creating an underlying code that describes the board on which an object is located.  There are many ways to do this.

Let's create a simple maze where you are guiding an X, and the walls are I's.  What we must first do is initialize the maze in one of the data types (which you will learn later).  The best way is to use a string; however the easiest way is by [matrices](matrix.html).  A matrix is a two dimensional array of information.  What we need to do is use three numbers: 1 will be a wall, 0 will be a space, and 2 will be the end of the maze.  Store the maze into a matrix variable by inputting the whole code.
```
:[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  [1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1]
  [1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1]
  [1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1]
  [1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1]
  [1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1]
  [1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1]
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]]→[A]
```
Notice that the dimensions of this code is 8 x 16, the exact dimensions of the home screen!  This code will be "under" the home screen so that the calculator can sense a collision when asked to.  Of course, you will still need some special code.

Next, you want to initialize the position of the object.  We want it near the top left corner, i.e. (2,2).
```
:2→A
:2→B
```
Okay, now we need to do a few different things.  You cannot jump into the movement phase just yet, because now the map needs to be shown.  To display the map, we need to use a couple of For( loops to represent each element.  The first represents the row while the second represents the column.  The code then needs to use the [sub(](sub.html) command to find which character, either I for a wall, a space for a 0, and a W for the winning space.  It tests what the matrix element is and outputs that accordingly.
```
:For(C,1,8)
:For(D,1,16)
:Output(C,D,sub("_IW",[A](C,D)+1,1))
:End
:End
```
Now we will start the main movement loop.  The first thing you need to do is define the loop with Repeat.  This time, the conditional needs to test when the player reaches the W, or the matrix number 2.  We can then define the loop like this.
```
:Repeat K=21 or [A](A,B)=2
```
The next natural step is to ask for input.  Use getKey as usual.
```
:getKey→K
```
Next, test to see if there was a key press.  If there was, clear the object for it to be redrawn later.
```
:If Ans
:Output(A,B,"_")
```
Now comes the movement code.  It is a little more complicated now that we have to test whether or not the player has collided with a wall.  Fortunately, since the surroundings are all walls, we won't need min( or max( to test the limits.  We only need the code to test the walls.  First, notice that the only way to reach the winning space is by going down.  This will help on the code.  Let's concentrate on vertical movement.  Here is the code:
```
:sum(ΔList(Ans={25,34}))
:A+Ans([A](A+Ans,B)≠1)→A
```
Here is what we are doing.  First, we need to find out whether we are going up or down.  So, we are using the normal code for that.  The next part tells us whether there is a wall in that direction or not.  Consider the condition `[A](A+Ans,B)≠1`.  This code is testing the square you want to move to.  If the square is a winning space or normal space, the condition gives off 1.  If the space is a wall, it says 0.  Since this is being multiplied by Ans, the direction, the object will not change position if the condition is 0.

So, similarly, we can use that code for the lateral movement.  The only difference is the conditional which is `not([A](A,B+Ans))`.  We use not because you cannot reach the winning square with a horizontal key press.  Thus, we do not need to test for 2 like before.
```
:sum(ΔList(K={24,26}))
:B+Ansnot([A](A,B+Ans))→B
```
Finally, we must output the result and close the loop.
```
:Output(A,Ans,"X")
:End
```
When we put all this code together, we get a functional maze program!
```
PROGRAM:MOVE4
:[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  [1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1]
  [1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1]
  [1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1]
  [1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1]
  [1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1]
  [1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1]
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]]→[A]
:2→A
:2→B
:For(C,1,8)
:For(D,1,16)
:Output(C,D,sub("_IW",[A](C,D)+1,1))
:End
:End
:Repeat K=21 or [A](A,B)=2
:getKey→K
:If Ans
:Output(A,B,"_")
:sum(ΔList(Ans={25,34}))
:A+Ans([A](A+Ans,B)≠1)→A
:sum(ΔList(K={24,26}))
:B+Ansnot([A](A,B+Ans))→B
:Output(A,Ans,"X")
:End
```
That sums up movement with collision.  Remember, depending on the situation of the map, you might have to alter the code.  That is the art of programming: it is not always consistent and needs constant intelligence from the programmer.

## An Alternate Method
There is another way to display movement.  It is faster, but it is also larger.  This method is capable of absorbing conditionals very well which makes it a much more lenient code.  Instead of using ΔList( and stuff, you can use a simple piecewise expression.
```
:A-(K=25 and A>1)+(K=34 and A<8)→A
:B-(K=24 and B>1)+(K=26 and B<16)→B
```
This code will also move something around the screen.

For collision detection, you could use
```
:A-(K=25 and [A](A-1,B)≠1)+(K=34 and not([A](A+1,B))→A
:B-(K=24 and not([A](A,B-1))+(K=26 and not([A](A,B+1))→B
```
See how easy it is just to add the extra condition?  This code's flexibility makes it very popular, but remember that it should only be used when needed because of its size!

## Full-screen on a TI-84+ CSE/CE

The TI-84+ CSE and CE models have a bigger screen size than previous models. Whereas the old dimensions were (for (Y,X)) (8,16), the new models are (10,26). The above programs are for the old dimensions, and while they will work on a 84+ CSE/CE, they don't display across the full screen. To change the programs MOVE and MOVE3, all you really have to do is change the Y and X maximums.

```
PROGRAM:MOVEC
:4→A
:8→B
:Repeat K=21
:getKey→K
:If Ans
:Output(A,B," ")
:min(10,max(1,A+sum(ΔList(Ans={25,34→A
:min(26,max(1,B+sum(ΔList(K={24,26→B
:Output(A,Ans,"X")
:End
```

```
PROGRAM:MOVE3C
:1→A
:1→B
:8→C
:16→D
:Repeat getKey or (A=C and B=D)
:Output(A,B,"_")
:Output(C,D,"_")
:min(10,max(1,A+randInt(-1,1)))→A
:min(26,max(1,B+randInt(-1,1)))→B
:min(10,max(1,C+randInt(-1,1)))→C
:min(26,max(1,D+randInt(-1,1)))→D
:Output(A,B,"X")
:Output(C,D,"O")
:End
```

Creating a full-screen maze is much more difficult, as it involves more than changing a few numbers. As opposed to making an 8x16 matrix, we have to make a 10x26 matrix, which obviously requires more work. Here is the code for a full-screen maze:

```
PROGRAM:MOVE4C
:[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
  [1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1]
  [1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1]
  [1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,0,1]
  [1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1]
  [1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1]
  [1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,0,0,1]
  [1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1]
  [1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1]
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]]→[A]
:2→A
:2→B
:For(C,1,10)
:For(D,1,26)
:Output(C,D,sub("_IW",[A](C,D)+1,1))
:End
:End
:Repeat K=21 or [A](A,B)=2
:getKey→K
:If Ans
:Output(A,B,"_")
:sum(ΔList(Ans={25,34}))
:A+Ans([A](A+Ans,B)≠1)→A
:sum(ΔList(K={24,26}))
:B+Ansnot([A](A,B+Ans))→B
:Output(A,Ans,"X")
:End
```


## Conclusion
Now that you know the core of movement, you now need to learn how to create the skeleton of all games: Loops.  As you progress through the lessons, you will find better ways to make maps, emulate movement, and create better games.  Have fun!

<center>

|**[<< Using getKey](sk:getkey.html)**|**[Table of Contents](starter-kit.html)**|**[The Game Loop >>](sk:game-loop.html)**|
| --- | --- | --- |

</center>
