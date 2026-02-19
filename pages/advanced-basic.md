# Advanced Basic
![advancedbasic.gif](advancedbasic.gif "") is a term that is loosely thrown around in the TI-Basic community on forums, sites, and even in tutorials/guides, but what does it really mean? The term advanced basic was first used by [SiCoDe Software](ti:sicode.html) when they were active from 1998-2001, and they used it to describe quality TI-Basic programming that is not only efficient in terms of size and speed, but is used to make genuinely fun games.

![war-screenshot.gif](war-screenshot.gif "")

At that time, SiCoDe was the premier TI-Basic programming group, releasing high-quality games such as Nibbles Arcade, War, Orion, and Connect 4. If you actually try out any of their games, you will probably find that they are in fact fun games, but they aren't considerably optimized by today's standards. That optimization level is actually reflective of the majority of the TI-Basic games released during that time period.

While it is somewhat ironic that SiCoDe referred to their games as advanced basic even though they weren't optimized particularly well, the primary reason for the poor quality of optimization is that TI-Basic knowledge was in its infancy at that time. Since then, the TI-Basic community has really matured in terms of understanding the TI-Basic language (including [optimization](optimization.html), [development](development.html), and [techniques](techniques.html)) and the internals of the TI graphing calculators, and the quality of TI-Basic games has increased accordingly.

### Hype vs. Substance

As a result of this increase in TI-Basic knowledge, the primary issue you see today with people referring to their games as utilizing advanced basic is that a lot of it is really just hype. The optimizations and techniques that were once considered advanced basic are now just part of the standard collection of basic optimizations and techniques that everyone uses.

For example, when comparing a value to multiple variables, here is how it is done today:

```
:If min(5={A,B,C
```

While this is how it used to be done:

```
:If 5=A and 5=B and 5=C
```

This change is ultimately inevitable because the TI-Basic community constantly changes, and the future TI-Basic community will probably have the same kind of progression over the current TI-Basic community's knowledge of TI-Basic. As a result, calling something advanced basic is really pretty pointless, so I think we should stop using the term, and simply *let our games and programs speak for themselves*.
