# Compatibility
When writing TI-Basic programs, it is ideal to have the program universally compatible with the entire [TI range](thecalcs.html). However, that is not always possible. For example, while there are no lowercase letters on the TI-83, excluding the statistical variables, all of the other calculators have them. Keep in mind that although the actual command may not exist on a calculator, it may be possible to transfer a program with the command to that calculator. Here is a table showing the TI-Basic commands that may provide compatibility issues between different calculator versions:

| | || || || || || || Calculator Models |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Command | TI-83 | TI-83+ | TI-83+ OS 1.15 | TI-84+ | TI-84+ OS 2.30 | TI-84+CSE | TI-84+CE/83PCE | TI-Nspire | TI-Nspire CX | TI-Nspire CX/CAS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [%](percent.html) [[footnote]]This command is only accessible in a hex editor[[/footnote]] |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Archive](archive.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Asm(](asm-command.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [AsmComp(](asmcomp.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Asm84CPrgm](asm84cprgm.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✘[[footnote]] Even though this command may not work on the TI-84+CE, you can still have access to the command through an assembly program. [[/footnote]] |
| [Asm84CEPrgm](asm84ceprgm.html)[[footnote]]Or "Asm83CEPrgm" on the TI-83 Premium CE[[/footnote]] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
| [AsmPrgm](asmprgm.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✘ |= ✘ [[footnote]] Even though this command may not work on the TI-84+CE, you can still have access to the command through an assembly program. [[/footnote]]|
| [BackgroundOff](backgroundoff.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [BackgroundOn](backgroundon.html) [[footnote]]And all of the Image tokens[[/footnote]] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [χ²GOF-Test(](chisquaregof-test.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |
| [checkTmr(](checktmr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Circle(](circle.html) |= ✓[[footnote]]Using a fourth argument will render a [syntax error](http://tibasicdev.github.io/errors#syntax)[[/footnote]] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ [[footnote]]This command can take five arguments, but cannot use {i} as an optimization.[[/footnote]]|= ✓ [[footnote]]This command can take five arguments, but cannot use {i} as an optimization.[[/footnote]]|
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
| [Get(](get.html) |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓[[footnote]]Requires OS 5.1.5 or later[[/footnote]] |
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
| [piecewise(](piecewise.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓[[footnote]]Requires OS 5.3 or later[[/footnote]] |
| [Send(](send.html) |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓[[footnote]]Requires OS 5.1.5 or later[[/footnote]] |
| [setDate(](setdate.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setDtFmt(](setdtfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setTime(](settime.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [setTmFmt(](settmfmt.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [startTmr](starttmr.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [sub(](sub.html) |= ✓[[footnote]]Using a single argument will render a [syntax error](http://tibasicdev.github.io/errors#syntax)[[/footnote]] |= ✓[[footnote]]Using a single argument will render a [syntax error](http://tibasicdev.github.io/errors#syntax)[[/footnote]] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Text(](text.html) |= ✓[[footnote]]Using ‾1 as the first argument will render a [syntax error](http://tibasicdev.github.io/errors#syntax)[[/footnote]] |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [TextColor(](textcolor.html) [[footnote]]And all of the color tokens[[/footnote]] |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Thick](thick.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [Thin](thin.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |
| [timeCnv(](timecnv.html) |= ✘ |= ✘ |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |
| [toString(](tostring.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
| [UnArchive](unarchive.html) |= ✘ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |= ✓ |
| [Wait](wait.html) |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✘ |= ✓ |
