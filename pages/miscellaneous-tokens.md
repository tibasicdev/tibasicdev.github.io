# Miscellaneous Two-Byte Tokens
Two-byte tokens beginning with the byte 0xBB are miscellaneous tokens, used for various commands that didn't fit in the one-byte range. With later OS versions, various symbols were also added to the 0xBB tokens.

The two tables on this page are split by calculator type, which means that (among other things) the tokens in the second table can't be sent to a TI-83 calculator from a TI-83+ calculator. Further version differences: tokens CF through DA are available with OS 1.15 or higher. Tokens DB through F5 are available with OS 1.16 or higher.

| || || || || ||~ Miscellaneous 2-Byte Tokens (0x00 - 0x67) |
| |~ 0 |~ 1 |~ 2 |~ 3 |~ 4 |~ 5 |~ 6|
| 0 | [npv(](npv.html) | [normalcdf(](normalcdf.html) | [tvm_Pmt](tvm.html) | [►Polar](polar-display.html) | [χ²-Test(](chisquare-test.html) | [ExprOn](expron.html) | **unused** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [irr(](irr.html) | [invNorm(](invnorm.html) | [tvm_I%](tvm.html) | [e](e-value.html) | [ZInterval](zinterval.html) | [ExprOff](exproff.html) | **unused** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | [bal(](bal.html) | [tcdf(](tcdf.html) | [tvm_PV](tvm.html) | [SinReg](sinreg.html) | [2-SampZInt(](2-sampzint.html) | [ClrAllLists](clralllists.html) | **unused** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | [Σprn(](sigmaprn.html) | [χ²cdf(](chisquarecdf.html) | [tvm_N](tvm.html) | [Logistic](logistic.html) | [1-PropZInt(](1-propzint.html) | [GetCalc(](getcalc.html) | **unused** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | [ΣInt(](sigmaint.html) | [Fcdf(](fcdf.html) | [tvm_FV](tvm.html) | [LinRegTTest](linregttest.html) | [2-PropZInt(](2-propzint.html) | [DelVar](delvar.html) | [G-T](g-t.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | [►Nom(](-nom.html) | [binompdf(](binompdf.html) | [conj(](conj.html) | [ShadeNorm(](shadenorm.html) | [GraphStyle(](graphstyle.html) | [Equ►String(](equ-string.html) | [ZoomFit](zoomfit.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | [►Eff(](-eff.html) | [binomcdf(](binomcdf.html) | [real(](real-func.html) | [Shade_t(](shade_t.html) | [2-SampTTest](2-sampttest.html) | [String►Equ(](string-equ.html) | [DiagnosticOn](diagnosticon.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | [dbd(](dbd.html) | [poissonpdf(](poissonpdf.html) | [imag(](imag.html) | [Shadeχ²](shadechisquare.html) | [2-SampFTest](2-sampftest.html) | [Clear Entries](clear-entries.html) | [DiagnosticOff](diagnosticoff.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | [lcm(](lcm.html) | [poissoncdf(](poissoncdf.html) | [angle(](angle.html) | [ShadeF(](shadef.html) | [TInterval](tinterval.html) | [Select(](select.html) | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | [gcd(](gcd.html) | [geometpdf(](geometpdf.html) | [cumSum(](cumsum.html) | [Matr►list(](matr-list.html) | [2-SampTInt](2-samptint.html) | [ANOVA(](anova.html) | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | [randInt(](randint.html) | [geometcdf(](geometcdf.html) | [expr(](expr.html) | [List►matr(](list-matr.html) | [SetUpEditor](setupeditor.html) | [ModBoxplot](plotn.html#modboxplot) | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B | [randBin(](randbin.html) | [normalpdf(](normalpdf.html) | [length(](length.html) | [Z-Test(](z-test.html) | [Pmt_End](pmt-end.html) | [NormProbPlot](plotn.html#normprobplot) | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C | [sub(](sub.html) | [tpdf(](tpdf.html) | [ΔList(](deltalist.html) | [T-Test](t-test.html) | [Pmt_Bgn](pmt-bgn.html) | **unused** | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D | [stdDev(](stddev.html) | [χ²pdf(](chisquarepdf.html) | [ref(](ref.html) | [2-SampZTest(](2-sampztest.html) | [Real](real-mode.html) | **unused** | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E | [variance(](variance.html) | [Fpdf(](fpdf.html) | [rref(](rref.html) | [1-PropZTest(](1-propztest.html) | [re^θi](re-thetai.html) | **unused** | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F |  [inString(](instring.html) | [randNorm(](randnorm.html) | [►Rect](-rect.html) | [2-PropZTest(](2-propztest.html) | [a+bi](a-bi.html) | **unused** | (next table) |
| --- | --- | --- | --- | --- | --- | --- | --- |

| || || || || || || ||~ Miscellaneous 2-Byte Tokens (0x68 - 0xF5) |
| |~ 6 |~ 7 |~ 8 |~ 9 |~ A |~ B |~ C |~ D |~ E |~ F |
| 0 | (prev. table) | Â | Î | Û | β | a | p | reserved | <sub>0</sub> | x |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | (prev. table) | Ä | Ï | Ü | γ | b | q | @ | <sub>1</sub> | ∫ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | (prev. table) | á | í | ú | Δ | c | r | # | <sub>2</sub> |![83lgfont/EFh_LUpBlk.gif](83lgfont/EFh_LUpBlk.gif "")|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | (prev. table) | à | ì | ù | δ | d | s | $ | <sub>3</sub> | ![83lgfont/F0h_LDnBlk.gif](83lgfont/F0h_LDnBlk.gif "") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | (prev. table) | â | î | û | ε | e | t | & | <sub>4</sub> | √ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | (prev. table) | ä | ï | ü | λ | f | u | ` | <sub>5</sub> | ![83lgfont/7Fh_LinvEQ.gif](83lgfont/7Fh_LinvEQ.gif "") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | (prev. table) | É | Ó | Ç | μ | g | v | ; | <sub>6</sub> | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | (prev. table) | È | Ò | ç | π | h | w | \ | <sub>7</sub> | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | [Archive](archive.html) | Ê | Ô | Ñ | ρ | i | x | | | <sub>8</sub> | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | [UnArchive](unarchive.html) | Ë | Ö | ñ | Σ | j | y | _ | <sub>9</sub> | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | [Asm(](asm-command.html) | é | ó | ´ | **unused** | k | z | [%](percent.html) | <sub>10</sub> | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | [AsmComp(](asmcomp.html) | è | ò | ` | φ | **unused** | σ | ... | ← | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C | [AsmPrgm](asmprgm.html) | ê | ô | ¨ | Ω | l | τ | ∠ | → | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D | compiled asm | ë | ö | ¿ | $\hat{p}$ | m | Í | ß | ↑ | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E | Á | **unused** | Ú | ¡ | χ | n | [GarbageCollect](garbagecollect.html) | <sup>x</sup> | ↓ | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F | À | Ì | Ù | α | **F** | o |  | <sub>T</sub> | **unused** | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
