# Optimization Exercises
**Here are some review exercises to help you practice your optimization skills.**

------

**1**. Write a program that, given a string in Ans containing letters A-Z, will return a list with the alphabetic positions of those letters.
Example:
```
"AZ
              AZ
prgmLETTONUM
Ans
           {1,26}
```


**Possible Solution**:<details style="display: inline;"><summary>show</summary>Here is one possibility:
```
:seq(inString("ABCDEFGHIJKLMNOPQRSTUVWXYZ",sub(Ans,A,1),A,1,length(Ans
```
</details>

------

**2**. Change this short program so it doesn't flicker and then optimize it as much as possible.

```
:0→X:0→Y:Repeat 0
:ClrHome
:Output(Y,X,"X")
:getKey→K
:If K=24:X-1→X
:If K=25:Y+1→Y
:If K=26:X+1→X
:If K=34:Y-1→Y
:End
```

**Possible Solution**:<details style="display: inline;"><summary>show</summary>Here is one possibility:
```
:4→X:4→Y:Repeat 0
:Output(Ans,X,"X
:Repeat Ans:getKey→K:End
:Output(Y,X,"  // 1 space
:X+(Ans=26)-(Ans=24→X
:Y+(K=34)-(K=25→Y
:End
```
</details>


<center>

|**[<< Summary](sk:optimize-summary.html)**|**[Table of Contents](starter-kit.html)**|**[Starter Kit Review >>](sk:review.html)**|
| --- | --- | --- |

</center>
