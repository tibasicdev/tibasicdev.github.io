![The expr() Command](68k_expr/expr.png "The expr() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Runs code stored inside a string.|expr(*string*)|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press MATH to enter the MATH popup menu.
- Press D to enter the Strings submenu.
- Press 2 to select expr(.
       
# The expr() Command

The expr() command runs code stored inside a string: for instance, expr("5→x") has the same effect as 5→x. The main use of expr() is with user input: the input you get from some commands comes in a string, and you might use expr() to convert it back to a number.

The other advantage of using expr() is that you can paste together code as the program is running, to run something you couldn't possibly have put in the program ahead of time. For instance, you might paste together a [68k:Dialog](68k:dialog.html)..EndDlog block whose elements might be different every time you run the program.

```
:expr("5→x")
           5
:expr("25")
          25
```

The expr() command is somewhat limited in what it is allowed to do. For instance, if a string contains a variable name, expr() of that string returns the *value* of that variable; to refer to the variable itself, use the # ([68k:indirection](68k:indirection.html)) operator.

Another limitation is that expr() cannot contain commands that aren't allowed on the home screen, even if you're running it from a function or program. For example, [68k:Local](68k:local.html) will cause an error in expr().

Finally, in some respects expr() is actually running in its own program. It will still be able to access local variables from outside the expr(), but [68k:Lbl](68k:lbl.html) and [68k:Goto](68k:goto.html) are limited — you can't jump out of expr() with them, nor can you jump in.

## Advanced Uses

It's best to use expr() sparingly. Characters inside a string are ignored during [68k:tokenization](68k:tokenization.html), so they will take up more space than actual commands, and there will be a short delay before the code inside expr() can run.

This also causes problems with language localization. Normally, once a command is tokenized, it will work in any language. However, with expr(), code is tokenized on the spot, so it will depend on the language being the same. If your program was written using English language localization, it will not work for someone who's working in German, Spanish, or French.

## Error Conditions



## Related Commands

- # ([68k:indirection](68k:indirection.html))
- [68k:string()](68k:string().html)
- [68k:ord()](68k:ord().html)
