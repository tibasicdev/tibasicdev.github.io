![The augment( Command](augment/AUGMENT.GIF "The augment( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Combines two lists or matrices into one. In the case of matrices, this is done horizontally rather than vertically.|augment(*list1*,*list2*<br><br>augment(*matrix1*,*matrix2*|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd LIST to access the List menu
2. RIGHT to access the OPS submenu
3. 9 to select augment(, or use arrows

Alternatively, press:
1. MATRX (on the TI-83) or 2nd MATRX (TI-83+ or higher) to access the Matrix menu
2. RIGHT to access the MATH submenu
3. 7 to select augment(, or use arrows
       
# The augment( Command

The `augment(` command is used to combine two lists or two matrices into one. For lists, this is done the obvious way: adding the elements of the second on to the elements of the first. For example:
```
augment({1,2,3,4},{5,6,7
	{1 2 3 4 5 6 7}
```

The lists *must* have at least one value. If you attempt to `augment(L₁,L₂)` and either of the lists are empty, you will receive an error. If you're using this within a program, you may want to use [`dim`](dim.html)() to check the size before performing an `augment`.

For matrices, the columns of the second matrix are added after the columns of the first matrix: an R by C matrix augmented with an R by D matrix will result in an R by (C+D) matrix. For example:

```
augment([[1][2]],[[3][4]
	[[1 3]
	 [2 4]]
```

## Combining 3 or more lists

The `augment()` command only accepts two parameters. If you need to combine 3 or more lists, you can nest the `augment` calls.

```
This will NOT work:  augment(L₁,L₂,L₃)
But this will:       augment(augment(L₁,L₂),L₃)
```

Just be sure that all lists have at least 1 value to prevent errors.

## Advanced Uses

Use the `<sup>[T](transpose.html)</sup>` (transpose) command if you want to combine two matrices vertically, rather than horizontally. For example:

```
augment([[1,2]]T,[[3,4]]T)T
	[[1 2]
	 [3 4]]
```

## Optimization

You may be tempted to use `augment(` to add one element to the end of a list:

```
augment(L1,{X→L1
```

However, the following way is faster and more memory-efficient while the program is running (although it increases the program's size):

```
X→L1(1+dim(L1
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#datatype)** is thrown if you try to augment a single number to a list, a common error — use {X instead of X.
- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if you try to augment two matrices with a different number of rows.
- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if one of the arguments is a list with dimension 0, or if the result would have dimension over 999 (for lists) or 99x99 (for matrices).

## Related Commands

- [`dim(`](dim.html) – for retrieving the size of a list
- [`seq(`](seq-list.html) – for creating a list based on a formula, or to create a subset of an existing list
- `<sup>[T](transpose.html)</sup>` – to transpose a 2D matrix
