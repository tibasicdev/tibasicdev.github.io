# Snake
If you have ever played any of the snake, mofrog, nibbles, etc. games, then this game should be familiar to you. The basic premise is to go around eating food and the snake grows longer with each piece of food. Like with the other games, try out the game and try to understand and think through the code.


### The Code


:26→K
:1.1→B
:{4Ans→A
:ClrHome
:For(A,1,ᴇ2
:randInt(1,16)+.1randInt(1,8→C
:Repeat C=Ans(1
:A→dim(ʟA
:ʟA(1
:Output(10fPart(Ans),int(Ans),"O
:Output(10fPart(B),int(B)," "

:Output(10fPart(C),int(C),"*
:getKey
:If Ans=45
:Goto 0
:If Ans=34 or 2>abs(Ans-25
:Ans→K
:ʟA(A→B
:ʟA(1)+(K=26)-(K=24)+.1((K=34)-(K=25
:If max(ʟA=Ans
:Goto 0
:Ans+16(not(int(Ans))-(17=int(Ans)))+.8(not(fPart(Ans))-(.9=fPart(Ans
:augment({Ans},ʟA→A
:End
:augment(Ans,{Ans(A→A
:End
:Lbl 0
:ClrHome
:A


### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Snake](http://tibasicdev.github.io/local--files/snake/snake.zip)

### Other Versions

Snake is a rather popular game to code since it showcases many features of the TI-BASIC language and provokes algorithmic thinking.  Below are some other snake clones that you can study and compare to observe the classic tradeoffs in speed, memory efficiency, features, and aesthetics.

- [XSnake](xsnake.html) by XprO — Optimized for pure speed
- [archives:Nibbles](archives:nibbles.html) by Edward H — Requires no auxiliary lists, and hence memory efficient
- [Nibbles Arcade](nibbles-arcade.html) by SiCoDe — Feature-heavy with snake variations and an AI
