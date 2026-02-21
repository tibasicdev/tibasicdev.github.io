![The IndpntAuto Command](indpntauto/INDPNTAUTO.GIF width="192" height="128" style="border: 1px solid black;" "The IndpntAuto Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Automatically fills in the table values for the independent variable.|IndpntAuto|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd TBLSET to access the table settings.
2. Use arrows to select Auto in the Indpnt line to select IndpntAuto.
       
# The IndpntAuto Command

The `IndpntAuto` setting sets the independent variable (X, T, θ, or *n* depending on [graphing mode](graphing-mode.html)) to be filled in automatically in the table (which is accessible by pressing 2nd TABLE, or from a program with the [`DispTable`](disptable.html) command).

The values which will be filled in start at the value [`TblStart`](system-variables.html#window) and increment by `ΔTbl`(which can be negative, but not 0). They will also be stored in the list `TblInput`. All these variables can be accessed through the VARS|6:Table... menu; `TblStart` and `ΔTbl` can also be edited in the [2ND][TBLSET] menu.

The other possibility for this setting is [`IndpntAsk`](indpntask.html) - if that setting is turned on, you must scroll to the corresponding row in the independent variable column, and enter a value.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if `ΔTbl=0`.

## Related Commands

- [`IndpntAsk`](indpntask.html)
- [`DependAuto`](dependauto.html)
- [`DependAsk`](dependask.html)
- [`DispTable`](disptable.html)
