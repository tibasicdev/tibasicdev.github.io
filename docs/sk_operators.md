# Operators
This article is currently in development. You can help TI-Basic Developer by expanding it. Do we need this page?

There are four main operations on the calculator that are used widely in programs.  They are the simple addition, subtraction, multiplication, and division.  Although these simple operators are used for simple application, they can be very useful when utilized in advanced matters.



## Addition
Addition is the first operator.  Mostly, the addition operator is used to combine the values of variables or to increase the value of a variable.  It can be used as a counter as well.  However, the addition operator can also be used to increase values in lists and combine strings.  When applied to lists, you can manipulate sprites.

Addition can be used to move sprites.  Well, no duh... Think of this.  In the previous chapter, you learned of [text sprites](sk:text.html).  They are typically a coordinate and at that coordinate, text is displayed to simulate a sprite.  However, addition can be used to move the pixels with a list.  This leads to the discussion of Stat Sprites.

A Stat Sprite is a sprite whose individual coordinates are stored into L<sub>1</sub> and L<sub>2</sub>.  When you turn Stat Plot 1 on, the sprite is automatically displayed onto the graph screen.  Addition can move this sprites really easily.  When you add a constant to a list, the calculator distributes that value across the entire list.  So, instead of adding each individual pixel, you can add the whole list.
```
:1+L₁
:1+L₂
```

## Subtraction

Subtraction is a powerful tool being the opposite of addition.  Although the subtraction operator cannot be used with strings, it can often replace addition.  This operator can be used as a countdown. You can also subtract from lists just like adding.

## Multiplication

Multiplication determines the product of two numbers. For example:

```
5*3
      15
```
TI-Calculators also use implied multiplication for variables by putting them next to each other. This can be handy and simplify math but it means that, unlike most programming languages, only single letters can store a value–Multiple letters are interpreted as each value being multiplied.

```
4*A is the same as 4A.
3→NUM Returns an error.
NUM is interpreted as N*U*M
```

## Division

Division is the opposite of division. It is shown with a slash (/)

```
18/9
      2
```

Fractions also use division. If you are in [MATHRINT](http://tibasicdev.github.io/mathprint-mode) mode on the home screen, it looks like a fraction while otherwise it looks like a bold slash.

<center>

|**[<< Introduction to Math](sk:math-intro.html)**|**[Table of Contents](starter-kit.html)**|**[Numbers Menu >>](sk:numbers.html)**|
| --- | --- | --- |

</center>
