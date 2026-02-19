![The DispTable Command](disptable/DISPTABLE.GIF "The DispTable Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Displays the table screen.|DispTable|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program, press:
1. PRGM to access the program menu
1. RIGHT to select the I/O submenu
1. 5 to select DispTable, or use arrows and ENTER
       
# The DispTable Command

The `DispTable` comand displays the table screen you normally see by pressing 2nd TABLE, from a running program. The user will see the table screen with a "paused" run indicator, and will be able to use arrows to scroll through it. Pressing ENTER will exit the screen and continue the program.

## Advanced Uses

The user can't select any cells in the table to be evaluated if they're not, already. So it's best to select the [`IndpntAuto`](indpntauto.html) and [`DependAuto`](dependauto.html) options from the 2nd TBLSET menu before using this command. [`IndpntAsk`](indpntask.html) can also work, however, as long as you store to [`TblInput`](system-variables.html#window) first.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this statement is used outside a program.

## Related Commands

- [`IndpntAsk`](indpntask.html)
- [`IndpntAuto`](indpntauto.html)
- [`DependAsk`](dependask.html)
- [`DependAuto`](dependauto.html)
