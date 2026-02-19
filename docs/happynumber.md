# Happy Number Finder (83-84)
This is a program to find out if any number from 1 to 999 is a happy number. Before I put the code in though, some of you may be wondering what a happy number is though.
To find a happy number:
Take X (Ex. 123)
Take each of the digits in X and square them (Ex. 1²,2²,3²)
Add the squares (Ex. 1+4+9=14)
Keep on doing this until you get either 1 or 4. If you get 1, the number is happy; if you get 4, it is not.
Here is the code. It might not be in the most convenient format, but here it is:

```
Lbl A
Prompt J
Goto B
Lbl B
If J>999:Goto A
If 1000>J>99:Goto C
If 100>J>9:Goto D
If 10>J>0 Goto E
```

Here's where things get complicated. I'll try to explain in words what the code is. The explanation is after the // on each line, so don't put it in the actual program.

```
Lbl C
(J/100)→K //To isolate each digit, I first divided the number by 100 (Ex. 123 becomes 1.23)
iPart(K)→T //Then, I took the integer part, which was formerly the hundreds digit. (Ex. 1.23 becomes 1)
(K-T)→O // Next, I subtracted the iPart from the full number, so that I had only 2 digits. (Ex. 1.23-1 becomes 0.23)
(O*10)→L //And then I multiplied the new number by 10 to get the next digit. (Ex. 0.23 becomes 2.3)
iPart(L)→U //(Ex. 2.3 becomes 2)
(L-U)→P //(Ex. 2.3-2 becomes 0.3)
(P*10)→V //(Ex. 0.3 becomes 3)
(T²+U²+V²)→J
Goto B //At the end, we plug the final number back into J and check for the number of digits.
```

The next piece of code (if J has 2 digits) works the same way.

```
Lbl D
(J/10)→K
iPart(K)→T
(K-T)→O
(O*10)→U
(T²+U²)→J
Goto B
```

The last part (if J has only 1 digit) is a bit different.

```
Lbl E
If J=1 or 4
Then
Goto F
Else
J²→J:Goto B
Lbl F
If J=1:Disp "HAPPY"
If J=4:Disp "NOT HAPPY"
```

Again, I know it isn't the most effective method, but it was the first one I came up with. Perhaps, when I am better at coding, I will find a more effective way to do this, but for now, here it is.

Have fun trying out numbers!
