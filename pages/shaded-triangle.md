# Shaded Triangle
|Routine Summary|Inputs|Variables Used|
|--- |--- |--- |
|Draws a triangle on the graph screen.|L1 - X-coordinates of 3 vertices<br>L2 - Y-coordinates of 3 vertices<br>S - Whether it is shaded<br>D - draw if 1, erase if 0|L1, L2, S, D, M, N, B, C|

```
:If S
:Then
:SortA(L1,L2)
:If L1(2)≠L1(1)
:Then
:(L2(2)-L2(1))/(L1(2)-L1(1))→M
:L2(1)-ML1(1)→B
:(L2(3)-L2(1))/(L1(3)-L1(1))→N
:L2(1)-NL1(1)→C
:For(I,L1(1),L1(2),ΔX)
:Line(I,MI+B,I,NI+C,D)
:End
:End
:If L1(2)≠L1(3)
:Then
:(L2(3)-L2(2))/(L1(3)-L1(2))→M
:L2(3)-ML1(3)→B
:For(I,L2(2),L1(3),ΔX)
:Line(I,MI+B,I,NI+C,D)
:End
:End
:Else
:Line(L1(1),L2(1),L1(2),L2(2),D)
:Line(L1(1),L2(1),L1(3),L2(3),D)
:Line(L1(2),L2(2),L1(3),L2(3),D)
:End
```

This is a routine to draw a shaded triangle, with an option to draw an unshaded triangle too.

## Error Conditions

- **[ERR:DIM MISMATCH](errors.html#dimmismatch)** is thrown if L1 and L2 have different dimensions.

## Related Routines

- [Shading Circles](http://tibasicdev.github.io/shading-circles)
