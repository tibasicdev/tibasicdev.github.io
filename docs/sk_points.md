# Drawing Points and Pixels
The Graph Screen is 95 pixels wide and 63 pixels high.  As can be seen from the Draw Menu there are a variety of ways to display graphics.  Manipulating points and pixels is one of the simplest yet most effective ways to get all you can out of the Graph Screen.


**Note:** Unless otherwise stated the window settings are Xmin=0, Xmax=94, Ymin=-62, and Ymax=0.

## ClrDraw

The first thing you need to know when you deal with the Graph Screen is how to erase your draw. The function you need is ClrDraw. It's found in the Draw Menu and has no syntax. Simply enter ClrDraw as above and the Graph Screen will erase.

```
:RecallPic1
:Pause
:ClrDraw
```

This code will recall Pic1 then wait for the user to press Enter and finally erase all it's content. Now, let's draw !

## Pixels

The graph screen is 95 pixels wide and 63 pixels high.  Similar to [Output(](output.html) on the Home Screen, the first argument of any Pxl- command is the y-coordinate.  This starts at 0 from the top (*not* at 1) and increases as you move down to the bottom row numbered 62.  The second argument is the x-coordinate, starting at 0 on the left and increasing to 94 at the right of the screen.

Two advantages using Pxl- commands has over Pt- commands are the coordinates and speed.  The coordinates always range from 0-94 and 0-62 so you don't have to worry about the user's window settings.  Turning pixels on/off takes almost [2/3](timings.html#toc10) the time it takes their Pt- counterparts.

### Pxl-On(

The [Pxl-On(](pxl-on.html) command is used to turn a pixel on.  It only takes two arguments which are the row and the column.  This is useful when you need just a little tweak for the perfect graphic.
Here's an example.  Let's say you want to draw a face.  You could use [Circle(](circle.html) (we'll get to that later) for the head but then you're missing the eyes.  Turn a couple pixels on!
```
:Circle(47,-31,4)
:Pxl-On(30,46)
:Pxl-On(30,48)
```

### Pxl-Off(

[Pxl-Off(](pxl-off.html) is used to turn a pixel off.  It's arguments are the same as Pxl-On.  This is useful when you need to get rid of a couple little things.  For example, if we wanted to add a mouth on our little head we could use Pt-On (which is coming right after this) and its special 'mark' argument and then turn off the 2 pixels we don't need.
```
:Pt-On(47,-32,3)
:Pxl-Off(31,47)
:Pxl-Off(33,47)
```

### Pxl-Change(

[Pxl-Change(](pxl-change.html) swaps the current state of a pixel.  The arguments are identical to those used with Pxl-On and Pxl-Off.  A great use for this is in animations where you have something moving through an object.  Here is an example.  For most shooting games you don't want to interfere with the background, but if you just turn a pixel on then turn it off after it leaves, you could have a big gaping hole where there shouldn't be!
The top image uses Pxl-Change( and the bottom uses Pxl-On/Pxl-Off.
![http://tibasicdev.github.io/local—files/sk:points/pxlChangeScreenshot](http://tibasicdev.github.io/local—files/sk:points/pxlChangeScreenshot "")

The code for the bullet(s) is
```
:For(A,46,94)
:Pxl-Change(16,A)
:Pxl-Change(16,A-1) \\Top part
:Pxl-On(36,A)
:Pxl-Off(36,A-1) \\Bottom part
:End
```
There is very little difference between the code for each but there are major differences between the outputs!.

### Pxl-Test(

[pxl-Test(](pxl-test.html) checks to see if a pixel is on or off.  It's two arguments are the same as the other pixel commands but instead of drawing/un-drawing something it returns a 1 if that pixel is on and a 0 if it is off.  This is incredibly useful for [collision detection](movement.html#toc4).  A common example of its use is in a game of snake/nibbles.  If the new position of the head was already 'on', then that means it hit something it shouldn't have so they lose.


## Points

In contrast with pixels, the coordinates used by Pt- commands depend on your current window settings.  This could be a problem if you don't want to worry about the user's window settings.  It can also be an advantage which allows you to simplify many arguments for drawing commands.

The first argument for Pt- commands is the *x* coordinate and the second is *y*, the reverse of modifying pixels.  Keep in mind that for the y-coordinate it increases as you move upwards just like a normal graph.
The third argument, unique to points, is the 'mark'.  The number 1 corresponds to a regular one-pixel point.  Two is a box with the center missing.  Three corresponds to a little '+'.

### Pt-On(

[Pt-On(](pt-on.html) draws the 'mark' at the indicated point.  The extra 'mark' argument allows you to make more complicated graphics without drawing them pixel-by-pixel.  Below shows how the different marks can be used for a snake/nibbles game.
![http://tibasicdev.github.io/local—files/sk:points/snakeScreenshot](http://tibasicdev.github.io/local—files/sk:points/snakeScreenshot "")

### Pt-Off(

[Pt-Off(](pt-off.html) erases the mark at a point.  This doesn't just turn off the pixel at the point, but it turns off every pixel that would be part of the mark.  An example of using these to get a cool-looking point is
```
:Pt-On(20,-20,2)
:Pt-Off(20,-20,3)
```
This will only leave the corner pixels of the little box.

### Pt-Change(

[Pt-Change(](pt-change.html) switches the state of the point.  Unlike the other two point commands there is not 'mark' argument making this essentially Pxl-Change( except for the coordinates used.

------
## Points and Pixels on TI 84+CSE and TI 84+CE Version Calculators

For those of you who have a TI 84+C version (i.e. one that is capable of displaying color), then the drawing systems are slightly altered. However, the color functionality and higher screen resolution allows for more detailed and colorful graphics!

**Note:** When working with colors in commands, if no color argument is given, then the pixel or point will automatically be BLUE.

### Screen Dimensions

On TI 84+C version calculators, the dimensions of the screen are 165 pixels high and 265 pixels wide. This is a MUCH higher resolution than the monochrome counterparts, allowing for very detailed graphics and sprites. Like other versions, the first pixel (0,0) is in the top left corner and the last pixel (164,264) is in the bottom right. 

The Pxl-On, Pxl-Off, and Pxl-Change commands still work the same, but with the new dimensions. Points are unaffected by the screen change, as they are still dependent on the graph screen.

### Working with Colored Pixels

If you have a TI 84+C version calculator, you are probably anxious to use its biggest upgrade: color! Color is only available on the graph screen (unfortunately, color text *cannot* be displayed on the home screen), and can be used with both pixels and points.

Let's start with pixel commands. To draw a colored pixel, simply add a color name to end of the Pxl-On( command, as shown below.

```
:ClrDraw
:Pxl-On(82,132,RED //Draws a red pixel near at the center of the screen
:Pxl-Off(82,132 //Turns off pixels regardless of pixel color
```

Notice that the pixel is much smaller than on the grayscale calculators. This allows for more detail, but this also means it takes more commands to draw simpler designs.

You can also call a pixel's color using the color ID, which ranges from 10 to 24. The ID can be stored in a variable, making it very useful for to change colors in a [For(](http://tibasicdev.github.io/for) loop. The code below will draw a pixel at the (A,B) and loop through all the possible colors in the order they appear in the VARS list. 

```
:ClrDraw
:Lbl 1
:For(X,10,24
:Pxl-On(A,B,X
:End
:Goto 1
```

Note that in the code above you must press [ON] in order to exit. You can change the loop to a [Repeat](http://www.tibasicdev.github.io/repeat) loop with a conditional if you want to use it in a game or other program.

The Pxl-Change( command can be used in a similar fashion as Pxl-On(, changing the pixel from on (color does not matter) to off or from off to a desired color, as shown below. If the pixel is already on, then it will be turned off, even if a color argument is given.

```
:ClrDraw
:Pxl-Change(82,132,YELLOW
```

The Pxl-Test( command works the same as it does on the monochrome calculators, but there is one catch: Pxl-Test( *cannot* be used to test for the color of a pixel, just whether it is on or off. Though this is an annoying handicap, Pxl-Test( is still just as useful for boundary detection, except now it can detect pixels of any color.

### Working with Colored Points

Now let's look at coloring points. Like on monochrome calculators, points are denoted the same way on the graph screen, using (X,Y) coordinates. The points, when drawn, cover more pixels than on grayscale calculators, but are still the same size relative to the graph screen. This makes point commands much more effective when drawing multiple pixels.

The Pt-On( command now takes a fourth argument for color to draw. The mark argument, as well as the color argument, are still optional, but can also now be interchanged in order. This means that you can draw a colored point of default mark without having to put an extra "1" to signify a default argument. Here is an example:

```
:ClrDraw
:Pt-On(0,0,1,GREEN
is the same as
:Pt-On(0,0,GREEN //The calculator will recognize no mark is given and draw the default point
:Pt-Off(0,0 //Turns off the point regardless of color
```

The Pt-Change( command, like the Pxl-Change( command, still changes the on or off status of a point, but now takes a color argument when turning points on. The point will still be turned off if it already on, even if a color argument is given:

```
:ClrDraw
:Pt-Change(0,0,ORANGE
```

Just like with monochrome calculators, there is still no mark argument for Pt-Change(.
<center>

|**[<< Introduction to the Graphscreen](sk:graphscreen.html)**|**[Table of Contents](starter-kit.html)**|**[Graph Format Settings >>](sk:graph-settings.html)**|
| --- | --- | --- |

</center>
