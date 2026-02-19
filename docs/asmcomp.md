![The AsmComp( Command](asmcomp/ASMCOMP.GIF "The AsmComp( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Compresses an assembly program in hexadecimal form into [binary](http://tibasicdev.github.io/binandhex) form.|Asm(prgm*ORIGINAL*,prgm*RESULT*)|TI-83+/84+/SE/CSE/CE<br><br>(not available on the regular TI-83)|2 bytes|

### Menu Location
This command is only found in the catalog. Press:<br># 2nd CATALOG to access the command catalog.<br># Scroll down to AsmComp( and press enter.
# The AsmComp( Command

This command is used to compress an assembly program written using [`AsmPrgm`](asmprgm.html) into an "assembled" assembly program. This will make the program about twice as small, and protect it from being edited, in addition to making execution faster.

To use `AsmComp(`, give it the ASCII represented assembly program, followed by the name you want the assembled program to have. That name can't be already taken. Since it's not easy to rename an assembled assembly program, if you want to write a program called prgmGAME, you type the ASCII represented code in a program with a different name (e.g. GAMEA) and then do `AsmComp(`(prgmGAMEA,prgmGAME).

Assembly programs can be run with [`Asm(`](asm-command.html).

## Error Conditions

- **[ERR:DUPLICATE](errors.html#duplicate)** is thrown if prgm*RESULT* is an already used program name;
- **[ERR:INVALID](errors.html#invalid)** is thrown if prgm*ORIGINAL* doesn't start with [`AsmPrgm`](asmprgm.html);
- **[ERR:SYNTAX](errors.html#syntax)** is thrown if prgm*ORIGINAL* is not an assembly program.

## Related Commands

- [`Asm(`](asm-command.html)
- [`AsmPrgm`](asmprgm.html)
