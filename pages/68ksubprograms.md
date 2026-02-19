# Subprograms
A long program can get complicated to manage when it's all in one piece. For this reason, it's often easier to write code with a main program that does its job by running several other programs called subprograms. In fact, it's fairly easy to start using this method from the [68k:planning](68k:planning.html) stage.

There are other benefits to using subprograms, of course. It's good to define a subprogram for a task that needs to be done more than once. Also, a subprogram can run itself recursively, if necessary.

Of course, you don't want to release a finished program in lots of pieces, so at the end of the day, you want to incorporate the subprograms in the main program. If the subprogram isn't recursive and is only used once, this is easy: just use 2nd RCL to recall the subprograms into the place where they're used, and remove their [68k:Prgm](68k:prgm.html)..EndPrgm parts. See the next section for what to do in more difficult cases.

## Defining a Subprogram

You can also define a subprogram right in your main program. This is done using the [68k:Define](68k:define.html) statement:

```
:Define subprgm()=Prgm
: © subprogram code
:EndPrgm
```

It's easiest if all the subprograms are defined at the same time, near the beginning of the program, but it doesn't really matter where you do it as long as you define the subprogram before you use it.

## Cleaning Up

It's important to realize that a subprogram defined in this way is just like a regular variable. If you don't do anything, then after the main program finishes running, the subprogram will be left hanging around, which is usually not a good thing. As with other variables, there are several ways to clean this up:
- Use [68k:Local](68k:local.html) to declare the subprograms as local variables (e.g. Local subprgm1, subprgm2).
- Use [68k:DelVar](68k:delvar.html) at the end of the program to delete the subprograms (e.g. DelVar subprgm1, subprgm2).
- Give the programs one-letter names, and use [68k:NewProb](68k:newprob.html) at the end of the program.

See [68k:Setup and Cleanup](68k:setup-and-cleanup.html) for more information on how to do this.

<center>

|**[<< System Variables](68k:sys-variables.html)**|**[Overview](68k:techniques-overview.html)**|**[Saving Data >>](68k:saving-data.html)**|
| --- | --- | --- |

</center>
