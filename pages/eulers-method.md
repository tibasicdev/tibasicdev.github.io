# Eulers Method
|Routine Summary|Inputs|Outputs|Variables Used|Author|Authors|Download|
|--- |--- |--- |--- |--- |--- |--- |
|Approximates a future value of a given function.|*X* - Initial X-Value<br>*Y* - Initial Y-Value<br>*Str1* - The equation<br>*D* - X-value at which the Y-value is approximated|*U* - X-value approximation<br>*V* - Y -value approximation|E, C, H, X, U, Y, Y1, V|Xeda Elnara, who optimized Myles_Zadok's optimization of the routine linked to below:|The Mathematics Department at the University of Arizona|http://tibasicdev.github.io/local—files/routine-page/routine.zip routine.zip|
Please note that there may be a graphical bug that displays the token <sup>-1</sup> as <sup>1</sup>.
```
:"INITIAL-
:Input Ans+"X=",X
:Input Ans+"Y=",Y
:Input "EQN=",Str1
:Str1→Y1
:Input "FINAL-X=",D
:Input "NO. OF ITERATIONS=",E
:Eֿ¹(D-X→H
:For(I,1,E
:ClrHome
:Y+Y1H→Y
:X+H→X
:ClrHome
:Disp "STEP",I,"X=",X,"Y=
:Pause Y
:End
```


Euler's method is used to predict the value of a function at a higher value than the initial value. The initial x- and y-values are used to find the y- value at the desired x-coordinate of the given function. Multiple iterations are done to reach a better approximation.

## Related Routines

- [Newtons Method](newtons-method.html)
