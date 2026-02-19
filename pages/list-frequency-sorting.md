# List Frequency Sorting
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Sorts a list based on frequency, then by value|*L₁* - A list to be sorted|*L₁* - The original list, sorted by frequency of elements|L₁, L₂, L₃|Trenly|

```
SortD(L₁
DelVar L₂DelVar L₃
SetUpEditor
For(θ,1,dim(L₁
L₁(θ→L₂(1+dim(L₂
sum(L₁=Ans→L₃(dim(L₂
θ-1+Ans→θ
End
DelVar L₁
SetUpEditor
While dim(L₂
1+sum(not(cumSum(L₃=max(L₃→θ
L₃(θ)→N
For(E,1,N
L₂(θ→L₁(1+dim(L₁
End
For(E,θ+1,dim(L₂
L₂(E→L₂(E-1
L₃(E→L₃(E-1
End
dim(L₂)-1→dim(L₂
dim(L₃)-1→dim(L₃
End
```

This routine uses the [List Frequency](list-frequency2.html) routine to find the frequency of each number. It then deletes, and reconstructs L₁ from the values in those lists by searching for the highest frequency, then adding it into L₁ the number of times it occurs. It then shifts the elements inside the frequency lists above the value down 1, overwriting the value which was just inserted into L₁. It then decreases the length of the frequency lists, and repeats until there are no more values to be added. This routine automatically cleans up, leaving L₂ and L₃ empty. If you wish to sort in ascending frequency, change the [max(](max.html) on line 12 to [min(](min.html). If you wish to sort the values in ascending order instead of descending order, change the [SortD(](sortd.html) on line 1 to [SortA(](sorta.html)

## Error Conditions
- **[ERR:INVALID DIM](errors.html#invalliddim)** is thrown if L₁ is defined but is empty
- **[ERR:UNDEFINED](errors.html#undefined)** is thrown if L₁ does not exist

## Related Routines
- [List Frequency](list-frequency2.html)
