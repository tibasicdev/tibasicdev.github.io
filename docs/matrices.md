# Matrices and Their Commands
Matrices are two-dimensional lists (row by column). They are used for holding lots of information. Matrices are often used for storing a [map](maps.html) of the screen, which is necessary for collision detection in [movement](movement.html).

There are only ten built-in matrices (from [A] to [J]). A matrix may have up to 99 rows and 99 columns, however the memory on a TI-83 calculator limits this: a 99x99 matrix would hold 9801 elements, and take up 88220 bytes! A matrix is like a grid. To access the matrix variables you need to press [MATRX] on a TI-83, or [2nd] [*x*<sup>-1</sup>] on a TI-83+ or higher. You can then scroll down to whatever matrix you want to use or press the corresponding number. Entering [, A, and ] for the matrix [A] will **not** work.

The square brackets, [ and ], are used when manually entering a matrix variable. The syntax is fairly complicated, and goes as follows:
- The matrix must start off with an opening bracket - [.
- After that comes the data in the matrix, row by row (left to right, and top to bottom).
- Each row begins with another opening bracket - [.
- Then come the elements in the row. Numbers or expressions, they must be separated by commas.
- A row ends with a closing bracket - ]. There is no comma between two rows.
- The matrix ends with another closing bracket - ].

Thus, a matrix will start with two opening brackets, [[, and end with two closing brackets, ]]. If all you're doing is storing the matrix, the last two brackets can be omitted.

Fortunately for you, you don't have to memorize this syntax — in fact, it's probably best if you don't, since there's good odds of making a mistake even if you know it well. The easiest way to store to a matrix variable in a program is first, to create the matrix you want in the matrix editor, and second, to paste it into the program by recalling the matrix's value.

## Commands

Some basic arithmetic commands can be used by matrices as well as real numbers. However, they don't all do what you would expect (unless of course you've taken an advanced algebra class):

- [Plus](add.html)(+) and [minus](subtract.html)(-) add or subtract the matching elements of two matrices with the same size (no surprise there). The [negating](negative.html) (-) will negate each element of the matrix.
- [Multiplication](multiply.html) (*) for matrices exists, but it does not work like adding and subtracting. For details, see [Matrix Multiplication](http://mathworld.wolfram.com/matrixmultiplication.html) at MathWorld.
- The [inverse](inverse.html) (<sup>-1</sup>) operator finds the inverse matrix, the NxN matrix such that [A]<sup>-1</sup>[A]=[A][A]<sup>-1</sup>=identity(N). This function only works for square matrices.
- The [^](power.html) operator raises a square matrix to a power, multiplying it by itself 0 to 255 times. The [²](2.html) and [³](3.html) commands are valid substitutes for ^2 and ^3.
- The [=](equal.html) operator tests if two matrices are exactly identical, and returns 1 if they are and 0 otherwise; [≠](notequal.html) works similarly.
- Some commands also work on matrices, by being applied to every element. They are: [abs(](abs.html), [fPart(](fpart.html), [iPart(](ipart.html), [int(](int.html), [round(](round.html), [►Frac](-frac.html), and [►Dec](-dec.html).
- [angle(](angle.html) might have been intended to work on matrices in this way, but actually returns a matrix of the same size filled with 0. (So, even though angle(-1) returns pi, angle([[-1]]) still returns [[0]].)

There are also, of course, special commands for dealing with matrices. They are:

- [augment(](augment.html)
- [cumSum(](cumsum.html)
- [det(](det.html)
- [dim(](dim.html)
- [Fill(](fill.html)
- [identity(](identity.html)

- [randM(](randm.html)
- [Matr►list(](matr-list.html)
- [List►matr(](list-matr.html)
- [ref(](ref.html)
- [rref(](rref.html)

- [rowSwap(](rowswap.html)
- [row+(](rowplus.html)
- [*row(](timesrow.html)
- [*row+(](timesrowplus.html)
- <sup>T</sup> ([transpose](transpose.html))


These can be found in the MATH submenu of the matrix menu.

## Optimizations

Even if you need to store a fixed matrix in a program, doing it in the standard fashion is usually inefficient memory-wise: consider that if each element is one digit, then over half the memory used is spent on commas and brackets. 

You may want to use a modified version of a routine on the [compressions techniques](compression.html) page.

If most of your matrix's elements are 0, consider deleting the matrix (so that any old data in it doesn't interfere), creating it using the [dim(](dim.html) command with all elements 0, then storing to the elements that are not. For example:
```
:DelVar [A]{5,5→dim([A]
:1→[A](1,2
:2→[A](3,4
:3→[A](5,5
```
