# Graphics
There is only so much that can be shown with text alone: sooner or later, any kind of program, whether it is a game or a complicated math tool, will have to use graphics. The purpose of this page is to describe the various methods of rendering graphics, along with their advantages and disadvantages. In many cases, you'll find that no one method suits your needs perfectly, and they will need to be combined to produce something that looks good without sacrificing too much speed or memory space.


## Picture Variables

The simplest and fastest way to display just about any image is to save it in a [picture variable](pictures.html) beforehand, and then use the [RecallPic](recallpic.html) command to instantly display it to the screen. There is no choice in positioning the picture, or displaying anything smaller than the entire screen, so this method is mostly limited to title screens. 

The main advantages of this method are:
- The speed — no other TI-Basic instruction can fill the screen as quickly.
- The image can be made as complex as desired, without loss of performance.

However, there are numerous drawbacks:
- Each picture variable uses 767 bytes of precious memory.
- Furthermore, the picture is stored *outside* the program, where it can be overwritten.
- There are only 10 picture variables to be shared between *all* TI-Basic programs.
- The picture is static and can't be moved around the screen easily.

There are several ways to get around this problem. A decent solution is to use [groups](grouping.html) to keep the program and its pictures together and backed up — this ensures that even if a picture is overwritten, that this will not be permanent. Another possibility is to hope that there won't be any other conflicting programs to cause problems.

An example of picture variables at their best is the title screen in [Contra](contra.html): the image is too complicated to reproduce easily in any other way, and the result has become iconic of the game. 

## Hard-coded Sprites

