# The Zoom Commands
The Zoom commands are found in the menu you get by pressing ZOOM. They are used to manipulate the [window variables](system-variables.html#window) to change the bounds of the graphing window. With the exception of [ZStandard](zstandard.html), [ZoomSto](zoomsto.html), and [ZoomRcl](zoomrcl.html), these commands only affect the variables universal to all [graphing modes](graphing-mode.html): Xmin, Xmax, Xscl, Ymin, Ymax, and Yscl. They ignore the variables specific to a single graphing mode:
- Xres (only used in [Func](func.html) mode)
- Tmin, Tmax, and Tstep (only used in [Param](param.html) mode)
- θmin, θmax, and θstep (only used in [Polar](polar-mode.html) mode)
- *n*Min, *n*Max, PlotStart, and PlotStep (only used in [Seq](seq-mode.html) mode)

## Zoom Variables

Virtually every window variable has a z-equivalent (ZXmin for Xmin, ZPlotStart for PlotStart, etc.) that are found under VARS|2:Zoom... — these are used by [ZoomSto](zoomsto.html) and [ZoomRcl](zoomrcl.html). Also, the variables XFact and YFact (found under VARS|1:Window...) are used by [Zoom In](zoom-in.html) and [Zoom Out](zoom-out.html).

## Commands

The commands themselves are only available in programs. Outside it, you can only choose the equivalent menu option (which doesn't leave an entry on the homescreen, and sometimes slightly differs in effect) — this happens, even if you choose the command from the catalog. Of course, with a bit of trickery, you can get the command token itself on the homescreen, but then [ERR:INVALID](errors.html#invalid) will be thrown if you try to use it. The [Trace](trace.html) command also works this way.

The following zoom commands are available:


- [ZBox](zbox.html)
- [Zoom In](zoom-in.html)
- [Zoom Out](zoom-out.html)
- [ZDecimal](zdecimal.html)
- [ZSquare](zsquare.html)


- [ZStandard](zstandard.html)
- [ZTrig](ztrig.html)
- [ZInteger](zinteger.html)
- [ZoomStat](zoomstat.html)
- [ZoomFit](zoomfit.html)


- [ZPrevious](zprevious.html)
- [ZoomSto](zoomsto.html)
- [ZoomRcl](zoomrcl.html)
- [ZFracX](zfrac.html)[^1]


[[footnoteblock]]

[^1]: Available only for OS 2.53MP+
