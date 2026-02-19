# Optimization
A dictionary would define *optimization* as the process of making something better. In the field of TI calculator programming, it refers to improving code to use less memory, whether as program size or in the size of variables used, or to run faster. It should be your goal, in virtually all cases, to make your programs as optimized as possible.

## Line-by-Line Optimization

Optimization techniques fall naturally into two classes. The first, which we'll call "line-by-line optimization", refers to ways of rewriting a line of code, or several lines, so that it does basically the same thing, but is smaller or faster. Typically, each such optimization doesn't have a huge effect. But since many lines can be improved this way, these optimizations add up over the entire program to produce a smaller and faster result.

Note that when optimizing for size, the size in question is the [tokenized](68k:tokenization.html) size of the program. For example, typing out [getKey()](68k:getkey.html) takes 8 characters, so initially when you type it in, the program's size will increase by 8 bytes. However, after the first time you run it, the program will be tokenized and getKey() will be replaced by a 3-byte code. It is this encoded size of the program that's worth improving.

Here are some common techniques of line-by-line optimization:

- [Commenting your code](68k:comments.html) is an efficient tool when writing the program, but the comments should be removed in the finished version (you might consider making two versions — one with comments, and a smaller one without).
- Similarly, [68k:variable names](68k:variable-names.html) in the final version should be kept as short as possible — each additional letter costs a byte each time it's used. Single-letter variables are an even better improvement, saving 3 bytes over two-letter variables.
- Avoid typing out constants you can replace by single-character variables: x^2, for example, should be rewritten as x*x.
- Fractions are better than their floating-point versions: write 1/2, for example, instead of 0.5.
- It's usually better to replace simple [If](68k:if.html) statements by their [when()](68k:when.html) equivalents.
- Avoid using strings to store code to be retrieved with [expr()](68k:expr.html). Local functions are usually better for the purpose.
- For complicated repeated chunks in the same line, use the | ([68k:with](68k:with.html)) operator to only calculate it once.

There are also pages devoted to specific types of optimizations:
- [68k:List Optimization](68k:list-optimization.html)
- ...hopefully some more will be added.

Finally, since there is no way to include every optimization on this page, consider looking up the commands you use most often. Their pages might list further optimizations.

## Algorithmic Optimization

An algorithm refers to your method of solving a problem. Algorithmic optimization, then, relies on choosing the best method to solve a particular problem. Unlike line-by-line optimization, even a single optimization of this type can have drastic results — but it also requires critical thinking and a case-by-case approach. 

Most programmers, after thinking about the methods they will use for a while, never spend much time on this kind of optimization. It becomes important when you're pushed in a corner: your program has become so large that it doesn't have enough memory to run, or takes half a minute to load each screen.

Identify the bottleneck in your program — what is it that takes up all the memory, or that the program spends so much time doing? Then consider several fundamentally different approaches to solving that particular problem (be it the problem of storing a large matrix or of displaying a tilemap). Write routines implementing each approach, fully optimize all of them, and compare the results. And make sure that you're not missing an approach too radical to think of. Virtually all of the techniques you find in this guide have been discovered by frustrated programmers doing exactly this kind of thinking.

<center>

|**[<< Usability](68k:usability.html)**|**[Overview](68k:development-overview.html)**|**[Code Timings >>](68k:timings.html)**|
| --- | --- | --- |

</center>
