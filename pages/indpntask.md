![The IndpntAsk Command](indpntask/INDPNTASK.GIF width="192" height="128" style="border: 1px solid black;" "The IndpntAsk Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Doesn't automatically fill in table values for the independent variable.|IndpntAsk|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># 2nd TBLSET to access the table settings menu.<br># Use arrows and ENTER to select Ask in the Indpnt: line.
# The IndpntAsk Command

With the `IndpntAsk` setting, the independent variable (X, T, θ, or *n* depending on [graphing mode](graphing-mode.html)) will not be calculated automatically in the table. Instead, when looking at the table, you must select an entry in the independent variable column, press ENTER, and enter a value. The values entered will also be stored to the [`TblInput`](system-variables.html#window) list.

(To access the table, press [2ND][TABLE], or use the [`DispTable`](disptable.html) command in a program)

The alternative, [`IndpntAuto`](indpntauto.html), fills in several values starting at `TblStart` and increasing by `ΔTbl`, and makes the table scrollable (up and down).

## Related Commands

- [`IndpntAuto`](indpntauto.html)
- [`DependAuto`](dependauto.html)
- [`DependAsk`](dependask.html)
- [`DispTable`](disptable.html)
