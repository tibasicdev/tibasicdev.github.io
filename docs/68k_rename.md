![The Rename Command](68k_rename/rename.png "The Rename Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Renames a variable into another one|Rename *var1,undefinedvar2*|This command works on all calculators.|X byte(s)|
       
### Menu Location
Catalog Menu
       
# The Rename Command

The Rename command allows you to rename a defined variable to an undefined variable. This is useful if you want to store the value of a variable into another variable, although the [68k:Store](68k:store.html) command is more commonly used for that purpose.
```
Rename a,b
```
The above code would run when "a" is a defined variable and "b" is an undefined variable. That means that if both "a" and "b" were defined, or if "a" was undefined and "b" was defined, it would not work (it would give you error 960).You would get an error if you try to redefine an already defined variable.
## Advanced Uses
The Rename command can also be used for strings. The below code would store the text in Str1 to "a".
```
Rename str1,a
```
## Error Conditions



## Related Commands
- [68k:Store](68k:store.html)
