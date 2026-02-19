# Asm84CEPrgm
Please see the [`AsmPrgm`](asmprgm.html) page. The functionality and use are the same between both commands. However, the `Asm84CEPrgm` is only available on the TI-84+CE calculator. Keep in mind that hexadecimal for the monochrome calculators may not work on color calculators. **This token does not work on OS 5.3.1**, it has been deprecated by Texas Instruments for no good reason. Even uploading a program with this token in it will not work as it will throw an `INVALID` error.

There is a workaround to this problem. A sendable program containing the command can be found [here](http://tibasicdev.github.io/archive:asm84ceprgm-command-for-os-5-3-1-0058).

To run assembly programs on the calculator, recall the command from the program you sent. Type your hex code in the editor. When you're done, quit the program. Type the following on the homescreen:

```
AsmComp(prgmNAME1,prgmNAME2
```

Then, find the program you compressed and run it with either the [Asm(](asm.html) command or like a normal BASIC progam.
