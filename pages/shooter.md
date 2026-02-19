# Shooter
I am currently working on this program. Check back in later. I will add in the part of the code that I finished. I'm having trouble making the "X" move while the two random targets move so feel free to edit if you figured out how to get it to work.

```
:ClrHome
:4->U
:8->V
:Repeat K=21
:getKey->K
:If Ans
:Output(u,V," "
:min(8,max(1,U+sum(List(Ans={25,34->U //Find the "List" with the triangle before it in the catalog. Same thing with the next line.
:min(16,V+sum(List(K={24,26->V
:1->A
:1->B
:8->C
:16->D
:Repeat getKey or (A=C and B=D)
:Output(A,B," "
:Output(C,D," "
:min(8,max(1,A+randInt(-1,1)))->A
:min(16,max(1,B+randInt(-1,1)))->B
:min(8,max(1,C+randInt(-1,1)))->C
:min16,max(1,D+randInt(-1,1)))->D
:Output(A,B,"O"
:Output(C,D,"Q"
:End
```
