![The Dialog Command](68k_dialog/dialog.png "The Dialog Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Displays a dialog box for input or output.|:Dialog<br>*(dialog elements)*<br>:EndDlog|This command works on all calculators.|2 bytes for Dialog;<br>2 bytes for EndDlog.|
       
### Menu Location
Starting in the program editor:
- Press F3 to enter the I/O menu.
- Press 1 to enter the Dialog submenu.
- Press 5 to paste Dialog..EndDlog.
       
# The Dialog Command

A `Dialog`..`EndDlog` block is used to display a [dialog box](https://en.wikipedia.org/wiki/dialog_box) that can be used for input, output, or both. There are several commands that can be used inside `Dialog`..`EndDlog` to determine its content:

- At most one [`68k:Title`](68k:title.html) instruction (to add a title).
- [`68k:Text`](68k:text.html) (to add a line of text).
- [`68k:Request`](68k:request.html) (to add a text entry box).
- [`68k:DropDown`](68k:dropdown.html) (to add a drop-down menu).

Except for the `Title` instruction, you can mix and match any number of these (as many as will fit on the screen), and their order will determine the order they are displayed. Finally, two "buttons" labeled Enter=OK and ESC=CANCEL will be displayed at the bottom of the dialog box.

Here is a typical dialog box to input a variable name:
```
:Dialog
: Title "Load file"
: Request "File name", name
: Text "(include folder name if not ""main"")"
:EndDlog
```

## Advanced Uses

The [system variable](68k:system-variables.html) "ok" will detect if Enter or ESC was used to exit the dialog: it will have a value of 1 if Enter was used, and 0 for ESC. 

This is particularly important when you're looking for input. If ESC is used, then the variables used in `Request` or `DropDown` will not be changed from what they were before (if they were undefined, they will remain undefined). It's probably a good idea to detect that sort of thing.

## Error Conditions






## Related Commands

- [`68k:ToolBar`](68k:toolbar.html)..`EndTBar`
- [`68k:Text`](68k:text.html)
- [`68k:Request`](68k:request.html)
- [`68k:DropDown`](68k:dropdown.html)
- [`68k:PopUp`](68k:popup.html)

## See Also

- [68k:Dialogs](68k:dialogs.html)
