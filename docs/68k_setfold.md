![The setFold() Command](68k_setfold/setfold.png "The setFold() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|A short description of what the command does.|setFold(*foldername*)|This command works on all calculators.|X byte(s)|
       
### Menu Location

       
# The setFold() Command


This command is used to set the current folder. The folder must exist, otherwise the function produces an error. This is a way around this error:

```
:example()
:Prgm
:Try
:setFold(fold1)
:Else
:ClrErr
:NewFold(fold1)
:EndTry
```

## Advanced Uses
If you are changing the current folder, but want to set it back later, the getFold() command is not required to store the old folder name.
For example:
```
:foldset()
:Prgm
:Local a
:getFold()→a
:setFold(fold1)
	...
:setFold(#a)
:EndPrgm
```
does the same thing as
```
:foldset2()
:Prgm
:Local a
:setFold(fold1)→a
	...
:setFold(#a)
:EndPrgm
```

## Error Conditions

**[420 - Invalid Folder Name](68k:errors.html#e420)** happens when the folder does not exist.

## Related Commands

- [68k:GetFold](68k:getfold.html)
- [68k:NewFold](68k:newfold.html)
