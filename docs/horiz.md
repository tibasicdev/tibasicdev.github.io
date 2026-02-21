![The Horiz Command](horiz/HORIZ.gif "The Horiz Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sets the screen mode to Horiz.|Horiz|TI-83/84/+/SE|1 byte|

### Menu Location
In the program editor,
1. Press [MODE]
2. Press [DOWN] seven times
3. Press [RIGHT]
4. Press [ENTER] to insert Horiz
       
# The Horiz Command

`Horiz` is usually at the beginning of a program. It is used at the beginning to ensure that the screen mode is `Horiz`, for programs such as Hangman that want to use [`Input`](input.html) but also have the graph screen shown. Note that if you use pixels, the y-coordinate can be no larger than 30, since that is the maximum pixel's range.

```
:Horiz
```

## Related Commands

- [`Full`](full.html)
- [`G-T`](g-t.html)
