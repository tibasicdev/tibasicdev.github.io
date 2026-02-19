# xLIB Tutorial
If you are considering using xLIB to produce amazing TI-Basic programs, I trust that you are an experienced programmer and already know the basics of TI-Basic programming.  If you don’t, then this tutorial will still teach you, but it may not be as easy to understand.

xLIB is a graphical all-around application to enhance TI-Basic programs with the power of assembly. Bundled in xLIB are many useful functions to allow you to use sprites, tilemaps, direct input, and many other features that you see in many assembly games from your TI-Basic programs. It is similar to Detached Solution’s [Omnicalc](http://www.detachedsolutions.com/omnicalc/), and if you have experience with Omnicalc, you should have no problem with xLIB.

When you install xLIB, it will install a parser hook that will detect real() requests. All xLIB functions begin with real(, and when the command is executed, the function will be intercepted and carried out by xLIB.

The real( function can be accessed by pressing [MATH] and scrolling to the CPX menu.

- [Collision Detection](#collision-detection)

## Clearing the Screen

This is one of the simplest commands in xLIB. Just enter real(0,1 in your program to quickly clear the screen. You will almost never have to use ClrDraw after this, and, in addition, it also clears the home screen, too!

```
:real(0,[updateLCD]
```

**updateLCD** — This can either be 0 (don’t update the screen; useful for when you want to draw something on the screen with multiple commands and want for your picture to appear all at once) or 1 (update screen). If you want, you can drop this argument and have only real(0, and xLIB will automatically update the screen, and you’ll save two bytes, but there is a small possibility you could get an unexpected result, so do so at your own risk.

```
:real(0,1
```

## Logic

A logic argument is often required in xLIB, here are the 4 possibilities:

- **0** represents Overwrite, which means the sprite will overwrite whatever is existing in that location on the screen.
- **1** represents AND logic. Please refer to the truth table first to try to understand it. Basically, for a pixel to be turned on in the final image, the background pixel must be black, and the sprite pixel must be back, making AND very useful for masking(more about that later)
- **2** represents OR logic. Please refer to the truth table to find out more. In OR logic, the turned on pixels of the sprite will overlap whatever is on the screen,it's sorta useful when nothing is on the screen, but if there is already a background, it'll overlap it,and then you can't see anything.
- **3** represents XOR logic. Please refer to the truth table to find out more. In XOR logic,if a pixel is already on in the background, and the sprite's pixel is on too, then it toggles it off.So basically,if pixels overlap,they get toggled on and off. This is an extremely useful feature as you can erase previous drawings of the same sprite on the screen by recalling the sprite again.

### Truth Table

| | | AND | OR | XOR | The 1s represent a Turned on Pixel |
| 1 | 1 | 1 | 1 | 0 | The 0s represent a turned off pixel |
| 1 | 0 | 0 | 1 | 1 | The 1st column represents the background |
| 0 | 1 | 0 | 1 | 1 | The 2nd Column represents the Sprite |
| 0 | 0 | 0 | 0 | 0 | |


## Sprites

We will first begin with one of the most useful tools xLIB has to offer: sprite commands. A sprite, in a few words, is an image that you can move around on the screen. If you have ever played a video game, the characters and elements such as people, weapon blasts, coins, bricks, etc. are sprites.

Before you can use the xLIB commands to draw sprites, you must create and store them.  Sprites are stored and read from normal TI-OS pictures.  xLIB can recall sprites from pictures 1-255, regardless if they're archived or not.

### The Sprite Command

Let us look at xLIB's sprite function.  It's used to place a single sprite on the screen.

```
:real(1,[X position],[Y position],[sprite width *],[sprite height],[sprite pic],[X offset *],[Y offset],[drawing logic],[horizontal flip],[update LCD]
```

Now, do not let the number of arguments of that command scare you into submission; it becomes very simple once you get the hang of it. Let's walk through it, shall we?

**real(1** — Indicates you want the sprite command of xLIB.

**X Position** -– The X-coordinate of where you want the sprite to be displayed on the screen. This can range from 0-95, so you generally want the X-coordinate to be displayed within that range, but xLIB supports clipped sprites, so in some cases you might want the x-coordinate to be larger or smaller than the screen's width.

**Y Position** — The Y-coordinate of where you want the sprite to be displayed on the screen. This can range from 0-63, but as with the X-coordinate, you may want this to be larger or smaller than the screen's height.

**Sprite Width** -– The width of your sprite, but this command might fool you at the beginning, because you must enter it in bytes.  One byte is equal to 8 pixels, so if you have a sprite that is 1x1 to 8x8 pixels, then the sprite width would be one (1*8==8); a 9x9 to 16x16 pixel sprite would be two (2*8==16), and a 17x17 to 24x24 sprite would be three (3*8==24), and so on.   Since you can't use pixel values, you may have some wasted space in the sprite picture, but sprites are generally kept widths as multiples of 8 for this reason. Sprite width can range from 0 to 12 bytes.

**Sprite Height** — Unlike the sprite width, this is the actual height in pixels of the sprite, so the height of an 8x8 sprite, for example, would be simply be 8. Don't get the values for sprite height and width confused, or you will get an unexpected result. Sprite height can range from 0 to 63 bytes.

**Sprite Pic** — This is the Pic# in which the sprite is located in. This ranges from 1 to 255. NOTE: xLIB considers 0 to be Pic 10, so entering zero here will actually read from Pic 10.

**X Offset** — This is the X offset where the sprite you want is located in the picture that the sprite is stored in. Like sprite width, this is the number of bytes from the left to where the sprite is located, so this might confuse you again in the beginning.

**Y Offset** — Is Y offset of the sprite you want, but is the number of pixels from the top to where the sprite is located.

To explain both X and Y offsets better in one paragraph, let's say you have an 8x8 pix sprite you want to use that is located 56 pixels from the left and 24 pixels from the top of the spritesheet picture. The X offset of that would be 7 bytes (because 7*8==56), and the Y offset would simply be 24 pixels.

**Drawing Logic** -– This arguments tells xLIB how it should draw the sprite on the screen. There are four possibilities: 0 == overwrite, 1 == and, 2 == Or, 3 == xor. More information can be found in the Logic section.

**Horizontal Flip** — This argument is either a 1 or 0. If it is 1, then xLIB will draw your sprite horizontally. This is a big time and space saver, as you only would have to draw a character, say, that looks to the left, and use this to flip it when you want the character to look the other direction.

**Update LCD** -– This argument is the same as it is for clear screen: 1 to update the screen; 0 to not update the screen. An Example:

```
PROGRAM:DispSprite         \\Displays a sprite at location (24,34) 
:real(1,24,34,1,8,10,0,0,3,0,1  \\from Pic0's top left sprite,uses xor logic,updates screen.
```

There are many ways to use the sprite command, even with [masked sprites](xlib:masked-sprites.html)!

### Tilemapping

One of the strongest features of xLIB is that it supports tilemapping through the request, real(2. First let me explain what tilemapping is. Let's say you have an RPG, and the main character enters a forest, the background of the forest, like all the trees and plants are all part of the tilemap. How do you do that though?

Well, you could store each individual background as a picture and then recall it as you come across it, but that takes up a lot of memory, and also, how would you do collision detection with the trees and plants? The solution programmers come up with is called a tilemap.

The tilemap is a matrix where each tile number corresponds with a particular sprite on a sprite sheet. Thus, you can do collision detection by checking what tile number it is in the tilemap. xLIB supports 8*8 tiles in a tilemap. Thus, a regular tilemap would have dimensions of 8*12. So if I have a tilemap like this

```
1,0,1,0,1,0,1,0,1,0,1,0
0,1,0,1,0,1,0,1,0,1,0,1
1,0,1,0,1,0,1,0,1,0,1,0
0,1,0,1,0,1,0,1,0,1,0,1
1,0,1,0,1,0,1,0,1,0,1,0
0,1,0,1,0,1,0,1,0,1,0,1
1,0,1,0,1,0,1,0,1,0,1,0
0,1,0,1,0,1,0,1,0,1,0,1
```

And I have a sprite sheet where tile number "0" corresponds with a blank space, and tile number "1" corresponds with a black square, then if I draw the tilemap to the screen, the screen would look like a checkerboard:

![checkerboard.png](checkerboard.png "")

Now, let's look at the xLIB function :)

```
:real(2,Matrix_Name,X_Offset,Y_Offset,MapWidth,MapHeight,ScreenStartX,ScreenEndX,ScreenStartY,ScreenEndY,mPIC_Num,Tile_Method,Tile_Size,Map_UpdateLCD
```

**Matrix name** is a number from 0-9. Xlib uses the TIOS matrices for its tilemap. 0 represents matrix [A], 1-[B],etc....9-[J]

**X_offset** is a number that pinpoints the x-coordinate in the matrix at which xLIB starts reading the tilemap. This is used for scrolling, so for now, you might just want to leave it 0.

**Y_offset** is a number that pinpoints the y-coordinate in the matrix at which xLIB starts reading the tilemap. This is used for scrolling, so for now, you might just want to leave it at 0.

**MapWidth** is a number that is the width of the map you want to display. Normally, you'd want to leave the MapWidth at 12, seeing that 12 is the width of the screen.There are a few exceptions, though.

**MapHeight** is a number that is the height of the map. Normally, you'd want to leave the MapHeight at 8, because 8 is the height of the screen in bytes. There are a few exceptions, though.

**ScreenStartX** is a number from 0-12 which pinpoints the column on the screen in which you want to start drawing the tilemap. This is used for a "windowed" tilemap. Note that when you're in 16*16 tilemap mode,the values are 0-6 (*16)

**ScreenEndX** is a number from 0-12 which pinpoints the column on the screen in which you want to end the tilemap. This is used for a "windowed" tilemap. Note that when you're in 16*16 tilemap mode,the values are 0-6 (*16)

**ScreenStartY** is a number from 0-8 which pinpoints the row in which you want to start drawing the tilemap on the screen. This is used for a "windowed" tilemap. Note that when you're in 16*16 tilemap mode,the values are 0-4 (*16)

**ScreenEndY** is a number from 0-8 which pinpoints the row in which you want to stop drawing the tilemap on the screen. This is used for a "windowed" tilemap. Note that when you're in 16*16 tilemap mode, the values are 0-4 (*16)

NOTE: The above 4 arguments are all in bytes.

**mPic_Num** is the PicNumber in which the tiles for the tilemap are located. Now in the Pic, the top left 8*8 sprite is tile0 (NOT tile1). Then the sprite at right of it (at 8,0) is tile1, the one right of that one (at 16,0) is tile2. Thus, in the picture, the first row of sprites are tiles 0-11, then the second row is tiles 12-23 and so on.

Now, an excellent feature of xLIB is that it can read picture data that is archived, and it supports multiple picture data! What does that mean? An ordinary picture has 12*8, 96 tiles. What if that isn't enough? Well, xlib can support unlimited tiles (actually 65536 tiles) so the picture after mPic_Num contains the next tiles 96-191.

**TileMethod** is basically the same as the "logic" argument of the sprite function. 0 = Overwrite, 1 = AND, 2 = OR, 3 = XOR

**TileSize** is an interesting argument. A "0" (or basically omit the argument) represents a tilesize of 8*8, the regular mode. If the number is "16" instead, it represents you want the normal tile size to be 16*16. This will change several of the other arguments in the tilemap function. What's the use of this? Well first of all, some games will have 16*16 tiles, so instead of forming 4 8*8 tiles in a matrix, you can have just one 16*16 tile. This allows for smaller matrix sizes and saves a lot of space.

**Map_UpdateLCD** is the same as all the other UpdateLCD's. "0" represents no, "1" represents yes, the current screen data will be updated.

```
PROGRAM:TileMap
:[[1,0,1,0,1,0,1,0,1,0,1,0]   //Store the tiledata to [A]
[0,1,0,1,0,1,0,1,0,1,0,1]
[1,0,1,0,1,0,1,0,1,0,1,0]
[0,1,0,1,0,1,0,1,0,1,0,1]
[1,0,1,0,1,0,1,0,1,0,1,0]
[0,1,0,1,0,1,0,1,0,1,0,1]
[1,0,1,0,1,0,1,0,1,0,1,0]
[0,1,0,1,0,1,0,1,0,1,0,1→[A]
:real(0,0
:real(2,0,0,0,12,8,0,12,0,8,1,0,8,1   //Draw the tiles to the screen, 12*8 tilemap
```

If you run this program and you have a black square as tile 0 in Pic1, then it will draw the following screen: 

![checkerboard.png](checkerboard.png "")

## Recalling Pics

Recalling pics can be a very useful ability for a number of functions.  The syntax is as follows:

```
:real(3,rPIC_Num,rPIC_Method,Recall_UpdateLCD
```

**rPIC_Num** is the picture you wish to recall.

**rPIC_Method** is the method you wish to use to recall, 0 for overwrite, 1 for AND (draws white for on pixels), 2 for OR (draws black for on pixels), or 3 for XOR (which inverts on pixels) like always.

**Recall_UpdateLCD** is the same as all the other UpdateLCD's. 0 represents no, 1 represents yes, the current screen data will be updated.

So, you may be wondering how this could be useful.  One very obvious use is grayscale splash screens.  If you have two pictures, lets say pic 0 and 1, you could switch between which is displayed within a loop, thus resulting in a gray effect where there is difference between the two pictures.

```
:Repeat A
:real(3,0,0,1
:getKey→A
:real(3,1,0,1
:End
```

![dithering.png](dithering.png "")

In Assembly programming, they have use of a buffer, basically another extra screen to work with. In normal TI-Basic, we don't have access to that, but we can essentially use pictures as buffers. One example of this is a background image to a game, you can save it in a separate picture, then recall it each time you want the background displayed.

Another code you can use uses the xor logic:
```
real(3,0,0,1
Repeat getkey
real(3,1,3,1
End
```

## Screen Scrolling

Screen scrolling is a very basic function, although it is very handy in some situations.

```
:real(4,Scrl_Direction,Scrl_Number,Scrl_UpdateLCD
```

Scrl_Direction = The direction in which the screen scrolls. 
Scrl_Number = The number of pixels the screen scrolls.
Scrl_UpdateLCD = Toggles a LCD update. 0 is no, 1 is yes.

The following numbers are what you put in place of Scrl_Direction, to tell the calculator which way you want your screen to move.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Up | Down | Left | Right | Up-Left | Up-Right | Down-Left | Down-Right |

```
:real(4,3,5,1
```

The code above will scroll the screen right 5 pixels, then toggle a LCD update.

## The Contrast

The contrast isn't all that hard to do inside TIOS, although if you want to set it to a certain level, or see what level you're on, this code is for you.

```
:real(5,Contrast_Function,ContrastVal
```

Contrast_Function = The action to take, shown below.

0 = Sets the contrast level.
1 = Get the contrast level.

ContrastVal = New contrast value. Can be a value from 0-39

If you're setting the contrast, then you need to input a number for ContrastVal. 

If you're just getting the contrast, then you don't need to. When you do get the contrast, the level is stored in Ans.

If you were to merely get the contrast level, you would input the following:

```
:real(5,1
```

Then, you would simply type in Ans, and then it will show you the level of contrast. Otherwise, if you were to type in:

```
:real(5,0,26
```

Then that would set your contrast to level 26. Simple, I know.

## xLIB Detection

If someone does not have xLIB installed, it may be difficult to alert them to this. To check for xLIB installation, the following code will work.

```
:1
:real(0
:If not(Ans:Then
:Disp "XLIB NOT ENABLED
:Stop
:End
```

In the case that xLIB is not installed, the message "XLIB NOT ENABLED" will be displayed and the program will quit. Otherwise, operation occurs normally.

## Collision Detection 

Collision detection is a necessity if you're going to make a graphic RPG, or any other game.

You can create collision detection many different ways. For instance; lists. If you wanted to use lists you would have to store all of the coordinates into a list, and then use if statements to check if the character is on that spot. Even though you can do collision detection with lists, I wouldn't reccomend it. The problem with using lists is that they aren't very memory efficient. That's why we are going to use the [fPart(](http://tibasicdev.github.io/fpart) command.

The fPart( command grabs the decimal part of a variable. Which means we can add decimals in the Tilemap where the character isn't supposed to stand. Here's an example of the decimals in the Tilemap.

```
[[1,0,1.01,0,1,0]
[0,1,0,1,0,1]
[1,0,1,0,1,0]
[0,1,0,1,0,1]       //Tilemap in matrix [A]
[1,0,1,0,1,0]
[0,1,0,1,0,1]
```

Here is the code example for detecting the decimal.
```
//character movement
If .01=fPart([A](X,Y:Then     //(X,Y are the location of the character) if the decimal of X,Y in the tilemap equals .01/a border then
//don't let the character move
End
```

Using the fPart( command you can also do detection for special spaces. For example a door. The decimal .01 can stand for a place you can't walk into, and .02 can stand for a door.

```
If .02=fPart([A](X,Y:Then     // If the decimal of X,Y in the tilemap equals .02/a door then
//enter the building or room
```

Using collision detection you can create much more than borders and doors. You can create many other spaces, such as coins, portals, water, etcetera.

## Memory Functions

Get RAM value

```
:real(4
```

Reset RAM (Crash)

```
:real(34
```
