# Number Or List
|Routine Summary|Inputs|Outputs|Author|
|--- |--- |--- |--- |
|Determines whether an input is a number or list.|*Ans* - the number or list to examine|*Ans* - 1 if the input is a number, 0 if it is a list (see criteria below)|Zeda|

As long as Ans is always contains more than one element and the second element is not twice that of the first, this will determine if Ans is a list or not:
```
Ans(2)=2Ans(1
```
If Ans is a number, this will always return 1, else if it is a list meeting the above criteria it returns 0. If you cannot guarantee the list will meet the above criteria (e.g. it might only have one element), then you may utilize the [number or string](number-or-string.html) routine, as it is also capable of differentiating between a number and a list. There does not exist, however, any method in Basic to distinguish a list from a string.
