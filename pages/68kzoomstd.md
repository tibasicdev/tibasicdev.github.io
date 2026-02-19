![The ZoomStd Command](68k_zoomstd/zoomstd.png "The ZoomStd Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Sets the window variables to their default settings.|ZoomStd|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

# The ZoomStd Command

The ZoomStd command initializes the [window variables](68k:system-variables.html#window) applicable to the current mode to their default values. These default values are:
- **xmin**=-10, **xmax**=10, **xscl**=1 (except in differential equation mode, where **xmin**=-1)
- **ymin**=-10, **ymax**=10, **yscl**=1
- **xres**=2 (in function mode)
- **tmin**=0, **tmax**=2π, **tstep**=π/24 (in parametric mode)
- **θmin**=0, **θmax**=2π, **θstep**=π/24 (in polar mode)
- **nmin**=0, **nmax**=10, **plotStrt**=1, **plotStep**=1 (in sequence mode)
- **eyeθ**=20, **eyeφ**=70, **eyeψ**=0, **xgrid**=14, **ygrid**=14, **zmin**=-10, **zmax**=10, and **ncontour**=5 (in 3D mode)
- **t0**=0, **tmax**=10, **tstep**=0.1, **tplot**=0, **ncurves**=0, **diftol**=0.001, and **fldres**=20 (in differential equation mode)

See the [68k:system-variables](68k:system-variables.html) article for details on what these variables actually do.

## Advanced Uses

One common use for ZoomStd is as a prelude to [68k:ZoomInt](68k:zoomint.html) in a program. This makes sure that the window variables are the same each time, which ZoomInt alone doesn't guarantee.

## Related Commands

- [68k:ZoomSqr](68k:zoomsqr.html)
- [68k:ZoomSto](68k:zoomsto.html)
- [68k:ZoomRcl](68k:zoomrcl.html)

## See Also

- [68k:system-variables](68k:system-variables.html#window)
