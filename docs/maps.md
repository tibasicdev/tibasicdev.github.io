# Making Maps
For many games, the gameplay consists of going through all of the maps in the game. For example, in a maze game where each map is a different maze, when you get through the first maze you go on to the second maze, and so on until you finish all of the mazes. Another common example is an RPG where the player can move their character around on the screen, and each screen is part of a larger map.



## How to Store Maps

In order to keep track of all of the different things in a map, it obviously requires that you store the map to a variable. There are three different variables that you can use to store maps, and they each have their own advantages and disadvantages:

- **[Matrices](matrices.html)** — Matrices are best used for two-dimensional data, and are easier to access and manage than both lists and strings. At the same time, matrices are the largest variable, which can be important if you are trying to keep your program as small as possible.
- **[Lists](lists.html)** — Lists are best used for one-dimensional data, and are faster to access than both matrices and strings. Lists also have the additional advantage that you can create your own custom lists, which decreases the likelihood that they will get messed with.
- **[Strings](strings.html)** — Strings can be adapted for basically any context, and they are smaller in size than both matrices and lists. In addition, unlike matrices and lists which have a set maximum size (99x99 and 999 respectively), strings can be as big as RAM will allow.

Generally speaking, it's best to use the most appropriate variable for the application. Going back to the maze game, for example, a matrix would probably be the preferred variable to use because a maze has a two-dimensional shape to it.

When storing a map in a variable, you have to assign numbers to represent the different things in the map: an empty space might be zero (0), a wall might be one (1), and the player might be two (2). You would then check for these numbers when determining what to do on the map or what to allow (such as [movement](movement.html) by the player).

