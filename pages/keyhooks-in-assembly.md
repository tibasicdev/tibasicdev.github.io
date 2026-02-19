# Keyhooks in Assembly
## Keyhooks in Assembly

First of all, it's important to know that Texas Instruments does not support keyhooks. Secondly, notice that this is an advanced topic; you can of course read this, but in order to let it prove useful to you, it is best if you understand Assembly quite well or are at least knowledgeable with its terms.
With that said, let's dive into it!
Every piece of keyhooking code begins with this
```
add a, e             ;This byte is not being run but it ensures that the pointer is valid in order to prevent
                     ;it from randomly executing some code.
```
Hooks are controlled by flags, which are located in IY+33 and in IY+36, and both of them have a RAM area consisting of four bytes. Each of those RAM areas contains the "little endian" (process the low bits first and then the high bits) pointer to the hook, then a page number, and last but not least, a byte that can be used as safe RAM for that hook.
An example of a hook is the GetKeyHook; this hook is enabled using
```
b_call $4F7B
```
and disabled using
```
b_call $4F7E
```
more information on Keyhooks can be found [here](http://www.detachedsolutions.com/forum/index.php?t-msg-th-1319)
