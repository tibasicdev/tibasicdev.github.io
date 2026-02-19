# Assembly
Besides TI-BASIC, assembly is the other primary programming language available for the TI-83 series calculators. Unlike TI-BASIC, which uses commands and functions that are easy to understand, assembly is programmed in the calculator's own machine language. Thus, it is much harder to program in and read.

This lack of usability, however, is more than made up for when you consider the fact that assembly is much faster and more feature rich than TI-BASIC. Games that normally can't be done (or, if they can be done, they aren't done very well) in TI-BASIC are just considered average in assembly.

At the same time, there aren't as many assembly programmers compared to TI-BASIC programmers; and subsequently, effort has been made to enhance TI-BASIC using assembly, to make it more capable of quality games and programs. This includes:

- **[Shells](asm:shells.html)** — A shell allows a person to run a program from inside one central place, and since most assembly programs are run through a shell, it makes sense to run your TI-BASIC programs there as well.
- **[Libraries](asm:libs.html)** — A library enhances a TI-BASIC program in some way, providing support to an internal function of the calculator (such as lowercase text) or access to a peripheral of the calculator (such as the USB port on the TI-84+/SE). If the ones available do not suit you, you can even [make your own](asm:diy-lib.html).
- **[Applications](asm:apps.html)** — BASIC Builder allows you to package your TI-BASIC program(s) into a Flash application, which appears in the APPS menu and gets executed just like a regular assembly application.

The TI-BASIC language itself provides three commands — [Asm(](asm-command.html), [AsmPrgm](asmprgm.html), and [AsmComp(](asmcomp.html) — for running and compiling shell-independent assembly programs, which you simply run from the home screen or inside a program. Writing these kinds of assembly programs is actually more difficult, however, because the assembly language instructions are represented as hexadecimal numbers.  There are some short [assembly programs](hexcodes.html) that can be written on the calculator and be of great use to BASIC programmers.

Two additional commands for running assembly programs have been added on the TI-84 Plus and TI-84 Plus SE calculators: [OpenLib(](openlib.html) and [ExecLib](execlib.html). They can be used for running routines from Flash application libraries that have been specifically written for use with these commands. So far, however, most major libraries use other methods, for compatibility with pre-TI-84 calculators. The only existing software that uses OpenLib( and ExecLib is [usb8x](http://usb8x.sourceforge.net/), a library for advanced use of the TI-84 Plus/SE USB port. Here, compatibility is obviously out of the question.

(*For more on assembly, visit [z80 Heaven](http://z80-heaven.wikidot.com/) and [WikiTI](http://wikiti.brandonw.net).*)
