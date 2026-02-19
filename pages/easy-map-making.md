# Easy Map Making
This article is currently in development. You can help TI-Basic Developer by expanding it. This article seems to lack info.  Needs attending.

Map making is a key part of making many types of games.

Most maps are created using pre-drawn images on the graph screen, while a select few make use of the home screen. The graph screen is more versatile with its larger size and compatibility. `pxl-test(` is often used to keep a character on or within the boundaries of a map.

### pxl-Test(

[`pxl-Test(`](pxl-test.html) is what the whole programs runs off of. The command returns either 1 or 0, indicating whether a pixel is activated or not. Using this, you can use a movement loop where the character will not move onto a designated area. For example:
```
:pxl-Test(5,2
```
This would check to see if there is a pixel at 5,2; if so then a 1 will be returned, if not, a 0 is returned.
### Code

Type in this code into your calculator: 

```
ClrDraw
RecallPic 1
55→X
60→Y
Repeat A=45
Pxl-On(Y,X
Repeat Ans
getKey→A
End
Pxl-Off(Y,X
X-(Ans=24 and not(pxlTest(Y,X-1)))+(Ans=26 and not(pxl-Test(Y,X+1→X
Y-(A=25 and not(pxlTest(Y-1,X)))+(A=34 and not(pxl-Test(Y+1,X→Y
End
```

### Instructions

Make any random map that pleases you and press [2ND] + [DRAW] + [LEFT] + [ENTER] + [1] + [ENTER] (StorePic 1). This will override [`Pic1`](pictures.html) with whatever map you created. The movement loop will need to be customized for your map though. A simple maze game is easier to make then a platformer that requires jumping, shooting, moving, etc.

### Things to make sure of

1)     Make sure that the pixel at (55,2) is not activated (black)
2)     Remember that `Pxl-On(` follows the syntax of Output where it is `Pxl-On(Row, Column)`.
