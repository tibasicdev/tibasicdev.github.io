# Mastermind (Alternate)
Mastermind is a fun game that involves trying to break a random code of five numbers (1-9) in fifteen guesses or less. To help assist you with the code-breaking, a list of two numbers is provided. The first number is the number of digits that are correct and in the wrong place, and the second is the number of digits that are correct and in the right place. Try out the game and try to understand and think through the code.

### The Code

```
:int(10rand(5))+1→L1  
:For(G,-15,-1 
:Input A 
:int(10fPart(A/10^(5-cumSum(1 or L1→L2 
:sum(L1=Ans 
:Disp {sum(seq(min(sum(L1=N),sum(L2=N)),N,0,9))-Ans,Ans 
:If Ans<4 
:End 
:If not(G 
:Disp L1 
:"LOSE 
:If G 
:"WIN 
:"YOU "+Ans
```

### Related Games

- [Mastermind](mastermind.html)
