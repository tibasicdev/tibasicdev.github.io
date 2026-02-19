# Matrices and Their Commands
A matrix is a rectangular grid of elements. On the TI-68k calculators, matrices can contain any mix of any scalar (non-list) variable type that's valid in an expression: you can have matrices of numbers, matrices of strings, matrices of truth values or expressions. You can even mix and match variable types — it's perfectly all right to have a string in one element, and a number in the next.

There are three ways to enter a matrix on the calculator:
- Using nested [ ] brackets: e.g. [[a,b,c][d,e,f]] (this is a matrix with 2 rows - the row a,b,c above the row d,e,f).
- Using [ ] brackets and semicolons: e.g. [a,b,c;d,e,f]
- Using { } brackets: e.g. {{a,b,c},{d,e,f}} (this works because matrices are actually stored as lists of lists)

You can access a certain element of the matrix by writing the coordinates of the element you want in [ ] brackets after it: matrix[r,c] would access the element in the r<sup>th</sup> ROW and the c<sup>th</sup> COLUMN of the matrix (Matrices are **always** indexed first by the row, top to bottom, and second by the column, left to right). Also, using one index — matrix[r] — returns the r<sup>th</sup> row of the matrix as a 1 by # matrix.

On earlier calculator models, matrices had the [random access](https://en.wikipedia.org/wiki/random_access) property: accessing any element of a matrix took the same amount of time. This was possible because the matrices were restricted to numbers. On the 68k calculators, since matrices can mix element types, they are no longer random access: the calculator has to go through the entire matrix to get to an element, so the larger an index is, the longer it takes to access. This isn't significant for small matrices. But the time keeps increasing linearly, so it can be very slow to access the last elements of a large matrix.

Except for the constraint of free memory, and of the time it takes to access elements, there is no limit on the number of elements a matrix may have.

## Matrices as Vectors

In mathematics, a vector is a list of *n* numbers with a geometrical representation in *n*-dimensional space (two representations, actually: as a point in *n*-space, and as a translation which takes the origin to that point). 2- and 3-dimensional vectors are used respectively for 2-dimensional space (the plane), and the usual 3-dimensional space.

On TI-68k calculators, matrices with only one row, or only one column, are interpreted as vectors for the purposes of the commands [dotP()](68k:dotp.html), [crossP()](68k:crossp.html), and [unitV()](68k:unitv.html), as well as the formatting commands [▶Cylind](68k:cylind.html), [68k:▶Polar](68k:-polar.html), [▶Rect](68k:rect.html), and [▶Sphere](68k:sphere.html).

## Linear Algebra Operations

Common mathematical commands and operators extend to matrices in a linear algebraic way. [+](68k:add.html), [-](68k:subtract.html), and [*](68k:multiply.html), for two matrices, are the corresponding matrix operations (in particular, [matrix multiplication](http://mathworld.wolfram.com/matrixmultiplication.html) is quite complicated). [^](68k:power.html) raises a square matrix to an integer power by multiplying it by itself; if the integer is negative, it takes the inverse first.

Matrices have a special operator just to themselves: <sup>[T](68k:transpose.html)</sup>, called the transpose operator. It flips the matrix about its main diagonal, so rows become columns and columns become rows.

The operators [+](68k:add.html), [-](68k:subtract.html), [*](68k:multiply.html), and [/](68k:divide.html) can be applied to a square matrix and a scalar as well, by multiplying the scalar by the [identity matrix](68k:identity.html). For multiplication and division, this results in the operation being done to each element, while addition and subtraction result in adding or subtracting the scalar to each element on the main diagonal.

Since occasionally you want to do these operations element-by-element, the alternatives [.+](68k:dotadd.html), [.-](68k:dotsubtract.html), [.*](68k:dotmultiply.html), [./](68k:dotdivide.html), and [.^](68k:dotpower.html) have been provided, which do this for both two matrices and for a matrix and an expression.

## Exponential and Trig Functions

The calculator gives a special interpretation to exponential and trig functions applied to matrices, *[e](68k:e-value.html)*^() being the most common. These commands require the matrix to be square and diagonalizable, and return an approximate floating-point value.

A *diagonalizable* matrix A is one that can be expressed in the form A = PDP<sup>-1</sup>, where D and P are square matrices, and D is *diagonal* — composed entirely of zeroes except on the main diagonal. If a matrix is diagonalizable, the calculator can compute explicit values for D and P using [68k:eigVl()](68k:eigvl().html) and [68k:eigVc()](68k:eigvc().html):
- D = diag(eigVl(A))
- P = eigVc(A)
If a matrix is not diagonalizable, the result of eigVc() will not have an inverse.

The calculator applies functions like *[e](68k:e-value.html)*^() to matrices by first writing the matrix in the form PDP<sup>-1</sup>, and then returning Pf(D)P<sup>-1</sup>. Here, the function is applied to D by taking f() of every diagonal element (the elements off the diagonal remain zero). 

This definition is used for the following commands:
- [^](68k:power.html), [68k:ln()](68k:ln().html), [68k:log()](68k:log().html), and [68k:root()](68k:root().html)
- [68k:cos()](68k:cos().html), [cosֿ¹()](68k:arccos.html), [68k:sin()](68k:sin().html), [sinֿ¹()](68k:arcsin.html), [68k:tan()](68k:tan().html), and [tanֿ¹()](68k:arctan.html).
- [68k:cosh()](68k:cosh().html), [coshֿ¹()](68k:arccosh.html), [68k:sinh()](68k:sinh().html), [sinhֿ¹()](68k:arcsinh.html), [68k:tanh()](68k:tanh().html), and [tanhֿ¹()](68k:arctanh.html)

## Other Operations on Matrices

Most math commands extend to matrices by being applied to each element; [gcd()](68k:gcd.html) is a good example. Yet other commands behave in unpredictable ways. The commands [SortA](68k:sorta.html) and [SortD](68k:sortd.html) sort row and column vectors as though they were lists. The following list math/statistics commands act on matrices as they would on lists of lists, which results in a row vector containing the operation done on each column:
- [min()](68k:min.html) and [max()](68k:max.html)
- [mean()](68k:mean.html) and [median()](68k:median.html)
- [sum()](68k:sum.html) and [product()](68k:product.html)
- [stdDev()](68k:stddev.html), [stDevPop()](68k:stdevpop.html), and [variance()](68k:variance.html)

Finally, there are the commands that are meant specifically for matrices. These are found in the Matrix submenu of the MATH popup menu.

- [augment()](68k:augment.html)
- [colDim()](68k:coldim.html)
- [colNorm()](68k:colnorm.html)
- [cumSum()](68k:cumsum.html)
- [det()](68k:det.html)
- [diag()](68k:diag.html)
- [dim()](68k:dim.html)
- [eigVc()](68k:eigvc.html)
- [eigVl()](68k:eigvl.html)
- [Fill](68k:fill.html)

- [identity()](68k:identity.html)
- [list▶mat()](68k:list-mat.html)
- [LU](68k:lu.html)
- [mat▶list()](68k:mat-list.html)
- [mRow()](68k:mrow.html)
- [mRowAdd()](68k:mrowadd.html)
- [newMat()](68k:newmat.html)
- [norm()](68k:norm.html)
- [QR](68k:qr.html)

- [randMat()](68k:randmat.html)
- [ref()](68k:ref.html)
- [rowAdd()](68k:rowadd.html)
- [rowDim()](68k:rowdim.html)
- [rowNorm()](68k:rownorm.html)
- [rowSwap()](68k:rowswap.html)
- [rref()](68k:rref.html)
- [simult()](68k:simult.html)
- [subMat()](68k:submat.html)




## Conditionals With Matrices

Conditional statements, like [If](68k:if.html), [when()](68k:when.html), and [While](68k:while.html), accept matrices of truth values as well as single truth values. The check will be interpreted as true if and only if every element of the matrix is true, effectively combining each element of the matrix with [and](68k:and.html).

The most common way for matrices of truth values to be created is with relational operators ([=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), [≤](68k:less-than-or-equal.html)) applied to matrices. They will return the single value ' false' unless both sides of the relation are matrices of equal size, in which case the matrices will be compared element by element, returning a new matrix.
