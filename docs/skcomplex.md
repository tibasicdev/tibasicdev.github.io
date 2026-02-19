# Complex Numbers
There are several ways to manipulate complex numbers in the context of calculator programming. This lesson will look at how complex numbers work, the commands associated with them, and a simple application for the commands.

## What are they?
A complex number is essentially what happens when you attempt to take an even root of a negative number. As a way of interpreting complex numbers, they are displayed as their rational part added with a multiple of the square root of -1. This second number is known as an imaginary number, because you cannot represent them on a normal coordinate graph. The square root of -1 is denoted as a lowercase i.  This is what it usually looks like:

```
:5+6i
```

## real( and imag(
The real( command is used to extract the first part of a complex number. Simply use the command like this:
```
:real(5+6i
```
This code will return the number 5 extracted from the complex number 5+6i. That's all there is to it.

The imag( command is used to extract the second part of a complex number, the imaginary part. It is used in the same way real( is.
```
:imag(5+6i
```
This will return the coefficient of i, which is 6.

## Application

The main use of real( and imag( in programming is to compress 2 real variables into one complex variable.  For instance, if you want the variable A to contain both the values of B and C, you can use the following code.
```
:B+Ci→A
```
To extract the independent values, use the real( and imag( commands you just learned about.
However, there is one small problem.  Two real variables take up 36 bytes, but complex variables take up 27 bytes.  This is only a compression of 9 bytes, and using the similar integer-decimal method saves you 18 bytes.  But you can use both the integer-decimal method combined with the real-imaginary method to store 4 different variables in one, saving you a whopping 45 bytes of storage!

<center>

|**[<< Trigonometry](sk:trigonometry.html)**|**[Table of Contents](starter-kit.html)**|**[Summary >>](sk:summary-math.html)**|
| --- | --- | --- |

</center>
