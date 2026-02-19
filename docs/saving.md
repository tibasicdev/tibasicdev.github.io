# Saving
The most efficient and versatile way to save data when a program exits is by using a custom [list](variables.html). The list can be named after your program, hold up to 999 values, and be archived for long-term storage. Below is an example of a simple saving routine that backs up the variables A,B, and C into ∟SAVE and archives the list. It then unarchives and restores the data from that list.

```
:{A,B,C→SAVE
:Archive ∟SAVE
```

```
:SetUpEditor SAVE
:If not(dim(∟SAVE
:{0,0,0→SAVE
:∟SAVE(1→A
:∟SAVE(2→B
:∟SAVE(3→C
```

## The Explanation

First, use the syntax {*value*, *value*, *value*, ...}→SAVE to back up as many values (usually variables) as you want. If ∟SAVE does not exist, it will be created with those values. If it does, the previous data will be overwritten and replaced.

```
:{A,B,C→SAVE
```

To prevent losing saved data, the list is stored in Archive memory. While in Archive memory, it will not be erased due to a RAM clear and cannot be overwritten by other programs. You might consider leaving this step out, however, to preserve compatibility with the TI-83 (which doesn't have Archive memory).

```
:Archive ∟SAVE
```

To load the saved data, it first must be moved out of archive memory, or an [ERR:ARCHIVED](errors.html#archived) will result. The most obvious method would be to use Unarchive ∟SAVE. However, using this command will cause problems if the list does not exist. The best command to use is [SetUpEditor](setupeditor.html), which was intended for use with the built-in list editor.

As a side effect of setting up a list in the editor, SetUpEditor will create the list if it does not exist, unarchive it in archive memory, or leave it alone in RAM. In other words, SetUpEditor will always result in an unarchived ∟SAVE in RAM, without any errors (also see the relevant section on [program cleanup](cleanup.html)). SetUpEditor can also be used on multiple lists separated by a comma.

```
:SetUpEditor SAVE
```

But what happens if this is the first time we're running the program? The answer is SetUpEditor will create our list for us, but it will have a length of 0. This allows us to check if we've saved data to it before: if we have, hopefully, it will have a length of more than that (in this case, 3). So this piece of code stores a default of {0,0,0} to the list if it's just been created (of course, you can put in anything you want as the default, or do something else entirely).

```
:If not(dim(∟SAVE
:{0,0,0→SAVE
```

Lastly, the stored data values are recalled into the [variables](variables.html) to be restored.

```
:∟SAVE(1→A
:∟SAVE(2→B
:∟SAVE(3→C
```

### Alternative Methods

You can also modify list entries (auto-save) directly during the game. Doing so saves the user from having to save the game before exiting, but may take more memory.
If you give the player the option to save in a linear/preset game, you can use variables and the Sto> key to create a way to save without using a list. This method branches off, and is infinitely expandable. Here is an example:

```
:ClrHome:Menu("Game","New",1,"Load",2,"Exit",3) 
:Lbl 2      // Ignore the other options for learning purposes. 
:If X=2
:Goto 45 :End     // Loads from where the player left off
...
:Menu("Save?","Yes",A,"No",45) 
:Lbl A :X → 2 :Goto 45 :End 
:Lbl 45 :Disp "Hi!" 
...     //Rest of code
```

## Protecting Saved Games

It's quite a pain when you go through all that trouble to get users to follow the game through its entirety without the user changing his/her list data to give himself/herself ultimate powers. There are a few ways to protect this from happening.

### Addition Method

To protect your saved lists, you can add up all the values of the list and store it to an element in the list right before the program leaves, and check it before allowing the user to reload that saved game.

Right before quitting:

```
:sum(∟SAVE,2→∟SAVE(1    // list element 1 is used to save the summation of all other list elements
```

Checking to make sure list elements add up:

```
:If sum(∟SAVE)≠2∟SAVE(1
:Disp "ERROR: DATA CORRUPTED
```

### Extra list elements

Another method available to your disposal is to add extra elements that do nothing (or even better, cause errors!). No code will be provided as it is easy enough to add useless (or destructive) list elements. See [program protection](protection.html) to get more details on destructive list elements.

### Dual List method

Another thing you can do to protect saved games is to use 2 lists. Both lists will contain the same data, and can be compared to for changes made by users. To add further protection mix the order up (one list the opposite of the other).

#### Simple Dual List code

To get both lists the same:

```
:∟SAVE1→SAVE2    // make both lists the same
```

Checking to make sure both lists are the same:

```
:If not(min(∟SAVE1=∟SAVE2
:Disp "ERROR: DATA CORRUPTED
```

#### Backwards Order

To get both lists the same and into reverse order:

```
:seq(∟SAVE1(I),I,dim(∟SAVE1),1,-1→SAVE2
```

Checking to make sure both lists are the same:

```
:If not(min(∟SAVE1=seq(∟SAVE2(I),I,dim(∟SAVE2),1,-1
:Disp "ERROR: DATA CORRUPTED    // same as above, can change error type
```

#### CoSinTan Method

Simple, just add all the list elements except for the last one, then get sin(, cos(, or tan( of it. Then just store the result into the last element.

```
:sin(sum(∟SAVE,1,dim(∟SAVE)-1→∟SAVE(dim(∟SAVE
```

Obviously "dim(∟SAVE)" should be replaced with the dimensions of your save list, to save bytes. You can also replace sin( with any trigonometric function, such as tanh(, for added protection. Also make sure to execute a Degree or Radian command, to avoid the user being suspected for corrupting data if he's only changed a mode setting...
