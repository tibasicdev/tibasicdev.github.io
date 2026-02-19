![The RecallPic Command](recallpic/RECALLPIC.GIF "The RecallPic Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Recalls a saved picture (one of Pic1, Pic2, ..., Pic0) to the graph screen.|RecallPic *number*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd DRAW to access the draw menu.
1. LEFT to access the STO submenu.
1. 2 to select RecallPic, or use arrows and ENTER.
       
# The RecallPic Command

`RecallPic` draws a saved picture to the graph screen (to save a picture, draw it on the graph screen, then save it with [`StorePic`](storepic.html)). If something is already drawn on the graph screen, `RecallPic` will draw new pixels where needed, but it will not erase anything. As a result, you often want to [`ClrDraw`](clrdraw.html) before recalling a picture.

The number passed to `RecallPic` must be one of 0 through 9. It has to be a number: `RecallPic X` will not work, even if X contains a value 0 through 9.

## Advanced Uses

A combination of `StorePic` and `RecallPic` can be used to maintain a background over which another [sprite](glossary.html#s) moves:

1. Draw the background, and save it to a picture file with `StorePic`.
1. Next, draw the sprite to the screen.
1. When you want to move the sprite, erase it, then use `RecallPic` to draw the background again.
1. Then draw the sprite to its new location on the screen again (this can be done before or after using `RecallPic`).

Also, if a screen in your program takes more than a second to draw, and is displayed several times, you might want to consider storing it to a picture the first time it's drawn, and then recalling it every next time you want to draw it.

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if the argument is not a **number** 0 through 9.
- **[ERR:UNDEFINED](errors.html#undefined)** is thrown if the requested picture does not exist.

## Related Commands

- [`ClrDraw`](clrdraw.html)
- [`StorePic`](storepic.html)
