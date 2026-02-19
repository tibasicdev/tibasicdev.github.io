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



[[row]]
[[cell]]11[[/cell]]
[[cell]]12[[/cell]]
[[cell]]13[[/cell]]
[[cell]]14[[/cell]]
[[cell]][[/cell]]
[[cell]]15[[/cell]]
[[/row]]
 
[[cell]][[/cell]]
[[cell]][[/cell]]
[[cell]][[/cell]]
[[cell]][[/cell]]
[[cell]]25[[/cell]]
[[cell]][[/cell]]
[[/row]]
[[row]]
[[cell]]21[[/cell]]
[[cell]]22[[/cell]]
[[cell]]23[[/cell]]
[[cell]]24[[/cell]]
[[cell]][[/cell]]
[[cell]]26[[/cell]]
[[/row]]
[[row]]
[[cell]]31[[/cell]]
[[cell]]32[[/cell]]
[[cell]]33[[/cell]]
[[cell]][[/cell]]
[[cell]]34[[/cell]]
[[/row]]
[[row]]
[[cell]]41[[/cell]]
[[cell]]42[[/cell]]
[[cell]]43[[/cell]]
[[cell]]44[[/cell]]
[[cell]]45[[/cell]]
[[/row]]
[[row]]
[[cell]]51[[/cell]]
[[cell]]52[[/cell]]
[[cell]]53[[/cell]]
[[cell]]54[[/cell]]
[[cell]]55[[/cell]]
[[/row]]
[[row]]
[[cell]]61[[/cell]]
[[cell]]62[[/cell]]
[[cell]]63[[/cell]]
[[cell]]64[[/cell]]
[[cell]]65[[/cell]]
[[/row]]
[[row]]
[[cell]]71[[/cell]]
[[cell]]72[[/cell]]
[[cell]]73[[/cell]]
[[cell]]74[[/cell]]
[[cell]]75[[/cell]]
[[/row]]
[[row]]
[[cell]]81[[/cell]]
[[cell]]82[[/cell]]
[[cell]]83[[/cell]]
[[cell]]84[[/cell]]
[[cell]]85[[/cell]]
[[/row]]
[[row]]
[[cell]]91[[/cell]]
[[cell]]92[[/cell]]
[[cell]]93[[/cell]]
[[cell]]94[[/cell]]
[[cell]]95[[/cell]]
[[/row]]
[[row]]
[[cell]][[/cell]]
[[cell]]102[[/cell]]
[[cell]]103[[/cell]]
[[cell]]104[[/cell]]
[[cell]]105[[/cell]]
[[/row]]
[[/table]]
