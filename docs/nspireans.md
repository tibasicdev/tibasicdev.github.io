![Ans](nspire_ans/sample.png "Ans")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|
|--- |--- |--- |
|A short description of what the command does.|The generic syntax of calling the command, with arguments.|If this is only available on certain versions of the nspire|

### Menu Location
Describe how to get the command from a menu.

# Ans

The `Ans` variable holds the last answer that was stored in the calculator. Because `Ans` is stored in a special storage area built-in to the calculator, and it is extensively used by the calculator, you cannot delete it. Ans is also useful; it can make your programs both smaller and faster:

- Unlike other variables which have a value type hard-coded in (i.e., a [string](strings.html) can only hold text, and [lists](lists.html) and [matrices](matrices.html) can only hold numbers), `Ans` can take on whatever value you want: a real or complex, list, matrix, or string are all acceptable.
- Along with the [finance](system-variables.html#finance) variables, `Ans` is faster than the real, complex, list, matrix, and string variables; and subsequently, you should try to use it as much as possible.

One of the most common places to use `Ans` is in place of storing a value to a variable. Just paste the `Ans` variable to the location where the variable was called, and then when the expression is evaluated, the calculator will use the current value of `Ans`. Using the `Ans` variable allows you to eliminate the variable, which helps save a little or a lot of memory (depending on the type of variable and its size).

```
30+5A→B
Disp 25A,30+5A
;can be
30+5A
Disp 25A,Ans
```

The one major drawback to using `Ans` is that its current value is only temporary. Whenever you [store](store.html) a value to a variable or place an expression or string on a line by itself, `Ans` is updated to the new value. This restriction essentially limits your use of `Ans` to only a single variable. If you are manipulating two or more variables, it's best to just use the variables.

There are several cases in which changing the value of a variable does not modify `Ans`, thus preserving its current value for later use: 
- storing to an [equation variable](system-variables.html#equation) 
- using the [`nspire:DelVar`](nspire:delvar.html) command to delete a variable (i.e., set its value to zero, if it's a real variable)
- initializing or changing the value in a [`nspire:For(`](nspire:for.html) loop.
These cases can be very useful, allowing you to use Ans to store an expression rather than create a temporary variable for it.
