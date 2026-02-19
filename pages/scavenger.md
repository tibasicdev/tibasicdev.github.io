# Scavenger
I am working on this game I will post the part of the code that I have finished. If anyone can figure out how to add a score please feel free to edit!

```
Program:SCAVENGER1
:Output(4,4,"LOADING..."
:Fill(0,[A]
:ClrHome
:Disp "DIFFICULTY?"
:Pause
:Menu("CHOOSE","EASY",1,"NORMAL",2,"HARD",3)
:Lbl 1
:ClrHome
:Lbl W
:4->U
:8->V
:Repeat Z=21
:getKey->Z
:If Ans
:Output(U,V," "
:min(8,max(1,U+randInt(-5,5)))->U
:min(16,max(1,V+randInt(-5,5)))->V
:Output(U,Ans,"X"
:5->A
:9->B
:Repeat K=21
:getKey->K
:If Ans
:Output(A,B," "
:min(8,max(1,A+sum(ΔList(Ans={25,34->A 
:min(16,max(1,B+sum(ΔList(K={24,26->B
:Output(A,Ans,"O"
:End
:End
:Goto W
:Lbl 2
:prgmSCAVENGER2
:Lbl 3
:prgmSCAVENGER3
```

Now we need to program SCAVENGER2

```
:ClrHome
```

Now Finally...SCAVENGER3!

```
insert the code here
```
