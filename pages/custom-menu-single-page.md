# Custom Menu Single Page
Simple homescreen menu without using the menu( command.

```
ClrHome
Disp ">OPTION 1"," OPTION 2"," OPTION 3     // note the spaces before OPTION 2 and OPTION 3
1->A
Repeat Ans=105
If Ans
Output(A,1,"                               // one space
min(3,max(1,A+sum(List(Ans={25,34->A       // the List has an implied delta sign (triangle) before it.
Output(A,1,">
getKey
End
If A=1
Disp "OPTION 1 ACTION
If A=2
Disp "OPTION 2 ACTION
If A=3
"OPTION 3 ACTION
```

Simple graphscreen menu.

```
ClrDraw
Horizontal Ymin
Horizontal Ymax
Vertical Xmax
Vertical Xmin
Text(-1,3,35,"MENU
Text(20,25,">OPTION 1
Text(26,29,"OPTION 2
Text(32,29,"OPTION 3
20->A
Repeat Ans=105
If Ans
Text(A,25,"                                                              // Four spaces
min(32,max(20,Ans+6sum(List(Ans={25,34->A               // The "List" has an implied delta (little triangle) before it.
Text(A,25,">
getKey
End
If A=20
Disp "OPTION 1 ACTION
If A=26
Disp "OPTION 2 ACTION
If A=32
"OPTION 3 ACTION
```


You can adjust the Text( values to determine what spacing you would like.
