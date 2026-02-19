![The Matr►list( Command](matr-list/MATRTOLIST.GIF "The Matr►list( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Stores one or more columns of a given matrix to list variables|Matr►list(*matrix*, *list-var1*, [*list-var2*, ...])<br>Matr►list(*matrix*, *column#*, *list-var*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:<br># MATRX (on the 83) or 2nd MATRX (83+ or higher) to access the matrix menu<br># LEFT to access the MATH submenu<br># 8 to select Matr►list(, or use arrows.
# The Matr►list( Command

The Matr►list( command stores one or more columns of a matrix (or expression resulting in a matrix) to list variables. The syntax is simple: first enter the matrix, then enter the list or lists you want to store columns to. The first (leftmost) column will be stored to the first list entered, the second column will be stored to the second list, and so on. For example:
```
[[11,12,13,14][21,22,23,24][31,32,33,34
		[[11 12 13 14]
		 [21 22 23 24]
		 [31 32 33 34]]
Matr►list(Ans,L1,L2
		Done
L1
		{11 21 31}
L2
		{12 22 32}
```

If there are more lists than columns in the matrix when doing Matr►list(, the extra lists will be ignored.

Matr►list( can also be used to extract a specific column of a matrix to a list. The order of the arguments is: matrix, column number, list name.

```
[[11,12,13,14][21,22,23,24][31,32,33,34
		[[11 12 13 14]
		 [21 22 23 24]
		 [31 32 33 34]]
Matr►list(Ans,4,L1
		Done
L1
		{14 24 34}
```

## Advanced Uses

While the command deals with columns, occasionally you might want to store the matrix to lists by rows. The <sup>[T](transpose.html)</sup> (transpose) command is your friend here: applying it to the matrix will flip it diagonally, so that all rows will become columns and vice-versa. For example:


[[11,12,13,14][21,22,23,24][31,32,33,34
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@[[11 12 13 14]
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@[21 22 23 24]
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@[31 32 33 34]]
Matr►list(Ans<sup>T</sup>,L<sub>1</sub>,L<sub>2</sub>
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@Done
L<sub>1</sub>
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@{11 12 13 14}
L<sub>2</sub>
@<&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>@{21 22 23 24}


## Optimizations

When using Matr►list( to store to named lists, only the first list must have an ∟ in front of its name — it can be omitted for the rest. For example:

```
:Matr►list([A],∟COL1,∟COL2,∟COL3
can be
:Matr►list([A],∟COL1,COL2,COL3
```

On the other hand, when storing a specific column of a matrix to a named list, the list does not need to be preceded by an ∟.

```
:Matr►list([A],N,∟COL1
can be
:Matr►list([A],N,COL1
```

## Related Commands

- [List►matr(](list-matr.html)
- <sup>T</sup> ([transpose](transpose.html))
