# Sprites
"Sprite" is a common name for a small image displayed on the screen (usually, this image is moved around as well, or repeated several times, as in a tilemap). In TI-68k Basic, support for sprites is built-in: a picture file can be any size (up to the total size of the screen) and can be displayed at any location using commands such as [RclPic](68k:rclpic.html). Sprites are always rectangular; even if the image itself is a circle, the sprite data will contain blank pixels around the circle to make it a square.



## Sprite Logic

There are four basic methods of displaying a black-and-white sprite. The simplest one is to overwrite whatever was at that location before. Alternatively, you can apply [AND](68k:and.html), [OR](68k:or.html), or [XOR](68k:xor.html) logic to each pixel of the background and the sprite to produce the result. 

#### Overwrite
[RplcPic](68k:rplcpic.html) uses overwrite logic to display a sprite. This is often useful when you intend to cover the whole screen with sprites, for example. The drawback is that this can erase bits of other things drawn on the screen.

![rplc.png](rplc.png "")

#### XOR

[XorPic](68k:xorpic.html) uses XOR logic to display a sprite. This means that for every dark pixel of the sprite, the pixel is flipped on the screen. XOR logic is the simplest to use for sprites, since XORing the same sprite to the same location a second time will erase it and restore any pixels under it. However, if sprites are going to be overlapping often (as opposed to occasionally), XOR sprites might not look that great.

![xor.png](xor.png "")

#### OR

[RclPic](68k:rclpic.html) uses OR logic to display a sprite. With OR logic, pixels can be set, but never cleared. For many possibly-overlapping sprites onscreen, sprites drawn with OR look best. However, they're not as easy to erase (you might store the background before drawing the sprite, but this can lead to very complicated code).

![or.png](or.png "")

#### AND

[AndPic](68k:andpic.html) uses AND logic to display a sprite. With AND logic, pixels can be cleared, but never set, so it has limited use by itself. It can be used as an equivalent of OR logic when drawing in white-on-black instead of black-on-white. Also, AND logic is useful in masking sprites (see below).

![and.png](and.png "")

## Masking

Masking is an advanced technique that allows sprites to be transparent in some places and opaque in others. To do this, you use two sprites: the sprite itself, and an auxiliary sprite, called a 'mask', that has dark pixels wherever you want the result to be transparent, and light pixels otherwise. To display the masked sprite, you first AND the auxiliary sprite, then OR or XOR (either one works) the main sprite.

![mask.png](mask.png "")

Like any sprite technique except XOR, masked sprites destroy what was in the background beneath them, so if you ever want to erase the sprite, you have problems. One solution: if you only have one sprite moving around the screen while the background stays the same, you can store the background to a picture the size of the screen. Then, whenever the sprite needs to be erased, you RplcPic the background, erasing the sprite. Another solution: for multiple sprites, you can [StoPic](68k:stopic.html) the area under the sprite to a picture, then RplcPic just that part of the background when you want to erase the sprite. This allows these sprites to be erased independently, but is complicated to manage (the simplest way is to use [indirection](68k:indirection.html)).

## Tilemapping

Tile maps are a widely used technique for making maps in games such as RPGs. The idea is to use small (such as 8x8) sprites in a grid pattern to cover the entire screen. Each terrain type (e.g. grass, water, brick wall) has its own sprite associated with it. A similar idea can be converted to side-scrolling games such as Mario.

The easiest way to store a tile map is in a matrix of integers; to convert from these integers to sprites easily, name the corresponding sprites 'tile1', 'tile2', ... and so on, or something similar (then #("tile"&string(n)) will get you the n<sup>th</sup> sprite). The tile map can be displayed in two nested [For](68k:for.html)..EndFor loops:
```
:For row,1,height
:For col,1,width
:RplcPic #("tile"&string(map[row,col])),8*row-8,8*col-8
:EndFor
:EndFor
```
(this code assumes 8x8 sprites, a tilemap stored in the matrix 'map', and sprites stored in the pictures 'tile1', 'tile2', etc.)

A more efficient method uses [68k:char()](68k:char.html) instead of [68k:string()](68k:string.html) — see the char() command page for more information.

#### Scrolling

Rather than display each screen as it comes up, it will look better if the map can be scrolled. This is possible using a combination of [StoPic](68k:stopic.html) and [RplcPic](68k:rplcpic.html). Use StoPic to store all but one row or column of the screen to a temporary picture. Then RplcPic that same picture, but one row or column over. Finally, use a For loop to overwrite the remaining row or column with tiles. 

Here's an example which scrolls left (row0 and col0 are variables used to track where you are in the map):
```
:StoPic temp,0,0,8*height,8*(width-1)
:RplcPic temp,0,8
:col0-1→col0
:For row,0,height-1
:RplcPic #("tile"&string(map[row0+row,col0])),8*row,0
:EndFor
```

An even more advanced technique is smooth scrolling. Here, the same idea applies, except you shift the screen one *pixel* over at a time. Also, since you can't draw to negative coordinates of the screen, you might have to apply some trickery when scrolling left or up, or just not use the entirety of the screen.

## Optimizing XorPic

This technique is useful when using XorPic to display a moving sprite, especially when it can only move in a few directions. The basic idea is that the XOR operation on bits is associative: (screen XOR pic1) XOR pic2 = screen XOR (pic1 XOR pic2).

The typical code form using XorPic to display a moving sprite is below:
```
XorPic pic1,row,col © erase old location
row+1→row © update coordinates
XorPic pic1,row,col © draw at new location
```

To optimize this, create a new picture that is the combination of pic1 and pic1 shifted down 1 row, combined using XorPic. You can think of this picture as the pixels that need to be changed in order to move pic1 down 1 row. If this picture is stored in pic2, then the optimized code is as folows:
```
XorPic pic2,row,col © update sprite
row+1→row © update coordinates
```

The advantage of this technique is that displaying one sprite is twice as fast as displaying two. On the other hand, it requires having two pictures displayed. Also, the code can get complicated if more than one direction is possible.

## Storing Pictures

A large, graphics-intense TI-Basic game might end up using lots of picture variables for sprites. Although you could release these pictures with your program, this might get annoying since the user has to transfer all these pictures to the calculator. A better way is to use an installation program which creates these pictures. There are three methods:

#### A Reference Picture

This method involves only one picture file which contains all of the sprites next to each other. The installation program recalls this picture to the screen, then uses StoPic to store the sprites to separate variables. The advantage of this method is that it's small and fast; but it's not as aesthetically pleasing as it could be because the user has to see the reference picture during installation.

#### NewPic

This method uses [NewPic](68k:newpic.html) to store each sprite individually. This method avoids drawing to the screen, and is still fast. However, a drawback is that NewPic uses a matrix to store sprites, which has two elements for every dark pixel of the sprite. This makes even small sprites take up a lot of space in the installation program.

#### Encoded Newpic

To fix this, you might try to encode the sprites in a different way (an example is using a large integer —  a single integer can store up to 254 bytes of data, which is good for about 2032 pixels, more than enough for any sprite). Then, the installation program creates the matrix for NewPic on the fly. This fixes the only disadvantage of NewPic, the size. However, another disadvantage appears: creating the matrix is a slow process.

<center>

|**[<< Dialogs](68k:dialogs.html)**|**[Overview](68k:techniques-overview.html)**|**[Animation >>](68k:animation.html)**|
| --- | --- | --- |

</center>
