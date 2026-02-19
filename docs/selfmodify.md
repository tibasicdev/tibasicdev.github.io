# Self-Modifying Code (SMC)
| ||~ Equation Variables |
| Function | Y<sub>0</sub>-Y<sub>9</sub> |
| --- | --- |
| Parametric | X/Y<sub>1T</sub>-X/Y<sub>6T</sub> |
| --- | --- |
| Polar | r<sub>1</sub>-r<sub>6</sub> |
| --- | --- |
| Sequence | u, v, w |
| --- | --- |


Self-modifying code (SMC) is code that changes itself while it is executing. While TI-Basic does not provide support for SMC like it is found in other programming languages, TI-Basic does allow you to implement a primitive form of SMC using the [equation variables](system-variables.html#equation) that are used when graphing an equation on the graph screen.

The function, parametric, and polar graphing variables are accessible in the VARS menu (options 1, 2, and 3 respectively), while the sequence graphing variables are accessible on the keypad by pressing 2nd 7, 8, and 9 respectively.

Each of these variables is the same size, so there is no real difference between which variable you use. However, since sequence graphing is the least used graphing mode, the sequence variables are probably the best variables to use when using SMC.

## How does it Work?

While the equation variables are primarily used for graphing, they are actually stored internally as [strings](strings.html) by the calculator. The string operations and commands do not work on them, however, but you can store a string to them and evaluate them in an expression.

Just like how you can evaluate an expression stored in a string using the [expr(](expr.html) command, the equation variables can be used the same way implicitly. The expression can contain whatever combination of numbers, variables, and functions that you want, just as long as they evaluate to a number or list of numbers.

For a simple example, let's initialize X with a value of 2 and store the expression "50X" to u:

```
:2→X
:"50X→u
```

When you access u, it will have a value of 100. But what would happen to the value of u if you changed the value of X to 5? Well, because the value of u depends on the value of X, u would change accordingly, and it would now have a value of 250. This is the basic premise of SMC: You can modify a variable elsewhere, and it will automatically update the respective equation variable. Hence, a program can change how it runs.

As it turns out, finding an occasion to use this technique is usually rare, so here is a made-up example. This program will count up and down with the arrow keys until you press ENTER. If you press 2ND, however, it will switch the order of the keys:

```
:5→A
:"(Ans=25)-(Ans=34→u        // initial expression for u
:Repeat Ans=105
:A+u→A
:Disp Ans
:Repeat Ans:getKey:End      // wait for a keypress
:If Ans=21
:"(Ans=34)-(Ans=25→u        // switch the arrow keys
:End
```

## Advanced Uses

While just using SMC for simple expressions doesn't really add any additional value to your programs, you can use it for more complicated purposes. One common situation is [optimization](optimize.html).

If you have a lengthy command or formula that you use multiple times throughout your program, you can simply store the statement to an equation variable, and then use the equation variable whenever you want to call the statement. This eliminates duplicate code, which makes your program smaller.

For example, if you want to generate a random integer from 1 to 9, here is what you would use:

```
:"randInt(1,9→u
```

Then each time you wanted to create a random integer, just use u.

## Limitations of SMC

There are a few limitations you need to be aware of when using SMC:

- It complicates your code, making it difficult to understand and maintain. This is why you should primarily stick to implementing SMC when you are done with your program.
- The equation variables will affect the graph settings, and likewise the graph screen will be affected if the respective graph mode is enabled.
- You can't store the equation variable to itself, or other variables, if they don't have a matching type (i.e., trying to store a string to a real will result in an [ERR:DATA TYPE](errors.html#datatype) error).
- Don't abuse SMC; the extra step of reading and executing through variables may slow down your code slightly and even cost a number of bytes if used improperly, so wield it wisely (i.e., only for the benefits it provides over other methods).
