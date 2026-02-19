![The Request Command](68k_request/request.png "The Request Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Asks for a string in a dialog box.|Request *promptString*, *var*|This command works on all calculators.|? bytes|
       
### Menu Location
Starting in the program editor:
- Press F3 to enter the I/O menu.
- Press 1 to enter the Dialog submenu.
- Press 2 to select Request.
       
# The Request Command

On its own, the Request command asks for a string in a dialog box, while showing the prompt string to its left. It can also be used inside a [`68k:Dialog`](68k:dialog.html)..EndDlog block, to add a line of text to a more advanced dialog.

The text must be a single string, but you can build one out of smaller strings and other data types using the & and string() commands.

`Request` will give an error if the string is too long — how long varies from model to model, and depending on if text is being used inside or outside Dialog..EndDlog, but in general anything below 30 characters is safe (otherwise, you should test the dialog first to make sure everything fits). It uses the small, variable-width font on the TI-89 and TI-89 Titanium, and the normal fixed-width font on widescreen calculators.

## Advanced Uses

You can add 0 as a third argument for the calculator to turn off alpha lock when typing text, but all Request commands in a dialog box must have the same alpha-lock setting. The setting can be used to ask for a number, using [`68k:expr`](68k:expr.html)() as well.

## Error Conditions




## Related Commands

- [68k:Dialog](68k:dialog.html)..EndDlog
- [68k:DropDown](68k:dropdown.html)
- [68k:Text](68k:text.html)
- [68k:Title](68k:title.html)

## See Also

- [68k:Dialogs](68k:dialogs.html)
