# Random Lines
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Displays random lines.|None|None|A, B, C|[file randomlines.zip]|

```
:ClrDraw
:ZStandard
:Delvar ADelvar B
:Repeat getKey
:randInt(Xmin,Xmax→C
:randInt(Ymin,Ymax
:Line(A,B,C,Ans
:Ans→B:C→A
:End
```

Before we can start displaying random lines on the graph screen, we need to perform some basic [setup](setup.html). We then create two variables for the first (X,Y) coordinate by setting their initial values to zero. Once inside the Repeat loop, we randomly select the second (X,Y) coordinate for the line. (Please note we didn't need to store the second variable, since [Ans](ans.html) is able to hold a numeric value, and it is also faster.)

Now that we have the two coordinates for the line figured out, we draw the line on the screen and store the first coordinate values to the second coordinate values, i.e., the second coordinate becomes the new first coordinate. This gets repeated over and over again until you press a key.