Hard-coded sprites are, in a sense, the other extreme to go to. The idea is to write out the specific commands (usually, ones like [Pt-On(](pt-on.html) or [Pxl-On(](pxl-on.html) to display an image. A [friendly window](friendly-window.html) might be useful. Here is an example, drawing a smiley face near the coordinate (X,Y):

```
:Pt-On(X,Y,2)
:Pt-On(X+2,Y,2)
:Pt-On(X,Y-2,2)
:Pt-On(X+2,Y-2,2)
:Pt-Off(X+1,Y-2)
```

Unless the image only needs to be drawn at one point, adding variables such as X and Y above is useful, allowing the same code to draw the same thing at multiple locations. It should also be noted that the Pt-On( and Pt-Off( commands have an optional third argument that allows you to draw a 3x3 box or cross (using 2 or 3, respectively), which is smaller and faster than the individual composite commands.

The advantages of this approach are:
- It is very flexible: no matter the image, it can be drawn with some amount of commands.
- It is still fairly fast, although slower than [RecallPic](recallpic.html).
- It's easy to make a sprite that moves around on the screen.

The drawbacks, on the other hand, are:
- Of all the methods on this page, this one uses **the** most memory.
- The more complex the image, the more commands it will require to draw.
- Every different image requires its own instructions, complicating program logic.
- It's easy to make a mistake or typo, and hard to fix one.

A good use for hard-coded sprites is a fancy cursor in a menu: these are usually small and relatively simple, don't require many different images, and play to the strengths of hard-coded sprites. You can also combine hard-coded sprites with [compression](compression.html) to reduce the number of graphic commands needed, although it often causes a hit to the program speed.

## Plot Sprites

A somewhat different idea for rendering graphics, plot sprites use the [Plot](plotn.html)#( commands to draw multiple points or multiple lines very quickly (taking a shortcut, so to speak, to the approach above). In this case, all of the information to draw the sprite (that is, the coordinates of the points or lines) is stored in a pair of lists. Since plots use point coordinates, a [friendly window](friendly-window.html) may be useful.

To display a sprite, first store the coordinates to two lists (this article will assume they are L<sub>1</sub> and L<sub>2</sub>). Next, set up the plot variable with Plot#(Scatter,L<sub>1</sub>,L<sub>2</sub>) (to draw points at the coordinates) or Plot#(xyLine,L<sub>1</sub>,L<sub>2</sub>) (to connect the coordinates with lines). Then, the [DispGraph](dispgraph.html) command will update the graph screen with all the plots that are currently in use. There are three plots available, which can be switched on and off with the [PlotsOn](plotson.html) and [PlotsOff](plotsoff.html) commands. 

Here is an example of the same image displayed using plot sprites:
```
:{4,0,0,4,4,4,0,2,2}→L1
:{0,0,4,4,0,2,2,2,4}→L2
:Plot1(xyLine,L1,L2
:DispGraph
```

Plot sprites are uniquely suited to being moved around the screen: once the setup phase is done, just modify the lists slightly and then use DispGraph again to draw the sprite at a different location, erasing it from where it was. Just using simple arithmetic on the lists lets you move, reflect, rotate, and stretch a sprite. The table below shows the formulas required (some intuitive, some not):

| Transformation | Formula |
| --- | --- |
| Horizontal translation | A+L<sub>1</sub>→L<sub>1</sub> |
| Vertical translation | B+L<sub>2</sub>→L<sub>2</sub> |
| Reflection about the x-axis | -L<sub>1</sub>→L<sub>1</sub> |
| Reflection about the y-axis | -L<sub>2</sub>→L<sub>2</sub> |
| Rotation 90° 
clockwise |  L<sub>1</sub>→L<sub>3</sub> 
 -L<sub>2</sub>→L<sub>1</sub> 
 L<sub>3</sub>→L<sub>2</sub> |
| Rotation 90° 
 counterclockwise | -L<sub>1</sub>→L<sub>3</sub> 
 L<sub>2</sub>→L<sub>1</sub> 
 L<sub>3</sub>→L<sub>2</sub> |
| Rotation by an angle of θ | L<sub>1</sub>cos(θ)-L<sub>2</sub>sin(θ)→L<sub>3</sub> 
L<sub>1</sub>sin(θ)+L<sub>2</sub>cos(θ)→ L<sub>2</sub> 
L<sub>3</sub>→L<sub>1</sub> |
| Horizontal stretch | AL<sub>1</sub>→L<sub>1</sub> |
| Vertical stretch | BL<sub>2</sub>→L<sub>2</sub> |

The advantages of using plot sprites are:
- The image data is stored in variables (lists), so the same code can display any sprite.
- Plot sprites are usually smaller than hard-coded sprites, at a comparable speed.
- As named lists, images can be saved outside a program without fear of being overwritten.
- The sprites are uniquely easy to move (arbitrary rotation, for instance, is only possible with plot sprites)

The drawbacks are:
- Since there are only three plots, only three independent sprites can be displayed at a time.
- Plot sprites don't work well with other graphics: [DispGraph](dispgraph.html) erases most things drawn on the graph screen.
- DispGraph erases before drawing, producing noticeable flicker.
- On the color calculators, plot sprites can only display one color.

There are two main avenues for plot sprites. The first is for displaying an image that won't have to be moved around (such as a title screen): this avoids the two problems that DispGraph causes. The other is for displaying a few images in complex motion, where the transformations can really come in handy.

## Text Sprites

Text sprites are the most bizarre method (known so far) of displaying graphics. They are efficient in a very limited application: displaying small (usually 5x5) images without the drawbacks of hard-coded sprites. The idea is to display several characters very close to each other using the [Text(](text.html) command, so that the first pixel column of each character is combined into an image. For example:

```
:"([X[("→Str1
:For(X,1,5)
:Text(0,X,sub(Str1,X,1))
:End
:Text(0,6,"  ")
```

To understand what is going on, add a Pause command in the For( loop, and watch the image being drawn piece by piece. 

When dealing with text sprites, the image data is stored in strings (in the example above, storing any other 5-character string to Str1 will produce a different 5x5 sprite). In fact, using properly chosen characters (see [this chart](textsprites.html)), nearly any sprite with 5 rows (since small text characters are 5 pixels tall) can be displayed, with only a few rarely-encountered exceptions.

The advantages of using text sprites are:
- At 5 pixels per byte (usually), they are the most efficient method of storing small images.
- The sprites are not made up of points and lines, so they can be fairly detailed.

The drawbacks are:
- Text sprites are usually slower than hard-coded sprites to display.
- They are limited to a 5xN size, which makes them less flexible than other methods.
- Displaying a text sprite erases a small space to the right of the sprite (this can be avoided with caching — see below).
- Code to produce text sprites is harder to learn and understand.
- It is extremely difficult to use text sprites on color calculators, as these use smaller pixels.

Tilemaps are a good application for text sprites: the code for hard-coded sprites would be too large and unwieldy, and plot sprites are too limited in number. This is demonstrated in [Donut Quest](donut-quest.html), a puzzle game whose graphics play to the strengths of text sprites while avoiding situations that would highlight their drawbacks.

Recently, someone came up with the idea of vertical sprites. It uses the same idea but it displays sprites from bottom to top. You can find more information in the [Text Sprites](textsprites.html) page.

## Layered text sprites

Similarly to text sprites, layered text sprites (also referred to as dual-layer ASCII sprites) use the [Text(](text.html) command in order to display custom sprites very efficiently and are usually used in order to display an entire level at once rather than to draw a single isolated sprite due to their limitations, however they are faster than most methods for displaying large images and use very little memory (2 bytes for a single sprite). The idea is to draw a first layer of large font characters, saving them using StorePic, drawing a second layer on top of them and finally using the RecallPic command to join the 2 layers together, creating an horizontal line of sprites. For example:

```
:”NNNHHH”→Str1
:”OOOOOI”→Str2
:Text(-1,1,1,Str1)
:StorePic1
:Text(-1,1,1,Str2)
:RecallPic1
```

A variation of this method can be found in the game Serenity, where the second layer is shifted 1 pixel to the right, allowing the creation of 6x7 sprites and the removal of the gaps created between sprites when using the regular method. 

**Advantages**

- Each sprite only uses 2 bytes of memory
- Due to the fast rendering speed of layered text sprites, they allow the entire screen to be filled very quickly, making them useful for drawing an entire level at once
- The sprites allow for a lot of detail compared to other methods

**Drawbacks**

- They are limited to a 5x7 or a 6x7 size, making them less flexible than other methods
- Only a few different characters can be used, limiting the amount of shapes possible
- Code to produce layered text sprites is harder to learn and understand
- They are inefficient for displaying individual sprites

Due to the drawbacks of this method, layered text sprites are mostly used by platformers whose graphics resemble the home screen, such as Zoith, Metroid Pi and Serenity, for their ability to fill the graph screen very quickly when moving to a new screen.

## Assembly Libraries

The fifth way to render graphics is to use an assembly library such as [xLIB](xlib.html) which includes sprite routines. These routines typically do what we all wish RecallPic could do: nearly instantly recall a small piece of a [picture variable](pictures.html) to an arbitrary part of the screen, often with extra features thrown in. 

Choosing a library to use for your program involves trade-offs: an obscure program might have all the features you want, but a popular library will be used by other games as well. Users probably wouldn't mind installing one library to play a bunch of cool games, but if every game uses its own assembly library, managing them becomes tricky (particularly because they may interfere with each other).

The advantages of using assembly libraries for graphics are:
- They are fast: usually faster than RecallPic, and definitely faster than any other method.
- They are versatile: once you make the decision to use a library, it can be applied to any situation.

The drawbacks are:
- An assembly library takes up lots of memory (not as much of a factor on newer calculators).
- Typically, you will have to use a picture variable, with all the drawbacks that entails.

It's best to use assembly libraries only for graphics-intensive programs. If you do decide to use an assembly library, make as much use of it as possible: there's usually no point in going halfway and mixing an assembly library with any of these other tricks.

## Advanced Techniques

**Caching**: with almost all of these methods, it takes some time to display an entire screen's worth of graphics. If there's a chance that this screen will have to be displayed more than once, it makes sense to avoid doing the extra work of drawing it all over again. To prevent this, take any unused picture variable, and use [StorePic](storepic.html) to save the current state of the screen. Then if it ever needs to be redrawn, [RecallPic](recallpic.html) the screen instead of rendering it the normal way. This technique makes sense for a title screen (if it wasn't a picture variable already) or for the initial state of a level of a game (in case the player restarts).

A similar technique can be used when drawing one image will erase another part of the screen, and both are necessary. In this case, StorePic the screen, draw the image, and then RecallPic. Because RecallPic uses "OR" logic (a fancy way of saying it doesn't ever erase dark pixels), this will keep the background while still drawing the new image. This is critical when combining plot sprites with any other method, and often comes in handy with text sprites as well.

**Greyscale**: if a pixel flashes on and off very quickly, it will appear grey to the eye (because erased pixels need time to fade to white). Switching back and forth between two or more pictures gives the effect of using three colors (black, white, and grey) on a calculator that can normally only handle two. Because this needs to be done quickly, usually only programs using assembly libraries attempt this. An example using xLIB:
```
:Repeat getKey
:For(N,1,2)
:real(3,N,0,1)
:End
:End
```

In this case, pixels that are on in both Pic1 and Pic2 will be displayed as black; pixels that are off in both of them will be displayed as white; pixels that are on in one and off in the other will be displayed as grey.

With precise timing, this technique can be improved to produce multiple shades of grey. Suppose that in this example, Pic2 were displayed twice as long as Pic1. In that case, black and white pixels would be the same; however, a pixel that was on in Pic1 and off in Pic2 would be on 1/3 of the time, while a pixel that was on in Pic2 and off in Pic1 would be on 2/3 of the time. This would give four colors:

| State in Pic1 | State in Pic2 | Result |
| --- | --- | --- |
| off | off | white |
| **ON** | off | light grey |
| off | **ON** | dark grey |
| **ON** | **ON** | black |

Even more shades are possible, but the more complicated the code, the worse the flicker. If you try for too much, eventually the "greyscale" will turn into two pictures quite obviously alternating onscreen. Given the limitations of TI-Basic, it might be best to stick to 3-color greyscale.
