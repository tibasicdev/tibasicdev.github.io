# Movement in Maps
Movement is commonly used in programs as a way to add user interaction. It is part of [user input](userinput.html) as it relies exclusively upon the [`getKey`](getkey.html) command to work. You can use movement in many programs and for many different things, including moving a cursor in a menu or moving a character around the screen. It is the latter case that we are going to explain and show here.



## The Code

### Homescreen

This is the basis for the code used in the two later examples.  An explanation for why it works can be seen [here](movement-explanation.html).

```
:4→A
:8→B
:Repeat K=21
:getKey→K
:If Ans
:Output(A,B," // 1 space
:min(8,max(1,A+sum(Δlist(Ans={25,34→A
:min(16,max(1,B+sum(Δlist(K={24,26→B
:Output(A,Ans,"X
:End
```

### Graphscreen

This is the same code as the first, but it has the [graphscreen](graphscreen.html) initialization process at the beginning, and you have to switch up the keypress codes.
```
:Zstandard
:104→Xmax
:72→Ymax
:Zinteger
:1→A
:1→B
:Repeat K=21
:getKey→K
:line(A,B,A,B,not(K
:min(94,max(0,A+sum(Δlist(K={24,26→A
:min(62,max(0,B+sum(Δlist(K={34,25→B
:End
```

Depending on what is being moved, the code might need to be revised.  This particular code will move a pixel, or you can make it a [line](line.html) if you want.  However, to move sprites, you will need to add to the coordinate variables instead.  If you are moving a group of pixels, it would be ideal to hard code it.
## Simultaneous Movement

Once you have learned how to create simple movement, the next natural step is to add some enhancement to make it more complex. One of the most common things desired is simultaneous movement — moving multiple things at the same time. Unfortunately, real simultaneous movement isn't really possible because of the limitations of the calculator, but you can emulate it.

When moving things, you need to be able to keep track of their position on the screen and the number of things. While the fastest way would be to use individual real [variables](variables.html) for each thing, the best approach in terms of speed and size is a [list](list.html) and real variable respectively.

Before you initialize the list, it is good to consider how many things you want to allow on the screen at any one time. This is an important consideration because the more things you need to keep track of, the slower the program runs. A good range to shoot for is 5-15.

Here is what the code looks like so far:

```
:DelVar ADelVar L110→dim(L1
```

We are using the A real variable as the counter and the L1 list variable to keep track of the 10 object positions on the screen. We chose to initialize the list elements to 0 because that is our flag to determine if the object is active or not.

Now when you want to add another object, you simply need to increment the counter and then store the object's position on the screen to the list. You also need to remember to check that you haven't exceed the maximum number of allowed objects on the screen. You can combine the X and Y screen coordinates together into one list element using [compression](compression.html).

```
:A+1→A
:If A<11
:YE2+X→L1(A
```

You also need to check for when a thing goes off the screen. When this happens, you first look at the counter to make sure it isn't at 0, and then loop through the thing positions and move all the things to the previous list element. You then decrement the counter.

```
:If A>1:Then
:For(X,1,A-1
:L1(X+1→L1(X
:End
:A-1→A
:End
```

When moving these things, you simply loop through the positions list and then change the position of whatever thing you want. You basically are moving one thing at a time and then switching to the next thing once it is done.

## Collision detection

If you want to restrict your character's movement so that it doesn't move through solid spaces such as walls, you will need some sort of collision detection. Since this example is on the [home screen](homescreen.html), the best method is to use a [string](string.html). Create a string with 128 elements, leaving spaces for nothing, which will be represented as zeros for visual aid.  Equal and unequal signs make good walls. Here is an example, a maze.  For more info maps, go to the page [making maps](maps.html)

```
:"================
  =000=000=000=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=000=000=000==
  ================→Str1
```

Notice how the "maze" is set up so that the outer boundaries are all walls. The advantage of this is that it allows us to save space and speed on the calculator by removing the specific boundary check.  The disadvantage is that it limits the amount of characters on screen to 6x14 instead of the full 8x16.

Now we can add the collision detection code in with our original movement code. You should notice that the main difference is the player's position for movement is checked to determine if the player is going to move onto an equals sign.

Notice how there is an extra argument after the [`Repeat`](repeat.html).  This allows us to have the character switch to the next maze when it reaches the end.  You could also use this to switch to another map at the screen's edge.

```
:ClrHome
:4→A:8→B
:"================
  =000=000=000=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=0=0=0=0=0=0==
  =0=000=000=000==
  ================→Str1   //remember, 0's are spaces
:Output(1,1,Ans
:Repeat K=21 and AB=26   //AB=26 can be changed for different exit point
:getKey→K
:If Ans
:Output(A,B,"_  //One space, checks for key press and erases
:sum(Δlist(Ans={25,34
:A+Ans(" "=sub(Str1,16(A-1+Ans)+B,1→A   //If future coordinate is a space, it moves
:sum(Δlist(K={24,26
:B+Ans(" "=sub(Str1,16A-16+B+Ans,1→B
:Output(A,Ans,"X
:End
:"     //second maze
```

And you can repeat this until all your mazes have run through.  In addition to using strings, you can also use lists, [matrices](matrices.html), or hardcode the whole map in if statements. The code is fundamentally the same, except there is a different formula used to display the map on the screen and you also check the available spot with that formula. Again, just try to understand the code and play around with it.

On the graph screen, you cannot make a string for collision detection.  Otherwise, you would be looking at a 5828 character string!  Instead, on the graph screen, you can use a command called [`pxl-Test(`](pxl-test.html) to tell you what is in the next space being moved to.

The pxl-Test( command finds the status of a pixel on the graph screen returning a 1 if the pixel is on or a 0 if the pixel is off.  Therefore, if you get a 1, the character shouldn't move to the next space.  If the pxl-Test( is 0, then the character moves to the next space.  The following code is the base of how this works, and you can alter it to add boundary checks or advanced sprite manipulation.

```
:sum(Δlist(K={25,34
:A+Ansnot(pxl-Test(A+Ans,B→A
```

## References

- Kerm Martian and his post at the UTI TI-Basic forum about keeping track of multiple shots.
- [darkstone knight's post](http://tibasicdev.github.io/forum/t-67037/new-faster-getkey) which led to the latest few updates in the formulas.
