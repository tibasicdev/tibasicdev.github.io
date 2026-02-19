# List Optimization
Any more-or-less complicated program will probably end up using a list at some point: they are the easiest way to organize a set of similar information. This article's purpose is to teach you to do so intelligently: list operations can be slow, and it's not always intuitive what the better approach even is.

The general idea of list optimization is that performing an operation on an entire list at once is good. Suppose that 'list' is a list variable containing a hundred elements. Consider this simple operation:
```
:list+1→list
```
With one line of code, this performs a mathematical operation on one hundred numbers at once. The size of the program goes way down if you can do something like this. It's fast, too: we've delegated going through the list to some internal calculator routine, which can do it much faster than a TI-Basic command.

The following sections are, in a sense, merely examples of situations in which this logic leads to a dramatic improvement in speed. Reading these and understanding not only what the optimizations are but how they work should give you an intuitive idea of what's slow and what's fast when working with lists.

## Avoid [68k:For](68k:for.html) Loops

Specifically, avoid using For loops to go through every element of a list, whenever possible. The operation list[index] takes an increasing amount of time to run as the index increases, because the calculator is forced to go through the whole list to get to the element you want. If you have just one list[index] inside the For loop, you're going through half the list, on average, in each cycle of the loop. And you're probably doing an operation that would only require going through the list once!

As an example, consider this rather intuitive routine for checking if a list contains an element:
```
:check1(list,val)
:Func
:Local i
:For i,1,dim(list)
: If list[i]=val
:  Return true
:EndFor
:Return false
:EndFor
```
The For loop in this routine is exactly the sort of thing you should avoid whenever possible. Instead, consider this routine:
```
:check2(list,val)
:product(list-val)=0
```
This routine approaches the problem in a very non-intuitive way: first, the value we're looking for is subtracted from each element; then, the elements are all multiplied together. If the value we're looking for was present in the list, then one of the elements in the product will be 0, making the whole expression 0.

The first thing you'll notice is that the second routine is much smaller. But, perhaps not quite so obviously, it's a great deal faster as well. Even for a list with 10 elements, the second routine is, on average, 3 times faster to finish running. For a list of 100 elements, the second routine is a whopping 12 times faster! In addition, the second routine is consistent. The first routine varies from very quick (if the element is the first in the list) to very slow (if the element is not in the list at all). The second routine takes the same amount of time in all cases.

Similar results hold true for every For loop that goes through a list. Although the optimization doesn't always end up being smaller, it's always faster, especially for large lists.

## Use [68k:newList()](68k:newlist().html) instead of [68k:seq()](68k:seq().html)

This seems like a nonsensical suggestion because newList() and seq() are very different commands. About the only thing they have in common is that they both return a list. How can one replace the other?

Half of the answer here is that one particular instance of seq() can be rewritten using newList() for a massive speed boost. The optimization is this:
```
:seq(i,i,1,n)

can be

:cumSum(1+newList(n))
```
The first line of code uses seq() to generate the list {1, 2, 3, ..., n}. The second does the same thing differently: newList(n) gives us {0, 0, ..., 0}. Adding 1 to this list gives {1, 1, ..., 1}. Finally, taking the cumulative sum results in {1, 2, 3, ..., n}. 

The second part of the answer is that 90% of the time, any other use of seq() can be reduced to this one, because of the way most operations distribute over lists. Consider this contrived, convoluted example:
```
:seq(tan(√(100-x^2)),x,1,10)

can be

:tan(√(100-seq(x,x,1,10)^2))
```
This is a good idea to do in any case, because applying an operation to an entire list at once is faster than doing it to an element many times. However, in this case, it also means that the newList() optimization above can be used here as well:
```
:tan(√(100-seq(x,x,1,10)^2))

can be

:tan(√(100-cumSum(1+newList(10))^2))
```
In some case, you might have to tweak the limits of the evaluation a bit. If the seq() starts at 0, not 1, for instance, you might subtract 1 from the cumSum(1+newList(n)) result.

Using the | ([68k:with](68k:with.html)) operator, it's possible to make this optimization into a truly brainless process:
```
:seq(<FOO>,x,1,n)

can be

:f(cumSum(1+newList(n)))|f(x)=<FOO>
```
If the optimization is possible at all, this setup will do the trick. Here are some reasons it might not work:
- Some operation in <FOO> doesn't distribute. E.g. if <FOO> is isPrime(x), you'll get a domain error.
- Part of <FOO> is random. In this case, seq() will generate n random numbers, but newList() will only generate one.

The reason that this optimization works can be explained with a "factory line" metaphor. The seq() command treats each case individually: like assembling 100 cars by first making the first one, then the second one, and so on. The newList() version applies each command to an entire list at once: this is the Industrial Revolution, where we assemble 100 cars by first making 100 hulls, then adding 100 motors, 100 doors, and so on.

A final, minor note: if you're trying to make a sequence of the same length as an existing list, then 0*list is faster than newList(dim(list)).

## Working with Logical Lists

A list of logical values such as {true, false, true, true, false} is a strange animal. First of all, it's not always easy to get one when you need it. Say you want to know which elements of a list are over 100. Unfortunately, this code does not work:
```
:list>100→ispos
```
Instead, you'll get the laconic answer "false". This probably translates to "You dummy, that thing there on the left is a list, and the one on the right is a number. It's like comparing apples and oranges!" Unlike virtually every other operation there is, the relational operators  [=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), and [≤](68k:less-than-or-equal.html) don't distribute over lists.

The trick here is to change the comparison to one that involves two lists. To do this, add 0*list to one side.
```
:list>100+0*list→ispos
```
Now, we're comparing two lists, so things start to make sense again.

We're not out of the woods yet, however. Once you have a logical list, what do you do with it? There are three common situations:
- We want to know if all of the elements are true.
- We want to know if *any* of the elements are true.
- We want to find the index of the first true element.

The first situation is actually default behavior, of sorts. You can stick a logical list in a condition for [68k:If](68k:if.html) or [68k:when()](68k:when().html). If all of the elements of the list are true, the condition will be interpreted as true. Otherwise, the 'false' branch (if there is one) will be taken. For instance:
```
:If list>100+0*list Then
: Disp "Everything is over 100!"
:Else
: Disp "Some elements are 100 or under..."
:EndIf
```

The second situation boils down to the first with a little trick, which is to *negate* the list (using [68k:not](68k:not.html), or simply reversing the condition). Then use an If or when(), but reversing the two branches. If the true branch is taken, that means that all of the negated elements are true, so all of the original elements were false. If the false branch is taken, that means some of the negated elements are false, so at least one of the original elements must have been true.

If you want to get a single truth value ahead of time, use the when() command as follows:
```
:Define alltrue(list)=when(list,true,false)
:Define anytrue(list)=when(not list,false,true)
```

The third situation is the trickiest one. From two sections up, we know using a For loop (which would be simple to write) is a no-no. Here is a decent alternative... to be honest, though, it's not that great either, being really ugly. The search for a better one is still on!

```
:Define first(list)=intDiv(k+inString(string(list),string(true)),k+1)|k=dim(string(false))
```

...Yes, this routine turns the entire list to a string, searches it for the word "true", then uses this to find the answer. You might replace k and k+1 by 5 and 6 respectively if you're not worried about language localization (the Spanish would be alright, but not the Germans with "falsch" nor the French with "faux").
