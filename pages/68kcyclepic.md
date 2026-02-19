![The CyclePic command](68k_cyclepic/cyclepic.png "The CyclePic command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Displays picture variables in a cycle for a given amount of time per picture.|CyclePic *picNameString*, *number of pictures* *[[,wait][,cycles][,direction]]*|This command works on all calculators.|
       
### Menu Location

# The CyclePic command

This command displays several picture variables in a cycle, with each picture getting an optional wait time, number of cycles, and the direction to display the pictures in. For instance, if you have saved 5 pictures: pic1, pic2, pic3, pic4, pic5, then you could do this to display them all: `CyclePic` "pic", 5, 3, 2, -1. This would display all 5 pictures for 3 seconds each, for 2 cycles, and backward, meaning it would display picture 5 first. Unfortunately, there is no way to use the command on pictures that are stored in a folder. For instance, if you had the previous case, but every picture is stored in a folder called PICTURES, there is no way to cycle them without moving them out of the folder.

```
:CyclePic "ham", 3, 1.5, 6, 1
```

The above code would display pictures "ham1", "ham2", and "ham3" in that order for 1.5 seconds each, and for 6 cycles.

## Advanced Uses

This command can be used to create a slideshow-style program, or it can be used to display a sprite so it looks like it is moving. Note that you cannot use this function if the pictures are not in the MAIN file folder.

## Error Conditions




## Related Commands

- [`68k:AndPic`](68k:andpic.html)
- [`68k:XorPic`](68k:xorpic.html)
- [`68k:NewPic`](68k:newpic.html)
- [`68k:RclPic`](68k:rclpic.html)
- [`68k:RplcPic`](68k:rplcpic.html)
- [`68k:StoPic`](68k:stopic.html)
