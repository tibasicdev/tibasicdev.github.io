# Area
|Routine Summary|Inputs|Outputs|Variables Used|
|--- |--- |--- |--- |
|Finds the area of any regular polygon.|N,S|F|A,B,F,N,P,S,V|

```
:ClrHome
:Input "NUMBER OF SIDES: ",N
:Input "SIDE LENGTH: ",S
:NS^2/(4tan(180/N→F
:Pause F
:ClrHome
```

This program uses the tangent ratio to find the area of a regular polygon when giver the number of sides and side length.
