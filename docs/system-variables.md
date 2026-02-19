# System Variables
System variables are, for the purposes of this guide, variables that certain commands will use or modify without asking (i.e. without supplying them in the command's arguments). This is a somewhat ill-defined category, and in fact the system variables we'll discuss are of a somewhat miscellaneous nature. They include equation and plot variables, window and table parameters, statistical variables, and finance variables.

## Equation variables and plot variables {#equation}

The equation variables include Y<sub>0</sub> through Y<sub>9</sub> (function variables), X<sub>1T</sub> and Y<sub>1T</sub> through X<sub>6T</sub> and Y<sub>6T</sub> (parametric variables), r<sub>1</sub> through r<sub>6</sub> (polar variables), and u, v, w (sequential variables). They are used when graphing an equation on the graph screen. From the point of view of a programmer, it's important to realize that these variables are actually [strings](strings.html) in disguise. That is to say, they are stored internally as strings, though the string operations and commands won't work on them. Instead, the following operations are valid for equations:
- Evaluating them, by using the equation variable in an expression.
- Evaluating them at a point, using the syntax EqVar(*value*) - for example, Y<sub>1</sub>(5). This will plug *value* in for the independent variable - X, T, θ, or *n* for function, parametric, polar, and sequential variables respectively.
- Storing a string to them.
- Using the [Equ►String(](equ-string.html) or [String►Equ(](string-equ.html) command to go back and forth from string to equation form.

In addition to their string contents, an equation variable contains two other pieces of information - the graphing style, set with the [GraphStyle(](graphstyle.html) command, and the state (enabled or disabled), set with the [FnOn](fnon.html) and [FnOff](fnoff.html) commands. There is unfortunately, no way to find out which graphing style or state a variable is in, you can only set these to a value.

Plot variables are used for displaying data graphically, in one of six styles: scatter plot, line plot, histogram, box plot, modified box plot, and normal plot. What the variables actually store varies with the plot type, but includes one or more data lists, and settings. All of this can be set with the [PlotN(](plotn.html) command. All or some plots can be turned on and off with the [PlotsOn](plotson.html) and [PlotsOff](plotsoff.html) commands. The [Select(](select.html) command is also useful for dealing with plots.

## Window and table parameters {#window}

These store auxiliary information about the graphing window and include:

- **Xmin, Xmax, Ymin, Ymax** — determine the lower and upper X and Y bounds of the graph screen itself.
- **ΔX, ΔY** — defined to be (Xmax-Xmin)/94 and (Ymax-Ymin)/62 respectively; storing to them will change Xmax and Ymax to arrange this.
- **Xscl, Yscl** — determine how wide the marks on the axes (and, with [GridOn](gridon.html), the grid marks) are spaced.
- **Xres** — determines the quality of [Function](graphing-mode.html#function) graphing (how many pixels apart points are calculated), and must be an integer 1-8.
- **Tmin, Tmax, Tstep** — determine the values at which T is evaluated in [Parametric](graphing-mode.html#parametric) graphing (as though it were a [For(](for.html) loop).
- **θmin, θmax, θstep** — the same idea, but for the θ variable in [Polar](graphing-mode.html#polar) graphing.
- ***n*Min, *n*Max** — bounds for the *n* variable to evaluate (the step is always 1; also, these must be integers).
- **u(*n*Min), v(*n*Min), w(*n*Min)** - override the value of u, v, and w at *n*Min, for the purposes of recursively defining them.
- **PlotStart, PlotStep** — actually have nothing to do with plots, but determine which values of *n* are graphed.
- all of the above have a Z equivalent (ZXmin, Zθstep, etc.) that's used by [ZoomSto](zoomsto.html) and [ZoomRcl](zoomrcl.html).
- **XFact, YFact** — the scaling factors for [Zoom In](zoom-in.html) and [Zoom Out](zoom-out.html).
- **TblStart, ΔTbl** — the starting value and step for the independent variable in the table screen.
- **TblInput** — a 7-element list of the values of a variable in the table.

When transferring variables between calculators, or grouping variables, these variables are grouped in Window, rclWindow, and TblSet.

You can store to each of the window variables directly, or use the [zoom](zoom.html) commands, which affect multiple variables at once to achieve some effect.

You can use these to some extent as real variables to store values in a program, but their use is limited to the home screen (because they affect the graph screen) and there are limits to their ranges. For example, Xmax must be greater than Xmin.

## Statistical Variables {#statistical}

These cannot be stored to, although their values can be used - instead they are modified by statistical commands, which use them as output. See the [statistics](statistics.html) pages for more information. Notably, the list |LRESID is taken up on the CE.

## Finance Variables {#finance}

The seven finance variables are **N**, I%, PV, PMT, FV, P/Y, and C/Y. They are used by the finance solver tool; to use the solver in a program, set these variables to the values you want, choose one of the options [Pmt_End](pmt-end.html) or [Pmt_Bgn](pmt-bgn.html), and then use the value tmv_VAR (where VAR is the variable you want to solve for).

Another use of the finance variables is in speed-critical sections of code: they are faster to access even than [Ans](ans.html). Somewhat off-setting this advantage is the fact that they are two byte tokens, and that they don't work as the variables of a [seq(](seq-list.html) command or a [For(](for.html) loop (they will actually throw a [ERR:SYNTAX](errors.html#syntax) error) or [IS>(](is-.html) and [DS>(](ds-.html). In addition the value of C/Y is altered when P/Y is altered.
