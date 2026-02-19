# Lists
Lists are one of the most used data types, and they can hold up to *999* elements (the only exception is the TI-83, which can only hold *99* elements). You can also name your own lists, making it the most secure data type available on the TI-83 calculators.

Note: To programmers coming from computers, this is the equivalent of a one-dimensional array.



## Before You Start

There are two "types" of lists: predefined and custom. Predefined lists are L₁...L₆, and are accessible by pressing 2nd 1-6 respectively. The casual calculator user is probably using these, so don't use these if you don't have to. Custom lists start with a tiny uppercase ∟, and have a maximum of five characters afterward. You can have lists such as ∟LUNCH, or ∟TODO, or ∟GRR. We will be working with custom lists on this page.

## Setting Up Lists

To create a list, all you have to do is this:

```
:5→dim(∟LIST)
```

The [dim(](dim.html) command creates the list, and the number 5 being put in it tells the list how many elements it has to have in it. But what if you archived it when the program was run last? Then, you need to unarchive it using the [UnArchive](unarchive.html) command:

```
:UnArchive ∟LIST
:5→dim(∟LIST)
```

But wait, it isn't that easy! If you try to unarchive something that doesn't exist, you get an [ERR:UNDEFINED](errors.html#undefined) error! So, we must make sure the list is created first, by using the dim( command. But, if the list does exist and it is archived, we must unarchive it first! What to do, what to do.
You could either wait until the user says whether or not the list exists (not the best choice), or you can use another command available called [SetUpEditor](setupeditor.html).

### SetUpEditor

When you use SetUpEditor, you put the name of the list afterwards, like SetUpEditor ∟LIST. If the list doesn't exist, it gets created, if it is archived, it gets unarchived; and if nothing special happened to it, it just does nothing. This one command fixes what would take quite a few lines of code and the possibility of user error. You can then use the dim( command to specify the number of elements in the list. You can use it like so:

```
:SetUpEditor ∟LIST
:5→dim(∟LIST)
```

Now your list is set up! Note that for custom lists, the ∟ prefix is not required.

## Using a list

### Writing
It isn't that hard to use a list. To write something to it, for example, you use this code:

```
:5→∟LIST(1)
```

This code writes the number five the the first element of the list. (Computer programmers: the index starts at 1, *not* 0) To write the first 5 powers of 2 into each element, starting at the first element (with the number 2 inside), you can use this code:

```
:SetUpEditor ∟LIST
:5→dim(∟LIST)
:For(L,1,5)
:2^L→∟LIST(L)
:End
```

Inside of the [For(](for.html) loop, we go through each respective element of ∟LIST and store the respective power of 2 into it. The end result of the list is {2 4 8 16 32}.

### Reading

Reading from a list is just as easy. To put an element from a list into the variable X, you use this command:

```
:∟LIST(1)→X
```

To display the element without storing into the variable, you can do something like:

```
:Disp ∟LIST(1)
```

Now, what if the program we made earlier was supposed to show the results? We would modify it like so:

```
:ClrHome
:SetUpEditor ∟LIST
:5→dim(∟LIST)
:For(L,1,5)
:2^L→∟LIST(L)
:Disp ∟LIST(L)
:End
```

The first addition is at the very top. ClrHome is just a precautionary measure. The second addition is just before the End, and that is the Disp command, which displays element number L on the screen. Try out the program, and you should see on the home screen:

2
4
8
16
32
Done

## Finishing Up

You need to do, at the most, only two things to clean up your list use.

The first is to archive your list using the [Archive](archive.html) command, if you want to protect it until next time. Or, if it is only used to hold temporary variables, you can delete it with Delvar.

The second is to SetUpEditor, like so:

```
:SetUpEditor
```

This sets up the Edit... command (on the STAT button) so that it allows edit of L₁...L₆. Don't use this, and the student who clicks on Edit... will see ∟GAME appear just as the teacher walks to check on him, and oops.


<center>

|**[<< Data Types (intro)](sk:data-types.html)**|**[Table of Contents](starter-kit.html)**|**[Data Types (matrices) >>](sk:matrices.html)**|
| --- | --- | --- |

</center>
