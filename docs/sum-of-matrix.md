# Sum of Matrix Elements
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Returns the sum of the elements of a matrix.|*[A]* - the matrix whose elements you want to sum|*Ans* - the sum of the matrix elements|[A], L₁, Ans|zada|[file sumofmatrix.zip]|

```
:dim([A]
:Matr►list(cumSum([A])<sup>T</sup>,Ans(1),L₁
:sum(L₁
```

The [cumSum(](cumsum.html) command gets the cumulative sum of each column in the [matrix](matrices.html), adding the value of the previous element to the next element, and repeating this for each consecutive element in the column. When the cumSum( command is finished, the last element in each column will contain the sum of that column. Taking the <sup>[T](transpose.html)</sup> (transpose) of the resulting matrix switches columns and rows.

Then, using the [Matr►list(](matr-list.html) command, the last column of this result is stored to L₁. This column was originally the last row of cumSum('s output, so it contains all the column sums. Finally, by calculating the sum of that list, we get the total of the matrix elements. L₁ is no longer necessary, and can be deleted.

If you want to use the sum for future use, you can store it to a more permanent variable, such as A or X. When you are done using [A], you should [clean it up](cleanup.html) at the end of your program.
