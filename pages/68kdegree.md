![The ° Command](68k_degree/degree.png "The ° Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts an angle to degrees, if necessary.|*angle*°|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.<br>* Press 2 to enter the Angle submenu.<br>* Press 1 to select °.
# The ° Command

The ° symbol used after an angle makes sure the angle is interpreted as being in degrees. If the calculator is already in degree mode, x° is equal to x; in radian mode, x° is equal to π*x/180; and in gradian mode, x° is equal to 10*x/9.

If you're using degree measure extensively in a program, it's a better idea to use [68k:setMode()](68k:setmode().html) to switch to degree mode and not worry about this. However, there are two reasons you might want to use °:
- If you need an angle in degrees only once or twice, don't bother changing the mode setting.
- In a function, you're forced to use °, since setMode() isn't valid in a function. 

In radian mode:
```
:sin(30)
           sin(30)
:sin(30°)
           1/2
:180°
           π
```

In degree mode (no conversion is necessary, so no conversion is done):
```
:sin(30)
           1/2
:sin(30°)
           1/2
:180°
           180
```

Another possible use of ° is to write an angle in degrees, minutes, and seconds as x°y'z" (using the usual apostrophe and quote symbols) — this stands for x degrees, y minutes (equal to 1/60th of a degree) and z seconds (equal to 1/60th of a minute). There's no "degree/minute/second" mode setting, so an angle entered in this form will always be simplified: first to (x+y/60+z/3600)<sup>2</sup> degrees, and then (if necessary) converted to the correct angle measure. However, you can use [68k:▶DMS](68k:-dms.html) to express output in this form.


## Related Commands

- <sup>[r](68k:radian.html)</sup> (radian)
- <sup>[G](68k:gradian.html)</sup> (gradian)
- [68k:▶DD](68k:-dd.html)
- [68k:▶DMS](68k:-dms.html)
