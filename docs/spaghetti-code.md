# Spaghetti Code
Spaghetti code is the unofficial name given to code that heavily relies on [Goto/Lbl](goto.html) for its structure and organization. Where the spaghetti name comes from is that the code becomes difficult to read and understand, similar to how it is difficult to untangle a spaghetti noodle from among the other noodles.

While there is nothing wrong with using Goto/Lbl when there are no other viable options available (such as when you need to exit a program), most situations can be dealt with using a combination of [loops](while.html) and/or [conditionals](if.html).

For example, say you want to have the user type in a number from 1 to 100. You can use the [Input](input.html) command for the input, and then use a Goto together with a conditional to check for whether the number is in the appropriate range:

```
:Lbl A
:Input "Number? ",A
:If A<1 or A>E2
:Goto A
```

This is just a simple example, but you can probably see that there is no reason to use a Goto here. It is functioning as a loop, which is a good indicator that you should use a real loop instead. In this case, the most appropriate loop to use would be [Repeat](repeat.html) since it always loops at least once.

```
:Repeat A≥1 and A≤E2
:Input "Number? ",A
:End
```

Besides making code hard to read and understand, spaghetti code also has some other disadvantages associated with it:

- **Slower Speed** — When the calculator reaches a Goto command, it stores the label name in memory, and then searches from the beginning of the program for the Lbl command with the supplied name. This obviously can be very slow if the program is rather large and the label is deep within the program.
- **Memory Leaks** — Using spaghetti code has the tendency to lead to [memory leaks](memory-leaks.html), where you use a Goto to jump out of an conditional or loop (anything that has an [End](end.html) command). Memory leaks will not only slow a program down, but also cause it to crash (given enough time).
