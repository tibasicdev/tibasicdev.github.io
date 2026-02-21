# Variable Tips
## General Tips

**Checking for Whole Number**

The fastest way to check for a whole number is:

```
:not(fPart(X
```

**Using DelVar**

When using the [DelVar](delvar.html) command, you don't need to use colons (:) between the DelVars:

```
:Delvar ADelvar Str1...
```

This also holds when you are dealing with a completely different command, so

```
:DelVar AClrHome
```

is perfectly legal.

**Know When to Use Variables**

Many times you will have to use a number repeatedly in a program. To save memory you can assign that number to a variable at the beginning of your program and then just call that variable whenever you need it. This also works for strings that are used a lot.

**Why Variables Get Messed Up**

There are several things that can cause variables to get messed up:

- The Equation Solver updates any given letter variable that is solved for.
- Function graphing, and the tracing thereof, causes X and Y to be updated.
- Parametric graphing, and the tracing thereof, causes X, Y, and T to be updated.
- Polar graphing, and the tracing thereof, causes X, Y, R, and θ to be updated.
- Sequence graphing, and the tracing thereof, causes X, Y, and n to be updated.
- Generally, moving the cursor on the graph screen updates X and Y.
- All the above update R and θ as well if in [PolarGC](polargc.html) mode.
- [Tangent](tangent.html), [DrawF](drawf.html), and [DrawInv](drawinv.html) update X and Y for each coordinate drawn.
- All [Shade(](shade.html) functions update X and Y for each coordinate drawn.
- Y is set to zero per each refresh of the graph screen. (The only reason I can think of is that Y is involved in the calculating of the regions.)
- Generating a list through sequencing does **not** update letter variables (but will create them if they didn't exist)

**Extra Variables**

Sometimes when doing a program you might run out of variables to use. If that happens there are many different places you can go to for more variables. Some are:

- Create lists or matrices and just use/manipulate them
- Extra N—Open the catalog and press LOG and ENTER  
- Window variables—Hit VARS and then ENTER
- Statistic variables—Hit VARS, 5, and scroll through the menus of variables
- Finance variables—Hit APPS and then go into the Finance application

(Note: You can also use most of them as characters.)

## List Tips

**Use Custom Lists before Built-In Lists**

Avoid using lists other than <sub>L</sub>1, <sub>L</sub>2,…, <sub>L</sub>6. You should only use custom lists when you need to [save](saving.html) something.

**Check if Elements are the Same**

The quickest way to check if all the elements of L1 are the same is max(Δlist(L1.

**Separate a List**

You can use seq(L<sub>1</sub>(A),A,C,D→L2 to separate a list into two or more lists, where C is the start and D is the stop.

**Favor cumSum(binomcdf( over seq(**

cumSum(binomcdf(X,0 is the same as seq(I,I,1,X and is smaller and faster. See [here](http://www.unitedti.org/index.php?showtopic-25-st-480-p-97478-#entry97478) for more information.

**Angle Values in List**

If you use the tangent, sine, or cosine function in programs you might notice they aren’t that fast. A better way to do it is to store the values in a list and then recall them from the list.

**Store to one List Element Higher than Exists**

You can store to one list element higher than exists. This even applies if the list does not exist, in which case the list would be created and the first element would be where the is stored.

```
:3→dim(L1
:Input A
:A→L1(4
```

(Note: This will create a fourth element in list 1, and then store A in the fourth element.)

**Create a List without the <sub>L</sub> in Front**

When you store to a custom list, usually you need the little “L” in front.  However, this is not true.  If you just have a letter or a number that is being stored to, it will actually store the list data to a list with the letter or number’s name.

```
:{1,2→LA
can be
:{1,2→A
```

**Shuffle a List**

The smallest and (almost) fastest way to shuffle a list (for instance, a deck of cards) is:

```
:seq(X,X,1,52→L1
:rand(52→L2
:SortA(L2,L1
```

This technique can, of course, be extended to lists of other lengths.

**Chop Off First Element of a List**

You can chop off the first element of a list by using the [∆List(](deltalist.html) and [cumSum(](cumsum.html) commands together, since they are essentially exact opposites. In this example, the first element of L1 is chopped off and the list is stored back to L1:

```
:∆List(cumSum(L1→L1
```

**User-Friendly Lists**

I'm sure others like me want to be able to type in a list without the brackets, separating the elements with only commas. Here's how: 

```
:Input Str1
:expr("{"+Str1→L1
```

**Load a User-Named List**

This will load any list the user names:

```
:Repeat 5≥length(Str1
:Input "Name of List:",Str1
:End
:expr("L"+Str1→L1
```

## Matrix Tips

**Initializing Matrices**

In games where you store [maps](maps.html) with all the same values in [matrices](matrices.html), you need to initialize the matrices in order to use them. There are three different ways that you can do this.

The first way is to set the dimensions of a matrix and then use the Fill( command:

```
:{8,8→dim([A]
:Fill(0,[A]
```

The second way you can initialize the matrix is to actually *delete* it before using it, and then set its dimensions to the desired row and width. This initialization method only works when you want all the matrix elements to have a value of zero.

```
:DelVar [A]{8,8→dim([A]
```

The last way you can initialize the matrix is to use the identity( command. The identity( command is used to create an identity matrix based on the matrix that it's given, which must be a square, n-by-n matrix. Because of the identity( command, this initialization method only works when you have a square matrix and you want all the matrix elements to have a value of zero.

```
:0identity(8→[A]
```

## String Tips

**Skip String►Equ( Command**

If you want to put a string into one of the function variables (Y0-Y9) you don’t need to use the [String►Equ(](string-equ.html) command. Instead, you can just simply store the string into the function variable.

```
:String►Equ(Str1,Y1
can be
:Str1→Y1
```

**Get → and " in a String**

Follow these steps to get the [→](store.html) or " symbols in a string:

1. Type them on the home screen and press [ENTER]
2. Select 2:Quit when the **[ERR:SYNTAX](errors.html#syntax)** comes up.
3. Press [Y=] to go to the equation editor.
4. Press [2nd] [ENTRY] to recall the symbols to Y<sub>1</sub>
5. Now, use [Equ►String(](equ-string.html)Y<sub>1</sub>,Str1) to store the symbols to a string.

**Use the expr( Command**

One of the most unknown and unused commands is [expr(](expr.html). What this command does is allow you to store an expression to a string (includes graph equations) and then execute the string. Since you may use graph equations, you have 28 "extra" strings to use for text and data storage. But if you use graph equations to store data in a graphics-based program, remember to turn the functions off with [FnOff](fnoff.html).

```
:Input “Formula:”,Str1
:Disp expr(Str1
```

**Converting a String to List**

The fastest way to convert a string that contains only alphanumeric characters and spaces to a list is:

```
:seq(inString("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",sub(Str1,A,1)),A,1,length(Str1→L1
```

**Copy & Paste Function**

If you store frequently used code to a string, you can recall the string into a program as a sort of "copy-and-paste" function. However you have to go through menus to get to the string, not to mention delete the quotes.  So store your three most frequently used pieces of string into those variables, u, v, and w. Recalling those doesn't make quotes, and it's faster than getting it from a string. See [seld-modifying code](selfmodify.html) for more information.

## Ans Tips

If you want to speed up your program while doing calculations, you can use the Ans variable. To use Ans, put the calculation in a line all by itself, then it will automatically be stored into Ans saving the need for storing the calculation into a variable. (NOTE: You should only use Ans if it involves changing just one variable.)

```
:If 8>C
:Output(4,2,"Higher
:If 8<C
:Output(4,2,"Lower
can be
:"Higher
:If 8<C
:"Lower
:Output(4,2,Ans
```

Whenever you are using the [pxl-Test(](pxl-test.html) command and speed is a priority, you should put the command on its own line and test for Ans:

```
:pxl-Test(0,0
:If Ans
is faster than
:If pxl-Test(0,0
```

When you are using a [For(](for.html) loop, you can use the following if you want to store something in A without messing up Ans:

```
:For(A,16,0,-1
:End
```

<center>

|**[<< Tips & Tricks](sk:tips-tricks.html)**|**[Table of Contents](starter-kit.html)**|**[Productivity Tips >>](sk:productivity-tips.html)**|
| --- | --- | --- |

</center>
