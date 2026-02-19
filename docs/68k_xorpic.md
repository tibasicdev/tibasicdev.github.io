![The xorPic command](68k_xorpic/xorpic.png "The xorPic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Logically "xors" a picture variable and the graph screen at *[row][, column]*|AndPic *picVar*,*[row][, column]*|This command works on all calculators.|
       
### Menu Location

       
# The xorPic command

This command logically takes the picture variable specified, and takes the current graph, and it finds the points at which only the graph or only the picture have pixels, but turns off the points at which both have pixels, and it displays them only. If specified, *[row,column]* tells where the top left corner of the picture is to be placed. If not specified, the default is (0,0), which is the top left corner of the screen.


## Error Conditions




## Related Commands

- [68k:AndPic](68k:andpic.html)
- [68k:CyclePic](68k:cyclepic.html)
- [68k:NewPic](68k:newpic.html)
- [68k:RclPic](68k:rclpic.html)
- [68k:RplcPic](68k:rplcpic.html)
- [68k:StoPic](68k:stopic.html)

## See Also

- [68k:Sprites](68k:sprites.html)
