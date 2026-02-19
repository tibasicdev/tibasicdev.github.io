![The ZoomRcl Command](zoomrcl/http://i66.tinypic.com/2evw0hi.gif "The ZoomRcl Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Recalls window settings previously saved with [ZoomSto](http://tibasicdev.github.io/zoomsto).|ZoomRcl|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. ZOOM to access the zoom menu.
1. RIGHT to access the MEMORY submenu.
1. 3 to select ZoomRcl, or use arrows and ENTER.
       
# The ZoomRcl Command

The ZoomRcl command restores a backup of the window settings previously saved by [ZoomSto](zoomsto.html) — this backup is stored in special variables found in the VARS>Zoom... menu, which are distinguished by a Z in front of their name. For example, Xmin is restored from ZXmin, PlotStart is restored from ZPlotStart, etc. 

Only those settings are restored that apply to the current graphing mode (that is, those that you can see in the window screen). And if no backup had been made, then the default settings are restored to (see [ZStandard](zstandard.html)).

One source of confusion with this command can be the fact that ZoomSto and ZoomRcl only deal with the current graphing mode (and don't touch settings from other graphing modes), but some window variables are shared by graphing modes. So some saved zoom variables only applicable to one mode, such as ZTmin, can be from older saves than those applicable to all modes, such as ZXmin.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program (but not if the menu option is used, of course).

## Related Commands

- [ZoomSto](zoomsto.html)
- [ZPrevious](zprevious.html)
