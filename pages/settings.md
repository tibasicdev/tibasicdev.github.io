# User Settings
![MODE.PNG](MODE.PNG "") ![FORMAT.PNG](FORMAT.PNG "") ![TBLSET.PNG](TBLSET.PNG "")

The TI-83 series of calculators has many options to select from that influence either the effect of commands or the way numbers or graphs are displayed. Outside a program, these can be changed by accessing the Mode, Format, or TblSet screens (shown above), and selecting the correct options. When editing a program, going to these screens and choosing an option will instead paste a command that sets that option for you.

These commands are given below, divided by the screen where it is found:

## Mode Settings (MODE)

- [Normal](normal.html), [Sci](sci.html), and [Eng](eng.html) determine how large numbers are displayed.
- [Float](float.html) and [Fix](fix.html) determine how decimals are displayed.
- [Radian](radian-mode.html) and [Degree](degree-mode.html) determine which form of angle measurement is used.
- [Func](func.html), [Param](param.html), [Polar](polar-mode.html), and [Seq](seq-mode.html) determine the [graphing mode](graphing-mode.html).
- [Connected](connected.html) and [Dot](dot.html) determine the default [graphing style](graphstyle.html).
- [Sequential](sequential.html) and [Simul](simul.html) determine how multiple equations are graphed.
- [Real](real-mode.html), [a+bi](a-bi.html), and [re^θi](re-thetai.html) determine how complex numbers are displayed (and affects [ERR:NONREAL ANS](errors.html#nonrealans))
- [Full](full.html), [Horiz](horiz.html), and [G-T](g-t.html) determine how and if the screen is split.

## Graph Format Settings (2nd FORMAT)

- [RectGC](rectgc.html) and [PolarGC](polargc.html) determine how coordinates of the cursor are displayed and stored.
- [CoordOn](coordon.html) and [CoordOff](coordoff.html) determine whether the coordinates of the cursor are displayed at all.
- [GridOn](gridon.html) and [GridOff](gridoff.html) determine whether the grid is displayed.
- [AxesOn](axeson.html) and [AxesOff](axesoff.html) determine whether the X and Y axes are displayed.
- [LabelOn](labelon.html) and [LabelOff](labeloff.html) determine whether the X and Y axes are labeled (if they are displayed)
- [ExprOn](expron.html) and [ExprOff](exproff.html) determine whether the equation graphed or traced is displayed.
- [Time](time.html), [Web](web.html), [uvAxes](uvaxes.html), [uwAxes](uwaxes.html), and [vwAxes](vwaxes.html) (visible in [Seq](seq-mode.html) mode) determine the way sequences are graphed, the default being Time.

## Table Settings (2nd TBLSET)

- [IndpntAuto](indpntauto.html) and [IndpntAsk](indpntask.html) determine whether values of the independent variable in the table are calculated automatically.
- [DependAuto](dependauto.html) and [DependAsk](dependask.html) determine whether the values in the table are calculated automatically for all equations.

## Miscellaneous Settings (2nd CATALOG)

- [DiagnosticOn](diagnosticon.html) and [DiagnosticOff](diagnosticoff.html) determine whether the statistics r and/or r<sup>2</sup> are displayed by [regressions](regression-models.html).
- [FnOn](fnon.html) and [FnOff](fnoff.html) determine whether equations are graphed.
- [PlotsOn](plotson.html) and [PlotsOff](plotsoff.html) determine whether plots are graphed.
- [Pmt_Bgn](pmt_bgn.html) and [Pmt_End](pmt_end.html) determine whether payments are done at the beginning or end of a period with the [finance](finance.html) solver.

## Using these settings in a program

A fair amount of these settings are important to programmers because, if set to the wrong value, they can easily mess up the program. At the beginning of the program, therefore, it's a good idea to set these settings to the correct value. At the very minimum, programs that use the graph screen should set AxesOff if necessary, since AxesOn is the default and a very common setting. This is a part of [program setup](setup.html).

However, another important consideration is that it's somewhat rude to change the user's settings without permission, so your program should change as little as possible. How to reconcile these diametrically opposite goals? There are several ways that work for different settings:

**Use GDBs (Graph DataBases)**

The graph screen settings can be backed up in (and retrieved from) a GDB file by the [StoreGDB](storegdb.html) and [RecallGDB](recallgdb.html) commands. If you store to a GDB at the beginning of the program, and recall from it at the end, you will have preserved all settings that deal with the graph screen.

**Change math settings implicitly**

Instead of changing settings like the Degree/Radian or the Real/a+bi setting, you can use certain commands that will force calculations to be done with that setting regardless of the mode. For example, you can use the [degree symbol](degree-symbol.html) or [radian symbol](radian-symbol.html) to make ambiguous calculations like sin(30) into unambiguous ones like sin(30<sup>o</sup>). Similarly, by adding 0i to a number, you force it to be complex, so that calculations done with it will never cause an [ERR:NONREAL ANS](errors.html#nonrealans) (even if you're in Real mode).

**Ignore uncommon settings**

You might ignore settings that are too uncommon to matter. For example, setting the Full command is unnecessary, because very few people would ever use a split screen, and people that do probably will also figure out why your program breaks when they do so.

**Be rude when you must**

For something like Float, there's no way to avoid changing the user's settings in a way you can't restore. If you have to change a setting so your program works, do it, and mention the issue in the readme. If you changed a setting to an uncommon value, change it back to "Float" (in general, to the default value) when you're done.
