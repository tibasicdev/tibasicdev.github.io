# List & Matrix One Liners
This page is dedicated to showcase small snippets of code may be useful. These small routines are designed to accomplish tasks involving lists, matrices, and their attributes. Unless specified, output is in [`Ans`](ans.html).

**Index of Maximum List Element – [jonbush](http://www.wikidot.com/user:info/jonbush)**

This line finds the index of first occurrence of a specific value in a list.
The list to be searched is in `Ans` at the beginning.
```
:1+sum(not(cumSum(Ans=max(Ans
```
This can also be used to find the index of the minimum or of any other value in place of `max(Ans`

**Shuffle a list**

This routine is the fastest way to shuffle a list. `L₁` is the list to be shuffled and `L₂` is a temporary list used to do the shuffling. Make sure to clean up `L₂` after your program.

```
:rand(dim(L₁->L₂
:SortA(L₂,L₁
```

**Reverse a list – [Xeda Elnara](http://www.wikidot.com/user:info/Xeda Elnara)**

This routine is the smallest way to reverse a list. `L₁` is reversed without affecting `Ans`.

```
:dim(L₁
:seq(L₁(Ans-K),K,0,Ans-1
```

**Remove list element – [jonbush](http://www.wikidot.com/user:info/jonbush)**

This routine is the smallest way to remove a single element from a list. The position of the element to be removed from `L₁` is in `Ans`, and the result is a list with that element removed.

```
:seq(L₁(A+(A≥Ans)),A,1,dim(L₁)-1
```

**Enter List using Input - [Trenly](http://www.wikidot.com/user:info/Trenly)**

This routine is a way to allow a list to be entered using the [`Input`](input.html) command. The values to store in the list should be a comma separated string of numbers e.g "1,2,3"

```
:Input Str1
:expr("{"+Str1→L₁
```

**Partial Probability - [Timothy Foster](http://www.wikidot.com/user:info/Timothy Foster)**

This routine takes a single list in `Ans`, and randomly selects an element according to the bin sizes in the list. As an example, if the input is {4,11,2,3,0} there is a 4/20 chance that Bin 1 is chosen, an 11/20 chance for bin 2, 2/20 for bin 3, a 3/20 chance for bin 4, and a 0/20 chance for bin 5.

```
1+sum(cumSum(Ans)<randsum(Ans
```

**Shift a list - [imcoraline](http://www.wikidot.com/user:info/imcoraline)**

This routine takes a list in `Ans`, and moves all the elements one over, while looping it around itself. For example, if the input is {1,2,3,4,5,6}, the output will be {2,3,4,5,6,1}.

```
augment(ΔList(cumSum(Ans)),{Ans(1
```

**Simulate randIntNoRep( - [imcoraline](http://www.wikidot.com/user:info/imcoraline)**

This routine simulates the randIntNoRep( command using variables A and B. It simulates it with the syntax `randIntNoRep(A,B)`. It is not a perfect simulation, as the outputs will differ, but it does what the original command does. The output is in L₁. (“E” is the E command, not the variable.)

```
:A-1+cumSum(binomcdf(B-A,0→L₁
:fPart(E7√(Ans+.1+randInt(0,9999→L₂
:SortA(L₂,L₁
```

This can also be used as a larger but faster way to shuffle a list, with a bit of modification.
