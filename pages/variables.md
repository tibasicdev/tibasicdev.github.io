# Variable Types
Variables are used extensively in programming, as most programs use variables in one form or another. They are used to keep track of numbers or text or stats; there are many uses for variables. Put simply, programming wouldn't be programming without variables.  Imagine variables being little boxes which you can store almost anything in.

A variable is a reference to the information that it holds. Variables allow you to store the information, so that you can later use it for whatever purpose is desired. The thing to remember, though, is that programs all share the variables.

There are several different kinds of variables available on the calculator, but the four main variables that you will be using are number variables, lists, matrices, and strings. Number variables are used for storing a single number. Lists are used for storing a collection of numbers. Matrices are used for storing numbers in a two-dimensional format. And, strings are used for storing text.



## Storing & Deleting Variables

Variables have values stored in them so that the values can be recalled for later use. When storing an expression containing a variable into another variable, the value of the variable at that time is used. The [store](store.html) (→) command is used for storing variables, and it is accessed by pressing the `[STO►]` key. When storing a value in a variable, you have the value on the left side of the store command and the variable that it will be stored to on the right side.

Format:

```
value→variable
```

Examples:

```
123→A
123+456→A
"Hello"→Str0
```

When you are done using variables, you should delete them with the [DelVar](delvar.html) command to save space. The DelVar command deletes the contents of a variable from memory. If the DelVar command is used with a real variable, the variable is not only deleted from memory but automatically set to zero the next time it is used. DelVar does not work on specific elements of a list or matrix. In fact, it will actually return an error.

Format:

```
DelVar variable
```

Examples:

```
DelVar A
DelVar B
DelVar Str0
DelVar L₁
```

## Numeric variables

Numeric variables are used for storing numbers. There are 27 numeric variables (from A to Z and θ) that can be easily accessed, and more that the calculator uses for its specific purposes. 

Examples:

```
1→A
2+3→B
(A+B)/(6+7→C
```

*Tip:* You don't need to close brackets before using the STO command. The calculator will automatically close any open brackets and string quotes as soon as it comes across a STO command.

Most numeric variables can either be real or complex (the latter involve *i*, the square root of -1, and are important to advanced algebra). In either case, up to 14 digits of a number can be stored, although only the first 10 will be displayed and used for comparison.

To access a real variable, press ALPHA and then the key corresponding to whatever letter you want your variable to be. You can initialize a real variable by storing a number, another variable, or an expression into the variable using the STO key (or, just using it almost anywhere will initialize it to 0).

#### Flag Variables

Flag Variables are a numeric variable that is used for the specific purpose of controlling program flow. They typically only contain the value 1 or 0 and are sometimes described as being binary, or Boolean variables. 

(for more information, see [Using Variables as Flags](flags.html))

## List Variables

Lists are used to hold multiple numbers at once, in a specific order. There are six "default" lists named L<sub>1</sub> through L<sub>6</sub>, but an important feature of lists is that they can be given names, so that there are millions of possible lists. Lists are important for programmers for many purposes - saving data after a program finishes running, and storing a level of a game are only two of them.

Examples:

```
{1,2,3}→L₁
L₁+10→L₂
{4,5,6}→⌊X
{7,8,9}→⌊DATA
```

There are 6 built-in list variables available: L₁, L₂, L₃, L₄, L₅, L₆. Beyond that, you can create custom list names using one to five characters, comprised of any combination of capital letters and numbers and theta, but it must begin with a letter or theta.

(for more information, see [Lists and Their Commands](lists.html))

## Matrix Variables

Matrices are two-dimensional lists (row by column). Equivalent to lists, they are used when the data needs more structure. Matrices are often used for storing a level or a map of the screen. There are only ten matrices available (from [A] to [J]).

(for more information, see [Matrices and Their Commands](matrices.html))

## String Variables

Strings are used for storing a sequence of characters, that is, text. A common use for strings is to manipulate text to be displayed in a program, but they have many different purposes: highscores, level and map data, and whatever else is desired. 

```
"Hello"→Str0
"World"→Str1
Str0+" "+Str1→Str2
```

Using the "`+`" sign will concatenate strings together, so the last line above will put "`Hello World`" into `Str2`.

Although there are only ten built-in string variables (`Str0` through `Str9`) available to use, strings can hold many different kinds of characters, including letters (both uppercase and lowercase), numbers, functions, and even other commands. The amount of free RAM is the only limit on the number of characters in a string.

*Tip:* You don't need to close the quotes before using the STO command. The calculator will automatically close any string quotes as soon as it comes across a STO command.

(for more information, see [Strings and Their Commands](strings.html))

## Picture Variables and GDBs

Picture variables and GDBs (short for Graph DataBase) are used to save two different elements of the current graph display. A picture variable is used to store the exact appearance of the graph screen. A GDB is used to store system variables relevant to the graph screen - equations, window settings, and the like. 10 built-in variables of each type exist: Pic0 through Pic9 for pictures and GDB0 through GDB9 for GDBs.

(for more information, see [Pictures and GDBs](pictures.html))

## System Variables

System variables are, for the purposes of this guide, variables that certain commands will use or modify without asking (i.e. without supplying them in the command's arguments). This is a somewhat ill-defined category, and in fact the system variables we'll discuss are of a somewhat miscellaneous nature. They include equation and plot variables, window and table parameters, statistical variables, and finance variables.

(for more information, see [System Variables](system-variables.html))

## Converting Between Variable Types

#### Between lists and matrices

The [List►matr(](list-matr.html) and [Matr►list(](matr-list.html) commands are used to convert between a matrix and several lists. Using these commands, it should be simple to implement any kind of conversion between these two data types.

#### Between strings and numbers

It is very easy to convert a string version of an expression to a number, list, or matrix: the [expr(](expr.html) command can do it — for example, expr("5") will give you the number 5, and expr("{1,2,3}") will give you the list {1 2 3}.

Going the other way, however, is slightly more complicated because there is no built-in command to do it. What you need to use instead are a few small routines: see [number to string](number-to-string.html) for how to convert a number to a string. To convert a list or matrix, convert each individual element instead.

## Archiving and Unarchiving Variables

On the TI-83+/84+/SE calculators, you can [archive](archive.html) and [unarchive](unarchive.html) variables. What this entails is the calculator moving the variable to the archive memory or the calculator moving the variable to RAM respectively. The main advantage of archiving a variable is that it is protected from calculator crashes, which clear the calculator's RAM. At the same time, you can't access a variable that's archived; it needs to be in RAM to use it.

```
:Archive L1
:UnArchive Str1
```

There are a couple things you need to be aware of when using Archive and UnArchive. First, since the TI-83 only has RAM, archiving is not possible, and subsequently neither of these commands are available. This means that you shouldn't use either of these commands if you plan on [porting](portability.html) a program to the TI-83. Second, archiving does not work with the majority of the [system variables](system-variables.html), including the graphing, statistical, and finance variables. You can archive the other types of variables, however, although list variables are actually more manageable using the [SetUpEditor](setupeditor.html) command.
