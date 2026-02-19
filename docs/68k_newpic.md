![The NewPic command](68k_newpic/newpic.png "The NewPic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Forms a new picture out of a n x 2 matrix.|NewPic *matrix, picVar[, maxRow][, maxColumn]*|This command works on all calculators.|
       
### Menu Location

       
# The NewPic command

This command forms a new picture from a matrix. The matrix must have only 2 columns, and should contain as many rows as there are "on" pixels (darkened pixels) in the image. If the picture variable specified already exists, this command will overwrite it. This command takes each row of the matrix, and forms pixel coordinates from the two numbers there. The optional arguments maxRow and maxColumn specify the boundaries of the picture, so this is a good way to form a small sprite from a matrix.

```
:newPic [1,1;2,2;3,3;4,4;5,5], picline
```

The above code would form a picture named "picline" which would have pixels at (1,1),(2,2),(3,3),(4,4), and (5,5), which would basically be a straight line.

## Error Conditions




## Related Commands

- [68k:CyclePic](68k:cyclepic.html)
- [68k:XorPic](68k:xorpic.html)
- [68k:AndPic](68k:andpic.html)
- [68k:RclPic](68k:rclpic.html)
- [68k:RplcPic](68k:rplcpic.html)
- [68k:StoPic](68k:stopic.html)

## See Also

- [68k:Sprites](68k:sprites.html)
