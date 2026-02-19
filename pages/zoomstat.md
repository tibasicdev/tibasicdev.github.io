![The ZoomStat Command](zoomstat/http://tibasicdev.github.io/local—files/zoomstat/zoomstat.gif width="200" "The ZoomStat Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Zooms to a graphing window which works for all currently selected [plots](http://tibasicdev.github.io/plotn).|ZoomStat|TI-83/84/+/SE|1 byte|

### Menu Location
Press:<br># ZOOM to access the zoom menu.<br># 9 to select ZoomStat, or use arrows and ENTER.
# The ZoomStat Command

The ZoomStat command command zooms to a graphing window that accurately represents all the currently defined stat plots (see the [PlotN(](plotn.html) commands). You can think of it as [ZoomFit](zoomfit.html), but for plots rather than equations.

The specific function of the command is as follows: first, the minimum and maximum X and Y coordinates that stat plots will be using are calculated. Xmin, Xmax, Ymin, and Ymax are calculated to fit all these coordinates plus a padding on either side. The padding is 10% of the unpadded range on the left and right (for Xmin and Xmax), and 17% of the unpadded range on the top and bottom (for Ymin and Ymax).

Of course, the exact function varies slightly with the type of plot defined. For example, Ymin and Ymax will not be affected by [Boxplot](plotn.html#boxplot) and [Modboxplot](plotn.html#modboxplot) plots, since they ignore Y-coordinates when graphing. Also, [Histogram](plotn.html#histogram) fitting is a bit trickier than others. Xscl and Yscl also are changed for histograms, though not for the other plots.

For all plots except Histogram, ZoomStat will create a window with Xmin=Xmax (or Ymin=Ymax) if the X range (or Y range) of the data is 0. This will throw an [ERR:WINDOW RANGE](errors.html#windowrange). If a Histogram causes this error, though, [ERR:STAT](errors.html#stat) is thrown, and *then* when you access the graphscreen [ERR:WINDOW RANGE](errors.html#windowrange) will occur.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if this command is using outside a program (although the menu option, of course, is fine).
- **[ERR:STAT](errors.html#stat)** is thrown when trying to ZoomFit to a Histogram with only one distinct number in the data list.
- **[ERR:WINDOW RANGE](errors.html#windowrange)** is thrown when the window ends up being empty.

## Related Commands

- [ZoomFit](zoomfit.html)
- [ZBox](zbox.html)
