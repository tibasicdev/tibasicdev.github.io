# Tunnel Racer
Tunnel Racer is a game of reaction in which you race through a twisting tunnel, trying to avoid crashing. By pressing the arrow keys, the player moves left and right. ESC exits the game.

This game showcases the following techniques and ideas:
- [Smooth scrolling](68k:sprites.html#toc8)
- [Optimization](68k:optimization.html) for speed (sometimes at the expense of size)
- [Compatibility](68k:cross-compatibility.html) with all 68k calculators.
- Effective [setup and cleanup](68k:setup-and-cleanup.html) stages.


 
## The Code

```
:tunnel()
:Prgm
:Local center,height,player,temp,wall,score,shift1,shift2,key,dir,i,modeset,graphset,graphopt
:StoGDB graphset
:setMode({"Graph","FUNCTION","Split Screen","FULL","Exact/Approx","AUTO","Base","DEC"})→modeset
:{}→graphopt
:setGraph("Grid","OFF")→graphopt[1]
:setGraph("Axes","OFF")→graphopt[2]
:setGraph("Labels","OFF")→graphopt[3]
:ClrDraw
:ClrGraph
:FnOff
:PlotsOff
:getConfg()[14]/2-1→center
:when(center=119,98,72)→height
:For i,center,18,-1
:  PxlVert center+i
:  PxlVert center-i
:EndFor
:NewPic [3,0;2,1;3,1;1,2;2,2;3,2;2,3;3,3;3,4],player
:NewPic [0,0;0,35],shift1
:NewPic [0,0;0,1;0,35;0,36],shift2
:center-17→wall
:0→score
:0→dir
:0→key
:0→d
:
:While not pxlTest(height,center) and key≠264
:  While not pxlTest(height,center) and key≠264 and d=0
:    score+1→score
:    Stopic temp
:    RplcPic temp,1
:    RclPic player,height,center-2
:    If rand(2)=1 Then
:      wall-1→wall
:      XorPic shift1,0,wall
:    Else
:      XorPic shift1,0,wall
:      wall+1→wall
:    EndIf
:    getKey()→key
:    when(key=340,1,when(key=337,-1,0))→d
:  EndWhile
:  While not pxlTest(height,center) and key≠264 and d>0
:    score+1→score
:    StoPic temp,0,1
:    RplcPic temp,1
:    RclPic player,height,center-2
:    If rand(2)=1 Then
:      wall-2→wall
:      XorPic shift2,0,wall
:    EndIf
:    getKey()→key
:    when(key=337,0,1)→d
:  EndWhile
:  While not pxlTest(height,center) and key≠264 and d<0
:    score+1→score
:    StoPic temp,0,7
:    RplcPic temp,1,8
:    RclPic player,height,center-2
:    If rand(2)=1 Then
:      XorPic shift2,0,wall
:      wall+2→wall
:    EndIf
:    getKey()→key
:    when(key=340,0,-1)→d
:  EndWhile
:EndWhile
:Text "Score: "&string(score)
:RclGDB graphset
:setMode(modeset)
:setGraph("Grid",graphopt[1])
:setGraph("Axes",graphopt[2])
:setGraph("Labels",graphopt[3])
:ClrDraw
:DispHome
:EndPrgm
```

## An Explanation

The general idea of the program is that we store all data about the tunnel directly on the screen. We test for collisions with the [pxlTest()](68k:pxltest.html) command, and use [StoPic](68k:stopic.html) and [RplcPic](68k:rplcpic.html) to scroll. There are, of course, other methods we could have used, such as keeping a list of the wall coordinates. This would have been effective if drawing to the screen was the time-consuming aspect of the program (since only two pixels on each row would need to be changed); however, updating a list turns out to be more time-consuming. Altogether, the method used in this program seems to be the fastest.

As a design choice, once a key is pressed, the player drifts in that direction until another key is pressed. This not only makes the game more interesting, but allows for an interesting optimization later on.

Now we'll go over the phases of the program in detail.

### Setup

This is the beginning of the program, starting from the first line (Local center, ... graphset) and ending with the 12th line (when...→height). Here, we prepare the settings that we will need for the program — this is a phase very specific to 68k TI-Basic programming (and would be very different or missing entirely in another language).

We will declare all the variables we use as [Local](68k:local.html), so they are deleted when the program finishes running. Next, we account for mode settings. [setMode()](68k:setmode.html) changes the general settings, while [setGraph()](68k:setgraph.html) changes the graph-specific settings. We need to save them, too: [StoGDB](68k:stogdb.html) saves the current graph as an image, while the output of [setGraph()](68k:setmode.html) saves the old settings in the variable graphopt. The next 4 instructions, [ClrDraw](68k:clrdraw.html) through [PlotsOff](68k:plotsoff.html), ensure that nothing on the screen interferes with what we draw to it. Finally, we use [getConfg()](68k:getconfg.html) to find out the screen dimensions, to calculate the two parameters we need: center (the center column of the screen) and height (the height at which to draw the player sprite).

### Initialization

This phase starts with the 13th line (For i,...,-1) and ends with the 23rd line (0→key). Here, we initialize all the variables, and prepare the screen for the main loop. This is different from the setup phase because it actually involves the logic of our program.

The [For](68k:for.html)..EndFor loop draws the initial sides of the tunnel. No matter the calculator model, the tunnel itself stays 35 pixels wide. Then, we initialize the three pictures — the player sprite, and two 'shift' sprites that we'll use later on. Since the sprites are small, it's better to use [NewPic](68k:newpic.html) to create them, than to keep them outside the program. Finally, we initialize four variables — wall, score, dir, and key. 

This is a good place to describe the meaning of all the variables we'll need in the main loop:
- *center* and *height*, as we've said, represent the coordinate of the center column, and the height at which to draw the player.
- *player*, *shift1*, and *shift2* are sprites.
- *temp* is a temporary sprite used to store the entire screen and then scroll it.
- *wall* stores the column coordinate of the left edge of the topmost part of the wall.
- *score* is the score (measured by the number of frames).
- *key* is the [key code](68k:key-codes.html) of the key pressed.
- *dir* represents the direction of motion: 0 for forward, 1 for right, and -1 for left.

### The Main Loop

The main loop of this game is the outermost While..EndWhile loop. The idea is that, as long as the game is still going, the program will be going through this loop over and over.

In optimizing for speed, this main loop has been split up into three sub-loops: one for drifting forward, one for drifting right, and one for drifting left. Whenever a key is pressed, the inner While loop ends, and the program goes to the While loop that matches the player's current direction. Since the game also needs to be exited whenever 1) a collision occurs or 2) the player presses the ESC key, these two conditions are also added to each loop.

You'll notice that the code in each inner loop is mostly similar. In fact, if we were optimizing for size, we could shrink the program significantly by combining these loops into one. However, the division into three loops has a purpose: the parts of the loop that are different would require a complicated conditional statement to combine, which would make going through each loop slower. As it is, the conditional checks only need to be done when the player presses a direction key.

Despite their differences, all three loops accomplish the same thing. First, the score is increased by 1 each time. Second, the screen is scrolled: it is stored to the temporary picture 'temp', and then the same picture is recalled a row lower. Of course, this has also shifted the player sprite one row lower, so we need to redraw it where it was before. Also, when we're drifting left or right, the temporary picture is recalled a column right or a column left of where it was, respectively.

(A fine point of the program: notice that when drifting left, instead of storing the picture from column 0 and recalling it at column 1, we store it from column 7 and recall it at column 8. This prevents a significant speed hit in this particular loop: recalling such a large picture to a column that's not a multiple of 8 (this is called displaying an *unaligned* sprite) is much slower)

Now, the only thing that remains to be done is to adjust the topmost row, shifting it left or right randomly. When drifting forward, this is simple. The shift1 picture is made up of only two pixels, which are 35 columns away. Using [XorPic](68k:xorpic.html) to display it will change these two pixels, resulting in a shift of 1 pixel (the direction depends on if we're changing the set pixels or the reset pixels near the boundary). We adjust the 'wall' variable accordingly.

When drifting left or right, the situation becomes slightly trickier. Say the player is drifting left. Then if we do nothing, the wall gets shifted a pixel right through the scrolling process. To shift the wall left, on the other hand, requires changing *two* pixels on either side. We accomplish this with the shift2 picture (which is just two copies of shift1). When drifting right, of course, the situation is reversed.

### Closing

The closing phase is what happens when the game is over. In this case, this means the player has crashed or pressed the ESC key; either way, this phase is simple. We merely display the score in a text box. It might have been more complicated if we'd included high score functionality.

### Cleanup

Only slightly trickier is the cleanup phase (going from RclGDB graphset to the final line). We don't have to worry about cleaning up variables, since they were declared as [Local](68k:local.html). We do have to take care of the settings: [RclGDB](68k:rclgdb.html) restores the graph settings we saved earlier, and [setMode()](68k:setmode.html) restores the rest. Finally, we should clear the screen. [ClrDraw](68k:clrdraw.html) does this, but does not refresh the screen, so if that's all we do, the player will be left on the graph screen and the image of the tunnel will still be there. To prevent this, we use [DispHome](68k:disphome.html) — this displays the home screen. 

## Final Optimizations

If this game were to be released, some changes would have to be made. Here, we've avoided any optimizations that would impact the readability of the program. Here they are, for completeness:
- Replace the arguments of [setMode()](68k:setmode.html) and [setGraph()](68k:setgraph.html) with their [numerical equivalents](68k:mode-settings.html) (which are smaller and foreign-language compatible).
- Replace all variables with one-letter variables (which are smaller and slightly faster to access)
- Rather than declaring them as Local, accomplish cleanup as follows:
 1. Create a new folder using [NewFold](68k:newfold.html).
 1. Use the one-letter variables as they are needed.
 1. Replace ClrDraw at the end with [NewProb](68k:newprob.html), this will delete all one-letter variables.
 1. End the program by deleting the new folder.

However, you might be surprised to find out that the indentations at the beginning of each line don't actually increase program size. The indentation count, for better or for worse, is stored with each new line, no matter if there is an indentation or not.
