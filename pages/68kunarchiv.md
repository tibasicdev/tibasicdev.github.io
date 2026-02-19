![The Unarchiv Command](68k_unarchiv/unarchiv.png "The Unarchiv Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|
|--- |--- |--- |
|Unarchives a given variable|Unarchiv *variable*|This command works on all calculators.|
       
### Menu Location

# The Unarchiv Command

The `Unarchiv` command removes a variable from the flash ROM.
```
Prgm
©                                //assuming var1 and var2 are actual variables
Archive var1,var2
isArchiv(var1)→check
Disp check
Pause
Unarchive var1,var2
Disphome
EndPrgm
```

## Related Commands

- [`68k:Archive`](68k:archive.html)
- [`68k:isArchiv`](68k:isarchiv.html)
