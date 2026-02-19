![The round() command](68k_round/Round.png "The round() command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Truncates a number to a specified number of decimal places.|round(*value*[,*number of decimal places to round to*])|This command works on all calculators.|1 byte|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 1 to enter the Number submenu.
- Press 3 to select round(.
       
# The round() command
The round command takes whatever value you give it, and it rounds the value to a given number of decimal places. For instance round(9.7,0) will return 10, since rounding to 0 decimal places will return the closest whole number. Another example would be if you entered round(5.46338,3) which would return 5.463, since it rounded 5.46338 to 3 decimal places. The round function can round 0 to 12 decimal places, and if you enter a value outside that range, you will get a domain error. Strangely enough, if you enter an imaginary number into the round() command, nothing happens and the calculator returns the same function in a simplified form.

```
:round(99.35847475,5)
:         99.35847
:round(4.392i,2)
:         round(4.392*i,2.)
:round(2.348972,2i)
:         round(2.348972,2*i)
```

## Unexpected results

Your calculator may also round, say for instance if you do this:
```
:round(2.4573485645,11)
```
If your calculator is set to float or to fix at 10 or less, the calculator will round the number that comes out of the function. The function above should return 2.4573485645, since that is less than 11 digits, but if your calculator is set to "Float 6" it will return 2.457349 instead of what you expected.

## Error Conditions



## Related Commands

- [68k:ceiling()](68k:ceiling().html)
- [68k:floor()](68k:floor().html)
- [68k:iPart()](68k:ipart().html)
- [68k:int()](68k:int().html)
