![The getTime Command](gettime/GETTIME.PNG "The getTime Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns a list with the current time that the clock has on the TI-84+/SE/CE.|getTime→*Variable*|TI-84+/SE/CE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:<br># 2nd CATALOG to enter the command catalog<br># g to skip to commands starting with G<br># Scroll down to getTime and select it
# The getTime Command

The `getTime` command returns the current time that the clock has on the TI-84+/SE/CE calculators in [list](lists.html) format —  {*hour*, *minute*, *second*}. You can [store](store.html) this list to a variable for later use, or manipulate it the same way you do with other lists. Of course, this command only works if the time has actually been set, so you should use the [`setTime(`](settime.html) command before using it.

An interesting note about this command is that you cannot index individual elements directly; if you try, each element of the clock is multiplied by the index. You can, however, call the demand and thus store the result in [`Ans`](ans.html), and then retrieve the individual elements.

![http://tibasicdev.github.io/local—files/gettime/SCREEN01.JPG](http://tibasicdev.github.io/local—files/gettime/SCREEN01.JPG "")
## Related Commands

- [`getTmFmt`](gettmfmt.html)
- [`getTmStr(`](gettmstr.html)
- [`setTime(`](settime.html)
- [`setTmFmt(`](settmfmt.html)
