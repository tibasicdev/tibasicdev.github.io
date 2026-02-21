![The getConfg() Command](68k_getconfg/getconfg.png "The getConfg() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns a list of calculator configuration info.|getConfg()|This command works on all calculators.|3 bytes|
       
### Menu Location
N/A

       
# The getConfg() Command

The getConfg() command returns a list of useful and not-so-useful information about the calculator. Every other entry in the list is a description of the next entry, so it's not too hard to figure out which entry you need if necessary.

The values returned by getConfg() are:

| List position | Value | List position | Value |
| --- | --- | --- | --- |
| 1 | "Product Name" | 2 | "Advanced Mathematics Software" |
| 3 | "OS Version" | 4 | "*version #*, *date*" |
| 5 | "Product ID" | 6 | *string unique to calculator model* |
| 7 | "ID #" | 8 | *string unique to specific calculator* |
| 9 | "Screen Width" | 10 | 160 or 240 |
| 11 | "Screen Height" | 12 | 100 or 128 |
| 13 | "Window Width" | 14 | varies (see Note 1.) |
| 15 | "Window Height" | 16 | varies (see Note 1.) |
| 17 | "RAM Size" | 18 | depends on model |
| 19 | "Free RAM" | 20 | varies (see Note 2.) |
| 21 | "Archive Size" | 22 | depends on model |
| 23 | "Free Archive" | 24 | varies |

Notes:
1. The window width and window height depend on calculator model and on the split screen setting. They're also off by varying amounts. It's best to use one of the other settings to determine calculator type (widescreen or standard), and [68k:getMode()](68k:getmode.html) to determine split screen status if necessary.
2. Even with all variables deleted, Free RAM will be considerably less than RAM Size, due to operating system variables taking up that much of it.

There are several interesting applications for getConfg(). One is [compatibility](68k:cross-compatibility.html) with other calculator models:
- If you want to make graphics compatible, use Screen Width or Screen Height to check if you're on a widescreen calculator.
- If you want to use an advanced OS feature, check the OS Version.
- If you use lots of features of your calculator model and think it won't work on any other, check Product ID and exit if it doesn't match your own.

Another application: if your program is very memory-intensive, you might want to make sure that there is enough free RAM to fit all the variables you will need. The same is, in theory, true for the archive, but having little archive memory available is rare.

Using the ID #, you might detect when the program has been transferred to a different calculator, and react accordingly (e.g. re-initialize certain variables). A more subtle application: supplying a number calculated from the ID # as the [random number seed](68k:randseed.html) will ensure that your program always behaves in the same way for the same calculator, but will be different on different calculators — this might be completely inappropriate in some cases, but an interesting gimmick in others!

## Related Commands

- [68k:getMode()](68k:getmode.html)
- [68k:getUnits()](68k:getunits.html)

## See Also

- [68k:cross-compatibility](68k:cross-compatibility.html)
