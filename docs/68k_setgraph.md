![The setGraph() Command](68k_setgraph/setgraph.png "The setGraph() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Changes any of the graph settings.|setGraph(*setting*,*value*)|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

       
# The setGraph() Command

The setGraph() command is an analog of the [68k:setMode()](68k:setmode.html) command, except that it's used specifically to change graph settings. setGraph(*setting*,*value*) will change *setting* to *value*, and return the old value of *setting*. Both settings and values are identified by strings (not case-sensitive, but very spelling-sensitive), which are listed on the [68k:mode-settings](68k:mode-settings.html) page.

```
:setGraph("Coordinates","OFF")
           "RECT"
:setGraph("Axes","OFF")
           "ON"
```

Unlike setMode(), you can't change more than one setting at a time; there isn't a getGraph() function either, although you could use setGraph() to determine the mode setting if you really needed to.

## Advanced Uses

As an alternative to the long and hard-to-remember strings, you can also identify the settings and values of setGraph() with short and still hard-to-remember numbers (or rather, string versions of numbers). The equivalents are also listed on the [68k:mode-settings](68k:mode-settings.html) page. For instance, "Coordinates" can be replaced with "1", and "IMPLICIT PLOT" with "5". If you use these codes as arguments to setGraph(), it will return such a code as well.

There are two advantages to this. First of all, writing the numbers is shorter, so it saves some space in the program. Second, it ensures that if, say, a French speaker is using your program with the language set to French, it will still work (normally, strings like "Coordinates" depend on the language setting).

------

Use the output of setGraph() to restore settings to what they were previously:
```
:setGraph("Axes","OFF")→oldaxes
...
:setGraph("Axes",oldaxes)
```

## Error Conditions

**[130 - Argument must be a string](68k:errors.html#e130)** happens when the data type of arguments is incorrect.
**[260 - Domain error](68k:errors.html#e260)** happens when the string used to identify a setting is incorrect or misspelled.
**[430 - Invalid for the current mode settings](68k:errors.html#e430)** happens when a setting depends on other settings that are incorrect (e.g. setting "XR Style" when the calculator is not in 3D graphing mode).
**[450 - Invalid in a function or current expression](68k:errors.html#e450)** happens when setGraph() is used in a function.

## Related Commands

- [68k:getMode()](68k:getmode.html)
- [68k:setMode()](68k:setmode.html)
- [68k:setTable()](68k:settable.html)

## See Also

- [68k:mode-settings](68k:mode-settings.html)
