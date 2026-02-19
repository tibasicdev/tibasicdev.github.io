# Angle of Intersection
This code finds the angle of intersection of two lines. 

|Routine Summary|Inputs|Outputs|Variables Used|Authors|
|--- |--- |--- |--- |--- |
|Finds the angle of intersection for any two lines.|Str1 and Str2|Ans|Y1, Y2, I, Ans, X|, |

```
:Degree
:Str1→Y1
:Str2→Y2    \\If your equations are already stored in Y1 and Y2, these two lines are unneccessary
:E‾9→I      \\This threshold can be changed to adjust the output accuracy
:angle(I+i(Y2(X+I)-Y2(X
:Ans-angle(I+i(Y1(X+I)-Y1(X
:Disp "ANGLE OF INTERSECTION IS",Ans
```

The routine works by assuming the graphs are almost straight lines at a very small scale around the point of intersection given by X. The two graphs are approximated by complex numbers made by combining the x and y coordinates. The [angle(](angle.html) command finds the angle for each complex number, then they are subtracted. This command is useful as it avoids domain errors caused by using [tanֿ¹(](arctan.html).

If you do not already know the x-coordinate of the intersection of the two graphs, you can add this line at the beginning to find it:

```
:solve(Y2(X)-Y1(X)=0,X,0→X
```
