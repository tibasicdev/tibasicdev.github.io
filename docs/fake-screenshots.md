# Faking Screenshots
Screenshots are one of the best ways to advertise your program at any stage of production. And as we all know, advertising lies. I mean, whoever said "Honesty is the best policy" obviously either wasn't referring to screenshots or didn't release many popular programs. After all, popularity is measured in how many people download your program, not how many aren't horribly disappointed afterwards!

On a more serious note, while faking screenshots to a submitted program is a BAD idea (on the off chance the archiver won't catch it, the first person to try the program will, and it will get taken down faster than you can say "LinRegTTest"), there are sometimes good reasons to fake a screenshot. For example, if you haven't finished your program yet, but want to hide the fact that you're desperately fixing that final bug. Or perhaps you're in an inconvenient situation in which you can't download screenshotting software, or you can't send the program you want screenshots of to your computer. 

Alternatively, you can look at this article as a guide to catching fake screenshots by people that haven't read this guide. Odds are they've made a mistake, then.

## The Basics

If the entire image is using the large 5x7 font in a home screen-like setting, your job is easy. Use a calculator or emulator to make a program that outputs the same thing to the screen using a single [Output(](output.html) command. Then, either take a screenshot of that (if you can), or at least use it as a reference.

Start with a 96 by 64 blank image in your favorite image editor (something as simple as Paint will do). If you can make any sort of reference image on a calculator or emulator that shows at least part of what you want, do it and it will make your job easier. Otherwise, you'll have to work from scratch. A useful reference, however, would be a table of all the characters, either in the [large 5x7 pixel font](83lgfont.html), or the [small variable-width font](83smfont.html) (whichever it is you're using). After drawing the image, you can stretch it to twice the size, but it's probably easier to draw it in a 1:1 ratio.

When you're done making the image, take a critical look at it from the point of view of a suspicious calculator programmer. Where would you look to find a flaw in the screenshot? You might want to start with the...

## Common Mistakes

- TI-Basic programs cannot access the bottom row and (usually) the rightmost column, so you had better leave those blank. Also, unless you're claiming to turn off the run indicator, you should put one in too.
- A glaring flaw is a character in the calculator font that isn't drawn correctly. Spacing is important here too. **All** characters in the 5x7 font are 5x7 pixels, with an extra 1-pixel gap. In the small font, characters are normally 1 pixel apart, but it's 2 pixels if there's a space.
- Make sure to look up the commands you're purportedly using in the program. If an [Output(](output.html) is the last line of the program, don't you dare add a "Done" to your screenshot. If you're showing the output of a [regression](regression-models.html), make sure the variables that get displayed are in the right order.
- The [Line(](line.html) command in TI-Basic draws a slightly different diagonal line than Paint. A few pixels here or there may be different due to round-off. This will probably not get you caught, but if possible, draw a real Line( in an emulator or on the calculator, and use it for reference.

## Finishing Touches

Finallly, you might try to add the effect of the screenshot having been taken in an actual emulator. For example, Pindur-TI uses a distinctive pattern for its dark pixels when using a 2:1 ratio — 1 dark pixel and three light pixels (try taking an actual screenshot — of anything — for reference). Of course, Pindur-TI's run indicator will have gray levels, so don't mess those up either. Or, you can go for the CalcCapture look and add a 1-pixel white border and 1-pixel black border to the outside.

## Easier than Fake

...is real. Seriously, if you can possibly take a real screenshot in an emulator, do it! It will be much less work than a fake screenshot (believe me, I've taken over a hundred screenshots for TI-Basic Developer so far).

## A Grain of Salt

Take this article with one.
