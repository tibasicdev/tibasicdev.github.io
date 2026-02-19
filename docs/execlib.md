![The ExecLib Command](execlib/http://tibasicdev.wdfiles.com/local—files/openlib/OPENLIB.png "The ExecLib Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calls a library routine from an application opened with [http://tibasicdev.github.io/OpenLib( OpenLib(]|ExecLib|TI-84+/SE|2 bytes|

### Menu Location
This command can be found in the Prgm Editor CTL menu, press:<br># Press "PRGM" while in the Program Editor.<br># Go to the last command and press "Enter".
# The ExecLib Command

Together with [`OpenLib(`](openlib.html), `ExecLib` is used on the TI-84 Plus and TI-84 Plus SE for running routines from a Flash App library. This only works, of course, with libraries that have been specifically written for this purpose. The only such library so far is [usb8x](http://usb8x.sourceforge.net/), for advanced interfacing with the USB port.

Since `ExecLib` doesn't have any arguments, it would normally be able to run only one library routine. To get around this, usb8x uses a list passed in `Ans` as arguments to the command. This is most likely how any future libraries will do it as well.

The following program, which displays the version of usb8x, is an example of how to use `OpenLib(` and `ExecLib`:

```
:OpenLib(USBDRV8X
:{6
:ExecLib
:Ans(2)+.01Ans(3
```

Download usb8x [here](http://usb8x.sourceforge.net/). You may also be interested in [MSD8x](http://tibasicdev.github.io/local--files/execlib/msd8x.zip) which is a GUI for usb8x.
## Related Commands

- [`OpenLib(`](openlib.html)
