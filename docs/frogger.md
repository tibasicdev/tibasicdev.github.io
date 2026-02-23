# Frogger
![Frogger](frogger/frogger.gif style="width:200px; height:135px;" "Frogger")

|Program Summary|Program Size|Uses Libraries?|Calculator Compatibility|Author|Download|
| --- | --- | --- | --- | --- | --- |
|A quality version of the classic frogger game.|1,232 bytes|No, it's pure TI-Basic|TI-83/84/+/SE|[SiCoDe](http://sicode.ticalc.org) (Douglas O'Brien)|[frogger.zip](http://tibasicdev.github.io/local--files/frogger/frogger.zip)|

Frogger's claim to fame is that it was the very first game to utilize the home screen [scrolling](movement.html) made possible by using the [Output(](output.html) command together with a [string](strings.html). The Output( command has wordwrapping functionality built-in, in which any text that goes over the 16 characters of a row will be wrapped to the next row (and likewise with that row), and subsequently you can use a single Output( command to display an entire screen of text.

This functionality not only allows the text to be displayed very quickly — in fact, there is no faster way to display text in TI-Basic — but also very efficiently. What people were doing previously was actually just using several Output( commands, and then displaying each row of the screen separately. Obviously, this approach does not lend itself to making fast games, and so most games were rather slow.

The basic idea behind Frogger is that you control a frog that you can move in the four directions, and you want to get to the other side of the road as quickly as possible. This is made more difficult because you have to avoid getting hit by the moving cars that are coming at you. You are given points based on how many times you make it across the road, as well as how fast you do it.
