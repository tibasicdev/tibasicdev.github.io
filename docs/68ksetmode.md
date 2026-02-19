![The setMode() Command](68k_setmode/setmode.png "The setMode() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Changes one or more mode settings.|* setMode(*setting*,*value*)<br>* setMode({*set1*,*val1*,...})|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:<br>* Press F6 to enter the Mode menu.<br>* Select the desired setting to enter its submenu.<br>* Select the desired value to paste setMode("setting", "value")
# The setMode() Command

The setMode() command is used, mainly by programmers, to change mode settings (outside a program, of course, you can just select the settings in the MODE menu). When a setting is changed, it returns the old value of the setting. There are two ways to use the command:
- setMode(*setting*,*value*) will change *setting* to *value*, and return the old value of *setting*.
- setMode({*set1*,*val1*,...}) will change *set1* to *val1*, *set2* to *val2*, and so on, for any number of settings, and return a list in the same format of settings and their old values.
The first format is used to change only one setting, and the second to change several settings.

Both settings and values are identified by strings (not case-sensitive). All the strings involved are given in the [Table of Mode Settings](68k:mode-settings.html).

An example of setMode():
```
setMode("Angle","DEGREE")
           "RADIAN"
setMode({"Angle","RADIAN","Split Screen","FULL"})
           {"Split Screen" "FULL" "Angle" "DEGREE"}
```

## Advanced Uses

Unfortunately, the strings depend on language localization. For [compatibility](68k:cross-compatibility.html) with other languages, there is an alternate identification for the settings and values: you can use a string containing a number identifying the setting or value (see the [Table of Mode Settings](68k:mode-settings.html)). This is also shorter.

As an example, the numerical version of the sample code above would be:
```
setMode("3","2")
           "1"
setMode({"3","1",8","1"})
           {"8" "1" "3" "2"}
```

------

Use the output of the list version of setMode() to restore settings to what they were previously:
```
:setMode({"Angle","RADIAN"})→oldmode
...
:setMode(oldmode)
```

This works with the numerical or the verbose versions of the command; the output of the command will be in the same format as the input.

## Error Conditions






## Related Commands

- [getMode()](68k:getmode.html)
- [setGraph()](68k:setgraph.html)
- [setTable()](68k:settable.html)

## See Also

- [Table of Mode Settings](68k:mode-settings.html)
