![The Lock Command](68k_lock/lock.png "The Lock Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Locks the specified variables|Lock *var1, var2, etc*|This command works on all calculators.|X byte(s)|
       
### Menu Location

       
# The Lock Command
The `lock` command prevents a variable's value from changing. In programs and functions, `lock` is usually used to stop a variable from undesirably changing. If a variable is universally defined (like files in folders), the `lock` command has a popular purpose of making the variable constant (unchanging) throughout use in sets of programs.

```
input "Input var1 here: ",var1
lock var1
text "You can no longer change var1."
© var1 can now be used as a constant variable.
©... <program statements that require the value of var1>
prgm2() ©var1 may not change in any other programs.
unlock var1
```
Note: the © command will turn any code written until the next ':' into comments. (neat-freaks love this.)
Comments are very helpful for people who forget, especially when dealing with tricky commands and code. Using comments for the *lock* command will help you remember to *unlock* the variable when the time comes to delete it.


## Related Commands

- [Unlock](68k:unlock.html)
- [Archive](68k:archive.html)
- [Unarchiv](68k:unarchiv.html)
