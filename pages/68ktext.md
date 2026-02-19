![The Text Command](68k_text/text.png "The Text Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Displays a line of text in a dialog box.|Text *string of text*|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F3 to enter the I/O menu.<br>* Press 1 to enter the Dialog submenu.<br>* Press 1 to select Text.
# The Text Command

On its own, the Text command displays a simple dialog box with a line of text (left-aligned) inside. It can also be used inside a [68k:Dialog](68k:dialog.html)..EndDlog block, to add a line of text to a more advanced dialog.

The text must be a single string; but you can build one out of smaller strings and other data types using the [&](68k:append.html) and [68k:string()](68k:string().html) commands.

Text will give an error if the string is too long — how long varies from model to model, and depending on if Text is being used inside or outside Dialog..EndDlog, but in general anything below 30 characters is safe (otherwise, you should test the dialog first to make sure everything fits). It uses the small, variable-width font on the TI-89 and TI-89 Titanium, and the normal fixed-width font on widescreen calculators.

## Advanced Uses

You can add Text "" to a dialog to skip a line between two other elements.

## Error Conditions




## Related Commands

- [68k:Dialog](68k:dialog.html)..EndDlog
- [68k:DropDown](68k:dropdown.html)
- [68k:Request](68k:request.html)
- [68k:Title](68k:title.html)

## See Also

- [68k:Dialogs](68k:dialogs.html)
