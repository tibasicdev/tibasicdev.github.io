# Polynomial Division
**Routine Summary**

This program will divide two polynomials of any positive integer degree.

**Inputs**

*L<sub>1</sub>*- Dividend
*L<sub>2</sub>*- Divisor

**Outputs**

*L<sub>3</sub>*- Quotient coefficients in descending degree

**Variables used**

L<sub>1</sub>, L<sub>2</sub>, L<sub>3</sub>, A, B, D

**Calculator Compatibility**

TI-83/84/+/SE

**Author**

Timothy Foster

**Download**

[polydiv.8xp](http://tibasicdev.wikidot-com/local--files/polynomial-division/polydiv.8xp)

<details style="display: inline;"><summary>show</summary>
```
:ClrHome
:DelVar L₁DelVar L₂
:Disp "DEGREE
:Input "DIVIDEND ",A
:Input "DIVISOR ",B
:A+1→dim(L₁
:B+1→dim(L₂
:ClrHome
:Disp "TERM COEFFICIENTS
:Disp "
:For(A,1,dim(L₁
:Output(2,1,"DIVIDEND
:Output(2,10,A
:Input D
:D→L₁(A
:End
:ClrHome
:Disp "TERM COEFFICIENTS
:Disp "
:For(A,1,dim(L₂
:Output(2,1,"DIVISOR
:Output(2,9,A
:Input D
:D→L₂(A
:End
```
</details>
```
:DelVar L₃
:For(A,1,dim(L₁)+1-dim(L₂
:L₁(A)/L₂(1→L₃(A
:For(B,2,dim(L₂
:L₃(A)L₂(B
:-Ans+L₁(A+(B-1→L₁(A+(B-1
:End
:End
:ClrHome
:For(A,dim(L₁)-(dim(L₂)-2),dim(L₁
:L₁(A→L₃(1+dim(L₃
:End
:Disp "FIRST TERM
:Output(2,1,"X^
:Output(2,3,dim(L₁)-dim(L₂
:Output(3,1,L₃
```

This routine will solve polynomial division with any given integer degrees.  The dimension of L<sub>1</sub> is the degree+1 of the dividend polynomial, and the dimension of L<sub>2</sub> is the degree+1 of the divisor. The numbers used in the list are the coefficients of the respective polynomial in descending degree order, including place holder 0's.  So, a polynomial of 3*x*<sup>3</sup>+2*x*<sup>2</sup>-1 would need to be {3,2,0,-1}.  The program outputs the code as L<sub>3</sub> in that form.  The program also displays the degree of the first term.  Once you reach the *x*<sup>0</sup> term, all the coefficients afterward are the remainders.  So, a display of X^2 {3,2,1,5,3} says 3*x*<sup>2</sup>+2*x*+1 and a remainder of 5*x*+3.

The program first asks for input.  It asks for the degree of each polynomial, and then it asks for the contents using a [For](for.html)( loop until there are no more terms.  It then commences with the main loop which is another For( loop.  The program works in very much the same way people would go about solving a division problem.  It divides the current leading terms of the dividend by the first term of the divisor and puts it into L<sub>3</sub>, our answer.  It then does a second For( loop multiplying the partial quotient by every term of the divisor.  At the end, it discovers the remainder in L<sub>1</sub> and stores them into the end of L<sub>3</sub> for a complete answer.

Here are a couple of examples for you to try out to see if the code was inputted correctly:

$$ {x^2+3x-2 \over x+1} = x+2- {4 \over x+1} \hspace{12pt} \{ 1,2,-4 \} $$

$$ {x^4+3x^2-2x+1 \over x^2+4x+6} = x^2-4x+13-{30x+77 \over x^2+4x+6} \hspace{12pt} \{1,-4,13,-30,-77\} $$

## Error Conditions
- **[ERR: INVALID DIM](errors.html#invaliddim)** occurs if the degrees are made negative or the divisor's degree is larger than the dividend
- **[ERR: DIVIDE BY 0](errors.html#divideby0)** happens if the leading coefficient of the divisor is 0
- **[ERR: DATA TYPE](errors.html#datatype)** is thrown if anything is imaginary
