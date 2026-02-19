# Find Sublist
|Routine Summary|Inputs|Outputs|Variables Used|Author|Authors|
|--- |--- |--- |--- |--- |--- |
|Finds a sublist within a list, with different degrees of specificity.|L₁ - List to search<br>L₂ - Sublist|*Ans* - Initial index of sublist in L₁*<br>L₃ - Indices of L₁ which match the sublist*<br><br>*See individual routines for details|*L*, *X**<br><br>*Only used for gapped sublist searching|kg583| Only include this if you aren't the author of the routine.|

## Find Exact Sublist (Permutation)

For a sublist stored in `L₂`, this routine will find where in `L₁` the precise sublist (in order, no gaps) is found and return the initial index as `Ans` (0 if not found).

```
:For(L,1,1+dim(L₁)-dim(L₂
:L
:If min(L₂=seq(L₁(X),X,L,L-1+dim(L₂
:Return
:End
:0
```

## Find Sublist with Gaps (Permutation w/ Gaps)

For a sublist stored in `L₂`, this routine will find if the ordered sublist is found, with gaps between entries allowed, in `L₁` and return 1 or 0 as `Ans`.

```
:1→X
:For(L,1,dim(L₁))
:If L₁(L)=L₂(X
:X+1→X
:1
:If X>dim(L₂
:Return
:End
:0
```

Alternatively, a few extra lines will return the matching indices as `L₃`.

```
:1→X
:ClrList L₃
:For(L,1,dim(L₁
:If L₁(L)=L₂(X:Then
:L→L₃(X
:X+1→X
:End
:If X>dim(L₂
:Return
:End
```

## Find Shuffled Sublist (Combination)

For a sublist stored in `L₂`, this routine will find where in `L₁` any shuffling (without gaps) of the sublist is found and return the initial index as `Ans` (0 if not found).

```
:For(L,1,1+dim(L₁)-dim(L₂
:L
:If prod(seq(max(L₁(X)=L₂),X,L,L-1+dim(L₂
:Return
:End
:0
```

## Find Shuffled Sublist with Gaps (Combination w/ Gaps)

For a sublist stored in `L₂`, this routine will find if any shuffling with gaps of the sublist is found in `L₁` and return 1 or 0 as `Ans`.

```
:prod(seq(max(L₁=L₂(X)),X,1,dim(L₂
```

Alternatively, two extra lines will return the matching indices as `L₃`.

```
:prod(seq(max(L₁=L₂(X)),X,1,dim(L₂
:If Ans
:seq(1+sum(not(cumSum(L₁=L₂(X)))),X,1,dim(L₂→L₃
```
