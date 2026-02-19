![The Disp Command](68k_disp/disp.png "The Disp Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Displays an output on the Home or I/O screen|Disp //[text],var|This command works on all calculators.|X byte(s)|
       
### Menu Location
From the program editor, press [F3][2]
# The Disp Command
The Disp command displays output in the Home App I/O screen. An example:
```
prgmexmp()
Prgm
Request "Enter something",var1   //Get a value for var1
Disp "var1=",var1
Pause
DelVar var1
ClrIO
DispHome
EndPrgm
```

## Error Conditions


## Related Commands
- [68k:DispHome](68k:disphome.html)
- [68k:DispG](68k:dispg.html)
- [68k:DispTbl](68k:disptbl.html)
## Credits
Credits to byobcello for the explanation and code, both were made by him. Modified for readability/corrections
