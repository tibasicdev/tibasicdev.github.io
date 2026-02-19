![The OpenLib( Command](openlib/http://tibasicdev.wdfiles.com/local—files/openlib/OPENLIB.png "The OpenLib( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets up a compatible Flash application library for use with [ExecLib](http://tibasicdev.github.io/execlib)|OpenLib(*library*)|TI-84+/SE|2 bytes|

### Menu Location
This command is only found in the catalog menu. Press:
1. 2nd CATALOG to access the command catalog.
1. O to skip to commands starting with O.
1. ENTER to select OpenLib(.
       
# The OpenLib( Command

Together with [`ExecLib`](execlib.html), `OpenLib(` is used on the TI-84 Plus and TI-84 Plus SE for running routines from a Flash App library. This only works, of course, with libraries that have been specifically written for this purpose. The only such library so far is [usb8x](http://usb8x.sourceforge.net/), for advanced interfacing with the USB port.

The following program, which displays the version of usb8x, is an example of how to use `OpenLib(` and `ExecLib`:

```
:OpenLib(USBDRV8X
:{6
:ExecLib
:Ans(2)+.01Ans(3
```

## Related Commands

- [`ExecLib`](execlib.html)
