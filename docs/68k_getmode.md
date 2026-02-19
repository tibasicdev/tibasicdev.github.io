![The getMode() Command](68k_getmode/getmode.png "The getMode() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Checks the current mode settings.|getMode(*setting*)|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

# The getMode() Command

The getMode() command checks any one current mode setting. Just give it the name of the mode setting to check, as a string, and it will give you the current value. For example:

```
:getMode("Angle")
           "RADIAN"
:getMode("Complex Format")
           "REAL"
```

The name of the setting is not case-sensitive, but is very typo-sensitive.

In practice, getMode() is almost entirely superseded by [68k:setMode()](68k:setmode().html) — usually, you don't care about a setting unless you want to change it if it's wrong. In particular, it is silly to do the following:

```
:If getMode("Angle")≠"RADIAN"
:  setMode("Angle","RADIAN")
```

In this case, just the setMode() command instruction by itself would have been fine, since changing the mode from radian to radian would've done nothing anyway. 

It is *also* silly to do the following:
```
:getMode("Angle")→oldmode
:setMode("Angle","RADIAN")
...
:setMode("Angle",oldmode)
```
It is a noble impulse to try to preserve the old setting and restore it later. However, the same is accomplished more elegantly with (note the { } brackets):
```
:setMode({"Angle","RADIAN"})→oldmode
...
:setMode(oldmode)
```

## Optimization

Every string like "Angle" or "FLOAT 12" can be replaced by a numerical equivalent (one that is, for some reason, still given as a string, e.g. "3" or "26"). Using these is shorter, and it has the benefit of being international. 

See the [Table of Mode Settings](68k:mode-settings.html) to look up these numbers, as well as read about what the various mode settings do.

## Error Conditions



## Related Commands

- [68k:setMode()](68k:setmode().html)
- [68k:setGraph()](68k:setgraph().html)
- [68k:setTable()](68k:settable().html)

## See Also

- [Table of Mode Settings](68k:mode-settings.html)
