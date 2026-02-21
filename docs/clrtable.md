![The ClrTable Command](clrtable/CLRTABLE.GIF "The ClrTable Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Clears saved calculations for the table screen.|ClrTable|TI-83/84/+/SE|1 byte|

### Menu Location
While editing a program, press:
1. PRGM to access the program menu.
2. RIGHT to access the I/O submenu.
3. 9 to select ClrTable.
       
# The ClrTable Command

The `ClrTable` command clears all calculations for the table screen shown if you press 2nd TABLE. That is, all already-calculated values in the table are cleared, and [TblInput](system-variables.html#window) is deleted. In [`IndpntAuto`](indpntauto.html) and [`DependAuto`](dependauto.html) mode, this usually isn't noticeable because the table will be recalculated almost immediately when you next look at it (unless one of the entered functions is so complicated it takes a while to calculate). This mainly has an effect in [`IndpntAsk`](indpntask.html) or [`DependAsk`](dependask.html) mode, where the corresponding parts of the table will be cleared entirely.

## Advanced Uses

As a side effect, `ClrTable` seems to have all the effects of [`ClrDraw`](clrdraw.html) — it clears the graph screen, and any equations or plots will be regraphed the next time the graph screen is displayed.

## Command Timings

`ClrTable` and `ClrDraw` take the same amount of time to clear the screen.

## Related Commands

- [`ClrDraw`](clrdraw.html)
- [`DispGraph`](dispgraph.html)
- [`DispTable`](disptable.html)
