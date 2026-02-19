# Synthetic Division
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|This is useful for factoring large nth degree polynomials (and finding their roots, of course), as well as finding an upper and lower limit for the roots of an nth degree polynomial, as per the remainder and factor theorems and some others.<br>It uses L₁ for input of the coefficients of the starting polynomial, uses X for r in (x-r) (what you're dividing by), so have those variables predefined (or put :Input L₁:Input X at the the beginning of the program), and it outputs L₂ as the answer with the last list entry as the remainder.|*R* - the value of r in (x-r)|*L₂* - the coefficients of the answer and the remainder is stored as the last list entry|L₁, L₂, A, R, Ans|TI-GBR, optimized by earthnite|http://tibasicdev.github.io/forum/t-1109444|

```
dim(L₁→dim( L₂ 
L₁(1→L₂(1
For(A,2,dim(L₁ 
L₁(A)+R(L₂(A-1→L₂(A
End
L₂
```

Synthetic division works for problems in the following format.

(a<sub>0</sub>x<sup>n</sup> + a<sub>1</sub>x<sup>n-1</sup> + a<sub>2</sub>x<sup>n-2</sup> + ... + a<sub>n-1</sub>x<sup>1</sup> + a<sub>n</sub>x<sup>0</sup>) / (x-r)

Where a<sub>0</sub>≠0


For example,
Problem: find the roots of x<sup>3</sup>-x<sup>2</sup>-2x-12=0

First we need to find all possible (r) in (x-r)
Factor a<sub>n</sub>:-12 {±1,±2,±3,±4,±6,±12
Factor a<sub>0</sub>:1 {±1
List of a<sub>n</sub>/a<sub>0</sub>:{±1,±2,±3,±4,±6,±12
This last list is the list of all possible r in (x-r)

Now for synthetic division.
See the [wikiHow website](http://www.wikihow.com/how-to-divide-polynomials-using-synthetic-division).

**Using the program.**

Input L1 with the polynomial's coefficients, {1,-1,-2,-12→L1
Input R for r in (x-r), 3→R

We get a L2 as an answer; the last entry in the list is the remainder. If this is 0, we know that (x-r) is a factor. The other entries in the list represent the coefficients of the quotient, a polynomial of 1 degree less than the starting polynomial.
So, for starting polynomial f(x) divided by (x-r) , f(x)= (x-r) * q(x) +R, where q(x) is the quotient of 1 degree less than f(x) and R is the remainder. If R is = 0 (x-r) is a factor of f(x) and f(x) can be broken down into q(x)*(x-r).

Now, remember we found all possible r's? Well, do synthetic division for each of those r's until the remainder (R, the last entry on L2) is 0. When you have that, you rewrite your equation. So, in our problem, 3 for r gives 0 for R so we would rewrite the problem, using the coefficients as:

Input: {1,-1,-2,-12→L1
Input: 3→R
Output {1,2,4,0
This means that (x<sup>3</sup>-x<sup>2</sup>-2x-12) / (x-3) = x<sup>2</sup>+2x+4
(x-3) is a factor of (x<sup>3</sup>-x<sup>2</sup>-2x-12
Then use the quadratic formula with x<sup>2</sup>+2x+4 to find the other factors.
