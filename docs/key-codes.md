# Key Codes
![getkey.png](getkey.png "")
![xlib-keys.png](xlib-keys.png "")


The picture to the right top contains the value returned by [getKey](getkey.html) for each keypress. The picture is organized so that the key codes are placed where they would be on the literal calculator. You should note that the [ON] key (the key in the bottom left corner) has no key code, so you cannot check for nor disable it.

If you look at the key codes, you will probably notice that they actually follow a pattern: a key is represented by putting its row and column together. For example, the [ENTER] key is row 10, column 5; therefore, its value is 105. The up, right, and left arrow keys are assumed to be in the second row, and the down arrow key is in the 3rd row.

In case you want to know the key codes while using your calculator, here is a simple program to use:

```
:Repeat Ans=105
:getKey
:If Ans:Disp Ans
:End
```

The picture to the right bottom contains the value returned by the real(8 command when using [xlib](xlib.html). The key placement is somewhat disorganized, but consistent for the most part. The [ON] key will return a value, according to the tutorial, but due to the [ON] break inherent to TI-Basic, it will not be returned.


11
12
13
14

15

 


25


21
22
23
24

26


31
32
33

34


41
42
43
44
45


51
52
53
54
55


61
62
63
64
65


71
72
73
74
75


81
82
83
84
85


91
92
93
94
95


102
103
104
105
