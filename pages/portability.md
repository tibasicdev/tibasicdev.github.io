# Portability
|**This article is part of the planning stage of the [development](development.html) cycle.**|
| --- |

Portability is the ability to run a program on more than one calculator, with little to no changes made to the program — you can literally transfer the program to a calculator, and then start using it. This ability is important because all of the TI-83 series calculators are very similar in TI-Basic support and calculator hardware, so people expect when they find a TI-83 series program it will work on their calculator.

There are five primary things that you need to consider when making a program portable:

- Making sure not to use assembly programs
- Making sure not to use new commands (see [compatibility](compatibility.html))
- Making sure not to use undocumented functionality (see [compatibility](compatibility.html))
- Making sure not to use extra characters
- The calculator's memory and speed

## Assembly Programs

Although assembly programs allow you to make your programs look nice, and to use functionality that isn't normally possible or viable in TI-Basic (such as creating parallax scrolling using [xLIB](xlib.html)), they are not portable because they need to be compiled to work on each calculator.

This is because assembly programs are programmed in the calculator's own machine language, and use memory addresses that are specific to a particular calculator model. This means, for instance, that a TI-83 assembly library that inverts the graph screen will not work on any of the new TI-83 series calculators.

The TI-83 also uses a different format to run assembly programs than the other TI-83 series calculators: Send(9prgmNAME). This use of the [Send(](send.html) command does not work on any of the other calculators, and in fact will result in a [ERR:SYNTAX](errors.html#syntax) error. Instead, the rest of the TI-83 series calculators provide three commands — [Asm(](asm-command.html), [AsmPrgm](asmprgm.html), and [AsmComp(](asmcomp.html) — for running and compiling shell-independent assembly programs.

Two additional commands for running assembly programs have been added to the TI-84+ and TI-84+SE calculators: [OpenLib(](openlib.html) and [ExecLib](execlib.html). These can be used for running routines from Flash application libraries that have been specifically written for use with them; the only application so far is [usb8x](http://usb8x.sourceforge.net/), which is used for interfacing with the USB port.

Apart from use of these last two commands, however, most assembly programs ought to be compatible between the TI-83+/SE and TI-84+/SE

## New Commands

With each release of a TI-83 series calculator, TI has added new commands to the calculator. The TI-83+ calculator introduced [Archive](archive.html), [UnArchive](unarchive.html), and [GarbageCollect](garbagecollect.html), which are designed to work with the Flash memory available on the calculator. This is in addition to the assembly commands that were mentioned earlier.

The TI-84+ and TI-84+SE calculators introduced several new [time and date](time-and-date.html) commands, some of which use the new built-in clock, while others are used for formatting times and dates; and the aforementioned [OpenLib(](openlib.html) and [ExecLib](execlib.html) for running routines from Flash application libraries. The new OS (2.30 or later) also includes some additional commands for statistics: [Manual-Fit](manual-fit.html), [invT(](invt.html), [LinRegTInt](linregtint.html), and [χ²GOF-Test(](chisquaregof-test.html).

## Undocumented Functionality

Along with documented changes, different calculators and OS versions have some undocumented differences. These are given below grouped by the first calculators they occur on:

**TI-83+ or higher:**
- **Large font on the graph screen** — Use the syntax [Text(](text.html)-1, *row*, *column*, *text*) to display text in the large font instead of the typical small font associated with the graph screen.
- **Fast circle drawing** — If you put a complex list, such as {*i*}, as the fourth argument of [Circle(](circle.html), the circle is displayed using its symmetries to only do 1/8 of the trigonometric calculations; this cuts the display time down to only about 30%. This is not available on the color calculators however.
**OS version 1.15 or higher:**
- **The [%](percent.html) Command** — The % symbol is an undocumented command that is a useful shortcut for percents — it divides by 100, so it will convert numbers to percentages. For example, 50% will become 50/100 or 1/2, which is just what 50% should be.
- **The [sub(](sub.html) Command** — If only one argument is given, and it contains an expression that evaluates to a real or complex number or list of numbers, the argument will be divided by 100. A simpler version of the % command above.
**TI-84+ and TI-84+ SE:**
- Using the [Text(](text.html) command for small text will sometimes erase the row of pixels below the text (usually not noticeable, when text is displayed on an already-white background). See the command itself for more information.

## Extra Characters

At three points in TI-83 series history, TI allowed more characters to be used in TI-Basic. However, this means that if you use a new character, it will not work on older calculator models.

- **First group:** This includes the lowercase letters, Greek letters, and international characters. These characters will work with all calculators starting with the TI-83+, but there may be some issues with computer programs such as the TI Program Editor.
- **Second group:** The ~ @  #  $  & `; \ | _ % characters were introduced only with OS version 1.15 (and will work on all higher versions).
- **Third group:** The … ∠ ß <sup>x</sup> <sub>T</sub> ← → ↑ ↓ x ∫ √ ![83lgfont/EFh_LUpBlk.gif](83lgfont/EFh_LUpBlk.gif "") ![83lgfont/F0h_LDnBlk.gif](83lgfont/F0h_LDnBlk.gif "") ![83lgfont/7Fh_LinvEQ.gif](83lgfont/7Fh_LinvEQ.gif "") characters and subscripts <sub>0</sub> through <sub>10</sub> were introduced only with OS version 1.16 (and will work on all higher versions).

## Calculator Memory & Speed

The TI-83 is the oldest TI-83 series calculator, and it only has 27KB of RAM and a 6MHz processor. A program cannot really even take up the whole 27KB of RAM, since there is the in-game use while running the program. In addition, the 6MHz processor is slower than any of the other calculator processors, so if a game is only marginally playable on the TI-83+SE (with its much speedier 15MHz processor), then there is no way it would even be playable on the TI-83.

This primarily affects large, complex games (like the RPG's made by Kevin Ouellet, among others), but can also affect games that need a lot of speed to be fun. For example, if you have a Mario-like game where you need to keep track of and display multiple enemies on the screen, this can be quite time-consuming on the TI-83. In fact, the game would probably slow to a crawl, and you would spend most of your time waiting for things to load.

This problem doesn't only plague the TI-83, but also the TI-83+. Because the TI-83+ only has 184KB of memory (24KB RAM and 160KB Flash), each of the aforementioned RPG's by Kevin Ouellet would literally take up all of the available memory on the calculator: Metroid II, for instance, takes up over 123KB in Flash, and you need to have several of the almost fifty programs unarchived in order to actually play the game.

The TI-83+ also only has an 8MHz processor (which is just marginally faster than the TI-83's 6MHz processor), while the TI-83+SE and TI-84+SE each have a 15MHz processor. So, if a game is specifically tailored to run on those two calculators (meaning that the speed of the game is just fast enough), there is no viable way that the TI-83+ would be able to run the game at a sufficient speed (even taking into account [optimization](optimize.html)).

## Thoughts to Consider

There are some additional ways that you can avoid portability problems:

- Use [SetUpEditor](setupeditor.html) instead of [UnArchive](unarchive.html) for a list — this is better, and doesn't lose compatibility with the TI-83.
- If possible, replace all lowercase letters from your program with lowercase stat variables from the VARS>Statistics... menu, or just use uppercase letters everywhere.
- Instead of using [dayOfWk(](dayofwk.html), use the [day of week](day-of-week.html) routine which uses the [dbd(](dbd.html) command instead.
- Place all of the calculator specific code into [subprograms](subprograms.html) that the main program calls: one program is your game functions that work on the respective calculators and the other program is the primary all-calculator code for the program.

<center>

|**[<< Planning Programs](plan.html)**|**[Overview](development.html)**|**[Usability >>](usability.html)**|
| --- | --- | --- |

</center>
