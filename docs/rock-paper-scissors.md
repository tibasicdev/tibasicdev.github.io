# Rock Paper Scissors
Rock Paper Scissors is a classic game that involves two players choosing among three different hand gestures, and seeing who has the best hand. Each of the hand gestures — rock, paper, and scissors — beats one of the other two hand gestures, so there is a good likelihood that somebody will win. (However, if both players choose the same gesture, it is a tie.) You can play this game indefinitely, but it does get monotonous after a while.

Here is a handy table that tells which hand gesture wins in each situation:

| |~ Rock |~ Paper |~ Scissors |
| Rock | Tie | Paper | Rock |
| --- | --- | --- | --- |
| Paper | Paper | Tie | Scissors |
| --- | --- | --- | --- |
| Scissors | Rock | Scissors | Tie |
| --- | --- | --- | --- |



### The Code

```
:ClrHome
:Disp "PAPER - SCISSORS
:Input "ROUNDS:",I
:For(I,1,I
:ClrHome
:Disp "CHOOSE WEAPON:
:Disp "1) ROCK","2) PAPER","3) SCISSORS
:Repeat 2>abs(Ans-2
:getKey-91→J
:End
:Disp "YOU: "+sub("ROCK    PAPER   SCISSORS",8J-7,8
:randInt(1,3
:Disp "CALC: "+sub("ROCK    PAPER   SCISSORS",8Ans-7,8
:Pause "WINNER IS "+sub("YOU CALCBOTH",1+4max(Ans={1,2,3} and J={3,1,2})+8(J=Ans),4
:End
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Rock Paper Scissors](http://tibasicdev.github.io/local--files/rock-paper-scissors/rockpaperscissors.zip)
