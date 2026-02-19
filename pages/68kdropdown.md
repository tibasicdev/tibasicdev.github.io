![The DropDown Command](68k_dropdown/dropdown.png "The DropDown Command")
       
|Command Summary|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |
|Creates a custom menu|This command works on all calculators.|2 bytes|
       
### Menu Location
Describe how to get the command from a menu.
# The DropDown Command
Similar to the Menu( command, the DropDown is used in a dialog box to make body text that includes a dropdown menu, with multiple options. This is good for use in text RPGs or game menus where a dialog box already exists and there isn't a need for another box. Look at this code for example:
``` 
:Dialog
:DropDown "Do you like food?", {"Yes", "No"}, t
:EndDlog
```
This will create a window with the title as "Do you like food" and the options as "Yes" and "No". "T" corresponds to the choice you selected For example, if you chose "Yes", the "T" would be equal to 1. However, if you pressed "No", then "T" would be equal to 2. Basically, the value of your chosen variable will correspond to the choice you made in the window.

## Error Conditions



## Related Commands

- [68k:Custom](68k:custom.html)
- [68k:Dialog](68k:dialog.html)

## Credits
Credits to an unknown user (who's account got deleted). He/she created the code and the first paragraph of the explanation.
