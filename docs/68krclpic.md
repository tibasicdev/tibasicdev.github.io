![The RclPic command](68k_rclpic/rclpic.png "The RclPic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Recalls a picture variable and the graph screen at *[row][, column]*|RclPic *picVar*,*[row][, column]*|This command works on all calculators.|
       
### Menu Location

# The RclPic command

This command is used to recall (open) a picture you have saved on your calculator. This is normally used in programs, because you can open pictures from the graph when you are not running a program. It is very useful for sprites as well, as it can recall a picture variable on top of a background, without deleting any of the background. In a program, however, you can recall a different picture for a different input, as shown below:

```
:If a=16
:RclPic 2
:Else
:RclPic 3
```

## Error Conditions




## Related Commands

- [68k:AndPic](68k:andpic.html)
- [68k:CyclePic](68k:cyclepic.html)
- [68k:NewPic](68k:newpic.html)
- [68k:XorPic](68k:xorpic.html)
- [68k:RplcPic](68k:rplcpic.html)
- [68k:StoPic](68k:stopic.html)

## See Also

- [68k:Sprites](68k:sprites.html)
