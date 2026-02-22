# Lists and Their Commands
A list is a collection of elements in order. On the TI-68k calculators, lists can contain any mix of any variable type that's valid in an expression: you can have lists of numbers, lists of strings, lists of truth values or expressions. You can even mix and match variable types — it's perfectly all right to have a string in one element, and a number in the next. The only special case is lists of lists: these are kind of allowed, but they're called [matrices](68k:matrices.html), and have some further restrictions.

Lists are written using curly brackets { and } around the elements, separated by commas. For example, {1,2,3,4,5} is a list containing the numbers 1 through 5 in that order. You can access a certain element of the list by writing the number of the element you want in [ ] brackets after it: listvar[5] would select the 5th element of listvar. Elements are numbered starting with 1.

On earlier calculator models, lists had the [random access](https://en.wikipedia.org/wiki/random_access) property: accessing any element of a list took the same amount of time. This was possible because the lists were restricted to numbers. On the 68k calculators, since lists can mix element types, they are no longer random access: the calculator has to go through the entire list to get to an element, so the larger an index is, the longer it takes to access. This isn't significant for short lists. But taking the 100th element, for example, takes approximately twice as long as taking the 1st element, and the time keeps increasing linearly, so it can be very slow to access the last elements of a long list.

Except for the constraint of free memory, and of the time it takes to access elements, there is no limit on the number of elements a list may have.

## Operations on Lists

Many commands, including [math](68k:math.html) commands and others, can be extended to lists by applying them to each element of the list. An example is [sin()](68k:sin.html):
```
sin({1,2,3})
	{sin(1) sin(2) sin(3)}
```
If a command has more than one argument, there are two ways to extend it to apply to lists. One is to use it with a list and a regular argument: then the command will be applied to each element of the list paired up with the regular argument. Here is this way illustrated with [mod()](68k:mod.html)
```
mod({10,20,30},7)
	{3 6 2}
```
The other way is to make both arguments lists. In that case, the lists must be the same size, and each element of the first list will be paired with the corresponding element of the second. For example:
```
mod({10,20,30},{7,8,9})
	{3 4 3}
```
Although in these examples, mod() could be extended in both ways, sometimes only one is possible. [PtOn](68k:pton.html), for example, (as well as other point commands) can be used with two numbers, or two lists, but not with a list and a number. [round()](68k:round.html), on the other hand, can be used with two numbers, or a list and a number, but will give a meaningless expression when applied to two lists.

A noteworthy special case is the basic math operators ([+](68k:add.html), [-](68k:subtract.html), [*](68k:multiply.html), [/](68k:divide.html), [‾](68k:negative.html), and [^](68k:power.html)), which can all be used with lists (in both ways).

## List-Specific Commands

Of course, there are commands specifically designed for use with lists. Several of these, such as [dim()](68k:dim.html) or [rotate()](68k:rotate.html), can be also used with strings. Many of these commands are found in the list menu (Press 2nd MATH to access the popup math menu, then select 3:List).


- [augment()](68k:augment.html)
- [crossP()](68k:crossp.html)
- [cumSum()](68k:cumsum.html)
- [dim()](68k:dim.html)
- [dotP()](68k:dotp.html)
- [exp▶list()](68k:exp-list.html)
- [Fill](68k:fill.html)
- [left()](68k:left.html)


- [Δlist()](68k:deltalist.html)
- [list▶mat()](68k:list-mat.html)
- [mat▶list()](68k:mat-list.html)
- [max()](68k:max.html)
- [mid()](68k:mid.html)
- [min()](68k:min.html)
- [newList()](68k:newlist.html)
- [polyEval()](68k:polyeval.html)


- [product()](68k:product.html)
- [right()](68k:right.html)
- [rotate()](68k:rotate.html)
- [seq()](68k:seq.html)
- [shift()](68k:shift.html)
- [SortA](68k:sorta.html)
- [SortD](68k:sortd.html)
- [sum()](68k:sum.html)


Several [statistics](68k:statistics.html) commands can be applied to lists as well.

## Conditionals With Lists

Conditional statements, like [If](68k:if.html), [when()](68k:when.html), and [While](68k:while.html), accept lists of truth values as well as single truth values. The check will be interpreted as true if and only if every element of the list is true, effectively combining each element of the list with [and](68k:and.html).

The most common way for lists of truth values to be created is with relational operators ([=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), [≤](68k:less-than-or-equal.html)) applied to lists. They will return the single value ' false' unless both sides of the relation are lists of equal size, in which case the lists will be compared element by element, returning a list.
