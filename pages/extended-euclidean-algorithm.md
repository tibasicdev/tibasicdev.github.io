# Extended Euclidean Algorithm
|Routine Summary|Inputs|Outputs|Variables Used|Author|
|--- |--- |--- |--- |--- |
|Calculates the GCD of two numbers.|*A,B* - Whole numbers|L₁(I) - Greatest common divisor (gcd) of A and B<br>L₂(I), L₃(I) - Bézout coefficients such that AL₂(I)+BL₃(I) = L₁(I)|I, Q||

```
:{A,B→L₁
:{1,0→L₂ 
:{0,1→L₃
:1→I
:While L₁(dim(L₁
:I+1→I
:int(L₁(Ans-1)/L₁(Ans→Q
:L₁(I-1)-AnsL₁(I→L₁(I+1
:L₂(I-1)-QL₂(I→L₂(I+1
:L₃(I-1)-QL₃(I→L₃(I+1
:End
```

The [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/extended_euclidean_algorithm) is a highly efficient algorithm for calculating the greatest common divisor ([GCD](gcd.html)) of two numbers. The algorithm, in the process of finding the GCD, also finds the Bézout coefficients x and y. These are integers such that

$$
ax+by=\gcd(a,b)$$
