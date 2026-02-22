# Mode Settings
These are the settings that can be used with [setMode()](68k:setmode.html) and [getMode()](68k:getmode.html), with a brief explanation. The 'Number' field refers to an alternate string that can be used for [compatibility](68k:cross-compatibility.html) with other language versions.

Tables are also given for the [setGraph()](68k:setgraph.html) and [setTable()](68k:settable.html) commands.

## Table for setMode() and getMode()

| ***Setting*** | ***Number*** | ***Meaning*** |
| "Graph" | "1" | The type of equations that can be graphed |
| --- | --- | --- |
| "FUNCTION" | "1" | Graphs functions of the form y(x) by connecting points (x,y(x)) for all x. |
| "PARAMETRIC" | "2" | Graphs functions of the form x(t), y(t) by connecting points (x(t),y(t)) for a range of t.|
| "POLAR" | "3" | Graphs functions r(θ) where θ is the angle with the x-axis and r is the radius. |
| "SEQUENCE" | "4" | Graphs possibly recursive functions u(n) in several ways. |
| "3D" | "5" | Graphs functions of the form z(x,y) on 3-dimensional x, y, and z axes. |
| "DIFF EQUATIONS" | "6" | Graphs solutions and slope fields for simple differential equations. |
| "Display Digits" | "2" | Number of digits that are displayed in decimal output |
| --- | --- | --- |
| "FIX #" | "1"-"13" | Displays a fixed number of digits after the decimal, # can be 0 to 12. |
| "FLOAT" | "14" | Equivalent to "FLOAT 12". |
| "FLOAT #" | "15"-"26" | Displays up to # digits total, omitting final zeros after the decimal. # can be 1 to 12. |
| "Angle" | "3" | The default angle format for trigonometric functions |
| --- | --- | --- |
| "RADIAN" | "1" | Most common for mathematicians: a full circle is equal to 2π radians. |
| "DEGREE" | "2" | Common for non-mathematicians: a full circle is equal to 360 degrees. |
| "GRADIAN" | "3" | (Requires AMS 3.10) An uncommon format in which a full circle is equal to 400 gradians. |
| "Exponential Format" | "4" | How large floating-point numbers are displayed |
| --- | --- | --- |
| "NORMAL" | "1" | Most numbers are displayed in the normal way; large numbers use scientific notation. |
| "SCIENTIFIC" | "2" | All numbers are displayed as *mantissa**10^*exponent* ([E](68k:e-ten.html) stands in place of *10^). |
| "ENGINEERING" | "3" | Similar to scientific notation, except *exponent* must be a multiple of 3. |
| "Complex Format" | "5" | How complex numbers are handled |
| --- | --- | --- |
| "REAL" | "1" | The [Non-real result](68k:errors.html#e800) error happens if the result of an expression is complex. |
| "RECTANGULAR" | "2" | Complex numbers are written as x+y*i*. |
| "POLAR" | "3" | Complex numbers are written as re<sup>θ*i*</sup>. |
| "Vector Format" | "6" | The coordinate system used for vectors (2x1, 3x1, 1x2, or 1x3 matrices) |
| --- | --- | --- |
| "RECTANGULAR" | "1" | Vectors are displayed just like any other matrix. |
| "CYLINDRICAL" | "2" | Vectors are displayed in [r ∠ θ] or [r ∠ θ z] format. |
| "SPHERICAL" | "3" | Vectors are displayed in [r ∠ θ] or [r ∠ θ ∠ φ] format. |
| "Pretty Print" | "7" | How mathematical formulas are displayed |
| --- | --- | --- |
| "OFF" | "1" | Pretty print is disabled: formulas are displayed the way they are typed. |
| "ON" | "2" | Pretty print is enabled: formulas are displayed the way they would be on paper. |
| "Split Screen" | "8" | Whether one or two screens are used |
| --- | --- | --- |
| "FULL" | "1" | The entire screen is devoted to one task. |
| "TOP-BOTTOM" | "2" | The screen is split into top and bottom halves devoted to separate applications. |
| "LEFT-RIGHT" | "3" | The screen is split into left and right halves. |
| "Split 1 App" | "9" | The first (or only) app on the screen |
| --- | --- | --- |
| || | (Apart from the defaults: "Home", "Graph", etc. the apps depend on what's installed, and aren't numbered.) |
| "Split 2 App" | "10" | The second app on the screen |
| --- | --- | --- |
| || | (Apart from the defaults: "Home", "Graph", etc. the apps depend on what's installed, and aren't numbered.)  |
| "Number of Graphs" | "11" |  Whether a second graphing mode, available if the screen is split, is enabled |
| --- | --- | --- |
| "1" | "1" | There is only one graphing mode. |
| "2" | "2" | There are two graphing modes. |
| "Graph 2" | "12" | The second graphing mode |
| --- | --- | --- |
| || | (See the "Graph" setting for the options here — they are the same) |
| "Split Screen Ratio" | "13" | The ratio of sizes between the two parts of a split screen |
| --- | --- | --- |
| "1:1" | "1" | The two parts are equal. |
| "1:2" | "2" | The second part is twice the size of the first. |
| "2:1" | "3" | The first part is twice the size of the second. |
| "Exact/Approx" | "14" | At which point the calculator switches into floating-point math |
| --- | --- | --- |
| "AUTO" | "1" | Exact results stay exact except to prevent overflow; floating-point numbers stay in floating-point. |
| "EXACT" | "2" | All numbers are automatically converted to exact integers or fractions |
| "APPROXIMATE" | "3" | All calculations are done in floating-point, as on the TI-83 series calculators. |
| "Base" | "15" | The base in which integer calculations are displayed |
| --- | --- | --- |
| "DEC" | "1" | Integers are displayed in the usual (decimal) base, in their entirety. |
| "HEX" | "2" | The lowest 32 bits of an integer are displayed in [hexadecimal](binandhex.html) (base 16). |
| "BIN" | "3" | The lowest 32 bits of an integer are displayed in [binary](binandhex.html) (base 2). |
| "Apps Desktop" | "16" | (requires AMS 2.07 or higher) The way applications are selected |
| --- | --- | --- |
| "OFF" | "1" | Applications are selected through a popup menu. |
| "ON" | "2" | Applications are selected through a graphic interface. |

## Table for setGraph()

| ***Setting*** | ***Number*** | ***Meaning*** |
| "Coordinates" | "1" | The coordinate system used for recording the cursor's location |
| --- | --- | --- |
| "RECT" | "1" | The standard (x,y) coordinates are displayed and stored to [xc](68k:system-variables.html#cursor) and [yc](68k:system-variables.html#cursor). |
| "POLAR" | "2" | The polar (r,θ) coordinates are displayed and stored to [rc](68k:system-variables.html#cursor) and [θc](68k:system-variables.html#cursor) (standard coordinates are also stored). |
| "OFF" | "3" | No coordinates are displayed, although the standard (x,y) coordinates are still stored. |
| "Graph Order" | "2" | The order in which different equations are graphed |
| --- | --- | --- |
| "SEQ" | "1" | Different equations are graphed one after the other. |
| "SIMUL" | "2" | Different equations are graphed simultaneously. |
| "Grid" | "3" | Whether the grid is displayed |
| --- | --- | --- |
| "OFF" | "1" | The grid is not displayed. |
| "ON" | "2" | The grid is displayed. |
| "Axes" | "4" | Whether the axes are displayed |
| --- | --- | --- |
| "OFF" | "1" | The axes are not displayed. |
| "ON" | "2" | The axes are displayed. |
| "AXES" (3D mode) | "2" | The axes are displayed. |
| "BOX" (3D mode) | "3" | A 3D box is displayed outside the graph. |
| "Leading Cursor" | "5" | Whether the crosshair cursor is displayed when graphing |
| --- | --- | --- |
| "OFF" | "1" | The cursor is not displayed. |
| "ON" | "2" | The cursor is displayed. |
| "Labels" | "6" | Whether the axes are labeled |
| --- | --- | --- |
| "OFF" | "1" | The axes aren't labeled. |
| "ON" | "2" | The axes are labeled. |
| "Seq Axes" | "7" | (in Sequence graphing mode) How the sequences are graphed |
| --- | --- | --- |
| "TIME" | "1" | Each sequence is graphed with n on the x-axis and ui(n) on the y-axis. |
| "WEB" | "2" | A web diagram of one sequence is graphed. |
| "Custom" | "3" | The variables for the x-axis and y-axis can be selected. |
| "Solution Method" | "8" | (in Differential Equation mode) How solutions are estimated |
| --- | --- | --- |
| "RK" | "1" | Runge-Kutta is used to estimate solutions. |
| "EULER" | "2" | Euler's method is used to estimate solutions. |
| "Fields" | "9" | (in Differential Equation mode) Whether a slope field is displayed |
| --- | --- | --- |
| "SLPFLD" | "1" | A slope field is displayed. |
| "DIRFLD" | "2" | A directed slope field is displayed. |
| "FLDOFF" | "3" | No field is displayed. |
| "DE Axes" | "10" | (in Differential Equation mode) How the axes are defined |
| --- | --- | --- |
| "TIME" | "1" | yi(t) is plotted against t. |
| "Y1-VS-Y2" | "2" | y1(t) is plotted against y2(t). |
| "T-VS-Y'" | "3" | t is plotted against yi'(t). |
| "Y-VS-Y'" | "4" | yi(t) is plotted against yi'(t). |
| "Y1-VS-Y2' | "5" | y1(t) is plotted against y2'(t). |
| "Y1'-VS-Y2'" | "6" | y1'(t) is plotted against y2'(t). |
| XR Style | "11" | (in 3D mode) How the 3D effect is achieved |
| --- | --- | --- |
| "WIRE FRAME" | "1" | A wire frame graph is displayed. |
| "HIDDEN SURFACE" | "2" | A non-transparent 3D surface is displayed. |
| "CONTOUR LEVELS" | "3" | The contours of a 3D graph are displayed. |
| "WIRE AND CONTOUR" | "4" | A combination of wire frame and contour levels is displayed. |
| "IMPLICIT PLOT" | "5" | The graph is plotted implicitly. |

## Table for setTable()

| ***Setting*** | ***Number*** | ***Meaning*** |
| "Graph <-> Table" | "1" | Source for automatic table values |
| --- | --- | --- |
| "OFF" | "1" | Automatic table values are based on [tblStart](68k:system-variables.html#table) and [Δtbl](68k:system-variables.html#table). |
| "ON" | "2" | Automatic table values are the same as those used to graph the equation. |
| "Independent" | "2" | Whether the automatic table values are used |
| --- | --- | --- |
| "AUTO" | "1" | Use the automatic table values (as above) for the independent variable. |
| "ASK" | "2" | Enter values for the independent variable manually, ignoring other table settings. |
