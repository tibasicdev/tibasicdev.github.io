# War
![War](war/war.gif style="width:200px; height:135px;" "War")

|Program Summary|Program Size|Uses Libraries?|Calculator Compatibility|Author|Download|
| --- | --- | --- | --- | --- | --- |
|Try to hit the enemy base while avoiding the missiles flying at you.|2,000 bytes|No, it's pure TI-Basic|TI-83/84/+/SE|[SiCoDe](http://sicode.ticalc.org) (Douglas O'Brien)|[war.zip](http://tibasicdev.github.io/local--files/war/war.zip)|

War's claim to fame is that it was one of the very first games to utilize the home screen [scrolling](movement.html) made possible by the [Output(](output.html) command. The Output( command has wordwrapping functionality built-in, in which any text that goes over the 16 characters of a row will be wrapped to the next row (and likewise with that row), and subsequently you can use a single Output( command to display an entire screen of text.

This functionality not only allows the text to be displayed very quickly — in fact, there is no faster way to display text in TI-Basic — but also very efficiently. What people were doing previously was actually just using several Output( commands, and then displaying each row of the screen separately. Obviously, this approach does not lend itself to making fast games, and so most games were rather slow.

The basic idea behind War is that you control a ship that you can move up or down, and you are flying over an enemy base that you must drop bombs on. This is made more difficult because you also have to avoid getting hit by the missiles that are flying at you, while at the same time you need to time the bomb drops so that you actually hit the enemy base. You are given points based on which type of enemy base you hit, and you must get a certain amount of points within the allotted time.
