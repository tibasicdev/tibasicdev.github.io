![The RplcPic command](68k_rplcpic/rplcpic.png "The RplcPic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Replaces whatever is on the graphscreen with a picture variable  at *[row][, column]*|RplcPic *picVar*,*[row][, column]*|This command works on all calculators.|
       
### Menu Location

       
# The RplcPic command

This command replaces whatever is on the screen at a specific spot (*[row][,column]*). If no row or column is specified, the default is the upper left corner (0,0). If the picture is less than the full screen, only the spot at which the picture is placed will be removed. If you do not want anything replaced, use [68k:RclPic](68k:rclpic.html) instead...

## Error Conditions




## Related Commands

- [68k:CyclePic](68k:cyclepic.html)
- [68k:XorPic](68k:xorpic.html)
- [68k:NewPic](68k:newpic.html)
- [68k:RclPic](68k:rclpic.html)
- [68k:AndPic](68k:andpic.html)
- [68k:StoPic](68k:stopic.html)

## See Also

- [68k:Sprites](68k:sprites.html)
