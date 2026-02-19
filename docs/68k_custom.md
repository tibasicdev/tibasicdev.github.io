![The Custom Command](68k_custom/custom.png "The Custom Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Creates a custom toolbar menu.|:Custom<br>*(list of titles and items)*<br>:EndCustm|This command works on all calculators.|2 bytes for Custom;<br>2 bytes for EndCustm.|
       
### Menu Location
Starting in the program editor:
- Press F2 to enter the Control menu.
- Press 7 to select Custom...EndCustm.
       
# The Custom Command

A `Custom`..`EndCustm` block creates a custom toolbar menu. The menu can have up to eight tabs for the F1 .. F8 keys, each with any number of sub-items. The contents of the menu are defined using the [`68k:Title`](68k:title.html) and [`68k:Item`](68k:item.html) commands inside the `Custom`..`EndCustm` block.

The `Title` command indicates a new tab, so you can have up to eight of these. After `Title`, put a string to use as the label for the tab. If the title has no items, you'll be able to select the title itself to insert this label somewhere.

The `Item` command indicates an item under the most recent tab — you can have as many items under a tab as you like, or none at all. This also takes a string that will be used as the label for the item, *and* will be inserted any time you select that item from the menu.

Here is an example of the syntax:
```
:Custom
: Title "Animals"
:  Item "Dog"
:  Item "Cat"
: Title "Rocks"
: Title "Plants"
:  Item "Grass"
:  ...
:EndCustm
```

In this case, the custom toolbar will display | F1 Animals | F2 Rocks | F3 Plants | ... |. Pressing F1 would bring up the Animals menu with items 1:Dog and 2:Cat. Then, pressing 1 or ENTER would insert Dog after the cursor. Pressing F2 would insert Rocks under the cursor since that tab has no items.

The custom toolbar can be accessed in any window. To switch to the custom toolbar or back, press 2nd CUSTOM (or use the [`68k:CustmOn`](68k:custmon.html) and [`68k:CustmOff`](68k:custmoff.html) commands).

The calculator comes with a default custom menu, which is overwritten whenever you create one of your own. To restore it, select F6 - Clean Up from the home screen toolbar, and select 3:Restore custom default. This also lets you see an example of `Custom`..`EndCustm` syntax.

A related command is [`68k:Toolbar`](68k:toolbar.html)..`EndTBar`. It also displays a custom menu, but can only be used in a program, and the entries of the menu jump to other parts of the program.

## Error Conditions





## Related Commands

- [`68k:Item`](68k:item.html)
- [`68k:Title`](68k:title.html)
- [`68k:Toolbar`](68k:toolbar.html)..`EndTBar`
