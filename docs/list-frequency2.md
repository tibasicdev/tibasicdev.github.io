# List Frequency Fast
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Returns a list of the frequency of values in another list sorted.|*L₁* - the list you want to find the frequency of|*L₂* - the values of L₁ without repetition sorted<br>*L₃* - the frequencies of the values in the list L₂ sorted|L₁, L₂, L₃, θ|Galandros|[file listfrequency2]|

```
:DelVar L₂DelVar L₃SortA L₁
:For(θ,1,dim(L₁
:L₁(θ→L₂(1+dim(L₂
:sum(L₁=Ans→L₃(dim(L₂
:θ-1+Ans→θ
:End
```

In the first line we initialize L₁, L₂, and L₃. We sort L₁ so like values will be adjacent.

Then we start looping by storing the first value encountered to the next element of list L₂.
In the next line we find the frequency of the value already stored in L₂ and is stored to the correspondent element in L₃. θ is increased by the frequency found minus 1 to pass to next number, but then incremented by 1 in the For loop.
We loop we reach the end of L₁.

And that's it. The output is put on L₂ and L₃ already sorted. Notice how well Ans is used for speed and size optimization.

When you are done using L₁, L₂, and L₃, you should [clean them up](cleanup.html) at the end of your program.
