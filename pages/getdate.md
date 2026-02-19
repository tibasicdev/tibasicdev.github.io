![The getDate Command](getdate/GETDATE.PNG "The getDate Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns a list with the current date that the clock has on the TI-84+/SE/CE.|getDate→*Variable*|TI-84+/SE/CE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:<br># 2nd CATALOG to enter the command catalog<br># G to skip to commands starting with G<br># Scroll down to getDate and select it
# The getDate Command

The `getDate` command returns the current date that the clock has on the TI-84+/SE/CE calculators in [list](lists.html) format —  {*year*, *month*, *day*}. You can [store](store.html) this list to a variable for later use, or manipulate it the same way you do with other lists. Of course, this command only works if the date has actually been set, so you should use the [`setDate(`](setdate.html) command before using it.

An interesting note about this command is that you cannot index `getDate` directly to get individual elements; if you try, each element of the clock is instead multiplied by the number. You may, however, call the command and thus store it in [`Ans`](ans.html), then retrieve individual elements.

![http://tibasicdev.github.io/local—files/getdate/SCREEN02.BMP](http://tibasicdev.github.io/local—files/getdate/SCREEN02.BMP "")
## Related Commands

- [`getDtFmt`](getdtfmt.html)
- [`getDtStr(`](getdtstr.html)
- [`setDate(`](setdate.html)
- [`setDtFmt(`](setdtfmt.html)
