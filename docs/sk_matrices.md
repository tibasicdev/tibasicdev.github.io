# Matrices
[Matrices](matrices.html) are a step up from lists. [Lists](lists.html) are a string of elements, like {5,4,3,2,1,0}. A matrix, on the other hand, is a list of lists, like [[5,5,5],[4,4,4],[3,3,3],[2,2,2]]. Below, we will start learning how to handle this more complex data type.


## Setting up Matrices

Unfortunately, unlike lists, there is no [`SetUpEditor`](setupeditor.html) command to make it easy for matrices. Fortunately, though, matrices [A] through [J] always exist, unless otherwise removed. This gets rid of the need to [`dim(`](dim.html) first. You do need to be careful with [`UnArchive`](unarchive.html). To ask if the user has already run the program, you could use a routine such as the following:

```
:Menu("CONTINUE?","YES",Y,"NO",N)
:Lbl Y
:UnArchive [J]
:Lbl N
:{2,3}→dim([J])
```

What does that last line of code do? Well, this is just like setting the size of lists in the last lesson. The only difference is that we need to have two numbers that are separated by a comma and surrounded by curly braces. The last line of code above says to give matrix [J] 2 rows and 3 columns. If you prefer to think of matrices as lists of lists, you can say that the last line of code says, "Provide 2 lists, each with 3 elements."

## Using Matrices

### Writing

It is really simple to store an element into a matrix. To store the number 5 into row 1 and column 2 of our matrix [J], we use this line:

```
:5→[J](1,2)
```

Simple, right? What if you want to store the powers of 2 from element (1,1) to (2,3)? We have to use this code:

```
:{2,3}→dim([J])
:0→P
:For(R,1,2)
:For(C,1,3)
:P+1→P
:2^P→[J](R,C)
:End
:End
```

Notice how it is a lot more complicated than the version with the list. This is because we first start the [`For(`](for.html) loop for both rows of our matrix, and then within that we start the [`For(`](for.html) loop for every column of the current row.

### Reading

Let's make this simple. To store a matrix element to a variable, use this line of code:

```
:[J](1,2)→A
```

This stores element (1,2) of [J] into the real variable A.
To display it, use this line:

```
:Disp [J](1,2)
```

Now, let's modify our program to show some results.

```
:ClrHome
:{2,3}→dim([J])
:0→P
:For(R,1,2)
:For(C,1,3)
:P+1→P
:2^P→[J](R,C)
:Disp [J](R,C)
:End
:End
```

We've added a [`ClrHome`](clrhome.html) command to the beginning, and a [`Disp`](disp.html) command above the two [`Ends`](end.html). If you do it right, your output should be:

2
4
8
16
32
64
Done

## Cleaning Up

Fortunately, you just need to use the [`Archive`](archive.html) command for a matrix to be archived.

## Final Notes

Now, you see how much more powerful a matrix is, when coming from a list. Matrices are usually used to store map data and such. Still, the bigger step up is the string data type. This is the most powerful variable type, and you will learn about it next.

<center>

|**[<< Data Types (lists)](sk:lists.html)**|**[Table of Contents](starter-kit.html)**|**[Data Types (strings) >>](sk:strings.html)**|
| --- | --- | --- |

</center>
