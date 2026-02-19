![The List►matr( Command](list-matr/LISTTOMATR.GIF "The List►matr( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Builds a matrix from one or more lists.|List►matr(*list1*, [*list2*, ...], *matrix*|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. MATRX (on the 83) or 2nd MATRX (83+ or higher) to access the matrix menu
1. LEFT to access the MATH submenu
1. 9 to select List►matr(, or use arrows.

Alternatively, press:
1. 2nd LIST to access the list menu
1. LEFT to access the OPS submenu
1. 0 to select List►matr(, or use arrows
       
# The List►matr( Command

The List►matr( builds a matrix by combining several list expressions, and stores it to the specified variable ([A] through [J]). Each list specifies a column of the matrix: the first list will be stored down the first (leftmost) column, the second list down the second column, and so on. For example:

```
List►matr({1,2,3},{10,20,30},{100,200,300},[A]
		Done
[A]
		[[1 10 100]
		 [2 20 200]
		 [3 30 300]]
```

## Advanced Uses

The calculator can actually handle lists that are not the same size. It will pad zeroes to the shorter lists, until they have the same length as the longest list.

```
List►matr({1,2,3},{10},{100,200},[A]
		Done
[A]
		[[1 10 100]
		 [2  0 200]
		 [3  0   0]]
```

## Error Conditions

- **[ERR:ARGUMENT](errors.html#argument)** is thrown if there are more than 99 lists (since a matrix can be at most 99x99)
- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if one of the lists is longer than 99 elements (since a matrix can be at most 99x99)

## Related Commands

- [Matr►list(](matr-list.html)
