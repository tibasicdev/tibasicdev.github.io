# Why TI-Basic?
**TI-Basic History**

Texas Instruments has included TI-Basic support with each graphing calculator (starting with the TI-81), and the TI-Basic language has evolved along with the calculators (adding new features and functionality).

With the TI-68k family of calculators, TI-Basic was enriched with symbolic calculation capability; the newest calculators (TI-89 Titanium and Voyage 200) take this even further with commands such as [impDif()](68k:impdif.html) for implicit differentiation.


TI-Basic is the built-in programming language of the TI graphing [calculators](68k:thecalcs.html). You can create TI-Basic programs on the computer using the Graph Link or TI Connect software, or on the calculator itself through the program editor (see [getting started](68k:getstarted.html) for more information). Knowing TI-Basic is important because it is one of the main ways that people use their calculators; if you are unable to program in TI-Basic, you will not be able to effectively communicate with others concerning your calculator.

## Advantages of TI-Basic

There are several advantages of programming your calculator in TI-Basic. First, and foremost, it is the most well known calculator programming language. With most high schools requiring TI graphing calculators for math and science classes, TI-Basic is often used by students to make small math or science programs. For many of these students, TI-Basic is the first programming language they have ever used.

Second, TI-Basic is extremely simple, both to learn and to use. In TI-Basic, most of the commands are easily understood. The commands are written in plain English or easily comprehended abbreviations: Disp, Rename, etc. In addition, the commands are generally self-explanatory. For example, it is not very hard to recognize that the [Pause](68k:pause.html) command pauses the program. As for simplicity of use, TI-Basic is (so far) the only language that can easily be programmed on the calculator directly — writing C, for example, requires a compiler such as [TIGCC](http://tigcc.ticalc.org/) that's currently only available on computers.

Third, it's very easy to do calculations in. Though TI-Basic can be used to write games as well, it's really useful for math programs. A math program in another language would probably have to call the same routines that TI-Basic uses anyway; this would be much more complicated, and wouldn't be an improvement in size or in speed.

Lastly, if you mess up in TI-Basic (your program has an error), it just gives you an [error message](68k:errors.html). If a C or assembly program has an error, however, the results wouldn't be as good. Depending on the severity of the error, you can cause your calculator's RAM to be cleared, or even leave your calculator in an endless loop, making it completely useless. TI-Basic does not have that problem, because no matter where you are in a TI-Basic program, you just have to press the ON key to stop execution.

## Disadvantages of TI-Basic

TI-Basic does have some disadvantages. Its main disadvantage is its speed. Because TI-Basic is converted by the calculator into machine code before it is executed, it loses much of its speed. Graphics, especially, come nowhere close to the speed of machine code — though assembly or C programs are fast enough to handle greyscale, for example, this is virtually impossible in TI-Basic.

The other disadvantage of TI-Basic is that it is does not have low-level access to the calculator's hardware. While this is intentionally done to prevent potential misuse, it has the result of limiting the quality of TI-Basic programs. This is mainly a problem with input (the [getKey()](68k:getkey.html) command is limited to one key at a time, and can handle modifier keys such as 2nd only indirectly) and graphics (which are limited to only about 2/3 of the screen — the rest is taken up by the menu and status bar).
