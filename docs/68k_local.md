![The Local Command](68k_local/local.png "The Local Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Declares variables to be local to the current function or program.|Local *var1*[,*var2*,...]|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting in the program editor:
- Press F4 to enter the Var menu.
- Press 3 to select Local.
       
# The Local Command

The Local command declares one or more variables to be local to the function or program it's used in. This means that the program "owns" these variables, so to speak: their values start out undefined, no matter if a variable with the same name was defined outside the program, and the variables will be cleaned up once the program exits. Even subprograms called from the main program can't see the main program's local variables.

Local is useful to avoid leaving lots of variables behind, but you could do that by [deleting](68k:delvar.html) them as well. More importantly, it assures that you won't overwrite any already existing variables. Finally, local variables are the only ones a [function](68k:func.html) can use.

You may get a few local variables for free, without the Local command: these are the parameters to a function or program. For example, if you define the function f(x), you can modify x all you like without the fear of changing any variables outside the function.

## Advanced Uses

The interaction of Local with [68k:expr()](68k:expr().html) is somewhat bizarre. In a way, expr() is a subprogram, so it can't see the local variables of the program that created it. This is a problem with output: for instance, expr("Disp x") will not work properly if x is a local variable. 

In many cases, this doesn't matter: for instance, expr("x^2") may not be able to access the value of x if x is local, but it will return the symbolic value x^2, which will later be simplified in the main program. Things change if there's already a global variable called x defined. In that case, expr("x^2") will not find the local value of x, but it will see the global variable instead, so it will evaluate x^2 based on that value. This isn't usually what you want. But it *does* give you a way to access global variables: expr("x") refers to the global variable x if there is one, and the local variable otherwise.

## Error Conditions




## Related Commands

- [68k:Define](68k:define.html)
- [68k:DelVar](68k:delvar.html)
- [68k:expr()](68k:expr().html)

## See Also

- [68k:setup-and-cleanup](68k:setup-and-cleanup.html)
