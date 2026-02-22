# xLIB Readme
xLIB is now an APP that adds some functionality to TI-83+ BASIC programs. It installs a parser hook which will intercept any real( requests.

To install xLIB simply copy xLIB.8xk to your calculator using your favorite flavor of linking software.

To enable xLIB you must run it from the APPS menu and select "1". A message should appear informing you that xLIB has been enabled. Pressing "2" will disable xLIB and "3" will quit.

xLIB uses both SavesScreen and AppBackupScreen, if you have any other libs that use those saferam areas the results could be unpredictable.


## 0- ClearScreen

```
:real(0,Clr_UpDateLCD
```

Clr_UpdateLCD = Toggle LCD update: 0 = No, 1 = Yes

This function Clears the graph buffer and the LCD.

## 1- DrawSprite

```
:real(1,Spr_X,Spr_Y,Spr_Width,SprHeight,sPIC_Num,sPIC_X,sPIC_Y,Spr_Method,Spr_Flip,Spr_UpDateLCD
```

|Spr_X | Sprite X location|
|Spr_Y | Sprite Y location|
|Spr_Width | Sprite width in bytes (so a 16 pixel wide sprite would have a width of 2)|
|Spr_Height | Sprite height in pixels|
|sPIC_Num | The picture in which the sprite is located PIC0 - PIC9|
|sPIC_X | X offset to sprite in PIC, must be ALIGNED. Can be a value from 0-11|
|sPIC_Y | Y offset to sprite in PIC|
|Spr_Method | The copy method 0 = Overwrite, 1 = AND, 2 = OR, 3 = XOR|
|Spr_Flip = Flip Sprite 0 | No Flip, 1 = Horizontal Flip|
|Spr_UpdateLCD | Toggle LCD update 0 = No, 1 = Yes|

This function will draw clipped sprites of ANY size anywhere on the screen.

Don't forget that sprites always have a width which is a multiple of 8. However with this routine we want the byte width of the sprite. It is 8 pixels per byte! So a 8x8 sprite has a byte width of 1, a 16x16 sprite would have a byte width of 2. A 12x12 sprite would still occupy 2 byte so it also has a byte width of 2.

sPIC_X is only at ALIGNED positions, can be a value from 0-11
sPIC_Y can be from 0-63

Horizontal Sprite Flipping has now been implemented. This should save you some space.

This function will still be able to read PIC data even if it is archived!

## 2- DrawTileMap

```
:real(2,Matrice_Name,X_Offset,Y_Offset,MapWidth,MapHeight,ScreenStartX,ScreenEndX,ScreenStartY,ScreenEndY,mPIC_Num,Tile_Method,Tile_Size,Map_UpdateLCD
```

|Matrice_Name | Name of matrice containing map data 0 - 9. 0 = [A] - 9 = [J]|
|X_Offsett | X Map Offsett. Which part of the map you wish to start drawing at|
|Y_Offsett | Y Map Offsett. Which part of the map you wish to start drawing at|
|MapWidth | Width of TileMap|
|MapHeight |Height of TileMap|
|ScreenStartX | Which COLUMN you wish to START drawing. Can be a value from 0-12 for 8x8 or 0-6 for 16x16|
|ScreenEndX | Which COLUMN you wish to END drawing at. Can be a value from 0-12 for 8x8 or 0-6 for 16x16|
|ScreenStartY | Which ROW you wish to START drawing. Can be a value from 0-8 for 8x8 or 0-4 for 16x16|
|ScreenEndY | Which ROW you wish to END drawing at. Can be a value from 0-8 for 8x8 or 0-4 for 16x16|
|mPIC_Num | The PIC in which the tile data is located PIC0 - PIC255|
|Tile_Method | The copy method 0 = Overwrite, 1 = AND, 2 = OR, 3 = XOR|
|Tile_Size | Size of tiles, 8 = 8x8, 16 = 16x16|
|Map_UpdateLCD | Toggle LCD update 0 = No, 1 = Yes|

The ScreenStartX, ScreenEndX, ScreenStartY, ScreenEndY enable you to draw a 'windowed' map. This means that you can draw your map and leave space for a HUD or something similar. Drawing smaller maps will also be a little faster.

To draw an 8x8 tilesize map centered with a 1 tile blank border the inputs would be:

|ScreenStartX | 1|
|ScreenEndX | 11|
|ScreenStartY | 1|
|ScreenEndY | 7|

The TileMap routine now supports MULTIPLE PICS and 16-bit TILE INDEXES. This means that you can have a map with more than 256 different tiles. If a tile is >95 it will overlap to the next PIC (if it exists).

PICS must follow each other numerically!

So if your input PIC is PIC0 any tiles > 95 will be taken from PIC1 and any tiles > 191 will be taken from PIC2.

If the PIC doesn't exist then the tile will be drawn as a BLANK.

This function will still be able to read PIC data even if it is archived! But it may slow things down.

## 3- RecallPIC

```
:real(3,rPIC_Num,rPIC_Method,Recall_UpdateLCD
```

|rPIC_Num | PIC to recall PIC0 - PIC255|
|rPIC_Method | The copy method 0 = Overwrite, 1 = AND, 2 = OR, 3 = XOR|
|Recall_UpdateLCD |Toggle LCD update 0 = No, 1 = Yes|

This will recall a pic and display it with some options (OR, XOR etc)

This function will still be able to read PIC data even if it is archived!

## 4- ScrollScreen

```
:real(4,Scrl_Direction,Scrl_Number,Scrl_UpdateLCD
```

|Scrl_Direction | direction to scroll|
|Scrl_Number | number of pixels to scroll|
|Scrl_UpdateLCD | Toggle LCD update 0 = No, 1 = Yes|

++* Directions

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Up | Down | Left | Right | Up-Left | Up-Right | Down-Left | Down-Right |

## 5 - ChangeContrast

```
:real(5,Contrast_Function,ContrastVal
```

|Contrast_Function | Contrast returned in Ans (0-39). 0 = Set Contrast, 1 = Get Contrast|
|ContrastVal | New contrast value. Can be a value from 0-39|

## 6 - UpdateLCD

```
:real(6
```

This function will copy the graph buffer to the LCD

## 7 - RunIndicator

```
:real(7,runIndicVal
```

|runIndicVal | Toggle Run Indicator. 0 = Off, 1 = On|

## 8 - getKey

```
:real(8
```

Scans the keypad and returns a key code in the ANS variable.

Has support for multiple arrow keypresses.

**Key Codes**
![http://tibasicdev.github.io/local—files/key-codes/xlib-keys.png](http://tibasicdev.github.io/local—files/key-codes/xlib-keys.png "")

## 9 - CreatePIC

```
:real(9,cPIC_Funtion,cPIC_Num
```

|cPIC_Function| Function to perform. 0 = StorePIC, 1 = DeletePIC|
|cPIC_Num |Number of PIC file to store to. Ranges from 1-255|

**NOTE**: PIC0 is actually PIC10 according to the TIOS. To store to PIC0 use: 

```
:real(9,10
```

**IMPORTANT**: Because the pics use tokens in their name that the TIOS doesn't really have (for PICS) the names in your memory management will be all strange. For example:

|PIC0 
inString( 
P/Y 
Z-Test(|

This is perfectly normal, nothing is wrong with your calculator. The TIOS just doesn't have the names for PIC variables above the 10th.

To transfer these pics to your calculator, you must group them. Sending may fail if you attempt to send them individually.

## 10 - ExecuteArchivedProg

```
:"PRGMNAME:real(10,exAction,Prgm_Dest:prgmXTEMP0XX
```

|"PRGMNAME | Name of program to be stored in the Ans variable. Program can be archived or in RAM|
|exAction | Action to perform. 0 = copy, 1 = clean specific, 2 = clean all|
|Prgm_Dest |Destination XTEMP program. Ranges from 0-15|

This function will copy a program from the archive or RAM to one of 16 XTEMP programs. The name of the
program to copy must be stored in the Ans variable prior to running this function.

This function will work with TI-Basic and TIOS ASM (nostub) programs.

For example, to copy the TI-Basic program ADEMO to XTEMP000 you would do:

```
:"ADEMO
:real(10,0,0
```

To copy the TI-Basic program MAP1 to XTEMP011, and then RUN XTEMP011 you would do:

```
:"MAP1
:real(10,0,11
:prgmXTEMP011
```

To copy the TIOS ASM program SCROLL to XTEMP009, and then RUN XTEMP009 you would do:

```
:"SCROLL
:real(10,0,11
:Asm(prgmXTEMP011
```

To remove program XTEMP006 you would do:

```
:real(10,1,6
```

To remove all XTEMP0XX programs you would do:

```
:real(10,2,0
```

**NOTE**: If the XTEMP0XX program already exists (in RAM or archive), then this function will exit without copying. You must manually remove the target program before attempting to replace it. (This is to stop accidents with nested programs trying to replace themselves).

## 11 - GetCalcVersion

```
:real(11
```

Returns a code in the ANS variable which will tell you what calculator version you are running.

| 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 83+ | 83+SE | 84+ | 84+SE |

## 12 - DrawShape

```
:real(12,Shape_Type,x1,y1,x2,y2,DrawShape_UpdateLCD
```

|Shape_Type | Type of Shape you want to draw:|

| ||~ Number|
|0 | DrawSingleLineBlack|
|1 | DrawSingleLineWhite|
|2 | DrawSingleLineInvert|
|3 | DrawEmptyRectangleBlack|
|4 | DrawEmptyRectangleWhite|
|5 | DrawEmptyRectangleInvert|
|6 | DrawFilledRectangleBlack|
|7 | DrawFilledRectangleWhite|
|8 | DrawFilledRectangleInvert|
|9 | DrawRectOutlineBlackFillWhite|
|10 | DrawRectOutlineWhiteFillBlack|
| ||~ Position|
|x1 | First x coord (for rectangles this is TOP LEFT corner)|
|y1 | First y coord (for rectangles this is TOP LEFT corner)|
|x2 | Second x coord (for rectangles this is BOTTOM RIGHT corner)|
|y2 | Second y coord (for rectangles this is BOTTOM RIGHT corner)|

|DrawShape_UpdateLCD | Toggle LCD update 0 = No, 1 = Yes|

## 13 - TextMode

```
:real(13,Text_Mode
```

|Text_Mode | Change the text mode: 0 = Normal, 1 = Inverse, 2 = Lowercase on, 3 = Lowercase off|

When Lowercase is enabled, press ALPHA twice to enter lowercase mode in the TIOS.

**NOTE**: Some TIOS functions (like errors and some menus) automatically reset these text flags to Normal.

## 14 - CheckRAM

```
:real(14
```

Returns the amount of FREE RAM in ANS

**WARNING**: You MUST provide the correct inputs for each function. If you do not, you risk a crash or worse.

Do NOT try to run your TI-Basic from MirageOS! I use a saferam area that MirageOS uses, so it may cause instability.

## Credits & Thanks

Dan Weiss (DWedit): APP Devkit 2.0
Dan Englender (Dan_E): WikiTI
Sean McLaughlin (Sigma): Ideas for masked/clipped sprite routine without smc
Patai Gergely (CoBB): PindurTI, greatest 83+ emulator by far
Badja: Initial Clipped line routine
James Montelongo (Jim e) & YUKI: DI wrapper routine ideas
Texas Instruments (TI): SDK and System Routine Documentation
Kevin Ouellet (Kevin, xlibman): Testing & ideas
George Daole-Wellman (Dysfunction): Testing & ideas
Kalan Scallan (kalan_vod): Testing & ideas
Fred Sparks (CDI, [froody]): Testing & ideas
threefingeredguy: Testing & ideas
Shaun McFall (Merthsoft): Testing & ideas
Fred Shen (dragon_lance): Testing & ideas
Brian Benson (Necro): Testing & ideas
Everyone on MaxCoderz Forums
Everyone in #TCPA (EfNet)

If I forgot you, please email me and I will update this section.

## Disclaimer

This program is still in early stages and may contain bugs. Program is use at own risk, I can not be held responsible for loss of data and or hardware damage.

If you have any questions please email me at <tr1p1ea@yahoo.com.au>

I have no problem with anyone using this program as long as you credit me properly. Please don't try to modify and/or pass this program off as your own with out first gaining my consent.

tr1p1ea — 04/02/2006 (DD/MM/YYYY)
