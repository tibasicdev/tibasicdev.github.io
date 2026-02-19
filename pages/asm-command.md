![The Asm( Command](asm-command/ASM.GIF "The Asm( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Runs an assembly program.|Asm(prgm*NAME*)|TI-83+/84+/SE<br><br>(not available on the regular TI-83)|2 bytes|

### Menu Location
This command is only found in the catalog. Press:<br># 2nd CATALOG to access the command catalog.<br># DOWN six times.<br># ENTER to select Asm(.
# The Asm( Command

The `Asm(` command is used for running an assembly program. Unlike TI-Basic programs, assembly programs are written in the calculator's machine code directly, which makes them more powerful in both speed and functionality. However, it also means that if they crash, they crash hard — there is no built-in error menu to protect you.

Keep in mind that many assembly programs these days are written for a [shell](asmshells.html) such as Ion or MirageOS. If you're dealing with one of those programs, calling `Asm(` on it will do nothing; you need to get the appropriate shell and run that instead.

With the [`AsmPrgm`](asmprgm.html) and [`AsmComp(`](asmcomp.html) commands, you can create small assembly programs yourself, directly on the calculator. If you are using at TI-84+CE with OS 5.3, the `Asm(` is unnecessary to run such programs.

## Error Conditions

- **[ERR:INVALID](errors.html#invalid)** is thrown if the program isn't an assembly program. 

## Related Commands

- [`AsmPrgm`](asmprgm.html)
- [`AsmComp(`](asmcomp.html)

## See Also

- [Assembly Shells](asmshells.html)
