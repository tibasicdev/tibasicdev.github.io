# First Non-Zero Element
|Routine Summary|Inputs|Outputs|Variables Used|
|--- |--- |--- |--- |
|Looks through a list to find the first non-zero element.|*list* - The list or list variable to look through.|The index of the first non-zero element in the list.<br><br>If all the elements are zero, the result is one greater than the size of the list.|None erased.|

```
:firstnz(list)
:1+sum(floor(1/(1+cumSum(abs(list))))
```

This function finds the first non-zero element in a list, and returns its index.

The innermost part of the formula makes the list easier to deal with: [68k:abs()](68k:abs.html) makes all non-zero elements positive, then [68k:cumSum()](68k:cumsum.html) ensures that after the first non-zero element, every next element in the result is also non-zero. After this, the list begins with some number of zeroes (possibly none at all), then only positive numbers. Now, to find the index of the first non-zero element, we must find the number of zero elements, and add 1.

The function [68k:floor(](68k:floor.html)1/(1+x)) sends 0 to 1/(1+0)=1, and every positive number to 0. After we apply it to the result above, all the zeroes are replaced by 1, and all the other numbers by 0. Then, [68k:sum()](68k:sum.html) adds all the 1s, counting the number of elements that used to be 0. Adding 1 to the result gets the index of the element one past all the zeroes, which is the result we want.

This explanation still doesn't answer the real question: why such a bizarre approach when a more simple one is possible — going through the list in a [68k:For](68k:for.html)..EndFor loop, and checking if each element is 0 until you get to one that's not? The answer is that accessing list elements one by one is very slow: to get to a middle element of a list, the calculator must go through all the elements before it. This means that when you access a list's elements in a For loop, you're going through the entire beginning of the list each time the loop cycles. 

To avoid this, we use commands that deal with all the elements of a list at once. Because their code is written in the calculator's own assembly language, it doesn't have to go through this rigmarole to access a list. As a result, the strange-looking routine is faster, and its advantage becomes greater and greater with long lists. 

## Error Conditions
