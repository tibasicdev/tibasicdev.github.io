![The Goto Command](68k_goto/goto.png "The Goto Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Jumps to a label somewhere else in the program.|:Goto *label-name*|This command works on all calculators.|2 bytes|
       
### Menu Location
N/A

# The Goto Command

The Goto command jumps to a label (declared with the [68k:Lbl](68k:lbl.html) command) somewhere else in the program — either before or after the Goto, it doesn't matter. The label has to be in the same program as the Goto — you can't jump into another program. If there are several labels with the same name, the Goto command will only find the first.

Virtually everyone critiques the Goto command for being unnecessary and encouraging bad coding habits. The argument is that it makes code hard to read: if you see a 'Goto x' somewhere in the program, you have to search through the entire program to find out where to continue reading. And most of the things that Goto is used for can be done better using commands like [68k:If](68k:if.html), [68k:While](68k:while.html), [68k:Cycle](68k:cycle.html), etc. TI seems to agree, because they didn't even bother putting Goto and Lbl in the program editor toolbar.

That being said, it is sometimes (very rarely) a good idea to use Goto. A good example is a situation when you need to exit several loops at once (this can't be done with the [68k:Exit](68k:exit.html) command, which only exits one loop).

A note for TI-83 series programmers: the issue of memory leaks from improper use of the Goto command does not occur on 68k calculators. The 68k TI-Basic parser doesn't use a stack to keep track of loops and If blocks entered: instead, End statements have a link back to what it is they're matching. This means that nothing special happens if a Goto jumps out of a loop: the calculator doesn't even *know* it's inside a loop except at the end when it has to do the looping. 

The 68k calculators have their own bit of unexpected Goto behavior: code like [68k:expr(](68k:expr.html)"Goto x") will not work. This is because the code that [68k:expr(](68k:expr.html) runs is treated as though it were inside its own program, so you can't jump out of that program into the program that it's actually in.

## Optimization

The [68k:Cycle](68k:cycle.html) and [68k:Exit](68k:exit.html) commands perform tasks that you might otherwise use Goto for. By all means, use these command instead if you can: they work much faster, since they don't have to look through the entire program for the label (in fact, they don't have to look at all — they already know where to jump).

## Error Conditions



## Related Commands

- [68k:Cycle](68k:cycle.html)
- [68k:Exit](68k:exit.html)
- [68k:Lbl](68k:lbl.html)
