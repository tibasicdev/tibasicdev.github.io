![The getKey() Command](68k_getkey/getkey.png "The getKey() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Returns the last keypress.|getKey()|This command works on all calculators.|3 bytes|
       
### Menu Location
Starting from the program editor:<br>* Press F3 to enter the I/O menu.<br>* Press 7 to paste getKey().
# The getKey() Command

The getKey() command returns the [key code](68k:key-codes.html) of the last keypress. If no key was pressed since the program, function, or expression started running, or since the last getKey() command, getKey() returns 0. It's important to note that once getKey() is used, the keypress is forgotten — even if it's used in the same line! So most of the time you want to store the result of getkey to a variable to use it.

The keypresses that getKey() deals with factor in modifier keys, such as 2nd or alpha. Because of this, it will not respond to the modifier keys pressed by themselves.

This example code using getKey() is commonly used in programs that wait for the user to press a key:
```
:0→key
:While key=0
: getKey()→key
:EndWhile
```

## Advanced Uses

Although the key codes are given in [a table](68k:key-codes.html) on this website, and are listed in your manual, it may be more convenient to write a short function to return key codes for you:

```
:keycode()
:Func
:Local k
:0→k
:While k=0
: getKey()→k
:EndWhile
:k
:EndFunc
```

If you run the function keycode(), it will wait for you to press a key. When you press it, it will return the key code. This function may also be a convenient subroutine in a program that requires waiting for a key in several different places.

## Related Commands

- [Input](68k:input.html)
- [InputStr](68k:inputstr.html)
- [Prompt](68k:prompt.html)

## See Also

- [Key Codes](68k:key-codes.html)
