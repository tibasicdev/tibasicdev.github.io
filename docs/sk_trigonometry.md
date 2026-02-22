# Trigonometry
|This article is currently in development. You can help TI-Basic Developer by expanding it. |
| --- |

Besides standard math, trigonometry functions are helpful for simulating rotation and making games like [http://en.wikipedia.org/wiki/Asteroids_(video_game) Asteroids].
## Key Commands
The trigonometric commands are [sin](sin.html), [cos](cos.html) and [tan](tan.html).
sin(θ) returns the sine of θ, which is defined as the y-value of the point of intersection of the unit circle and a line containing the origin that makes an angle θ with the positive x-axis.
cos(θ) returns the cosine of θ, which is defined as the x-value of the point of intersection of the unit circle and a line containing the origin that makes an angle θ with the positive x-axis.
tan(θ) returns the tangent of angle θ, which is defined as $\frac{\sin \theta}{\cos \theta}$
It is slightly unnecessary, as most games that use trigonometry only require sin and cos. 

Let's say you are making an object firing simulation and you are keeping track of the angle θ. When you fire, you can increment the location variables X and Y with speed a and angle θ using these formulas:
```
X+Acos(θ→X
Y+Asin(θ→Y
```
## Examples

The following code illustrates and then calculates the area of a rectangle inscribed in a circle after the user presses [Enter].
```
Input "RADIUS: ",R
Input "ANGLE: ",θ
AxesOff
ZSquare
Rcos(θ→A
Rsin(θ→B
Circle(0,0,R
Line(0,0,A,B
Line(A,B,A,­B
Line(A,B,­A,B
Line(­A,­B,­A,B
Line(­A,­B,A,­B
Pause 
4abs(AB
```


The following code awaits the user to input an angle to fire at, using a [line](line.html) to guide, and fires a projectile at that angle until the user presses [Clear]
```
:AxesOff
:DelVar XDelVar θDegree
:ClrDraw
:94→Xmax
:62→Ymax
:0→Ymin
:Ans→Xmin
:Repeat K=21
:Line(0,0,2cos(θ),2sin(θ
:Repeat Ans
:getKey→K
:End
:Line(0,0,2cos(θ),2sin(θ),0
:max(0,min(90,θ+(Ans=25)-(Ans=34→θ
:End
:Repeat K=45
:X+2cos(θ→X
:Y+2sin(θ→Y
:Pt-On(X,Y
:getKey→K
:End
```

Of course, Earth has gravity, doesn't it? We can account for that pretty easily. To simplify the problem, we'll just assume that Earth is flat and that the projectile follows a parabolic path:
```
:AxesOff
:DelVar XDelVar θDegree
:ClrDraw
:94→Xmax
:62→Ymax
:0→Ymin
:Ans→Xmin
:Repeat K=21
:Line(0,0,2cos(θ),2sin(θ
:Repeat Ans
:getKey→K
:End
:Line(0,0,2cos(θ),2sin(θ),0
:max(0,min(90,θ+(Ans=25)-(Ans=34→θ
:End
:2sin(θ→G
:Repeat K=45
:X+2cos(θ→X
:Y+G→Y
:G-.05→G    // :D Now it follows a parabolic path! You can change gravity by changing this number.
:Pt-On(X,Y
:getKey→K
:End
```
<center>

|**[<< Probability](sk:probability.html)**|**[Table of Contents](starter-kit.html)**|**[Complex Numbers >>](sk:complex.html)**|
| --- | --- | --- |

</center>
