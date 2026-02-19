# Windows
Sometimes, you need to just separate one thing from another, want some sort of pop-up window, or want a nice looking frame for the menu on your game.  Well, here's some ways on how to do just that.

## Making Windows
- **Pen**
 - The [`Pen`](pen.html) tool helps you to make lines that are continuous. Good to use if you don't want to repeatedly use the `Line(` command
- **Line(**
 - The [`Line(`](line.html) command allows you to draw straight lines on the graphscreen
- **Horizontal** and **Vertical**
 - Much like the name says, the [`Horizontal`](horizontal.html) command draws a horizontal line and the [`Vertical`](vertical.html) command draws a vertical line
- **Circle**
 - The [`Circle(`](circle.html) command allows you to draw a circle at a specified point.
- **The POINTS commands**
 - [`Pt-On(`](pt-on.html), [`Pt-Off(`](pt-off.html), [`Pt-Change(`](pt-change.html), [`Pxl-On(`](pxl-on.html), [`Pxl-Off(`](pxl-off.html), and [`Pxl-Change(`](pxl-change.html) are all commands that allow you to draw points on the graph screen. Make sure you know how the "Pxl" commands work since their coordinates are a little bit more restricted.

## Full Screen Windows
When you need to put your game or program in some sort of "frame," then you need to decide what you are going to use it for.  If you want to have something that looks very professional, and have it still look simple, here is one way to do that:

![http://tibasicdev.wdfiles.com/local—files/windows/professional%20window](http://tibasicdev.wdfiles.com/local—files/windows/professional%20window "")

If you want a window for a game, say one that is supposed to look medieval, then this might be an appropriate window:

![http://tibasicdev.github.io/local—files/windows/medieval%20window](http://tibasicdev.github.io/local—files/windows/medieval%20window "")

You just have to experiment with what window looks good and what would work with your game/program.

## Pop-up Windows
Pop up windows are a great way to show the user some sort of information.  For example, if you have made a game that uses the list "GAME", then you can put a pop-up menu using [RecallPic](recallpic.html) if the dimensions of the list is 0 (meaning that the user hasn't played your game before).
```
Setupeditor GAME
If dim(GAME)=0:Then
RecallPic 1  //You can replace "1" with any other picture variable
End
```
Here is a picture of a popup menu like that:
![http://tibasicdev.github.io/local—files/windows/pop%20up%20window](http://tibasicdev.github.io/local—files/windows/pop%20up%20window "")
## Game screen
If you want a game screen to show your game statistics like health, money, number of battles, current level, or your character name, then you could use a layout screen for a game.  Let's use the medieval screen from above.
![http://tibasicdev.wdfiles.com/local—files/windows/Game%20screen](http://tibasicdev.wdfiles.com/local—files/windows/Game%20screen "")

## Recalling Windows
As stated previously, you can call your windows in a program with the [`RecallPic`](recallpic.html) command. For more information on how to make windows/the graphscreen, you can look at the Advanced Graphics section of the [TI-Basic Starter Kit](http://tibasicdev.github.io/starter-kit) (specifically [here](http://tibasicdev.github.io/sk:summary-graphics)).
You can create your own window if you want, but these are some suggestions.
