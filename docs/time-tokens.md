# TI-84+ Tokens
**Note:** The top half of this table is incorrect. An accurate version can be found in the [TI Toolkit token sheets](https://github.com/ti-toolkit/tokens).

The token 0xEF signifies the beginning of a two-byte token added on the TI-84+(C[S]E). The tokens up to [Manual-Fit](manual-fit.html) are for the TI-84+ and the others for the corresponding TI-84+C(S)E.

| || || || || ||~ TI-84+(C[S]E) Tokens (0x00 - 0x6F) |
| |~ 0 |~ 1 |~ 2 |~ 3 |~ 4 |~ 5 |~ 6|
| 0 | [setDate(](setdate.html)| [ClockOn](clockon.html) |  | [►n/d◄►Un/d](n-d-un-d.html) |  | Image1 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [setTime(](settime.html) | [OpenLib(](openlib.html) |  | [►F◄►D](f-d.html) | BLUE | Image2 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | [checkTmr(](checktmr.html) | [ExecLib](execlib.html) |  | [remainder(](remainder.html) | RED | Image3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | [setDtFmt(](setdtfmt.html) | [invT(](invt.html) |  | [Σ(](summationsigma.html) | BLACK | Image4 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | [setTmFmt(](settmfmt.html) | [χ²GOF-Test(](chisquaregof-test.html) |  | [logBASE(](logbase.html) | MAGENTA | Image5 | [BackgroundOff](backgroundoff.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | [timeCnv(](timecnv.html) | [LinRegTInt](linregtint.html) |  | [randIntNoRep(](randintnorep.html) | GREEN | Image6 | [GraphColor(](graphcolor.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | [dayOfWk(](dayofwk.html)| [Manual-Fit](manual-fit.html) |  | [MATHPRINT](mathprint-mode.html) | ORANGE | Image7 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | [getDtStr](getdtstr.html) | [ZQuadrant1](zquadrant1.html) |  | [CLASSIC](classic-mode.html) | BROWN | Image8 | [TextColor(](textcolor.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | [getTmStr(](gettmstr.html) | [ZFrac1/2](zfrac.html) |   | [n/d](n-d.html) | NAVY | Image9 | [Asm84CPrgm](asm84cprgm.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | [getDate](getdate.html) | [ZFrac1/3](zfrac.html) |   | [Un/d](un-d.html) | LTBLUE | Image0 | *compiled asm (CSE)*  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | [getTime](gettime.html) | [ZFrac1/4](zfrac.html) |  | [AUTO](auto-answer.html) | YELLOW | Gridline | [DetectAsymOn](detectasymon.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B | [startTmr](starttmr.html) | [ZFrac1/5](zfrac.html) |  | [DEC](dec-answer.html) | WHITE | [BackgroundOn](backgroundon.html) | [DetectAsymOff](detectasymoff.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C | [getDtFmt](getdtfmt.html) | [ZFrac1/8](zfrac.html) |  | [FRAC](frac-answer.html) | LTGREY |  | [BorderColor](bordercolor.html) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D | [getTmFmt](gettmfmt.html) | [ZFrac1/10](zfrac.html) | | FRAC-APPROX | MEDGREY |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E | [isClockOn](isclockon.html) | mathprintbox | |  | GREY |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F | [ClockOff](clockoff.html) |  | |  | DARKGREY |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |

Note: these are tokens for the CE, from 80h and upper only OS 5.2 and from 9Eh and upper only OS 5.3.

| || || || || ||~ TI-84+(C[S]E) Tokens (0x70 - 0xAF) |
| |~ 7 |~ 8 |~ 9 |~ A |
| 0 | | | SEQ(n+1) | Insert Line Above |
| --- | --- | --- | --- | --- |
| 1 | | Quartiles Setting... | SEQ(n+2) | Cut Line |
| --- | --- | --- | --- | --- |
| 2 | | u(n-2) | LEFT | Copy Line |
| --- | --- | --- | --- | --- |
| 3 | tinydotplot | v(n-2) | CENTER | Paste Line Below |
| --- | --- | --- | --- | --- |
| 4 | [Thin](thin.html) | w(n-2) | RIGHT | Insert Comment Above |
| --- | --- | --- | --- | --- |
| 5 | [Dot-Thin](dot-thin.html) | u(n-1) | [invBinom(](invbinom.html) | Quit Editor |
| --- | --- | --- | --- | --- |
| 6 | | v(n-1) | [Wait](wait.html) | [piecewise(](piecewise.html) |
| --- | --- | --- | --- | --- |
| 7 | | w(n-1) | [toString(](tostring.html) | |
| --- | --- | --- | --- | --- |
| 8 | | u(n) | [eval(](eval.html) | |
| --- | --- | --- | --- | --- |
| 9 | *PlySmlt2* | v(n) | | |
| --- | --- | --- | --- | --- |
| A | Asm84CEPrgm | w(n) | | |
| --- | --- | --- | --- | --- |
| B | *compiled asm (CE)* | u(n+1) | | |
| --- | --- | --- | --- | --- |
| C | | v(n+1) | | |
| --- | --- | --- | --- | --- |
| D | | w(n+1) | | |
| --- | --- | --- | --- | --- |
| E | | | Execute Program | |
| --- | --- | --- | --- | --- |
| F | | SEQ(n) | Undo Clear | |
| --- | --- | --- | --- | --- |
