# Stack
A stack is an abstract data structure that stores objects in a Last In First Out basis. The two main operations that can be performed on a stack are *push* and *pop*. *Push* adds an element to the top of a stack. *Pop* removes the top element from the stack, and returns it. A stack can be visualized as a stack of plates in a spring-loaded cafeteria stack. Only the top plate can be accessed, and plates can be placed onto the top of the stack, or removed from the top of the stack. 

Stacks are used in virtually every computer architecture out there, in almost all operating systems, and in many higher-level programs as well. In fact, the TI operating system juggles two stacks (one for operations and one for numbers) to evaluate mathematical expressions, using a modified version of the [shunting yard algorithm](https://en.wikipedia.org/wiki/shunting-yard_algorithm). And every time your program runs another program, a stack is used: to keep track of the programs to return to.

## Reasons to Use Stacks

In general, stacks are frequently related to [recursion](glossary.html#recursion) — programs or routines that call on themselves again to do their jobs. In most modern languages, the use of stacks is hidden from the program through the use of local variables: variables that one program uses that another can't modify. In TI-Basic, all variables are global, and accessible to all programs, so you'll need to create your own stack almost every time you write a recursive program.

This is best illustrated with a classic example: calculating the factorial of a number N, written N! (there is already a [factorial](factorial.html) operation in TI-Basic, but pretend it doesn't exist for now). The factorial of N is defined recursively: N! = N*(N-1)! (with 1! and 0! being defined as 1). The actual code for a stack will be given in the next few sections; for now, let the fictional instructions Push(N) and Pop stand in for them.

**prgmFACT**
```
If N≤1:Then
1→F
Else
Push(N)
N-1→N
prgmFACT
Pop→N
FN→F
End
F
```
Here, the Push and Pop are necessary to save the value of N, because each time prgmFACT runs, it has a different value of N in mind. 

Observe that the behavior of Pop isn't defined when the stack is empty. In fact, you'll see in the next section that most ways of implementing a stack will crash when you try to do that. In most cases, you can watch your code to make sure that pushes and pops come in pairs, to prevent this from happening — in the program above, each Pop has a corresponding Push. The only exception might be if you're trying to deal with user input (such as evaluating a mathematical expression) — in this case, bad input might cause this error, so you should always make sure to check if the stack is empty.

## Implementation in TI-Basic

TI-Basic does not have a stack data structure by default, but depending on what needs to be stored, a stack can be implemented as either a list or a string.

### Lists

You might consider two approaches to make a stack using a list: either the first element or the last can be considered the "top" of the stack. In practice, it's best to make the top be the end of the list — if it were at the front, the entire list would need to be shifted around in memory every time that an element got pushed or popped, which is much slower even for relatively small lists, and would get slower and slower for large ones.

To create the stack, just store 0 to its size: this will create the list if it doesn't exist, and make sure it has no elements in it.
```
:0→dim(L₁
```

Pushing to the stack is simple: to push a number N, the code is
```
:N→L₁(1+dim(L₁
```
This increases the size of the list, and stores N to the last element.

Popping of the list is done by getting the value of the last element and then decreasing the list size. This can be done with the following code:
```
:L₁(dim(L₁→N
:dim(L₁)-1→dim(L₁
```

If the stack is empty, this will cause an error: dim(L₁) will be 0, but L₁(0) is out of bounds. 

### Strings

The main difference between strings and numbers is that strings can be of any length. As a result, to separate the entries in the stack, we'll use a delimiter: a short string that will **never** appear in the entries of the stack. This delimiter will depend on what you're storing in the stack. In this code, we'll use the string "::" as the delimiter.

To create the stack, just store any single character (preferably *not* the delimiter) into the string you're going to use (we'd like the string to be empty, but empty strings aren't allowed in TI-Basic, so we'll go with the next best thing):
```
:"?"→Str0
```

For strings, we're going to think of the beginning of the string as the top of the stack — the reasons why will become clear later on. So to push an element to the stack, we're going to add the new data (Str1) to the beginning of the string, and a delimiter to separate it from everything else:
```
:Str1+"°"+Str0→Str0
```

To pop the data off the string, use the [inString(](instring.html) function for find the first instance of the delimiter (this is why we're working with the beginning of the string — it's much harder to find the *last* instance). Everything before the delimiter is the element we're going to pop, but we want to remove the delimiter as well:
```
:inString(Str0,"°→N
:sub(Str0,1,N-1→Str1
:sub(Str0,N+1,length(Str0)-N→Str0
```

A critical observation is that this code depends on the length of the delimiter (in our case, it's 1). In general, for a delimiter of length K, replace the last line with the following (simplified, of course):
```
:sub(Str0,N+K,length(Str0)-N-K+1)→Str0
```

If the stack is empty, the string will contain no delimiters at all, so inString( will return 0, and an error will occur when we try to take sub(Str0,1,0). This gives a quick way to check if the stack is empty: just take the first line of the pop code.
