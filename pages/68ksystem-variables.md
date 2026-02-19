# System Variables
System variables are special reserved variable names used by some of the commands internally. They exist outside the folder structure that the other variables are located in, so they can be accessed in the same way from any folder.

Unlike normal variables, which take between 1 and 10 bytes to reference, system variables always take up 2 bytes, no matter how long the name.

## Graph Variables

###Equation Variables

The equation variables contain the equations that get graphed for each [graphing mode](68k:setmode.html). They include:
- **y1(x)–y99(x)** in function mode
- **xt1(t)–xt99(t)** and **yt1(t)–yt99(t)** in parametric mode
- **r1(θ)–r99(θ)** in polar mode
- **u1(n)–u99(n)** and **ui1–ui99** in sequential mode
- **z1(x,y)–z99(x,y)** in 3D mode
- **y1'(t)–y99'(t)** and **yi1–yi99** in differential equation mode

###Cursor Variables

The cursor variables include **xc**, **yc**, **zc**, **tc**, **rc**, **θc** and **nc**. Some of them are updated whenever the crosshair cursor is being moved around on the graph screen, and are especially useful with the [Input](68k:input.html) command. However, the rules that determine which ones get updated are a little tricky:
- **xc** and **yc** are always updated, regardless of any settings.
- The rest get updated depending on graphing mode: **zc** for 3D mode, **tc** for parametric mode, **rc** and **θc** for polar mode, and **nc** for sequential mode.
- In addition, **rc** and **θc** get updated even outside polar graphing mode, if the [graph format](68k:setgraph.html) is set to polar coordinates.

###Window Variables

The window variables define the parameters of the graphing window - they are not only used for graphing, but also with point commands such as [PtOn](68k:pton.html). The most basic of them are **xmin**, **xmax**, **ymin**, and **ymax**: these determine the lower and upper bounds of the window. There are also more advanced settings:
- **xscl** and **yscl** determine the distance between tick marks on the axes, if the axes are enabled.
- **Δx** and **Δy** determine the distance between two pixels next to each other. They are calculated automatically from **xmin**-**ymax**, but you can set them yourself (**xmax** and **ymax** will be adjusted to fit).
- **xfact** and **yfact** determine the factor by which the window is stretched when you zoom in or zoom out.

Some window variables are specific to graphing mode:
1. In function mode:
 - **xres** determines the number of pixels between sample points for graphs (a higher value means lower quality).
1. In parametric mode:
 - **tmin** and **tmax** determine the range of the variable t when graphing.
 - **tstep** determines the increment of the t variable between two sample points on the graph (a higher value means lower quality).
1. In polar mode:
 - **θmin** and **θmax** determine the range of the variable θ when graphing.
 - **θstep** determines the increment of the θ variable between two sample points on the graph (a higher value means lower quality).
1. In sequential mode:
 - **nmin** and **nmax** determine the n values to evaluate at: u(**nmin**), u(**nmin**+1), ..., u(**nmax**) will be evaluated.
 - **plotStrt** and **plotStep** determine the n values that actually get graphed: starting at **plotStrt**, and increasing by **plotStep** each time.
1. In 3D mode:
 - **zmin** and **zmax** (similarly to **xmin** and **xmax**) control the upper and lower bounds of the graphing window, for the z coordinate.
 - **zscl** (similarly to **xscl**) controls the distance between tick marks on the z axis, if the axes are enabled.
 - **zfact** (similarly to **xfact**) controls the factor by which the z-coordinate is stretched when you zoom in or out.
 - **xgrid** and **ygrid** determine the resolution of the wireframe grid.
 - **eyeθ**, **eyeφ**, and **eyeψ** control the viewing angle (**eyeθ** is the angle with the x-axis, **eyeφ** is the angle with the z-axis, and **eyeψ** is a rotation around the resulting line of sight)
 - **ncontours** is the number of contours to graph.
1. In differential equation mode:
 - **t0** determines the t-value for the initial conditions.
 - **tplot** and **tmax** determine range of the variable t when graphing.
 - **tstep** determines the increment of the t variable between two sample points on the graph (a higher value means lower quality). 
 - **ncurves** determines the number of solution curves drawn if you don't give an initial condition.
 - **diftol** (with the Runge-Kutta method) and **Estep** (with the Euler method) determine a step size for calculations.
 - **fldres** determines the number of columns for the slope field, if one is drawn.
 - **dtime** determines the point in time at which a direction field is drawn (if one is drawn at all).
 - **fldpic** is a picture variable that stores the slope field to avoid redrawing it if it's unnecessary.

###Graph Zoom

Many of the above window variables have a zoom variable counterpart, prefixed with a z. These are saved by the [ZoomSto](68k:zoomsto.html) and [ZoomRcl](68k:zoomrcl.html) commands. 

##Statistics Variables

###Regression models

These variables are created when you calculate a curve to fit a set of data, using one of these commands: [LinReg](68k:linreg.html), [MedMed](68k:medmed.html), [QuadReg](68k:quadreg.html), [CubicReg](68k:cubicreg.html), [QuartReg](68k:quartreg.html), [PowerReg](68k:powerreg.html), [ExpReg](68k:expreg.html), [LnReg](68k:lnreg.html), or [Logistic](68k:logistic.html).

- **regeq(x)** is the curve that was calculated, as a function of x.
- **regcoef** is a list of the coefficients calculated.
- **corr** is the correlation coefficient (a measure of the direction and goodness of fit) of a linear model.
- **R<sup>2</sup>** is the square of **corr**, but can be calculated for all models. A value close to 1 indicates a good fit; a value close to 0 is poor.
- **medx1**, **medx2**, **medx3**, **medy1**, **medy2**, and **medy3** are calculated by the MedMed method.

###Sample Statistics

These variables are calculated by the [OneVar](68k:onevar.html) and/or [TwoVar](68k:twovar.html) commands (only those that deal with one variable are calculated by OneVar).

- $\bar{x}$ and $\bar{y}$ are the averages of each data set.
- **Σx** and **Σy** are the sums.
- **Σx<sup>2</sup>** and **Σy<sup>2</sup>** are the sums of the squares.
- **Σxy** is the sum of the products of matching pairs of the two data sets.
- **minX**, **maxX**, **minY**, and **maxY** are the minimum and maximum.
- **Sx** and **Sy** are the sample standard deviations.
- **σx** and **σy** are the population standard deviations.
- **nStat** is the number of elements in a data set.
- **medStat**, **q1**, and **q3** (for OneVar only) are the median, first quartile, and third quartile.

## Other Variables

The rest of the variables don't fit into any of the above categories.

-**c1–c99** are columns in the last data variable shown in the Data/Matrix editor.
-**errornum** contains an [error code](68k:errors.html) once an error has occured, for use in [Try](68k:try.html)..Else..EndTry blocks.
-**eqn** and **exp** are used by the numerical solver (the equation to be solved is stored in **eqn**, and this is set equal to **exp** if the = sign was omitted).
-**ok** is set to 1. if a [Dialog](68k:dialog.html) menu has been exited successfully, and 0. if it was exited with the ESC key.
-**seed1** and **seed2** are the seeds for the random number generator used by [rand()](68k:rand.html).
-**sysData** is the default data variable used by the [BldData](68k:blddata.html) command.
-**sysMath** stores the result of any graphing calculation (for example, for calculating the derivative at a point on the graph)
-**tblStart** and **Δtbl** are used to calculate the table input when it is automatic.
-**tblInput** stores the table input when it's not automatic.