Here is an example of a simple 8x16 map stored in each of three different variables (note: the respective variable is all on one line, it's just split up to make it easier to read):

[[table]]
[[row]]
[[cell]]
```
:[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
 [1,2,1,0,0,0,1,0,0,0,1,0,0,0,1,1]
 [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]
 [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]
 [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]
 [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1]
 [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1→[A]
```
[[/cell]]
[[cell]]
```
:{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
 ,1,2,1,0,0,0,1,0,0,0,1,0,0,0,1,1,
 ,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,
 ,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,
 ,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,
 ,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,
 ,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,
 ,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1→L₁
```
[[/cell]]
[[cell]]
```
:"1111111111111111
 1210001000100011
 1010101010101011
 1010101010101011
 1010101010101011
 1010101010101011
 1000100010001000
 1111111111111111→Str1
```
[[/cell]]
[[/row]]
[[/table]]

As you can see, the string map is the smallest of the three variables because you don't have to add all of the additional characters (the braces and the commas) like you do with the matrix and list. (You can actually get around this problem by storing your maps as a string, and then [converting](string-to-list.html) them to a matrix or list when you need to use them.)

## How to Display Maps

Once you have your map stored in one of the variables, the next thing to do is to display it on the screen. The calculator has two different screens for displaying things — the [home screen](homescreen.html) and the [graph screen](graphscreen.html). The home screen is generally reserved for text, while the graph screen is generally reserved for [graphics](graphics.html).

### On the Home Screen

When displaying a map on the home screen, you use the [Output(](output.html) command together with a [For(](for.html) loop. You also need to decide what you want to display for the different things in the map. The easiest option is to just display the literal values stored in the map (i.e., 0, 1, 2, 3, etc.). A better option, although it's a little more complex, is to display a character that is representative of what the value stands for.

For example, in our maze map, we had spaces (0), walls (1), and the player (2). The spaces are what the player is going to be able to move on, so they naturally should not be displayed on the screen. A wall, on the other hand, is something that the player cannot move through, so it should be displayed on the screen. A good choice for a wall character is a 1 or an uppercase X. The player is what the user is in control of, so you want it to stand out. A good choice for a player character is an S or uppercase O.

Besides deciding what character you will use for each type of thing in a map, you also need to have a check for each one when displaying the characters. The most straightforward way to do this would be to have a separate [If](if.html) conditional that goes with each type of character. A better way to do this, however, is to put all of the characters in a string, and use the [sub(](sub.html) command to access the appropriate character. For example, here is how you would display the maze from before:

```
:For(Y,1,8
:For(X,1,16
:Output(Y,X,sub(" XO",1+[A](Y,X),1
:End:End
```

As you can see, we decided to use an X for the walls and an O for the player. The other important thing to notice is that we used two nested [For(](for.html) loops to display the map. Since the maze is two-dimensional, two For( loops are needed: the first loop gets the Y-coordinates and the second loop gets the X-coordinates. Inside the second For( loop is where we access the respective (Y,X) coordinate of the matrix and display it using Output(.

Displaying a maze level stored in a list or string is very similar, but it requires you to use a simple formula to convert the respective coordinates on the screen: X+16(Y-1). For the string, you also need to use the [sub(](sub.html) command to access the individual character in the string, and the [expr(](expr.html) command to convert it to a number.

```
:Output(Y,X,sub(" XO",1+L₁(X+16(Y-1)),1
:Output(Y,X,sub(" XO",1+expr(sub(Str1,X+16(Y-1),1)),1
```

Where this formula comes from is that each row on the home screen is 16 characters wide, and the first row you just access the X coordinate by itself (i.e., when Y is 1, Y-1=0, and subsequently 16*0=0). If you create a similar map on the graph screen, you need to modify this formula to match the number of characters per row on the graph screen and to take into account that the graph screen coordinates start at zero.

Besides using the formula, the string can also be displayed one other way. The [Output(](output.html) command will wrap any text that goes over the 16 characters of a row to the next row (and likewise with that row), and subsequently you can use a single command to display the entire map across the whole screen.

Since every space is overwritten with the map, this does not require a [ClrHome](clrhome.html) command to clear previously displayed characters. Unfortunately, there is no equivalent for the graph screen.

### On the Graph Screen

Displaying a map on the graph screen is essentially the same as displaying a map on the home screen, except you can make the map much more detailed because the graph screen can be manipulated on a pixel level. There are several graphics commands available:

- [Pxl-On(](pxl-on.html), [Pxl-Off(](pxl-off.html), [Pxl-Change(](pxl-change.html), [pxl-Test(](pxl-test.html)
- [Pt-On(](pt-on.html), [Pt-Off(](pt-off.html), [Pt-Change(](pt-change.html)
- [Line(](line.html), [Horizontal](horizontal.html), [Vertical](vertical.html)
- [Circle(](circle.html), [Shade(](shade.html), [Text(](text.html)

When displaying a particular part of the map, you can use a combination of these commands to create almost anything you want, whether it is a wall, a monster, a rock, or even a smiley face. For example, using our 8x16 maze level from before, instead of outputting the X character for the wall in the matrix, we can draw a wall using lines:

```
:For(Y,1,8
:For(X,1,16
:If 1=[A](Y,X:Then
:Line(4X-2,57-6Y,4X-2,53-6Y
:Line(4X-3,57-6Y,4X-3,53-6Y
:End:End:End
```

You should note that the window dimensions need to be X=0...94 and Y=0...62 for this example to show up correctly. In fact, with exception to the Pxl- and Text( commands, all of the graphics commands are dependent upon the window dimensions, so you should always use a [friendly graphing window](friendly-window.html) to ensure everything shows up as you intended.

There are several other ways to create graphics, and you should check out the [graphics](graphics.html) page for more information.

## Where to Store Maps

After deciding on how you will store and display your maps, you then need to determine where you will store the maps: in the program itself or in a [subprogram](subprograms.html) (or subprograms). When deciding which route to go, you need to think about how many maps you plan on having. If there aren't many maps (i.e., ten or less), they should usually all be stored in the program itself.

### In the Program

For storing the maps in a program, you place each map inside its own [If](if.html) conditional and list the maps one after another. You then check to see which map the player needs and set up the variables for that map. Each map might also have some related information that goes along with it, such as the number of coins the player has to collect or the number of lives, so you would need to use an If-Then conditional instead:

```
:If A=1:Then  // Check if the player is at map 1
:{1,2,0,0,0,1,5,5,7,3,4,2,9,8,7,1→L₁
:3→B:4→C
:End
```

Once you have your maps stored in their individual conditionals, the next thing to do is decide where you you want to store them in the program. An obvious choice is just placing them right at the beginning of the program. In order to do this, however, it requires that you be able to access them. This normally entails placing a label before the maps, and then using a [Goto](goto.html) to jump to them.

An important consideration when placing maps at the beginning of a program is what values you use for the If conditional variable. While you could use something simple like one or two, those values have a high probability of being accidentally entered in by the user or being set by another unrelated program, which would cause your program to store the respective map. What works better is to use random decimals (like .193 or 1.857) or math symbols (like e or π).

### In a Subprogram

If there are several maps, you might want to consider placing them in a separate subprogram. The main reason is that when the maps are stored in the program, the program has to go through all of the code before the maps to reach a particular map. Depending on the size of the program, this can make for some major slowdowns in between maps. The internal maps also slow down the main program code itself.

Related to the first reason, the second reason to consider using a separate subprogram is that changing the maps is much easier in a subprogram. Instead of having to go through the entire program, looking for the map to change, you can just focus on one map at a time. This makes the maps more manageable, and also prevents you from accidentally changing other parts of the program.

The program code for the maps basically remains the same, it's just in another program. You might notice, though, that if you have lots of maps it takes a while for program execution to go back to the main program. This happens because program execution doesn't return to the main program until after it reaches the end of the program. You can fix this problem by placing the [Return](return.html) command at the end of each map conditional:

```
:If C=3:Then
:[[0,1,0][2,1,2][1,2,0→[B]
:3→A:3→B
:Return  // Stop program execution and return to main program
:End
```

Now that the maps are in a separate subprogram, you need a way to access them. When you want to access a map, you set the respective variable to the value of the map that you want, and then call the subprogram from the main program using the [prgm](prgm.html) command and the subprogram name:

```
:2→A
:prgmGAMELVLS
```

Unfortunately, storing the maps in a subprogram does have one major disadvantage. The user now needs another program to use the main program. If somebody tries to run the program and they don't have the maps subprogram, the main program will not work properly, and will actually return an [ERR:UNDEFINED](errors.html#undefine) error when the program tries to call the non-existent maps subprogram. Even if this isn't your fault, the result is that your program looks very sub par.

Because of this problem, doing an all or nothing map separation (i.e., all of the maps are either stored in the program or in a separate subprogram) is usually a bad idea. The better alternative is to split up the maps so that the first ten maps (or so) are stored in the program, and the rest are stored in the subprogram. The user will now at least have some built-in maps to play, regardless of if they have the maps subprogram. The user simply won't have knowledge of the other maps available for them to play.

## Sample Map-Based Game

This is a sample map-based game and the objective in each level is to get the "+" (plus sign), which causes you to advance to the next level. The game is played on the home screen using the arrow keys to move and CLEAR to quit. The maps are stored as lists in a separate program, along with the starting coordinates for your character.

(NOTE: Each list is all on one line, it's just split up to make it easier to read.)

```
PRGM:MAZELVLS
:If not(A:Then
:{1,2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,
1,2,1,2,2,1,2,2,1,2,2,2,2,2,2,1,
1,2,1,2,2,1,2,2,1,2,1,1,1,1,1,1,
1,2,1,2,2,1,1,1,1,2,1,2,2,2,2,2,
1,2,1,2,2,2,2,2,2,1,1,2,2,1,1,1,
1,2,1,1,1,1,1,1,2,1,2,2,2,1,2,1,
1,2,2,2,2,2,2,1,2,1,2,2,2,1,2,1,
1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,3→L1
:1→Y:1→X
:Return
:End
:If A=1:Then
:{1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1,
1,2,1,2,1,1,1,1,1,1,1,1,1,1,2,1,
1,2,1,2,3,2,2,2,2,2,2,2,2,1,2,1,
1,2,1,2,2,2,2,2,2,2,2,2,2,1,2,1,
1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1→L1
:8→Y:16→X
:Return
:End
:If A=2:Then
:{1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,3,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,2→L1
:1→Y:1→X
:End
```

```
PRGM:MAZE
:For(A,0,2
:prgmMAZELVLS
:" // 1 space
:For(I,1,dim(L1
:Ans+sub(" =+",L1(I),1
:End
:ClrHome
:Output(1,1,sub(Ans,2,dim(L1
:Repeat 3=L1(Ans+16Y-16
:Output(Y,X,"X
:Repeat Ans
:getKey→K
:End
:If Ans=45:Goto Q
:Output(Y,X," // 1 space
:min(16,max(1,X+sum(ΔList(Ans={24,26→C
:min(8,max(1,Y+sum(ΔList(K={25,34
:If 2≠L1(C+16Ans-16:Then
:Ans→Y:C→X
:End:End:End
:Lbl Q
:DelVar L1
:ClrHome
:"Lost
:If A=3
:"Winner
```
