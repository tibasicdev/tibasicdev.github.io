![The Title Command](68k_title/title.png "The Title Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Supplies the title text in one of several types of menus.|Title *text*<br><br>or (with [68k:ToolBar](68k:toolbar.html) only)<br><br>Title *text-or-icon*[,*label*]|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:
- Press F3 to enter the I/O menu.
- Press 1 to enter the Dialog submenu.
- Press 7 to select Title.
       
# The Title Command

The Title command is used in different ways with several types of menus:
- Inside a [68k:Dialog](68k:dialog.html)..EndDlog block, it gives the title text for the dialog.
- Inside a [68k:ToolBar](68k:toolbar.html)..EndTBar or [68k:Custom](68k:custom.html)..EndCustm block, it gives a title for a tab.

Usually, all that the Title command wants is a string that will be used for the title (the [68k:string()](68k:string().html) command might be useful for other data types). The exception is ToolBar: then, if the tab has no options under it, Title should also have a label to jump to when that tab is selected.

## Advanced Uses

On the widescreen calculators (the TI-92, TI-92 Plus, and Voyage 200), a [68k:Toolbar](68k:toolbar.html) tab can have a picture for a title (the result will look like the F1 tab of the default toolbar menu). To do so, create a 17x17 picture to be used as the icon, and use the picture variable in place of the tab's title string. If this syntax is used on a TI-89 or TI-89 Titanium calculator, the name of the variable will be displayed instead of the icon (the check for the picture size is still done, and will cause an error if it's the wrong size).

## Error Conditions






## Related Commands

- [68k:Custom](68k:custom.html)..EndCustm
- [68k:Dialog](68k:dialog.html)..EndDlog
- [68k:Text](68k:text.html)
- [68k:ToolBar](68k:toolbar.html)..EndTBar

## See Also

- [68k:dialogs](68k:dialogs.html)
