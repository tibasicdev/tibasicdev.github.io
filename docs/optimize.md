# Optimization
|**This article is part of the revising stage of the [development](development.html) cycle.**|
| --- |

A dictionary would define *optimization* as the process of making something better. In the field of TI calculator programming, it refers to improving code to use less memory, whether as program size or in the size of variables used, or to run faster. It should be your goal, in virtually all cases, to make your programs as optimized as possible.

## Line-by-Line Optimization

Optimization techniques fall naturally into two classes. The first, which we'll call "line-by-line optimization", refers to ways of rewriting a line of code, or several lines, so that it does basically the same thing, but is smaller or faster. Typically, each such optimization doesn't have a huge effect. But since many lines can be improved this way, these optimizations add up over the entire program to produce a smaller and faster result.

Read the [basic techniques](optimize-general.html) of line-by-line optimization. Then, consult the following pages to see techniques for specific topics:


- [Displaying Text](optimize-text.html)
- [Storing Variables](optimize-variables.html)
- [Deleting Variables](optimize-deleting.html)
- [User Input](optimize-input.html)


- [Exiting Programs](optimize-exiting.html)
- [Logic Operations](optimize-logic.html)
- [Conditionals](optimize-conditions.html)
- [Loops & Branching](optimize-loops.html)


- [Math Operations](optimize-math.html)
- [Using the Ans variable](optimize-ans.html)
- [The Graph Screen](optimize-graph.html)
- [Using Finance Variables](optimize-finance.html)


Alternatively, you can read the [optimization walkthrough](optimization-walkthrough.html) for a look at applying the optimizations in a real program.

## Algorithmic Optimization

An algorithm refers to your method of solving a problem. Algorithmic optimization, then, relies on choosing the best method to solve a particular problem. Unlike line-by-line optimization, even a single optimization of this type can have drastic results — but it also requires critical thinking and a case-by-case approach. 

Most programmers, after thinking about the methods they will use for a while, never spend much time on this kind of optimization. It becomes important when you're pushed in a corner: your program has become so large that it doesn't have enough memory to run, or takes half a minute to load each screen.

Identify the bottleneck in your program — what is it that takes up all the memory, or that the program spends so much time doing? Then consider several fundamentally different approaches to solving that particular problem (be it the problem of storing a large matrix or of displaying a tilemap). Write routines implementing each approach, fully optimize all of them, and compare the results. And make sure that you're not missing an approach too radical to think of. Virtually all of the techniques you find in this guide have been discovered by frustrated programmers doing exactly this kind of thinking.

Read the [algorithmic optimization](algorithmic-optimization.html) tutorial for a demonstration of the process of algorithmic optimization in a real programming situation.

<center>

|**[<< Debugging](debug.html)**|**[Overview](development.html)**|**[Code Timings >>](timings.html)**|
| --- | --- | --- |

</center>
