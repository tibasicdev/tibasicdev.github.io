![Clrerr](68k_clrerr/sample.png "Clrerr")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Clears the error status.<br>and clears the internal error context variables.|ClrErr|This command works on all calculators.|? byte(s)|
       
### Menu Location
This command can only be found in the CATALOG
# Clrerr

Clears the error status. It sets errornum to zero and clears the internal error context variables. The Else clause of the Try...EndTry in the program should use ClrErr or PassErr. If the error is to be processed or ignored, use ClrErr. If what to do with the error is not known, use PassErr to send it to the next error handler. If there are no more pending Try...EndTry error handlers, the error dialog box will be displayed as normal.

## Related Commands

Several (around 3) commands have a similar function or are used in a similar context to this command. Make a bulleted list of them, with links to the other commands' pages. It will often be the case that several commands all link to each other.

- [PassErr](passerr.html)
- Command 2
- Command 3
