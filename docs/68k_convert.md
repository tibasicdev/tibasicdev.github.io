![The ▶ Command](68k_convert/convert.png "The ▶ Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts an expression from one unit to another.|*expression*▶*units*|This command works on all calculators.|2 bytes|
       
### Menu Location
Press [2nd][▶] to enter ▶: this is<br>* [2nd][MODE] on a TI-89 or TI-89 Titanium<br>* [2nd][Y] on a TI-92, TI-92 Plus, or Voyage 200
# The ▶ Command

The ▶ operator converts an expression to a different unit. Usually, this refers to the built-in units (such as _m (meters), _mph (miles per hour, etc.) which you can select from the UNITS menu.

To use it, you must first have the expression on the left in terms of some unit — this is done by multiplying it by that unit. For instance, "5 meters" is written as 5_m or 5*_m (where _m is the unit). You can combine units as well: for instance, 5_m^2 (5 square meters) or 30_km/_hr (30 kilometers per hour).

To convert that into a different unit, type ▶ and then a different unit to convert to (again, you can combine units). For instance, to convert 5 square meters to acres, type 5_m^2▶_acre. (Note: the result will always be expressed as a decimal)

```
:30_km/_hr▶_m/_s
           8.33333*_m/_s
:5_N▶_dyne
           500000.*_dyne
```

You can't use ▶ to convert between units of temperature (degrees Celsius to degrees Fahrenheit, for instance), since the calculator isn't sure if you mean absolute temperature or a change in temperature instead. Use the [68k:tmpCnv()](68k:tmpcnv().html) and [ΔtmpCnv()](68k:deltatmpcnv.html) commands instead.

## Advanced Uses

It's possible to define your own units as well: units are just any variable beginning with an underscore, and ▶ will perform just as well converting between those. There are two ways to go about it. The first is to define your units in terms of existing ones: for instance, you might define a furlong (one-eighth of a mile) as follows:
```
:1/8_mi→_furlong
           1/8*_mi
:110_yd▶_furlong
           .5*_furlong
```
The second method is to start with a unit or several units to keep undefined (for instance, _x). You can then define other units in terms of _x, and convert between them:
```
:5_x→_y
           5*_x
:3_y▶_x
           15.*_x
:10_x/_s▶_y/_s
           2.*_y/_s
```
Units are treated just like variables, except that they're universal across folders: you can have only one instance of _x, and you can access it as _x no matter which folder you're in. You can use this if you want to define a universal variable to access in any folder: for instance, if you define a program as _prgm(), you can run it with _prgm() from any folder.

## Error Conditions



## Related Commands

- [68k:getUnits()](68k:getunits().html)
- [68k:setUnits()](68k:setunits().html)
- [68k:tmpCnv()](68k:tmpcnv().html)
- [ΔtmpCnv()](68k:deltatmpcnv.html)

## See Also

- [68k:order-of-operations](68k:order-of-operations.html)
