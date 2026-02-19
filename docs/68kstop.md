![The Stop Command](68k_stop/stop.png "The Stop Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Stops the program at the given point of the program|No special syntax|This command works on all calculators.|X byte(s)|
       
### Menu Location
In the program editor, [F2][8][4]
# The Stop Command
Simply put, the Stop command stops the program wherever it is placed. 
```
stop()
Prgm
0->X
While true
getkey()->k
x+1->x
Output 5,5,x
If k=13
Stop
EndWhile
EndPrgm
```

This program will increase the value of x by one, but when the user presses the ENTER button, it will stop. Keep in mind to put the Stop EXACTLY where you want it to stop.

## Related Commands
- [68k:Exit](68k:exit.html)
- [68k:Pause](68k:pause.html)
- [68k:Return](68k:return.html)
