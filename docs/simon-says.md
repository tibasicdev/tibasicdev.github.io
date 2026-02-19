# Simon Says
Simon Says is a simple game where you are given a pattern that must repeat, and the pattern gets longer and longer which subsequently increases the difficulty. This version of the game is played on the home screen, and is quite small (approximately 214 bytes). You use the respective number keys to type the matching number. Like with the other games, try to understand the code and experiment with it.



### The Code

```
:For(I,1,16
:ClrHome
:DelVar L₁"?→Str1
:For(J,1,I
:randInt(1,5→B
:{92,93,94,82,83
:Ans(B→L₁(J
:Str1+sub("12345",B,1→Str1
:End
:Output(1,1,sub(Ans,2,length(Ans)-1
:rand(10I
:ClrHome
:For(J,1,I
:Repeat Ans
:getKey
:End
:If Ans≠L₁(J:Goto Q
:Output(1,J,sub(Str1,J+1,1
:End
:rand(20
:End
:Lbl Q
:Pause "YOU "+sub("LOSE!WIN! ",1+5(I=17),5
:ClrHome:"
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Simon Says](http://tibasicdev.github.io/local--files/simon-says/simonsays.zip)
