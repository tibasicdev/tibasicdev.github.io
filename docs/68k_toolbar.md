![The ToolBar Command](68k_toolbar/toolbar.png "The ToolBar Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Creates a toolbar menu and waits for input.|:ToolBar<br> (list of titles and items)<br>:EndTBar|This command works on all calculators.|2 bytes for ToolBar;<br>2 bytes for EndTBar.|
       
### Menu Location
Starting in the program editor:
- Press F3 to enter the I/O menu.
- Press 1 to enter the Dialog submenu.
- Press 6 to select ToolBar..EndTBar.
       
# The ToolBar Command

A ToolBar..EndTBar block, usable only inside a program, displays a custom toolbar menu in place of the usual toolbar, and immediately asks for one of the options to be selected. Selecting an object transfers program flow to a [label](68k:lbl.html) somewhere else in the program.

The toolbar menu can have up to eight tabs (on certain models, there is no upper limit, i.e. TI-92), which correspond to the F1-F8 keys, with any number of options under each tab, or none at all. These are defined by putting the [68k:Title](68k:title.html) and [68k:Item](68k:item.html) commands inside the ToolBar..EndTBar block.

The Title command indicates a new tab, so you can have up to eight of these. After Title, put a string to be displayed for the tab. If the tab doesn't have any options under it, you should also add a label that selecting this tab will jump to.

The Item command indicates an option under the most recent tab — you can have as many items as you like, or none at all. As with Title, you should give Item a name (which will be displayed as the option) and a label that the program will jump to if the option is selected.

Here is an example of the syntax:
```
:ToolBar
: Title "Animals"
:  Item "Dog",lab1
:  Item "Cat",lab2
: Title "Rocks",lab3
: Title "Plants"
:  Item "Grass",lab4
:  ...
:EndTBar
```
In this case, the custom toolbar will display | F1 Animals | F2 Rocks | F3 Plants | … |. Pressing F1 would bring up the Animals menu with items 1:Dog and 2:Cat. Then, pressing 1 or ENTER would continue the program from Lbl lab1. Pressing F2 would immediately jump to Lbl lab3, since that tab has no items.

A related command is [68k:Custom](68k:custom.html)..EndCustm. It also creates a toolbar menu, but one that's intended for use as a custom menu outside a program.

## Advanced Uses

On the widescreen calculators (the TI-92, TI-92 Plus, and Voyage 200), a tab can have a picture for a title (the result will look like the F1 tab of the default toolbar menu). To do so, create a 16x16 (e.g.[0,0;15,15])picture to be used as the icon, and use the picture variable in place of the tab's title string. If this syntax is used on a TI-89 or TI-89 Titanium calculator, the name of the variable will be displayed instead of the icon (the check for the picture size is still done, and will cause an error if it's the wrong size).

## Error Conditions






## Related Commands

- [68k:Custom](68k:custom.html)..EndCustm
- [68k:Dialog](68k:dialog.html)..EndDlog
- [68k:Item](68k:item.html)
- [68k:Title](68k:title.html)
