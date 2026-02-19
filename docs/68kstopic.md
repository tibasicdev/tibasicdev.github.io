![The StoPic command](68k_stopic/stopic.png "The StoPic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Stores a picture variable at *[PxlRow, PxlColumn]* with *[width, height]*|StoPic *picVar*,*[PxlRow, PxlColumn][,width, height]*|This command works on all calculators.|
       
### Menu Location

# The StoPic command

This command is used to store a picture that is on your calculator's graphscreen. This is useful for sprites in programs, where you can draw a sprite and save it to a picture that you can later redraw on a background. It is also useful for saving a copy of whatever you are drawing, so that it is not accidentally deleted if you graph something... The row and column arguments specify where on the graphscreen should be stored. Also the width and height arguments specify how tall or wide the stored area should be. The default for the row and column is (0,0), which is the top left corner of the graphscreen. The default width and height is the whole screen.

```
:StoPic 2a, 2,7,10,10
```

The above code would take a 10 x 10 square of the graphscreen with the top corner being at (2,7), ans it would store whatever is there to the picture variable "2a".

## Error Conditions



## Related Commands

- [68k:AndPic](68k:andpic.html)
- [68k:CyclePic](68k:cyclepic.html)
- [68k:NewPic](68k:newpic.html)
- [68k:XorPic](68k:xorpic.html)
- [68k:RplcPic](68k:rplcpic.html)
- [68k:RclPic](68k:rclpic.html)

## See Also

- [68k:Sprites](68k:sprites.html)
