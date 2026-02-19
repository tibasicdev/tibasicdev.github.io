# One Byte Tokens
The two tables below show all the one-byte tokens by their hexadecimal value - the column is the first hex-digit, and the row is the second, so something in the 2 column and the F row would correspond to the hexadecimal number 0x2F. **2-byte** means that this byte signifies the beginning of a 2-byte token (with a link to the appropriate table); **unused** means that this token isn't used for any actual command.

| || || || || || |~ One-byte tokens by hex code (0x00 - 0x7F) |
| |~ 0 |~ 1 |~ 2 |~ 3 |~ 4 |~ 5 |~ 6 |~ 7 |
| 0 | **unused** | ( | [randM(](randm.html) | 0 | [and](and.html) | P | **[2-byte](variable-tokens.html#toc3)** | [+](add.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [►DMS](-dms.html) | ) | [mean(](mean.html) | 1 | A | Q | **[2-byte](variable-tokens.html#toc4)** | [-](subtract.html) (sub.) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | [►Dec](-dec.html) | [round(](round.html) | [solve(](solve.html) | 2 | B | R | **[2-byte](statistics-tokens.html)** | [Ans](ans.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | [►Frac](-frac.html) | [pxl-Test(](pxl-test.html) | [seq(](seq-list.html) | 3 | C | S | **[2-byte](window-tokens.html)** | [Fix](fix.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | [→](store.html) | [augment(](augment.html) | [fnInt(](fnint.html) | 4 | D | T | [Radian](radian-mode.html) | [Horiz](horiz.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | [Boxplot](plotn.html#boxplot) | [rowSwap(](rowswap.html) | [nDeriv(](nderiv.html) | 5 | E | U | [Degree](degree-mode.html) | [Full](full.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | [ | [row+(](rowplus.html) | **unused** | 6 | F | V | [Normal](normal.html) | [Func](func.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | ] | [*row(](timesrow.html) | [fMin(](fmin.html) | 7 | G | W | [Sci](sci.html) | [Param](param.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | { | [*row+(](timesrowplus.html) | [fMax(](fmax.html) | 8 | H | X | [Eng](eng.html) | [Polar](polar-mode.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | } | [max(](max.html) | (space) | 9 | I | Y | [Float](float.html) | [Seq](seq-mode.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | <sup>[r](radian-symbol.html)</sup> | [min(](min.html) | ["](characters.html) | [.](characters.html) | J | Z | [=](equal.html) | [IndpntAuto](indpntauto.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | [°](degree-symbol.html) | [R►Pr(](r-pr.html) | [,](characters.html) | [E](e-ten.html) | K | θ | [<](lessthan.html) | [IndpntAsk](indpntask.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C | [ֿ¹](inverse.html) | [R►Pθ(](r-ptheta.html) | *[i](i.html)* | [or](or.html) | L | **[2-byte](variable-tokens.html#toc0)** | [>](greaterthan.html) | [DependAuto](dependauto.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | [²](2.html) | [P►Rx(](p-rx.html) | [!](factorial.html) | [xor](xor.html) | M | **[2-byte](variable-tokens.html#toc1)** | [≤](lessthanequal.html) | [DependAsk](dependask.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E | <sup>[T](transpose.html)</sup> | [P►Ry](p-ry.html) | [CubicReg](cubicreg.html) | [:](characters.html) | N | **[2-byte](variable-tokens.html#toc2)** | [≥](greaterthanequal.html) | **[2-byte](format-tokens.html)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F |  [³](3.html) | [median(](median.html) | [QuartReg](quartreg.html) | newline | O | [prgm](prgm.html) | [≠](notequal.html) | ![83lgfont/0Ah_LboxIcon.gif](83lgfont/0Ah_LboxIcon.gif "") mark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| || || || || || |~ One-byte tokens by hex code (0x80 - 0xFF) |
| |~ 8 |~ 9 |~ A |~ B |~ C |~ D |~ E |~ F |
| 0 | ![83lgfont/0Bh_LcrossIcon.gif](83lgfont/0Bh_LcrossIcon.gif "") mark | [ZoomRcl](zoomrcl.html) | [Pt-Change(](pt-change.html) | [-](negative.html) (neg.) | [log(](log.html) | [Else](if.html) | [Output(](output.html) | [^](power.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ![83lgfont/0Ch_LdotIcon.gif](83lgfont/0Ch_LdotIcon.gif "") mark | [PrintScreen](printscreen.html) | [Pxl-On(](pxl-on.html) | [int(](int.html) | [10^(](ten-exponent.html) | [While](while.html) | [ClrHome](clrhome.html) | [×√](xroot.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | [*](multiply.html) | [ZoomSto](zoomsto.html) | [Pxl-Off(](pxl-off.html) | [abs(](abs.html) | [sin(](sin.html) | [Repeat](repeat.html) | [Fill(](fill.html) | [1-Var Stats](1-var-stats.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | [/](divide.html) | [Text(](text.html) | [Pxl-Change(](pxl-change.html) | [det(](det.html) | [sinֿ¹(](arcsin.html) | [For(](for.html) | [SortA(](sorta.html) | [2-Var Stats](2-var-stats.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | [Trace](trace.html) | [nPr](npr.html) | [Shade(](shade.html) | [identity(](identity.html) | [cos(](cos.html) | [End](end.html) | [SortD(](sortd.html) | [LinReg(a+bx)](linreg(a-bx).html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | [ClrDraw](clrdraw.html) | [nCr](ncr.html) | [Circle(](circle.html) | [dim(](dim.html) | [cosֿ¹(](arccos.html) | [Return](return.html) | [DispTable](disptable.html) | [ExpReg](expreg.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | [ZStandard](zstandard.html) | [FnOn](fnon.html) | [Horizontal](horizontal.html) | [sum(](sum.html) | [tan(](tan.html) | [Lbl](goto.html) | [Menu(](menu.html) | [LnReg](lnreg.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | [ZTrig](ztrig.html) | [FnOff](fnoff.html) | [Tangent(](tangent.html) | [prod(](prod.html) | [tanֿ¹(](arctan.html) | [Goto](goto.html) | [Send(](send.html) | [PwrReg](pwrreg.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | [ZBox](zbox.html) | [StorePic](storepic.html) | [DrawInv](drawinv.html) | [not(](not.html) | [sinh(](sinh.html) | [Pause](pause.html) | [Get(](get.html) | [Med-Med](med-med.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | [Zoom In](zoom-in.html) | [RecallPic](recallpic.html) | [DrawF](drawf.html) | [iPart(](ipart.html) | [sinhֿ¹(](arsinh.html) | [Stop](stop.html) | [PlotsOn](plotson.html) | [QuadReg](quadreg.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | [Zoom Out](zoom-out.html) | [StoreGDB](storegdb.html) | **[2-byte](variable-tokens.html#toc5)** | [fPart(](fpart.html) | [cosh(](cosh.html) | [IS>(](is-.html) | [PlotsOff](plotsoff.html) | [ClrList](clrlist.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | [ZSquare](zsquare.html) | [RecallGDB](recallgdb.html) | [rand](rand.html) | **[2-byte](miscellaneous-tokens.html)** | [coshֿ¹(](arcosh.html) | [DS<(](ds-.html) | [∟](lists.html) | [ClrTable](clrtable.html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C | [ZInteger](zinteger.html) | [Line(](line.html) | [π](pi.html) | [√(](square-root.html) | [tanh(](tanh.html) | [Input](input.html) | [Plot1(](plotn.html) | [Histogram](plotn.html#histogram) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | [ZPrevious](zprevious.html) | [Vertical](vertical.html) | [getKey](getkey.html) | [³√(](cube-root.html) | [tanhֿ¹(](artanh.html) | [Prompt](prompt.html) | [Plot2(](plotn.html) | [xyLine](plotn.html#xyline) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E | [ZDecimal](zdecimal.html) | [Pt-On(](pt-on.html) | ['](characters.html) | [ln(](ln.html) | [If](if.html) | [Disp](disp.html) | [Plot3(](plotn.html) | [Scatter](plotn.html#scatter) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F | [ZoomStat](zoomstat.html) | [Pt-Off(](pt-off.html) | [?](characters.html) | *[e^(](e-exponent.html)* | [Then](if.html) | [DispGraph](dispgraph.html) | **[TI-84+(C(S)E)](time-tokens.html)** | [LinReg(ax+b)](linreg(ax-b).html) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Comments

- [PrintScreen](printscreen.html) is an unimplemented command that nevertheless has a token associated with it. It doesn't do anything, least of all print the screen. Sorry to get your hopes up.
- The following commands are 2-byte commands even though other similar commands are only one byte:
 - [SinReg](sinreg.html) and [Logistic](logistic.html)
 - [G-T](g-t.html)
 - [randInt(](randint.html), [randNorm(](randnorm.html), and [randBin(](randbin.html)
 - [GetCalc(](getcalc.html) 
 - the *[e](e-value.html)* constant
 - [ZoomFit](zoomfit.html)
 - [ModBoxplot](plotn.html#modboxplot) and [NormProbPlot](plotn.html#normprobplot)
 - [ClrAllLists](clralllists.html)
- The ![83lgfont/0Ah_LboxIcon.gif](83lgfont/0Ah_LboxIcon.gif ""), ![83lgfont/0Bh_LcrossIcon.gif](83lgfont/0Bh_LcrossIcon.gif ""), and ![83lgfont/0Ch_LdotIcon.gif](83lgfont/0Ch_LdotIcon.gif "") marks are for the [Plot1(](plotn.html), [Plot2(](plotn.html), and [Plot3(](plotn.html) commands.
- 0xEF is the first half of a 2-byte token on the TI-84+ and TI-84+ SE, and is unused on other models.
