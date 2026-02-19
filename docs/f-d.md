![The ►F◄►D Command](f-d/FD2.gif "The ►F◄►D Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Converts a number between fraction form and decimal form.|*number*►F◄►D|TI-84 2.53MP only|2 bytes|

### Menu Location
Press:<br># MATH<br># RIGHT to NUM<br># ALPHA B<br><br>Alternatively, access the catalog.
# The ►F◄►D Command

The `►F◄►D` command is used to convert a number from fraction form to decimal form, or vice versa.  Regardless of what form the given number is, this command is meant to automatically determine the form so that it returns the other.  It is in essence a combination of the [`►Frac`](-frac.html) and [`►Dec`](-dec.html) commands, applying `►Frac` if the input is in decimal form and `►Dec` if it is a fraction.

```
7.5►F◄ ►D
        15/2
Ans►F◄ ►D
        7.5
```

## Related Commands

- [`►Frac`](-frac.html)
- [`►Dec`](-dec.html)
