# Compatibility
When writing TI-Basic programs, it is ideal to have the program universally compatible with the entire [TI range](thecalcs.html). However, that is not always possible. For example, while there are no lowercase letters on the TI-83, excluding the statistical variables, all of the other calculators have them. Keep in mind that although the actual command may not exist on a calculator, it may be possible to transfer a program with the command to that calculator. Here is a table showing the TI-Basic commands that may provide compatibility issues between different calculator versions:

| | || || || || || || Calculator Models |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Command | TI-83 | TI-83+ | TI-83+ OS 1.15 | TI-84+ | TI-84+ OS 2.30 | TI-84+CSE | TI-84+CE/83PCE | TI-Nspire | TI-Nspire CX | TI-Nspire CX/CAS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [%](percent.html) [^1] |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Archive](archive.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Asm(](asm-command.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [AsmComp(](asmcomp.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Asm84CPrgm](asm84cprgm.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✘[^2] |
| [Asm84CEPrgm](asm84ceprgm.html)[^3] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
| [AsmPrgm](asmprgm.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✘ |= ✘ [^4]|
| [BackgroundOff](backgroundoff.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [BackgroundOn](backgroundon.html) [^5] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [χ²GOF-Test(](chisquaregof-test.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |
| [checkTmr(](checktmr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Circle(](circle.html) |= ✓[^6] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ [^7]|= ✓ [^8]|
| [ClockOff](clockoff.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [ClockOn](clockon.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [dayOfWk(](dayofwk.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [DetectAsymOff](detectasymoff.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [DetectAsymOn](detectasymon.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Dot-Thick](dot-thick.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Dot-Thin](dot-thin.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [eval(](eval.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
| [ExecLib](execlib.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [GarbageCollect](garbagecollect.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Get(](get.html) |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓[^9] |
| [getDate](getdate.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [getDtFmt](getdtfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [getDtStr(](getdtstr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [getTime](gettime.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [getTmFmt](gettmfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [getTmStr(](gettmstr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [GraphColor(](graphcolor.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [invT(](invt.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |
| [isClockOn](isclockon.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [LinRegTInt](linregtint.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |
| [Manual-Fit](manual-fit.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |
| [OpenLib(](openlib.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [piecewise(](piecewise.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓[^10] |
| [Send(](send.html) |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓[^11] |
| [setDate(](setdate.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setDtFmt(](setdtfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setTime(](settime.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setTmFmt(](settmfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [startTmr](starttmr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [sub(](sub.html) |= ✓[^12] |= ✓[^13] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Text(](text.html) |= ✓[^14] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [TextColor(](textcolor.html) [^15] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Thick](thick.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Thin](thin.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [timeCnv(](timecnv.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [toString(](tostring.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
| [UnArchive](unarchive.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Wait](wait.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |


[^1]: This command is only accessible in a hex editor
[^2]: Even though this command may not work on the TI-84+CE, you can still have access to the command through an assembly program.
[^3]: Or "Asm83CEPrgm" on the TI-83 Premium CE
[^4]: Even though this command may not work on the TI-84+CE, you can still have access to the command through an assembly program.
[^5]: And all of the Image tokens
[^6]: Using a fourth argument will render a [syntax error](d993808f-ece2-400d-8a50-f35769e358a2)
[^7]: This command can take five arguments, but cannot use {i} as an optimization.
[^8]: This command can take five arguments, but cannot use {i} as an optimization.
[^9]: Requires OS 5.1.5 or later
[^10]: Requires OS 5.3 or later
[^11]: Requires OS 5.1.5 or later
[^12]: Using a single argument will render a [syntax error](69511b5c-fa3f-41b6-a4e0-8a77d4fb592c)
[^13]: Using a single argument will render a [syntax error](d561ad49-d9f6-4139-9afd-50fc9d9a4164)
[^14]: Using ‾1 as the first argument will render a [syntax error](ede19392-c8fb-485d-82d1-a4476941d9b6)
[^15]: And all of the color tokens
