![The getDtStr( Command](getdtstr/GETDTSTR.PNG "The getDtStr( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns the current date of the clock on the TI-84+/SE/CE as a string.|getDtStr(*value*)→*variable*|TI-84+/SE/CE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:<br># 2nd CATALOG to enter the command catalog<br># g to skip to commands starting with G<br># Scroll down to getDtStr( and select it
# The getDtStr( Command

The `getDtStr(` command returns the current date of the clock on the TI-84+/SE/CE calculators as a string based on the date format that is specified. There are three different date formats available: 1 (M/D/Y), 2 (D/M/Y), or 3 (Y/M/D). You can store this value to a [string](strings.html) variable for later use, or manipulate it the same way you do with other strings. Of course, this command only works if the date format has actually been set, so you should use the [`setDtFmt(`](setdtfmt.html) command before using it.

## Related Commands

- [`getDate`](getdate.html)
- [`getDtFmt`](getdtfmt.html)
- [`setDate(`](setdate.html)
- [`setDtFmt(`](setdtfmt.html)
