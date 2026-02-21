![The getDtFmt Command](getdtfmt/GETDTFMT.PNG "The getDtFmt Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the date format of the clock on the TI-84+/SE/CE.|getDtFmt→*Variable*|TI-84+/SE/CE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:
1. 2nd CATALOG to enter the command catalog
2. g to skip to commands starting with G
3. Scroll down to getDtFmt( and select it
       
# The getDtFmt Command

The `getDtFmt(` command returns the current date format of the clock on the TI-84+/SE/CE calculators as an integer. There are three different date formats available: 1 (M/D/Y), 2 (D/M/Y), and 3 (Y/M/D). You can store this value to a [variable](variables.html) for later use. Of course, this command only works if the date format has actually been set, so you should use the [`setDtFmt(`](setdtfmt.html) command before using it.

## Related Commands

- [`getDate`](getdate.html)
- [`setDate(`](setdate.html)
- [`setDtFmt(`](setdtfmt.html)
- [`getDtStr(`](getdtstr.html)
