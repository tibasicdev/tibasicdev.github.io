# Temperature Conversion
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Converts temperature to Fahrenheit, Celsius, or Kelvin.|*A* - the starting temperature value|None|A, B, C|Weregoose|[file temperatureconversion.zip]|

```
:Input A:0
:Menu("  Convert From  ","F",0,"C",1,"K",2
:Lbl 2:Ans+1
:Lbl 1:Ans+1
:Lbl 0:Ans→B
:For(C,0,2
:A-273.15(2B>C+2
:If Bnot(C
:1.8Ans+32
:If Cnot(B
:5/9(Ans-32
:Disp sub("FCK",C+1,1),Ans+273.15(B+2<2C
:End
```

With the temperature value stored in A, we ask the user to select which temperature format they want to convert it to — *F*ahrenheit, *C*elsius, or *K*elvin — and then initialize the B variable to the appropriate value that matches up with the format associated with it (K is 2, C is 1, and F is 0).

We then use a [For(](for.html) loop to display what the respective temperature value would be in the other temperature formats, based on the respective temperature conversion formulas:

| |~ Fahrenheit |~ Celsius |~ Kelvin |
| Fahrenheit | | (9C/5)+32 | 9(K-273.15)/5+32 | 
| --- | --- | --- | --- |
| Celsius | 5(F-32)/9 | | K-273.15 |
| --- | --- | --- | --- |
| Kelvin | 5(F-32)/9+273.15 | C+273.15 | |
| --- | --- | --- | --- |

One thing you will probably notice is that the formulas aren't exactly the same in the code. The reason is because the code is designed to be optimized, and rather than displaying each temperature conversion by itself, you can simply add the respective formulas as modifiers and display all of the temperature conversions together.
