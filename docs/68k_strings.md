# Strings and Their Commands
A string is a collection of letters (usually called *characters*) in order. They are most commonly used for displaying text, although they can be adapted to any purpose. See the [character codes](68k:character-codes.html) page for a table of the characters that can be part of a string.

To write a string, use quote marks around the characters you want it to contain. For example, "Hello" is a string containing the characters H, e, l, l, and o, in that order. Using the [string()](68k:string.html) command, you can also create a string out of any other variable type.

On the TI-68k calculators, strings have an advantage over [lists](68k:lists.html) or [68k:matrices](68k:matrices.html) - they are a [random access](https://en.wikipedia.org/wiki/random_access) structure, which means that accessing the end of the string is just as fast as accessing the end of the string (for a list, on the other hand, the calculator has to go through every previous element of the list to get to an element at the end). Although strings are awkward to access normally, so short strings are at a disadvantage compared to lists, long enough strings will beat out lists and matrices, at least for accessing a specific character.

Except for the constraint of memory, there is no limit to the amount of characters in a string.

## Operations on Strings

There are two special operators that can be used on strings - & ([concatenation](68k:append.html)) and # ([68k:indirection](68k:indirection.html)). The *concatenation operator*, &, joins two strings together - "Hello"&" world" returns "Hello world". The *indirection operator*, #, replaces a string containing the name of a variable by the variable itself - #"f"(x) is the same as f(x) (this can be very powerful, especially for non-algebraic variables such as pictures).

(annoyingly, there is no easy way to type #, on a TI-89. You can select it from the character menu (2nd CHAR, 3, 3) or from the catalog)

The relational operators ([=](68k:equal.html), [≠](68k:not-equal.html), [>](68k:greater-than.html), [≥](68k:greater-than-or-equal.html), [<](68k:less-than.html), [≤](68k:less-than-or-equal.html)) can also be applied to strings. It's easy to see how = and ≠ work: two strings are equal if they are made up of the same characters. For the other relational operators, alphabetical order is used: a string is less than another if it would come before it in a dictionary. But.. not quite — there is a problem with uppercase and lowercase letters. These comparisons are actually done by comparing the [character codes](68k:character-codes.html) of each character in the strings, so all lowercase letters are considered to come after all uppercase letters. That is, "cat"<"dog", as you would expect (because cat comes before dog in the dictionary), but "Dog"<"cat".

The tricky aspect of strings is accessing a character. To do this, you have to use the [mid()](68k:mid.html) command: mid(*string*,*start*,*length*) will return *length* characters from *string*, starting from *start*. As a special case, mid(*string*,*n*,1) will return the *n*<sup>th</sup> character of *string*. Characters are numbered starting from 1.

## String-Specific Commands

Of course, there are several commands specifically designed to be used with strings (though not as many as we'd like). All of them except shift() and rotate() are found in the string menu (Press 2nd MATH to access the popup math menu, then select D:String).

- [char()](68k:char.html)
- [dim()](68k:dim.html)
- [expr()](68k:expr.html)
- [format()](68k:format.html)

- [inString()](68k:instring.html)
- [left()](68k:left.html)
- [mid()](68k:mid.html)
- [ord()](68k:ord.html)

- [right()](68k:right.html)
- [rotate()](68k:rotate.html)
- [shift()](68k:shift.html)
- [string()](68k:string.html)
