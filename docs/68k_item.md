![The Item Command](68k_item/item.png "The Item Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Adds an item to a [68k:Custom](68k:custom.html) or [68k:ToolBar](68k:toolbar.html) menu.|Item *text* (with Custom)<br>Item *text*,*label* (with ToolBar)|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:
- Press F3 to enter the I/O menu.
- Press 1 to enter the Dialog submenu.
- Press 8 to select Item.
       
# The Item Command

The Item command is used in [68k:Custom](68k:custom.html)..EndCustm and [68k:ToolBar](68k:toolbar.html)..EndTBar blocks (both of which create toolbar menus) to add an option to one of the tabs. See these commands for more details on how to use it.

Inside a Custom..EndCustm menu, the correct syntax is Item *text* (*text* being a string). This will display *text* for the menu option, and also paste *text* every time the option is selected.

Inside a ToolBar..EndTBar menu, the correct syntax is Item *text*,*label*. This will, as in the previous case, display *text* for the menu option; when the option is selected, the program will resume running from [68k:Lbl](68k:lbl.html) *label*. 

## Error Conditions




## Related Commands

- [68k:Custom](68k:custom.html)..EndCustm
- [68k:Title](68k:title.html)
- [68k:ToolBar](68k:toolbar.html)..EndTBar
