# Code Timings
This page documents the speed of certain commands in 68k TI-Basic. Now, obviously, the times given here (in seconds) will vary from model to model and even from calculator to calculator (due to battery levels, free memory, and other factors). However, one thing that does not change is the relative speed of the commands. So if you come here to see if [If Then..Else..EndIf](68k:if.html) is faster than [when()](68k:when.html), the information will be useful on any calculator.

Elsewhere in this guide, you might see assertions like "foo() is faster than bar()" without any reason or proof. The information on this page is the reason and proof behind them. 



## Testing Format

For each test done on this page, a variation on the following function was used:
```
timetest(n)
:Func
:Local t,i
:startTmr()→t
:For i,1,n
	<command>
:EndFor
:approx(1000{checkTmr(t),1}/n)
:EndFunc
```

This function's input, n, is the number of times to loop over the command. The bigger this is, the more accurate the test; however, it will also take longer. 

The output of this function is a list such as {185 5}. The first of these is the time measurement: how many **milliseconds** the <command> being measured takes to work. The second of these is an error margin for this measurement. The error occurs because [startTmr()](68k:starttmr.html) and [checkTmr()](68k:checktmr.html) use whole numbers of seconds, so the actual time could be off by just under one second in either direction. In the tables below, such a result will be written as "185±5 milliseconds."

For commands that take a very short amount of time, this alternate form may be useful. It takes into account the time that the [68k:For](68k:for.html)..EndFor loop itself takes to run.
```
timetest(n)
:Func
:Local s,t,i
:startTmr()→s
:For i,1,n
:EndFor
:checkTmr(s)→s
:startTmr()→t
:For i,1,n
	<command>
:EndFor
:approx(1000{checkTmr(t)-s,2}/n)
:EndFunc
```

## Contributing your own Tests

Feel free to experiment with code timings, and to put your results up on this page. However, be sure to use the same format and method! Also, list the calculator model and the OS version (found in the F1, A:About... menu). Unless stated otherwise, all tests on this page were done with a Voyage 200 calculator and OS version 3.10.

That's it for details and explanations. Now come the actual timings!

## Loops and Conditionals

### If vs. When

The [when()](68k:when.html) command is often a simpler alternative to [If](68k:if.html)..Else..EndIf blocks, when only a single value needs to be stored. It is smaller; this test attempts to ascertain whether it is faster as well.

The when() code tested was
```
:when(condition,1,0)
```
The If code tested was
```
:If condition Then
:1
:Else
:0
:EndIf
```
Both tests were done with a true as well as a false condition.

| Code | Time (ms) |
| --- | --- |
| when(), true condition | 8.2±0.05 |
| when(), false condition | 8.15±0.05 |
| If..Else..EndIf, true condition | 8.5±0.05 |
| If..Else..EndIf, false condition | 8.65±0.05 |

**Conclusion:** The when() command wins, but not by a lot (though there is a difference that can't be explained by error alone). In addition, the true and false conditions' results are so close, they are probably equal.

## Variables

### expr() vs. #

Although the [68k:expr()](68k:expr.html) and # ([68k:indirection](68k:indirection.html)) commands do different things, they overlap considerably. If you have a string with a variable name inside, both # and expr() can be used to get you the value of that variable. (In case you're curious, the difference is that #, unlike expr(), can be used to refer to the variable itself, not just its value — but expr() can be used for the value of a whole expression stored to a string).

Both commands take 2 bytes when tokenized, so there's no difference in size. The question is — which is faster?

| Code | Time (ms) |
| --- | --- |
| # | 14.35±0.05 |
| expr() | 17.05±0.05 |

**Conclusion:** it's better to use # than expr() when you can.

### List vs. String vs. Matrix

This test attempts to compare the time it takes to access elements of lists, strings, and matrices. Before the test, all three variables were initialized to comparable values:
- The list was set to 2048 elements, all of them 0 (as an integer).
- The string was set to 2048 spaces.
- The matrix was set to 32 rows of 64 columns (a total of 2048 elements), all of them 0 (as an integer).

The elements in each case contain one byte of data. However, only the string stores them all with no padding and only a single header; as a result, the list and matrix variables are larger.

It's known that while strings are internally stored as an array, lists and matrices are stored as expressions in Reverse Polish Notation. As a result, it's expected that accessing any element of the string will take an equal amount of time; accessing an element of a list or matrix will take longer as the element gets further away from the beginning. Although this wasn't tested, the total size of the variable shouldn't change the access time significantly.

| ||~ List | ||~ String | ||~ Matrix |
| Code | Time (ms) | Code | Time (ms) | Code | Time (ms) |
| --- | --- | --- | --- | --- | --- |
| list[1] | 9.1±0.05 | mid(str,1,1) | 40.5±0.1 | mat[1,1] | 9.8±0.05 |
| list[500] | 36.8±0.2 | mid(str,500,1) | 41.8±0.1 | mat[1,64] | 13.35±0.05 |
| list[1000] | 64.5±0.5 | mid(str,1000,1) | 44.3±0.1 | mat[32,1] | 115±1 |
| list[2048] | 122±1 | mid(str,2048,1) | 49.6±0.1 | mat[32,64] | 118±1 |

**Conclusion:** Initially, of course, it's faster to access list or matrix elements than string characters. However, the cost rises fairly steeply: for around 600 elements, the string will win. Of course, for storing numerical data, the list will have an additional advantage, but in the long run (say, for 800-1000 elements, depending on the method), the string will be better even for that. You might also consider using several small lists rather than one large one if it's possible.

As for the matrix, it's clear that the time cost increases much more quickly going down a column, than across a row. This may be a factor in how you choose to orient your data when it doesn't really matter. You probably won't improve the total time, but the proper orientation will make sure that the time doesn't vary dramatically.

<center>

|**[<< Optimization](68k:optimization.html)**|**[Overview](68k:development-overview.html)**|**[Releasing Programs >>](68k:releasing-your-program.html)**|
| --- | --- | --- |

</center>
