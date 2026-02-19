![The ZoomSto Command](zoomsto/http://i66.tinypic.com/2evw0hi.gif "The ZoomSto Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Saves the current window settings.|ZoomSto|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. ZOOM to access the zoom menu.
1. RIGHT to access the MEMORY submenu.
1. 2 to select ZoomSto, or use arrows and ENTER.
       
# The ZoomSto Command

The ZoomSto command backs up all window settings applicable to the current graphing mode (those that are shown in the WINDOW menu) to backup variables used specifically for this command. These backup variables are found in the VARS>Zoom... menu, and are distinguished by a Z in front of their name. For example, Xmin is backed up to ZXmin, PlotStart is backed up to ZPlotStart, etc.

Using [ZoomRcl](zoomrcl.html), these backup variables can be used to overwrite the current window settings, recalling the saved window.

One source of confusion with this command can be the fact that ZoomSto and ZoomRcl only deal with the current graphing mode (and don't touch settings from other graphing modes), but some window variables are shared by graphing modes. So some saved zoom variables only applicable to one mode, such as ZTmin, can be from older saves than those applicable to all modes, such as ZXmin.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** occurs if this command is used outside a program (but not if the menu option is used, of course).

## Related Commands

- [ZoomRcl](zoomrcl.html)
- [ZPrevious](zprevious.html)
