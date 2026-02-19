# Hangman
Like [Tic-Tac-To](tic-tac-to.html), Hangman is a game that almost everybody has played at some point in their life. The basic premise behind the game is that two people alternate turns, with one person picking a word, and then the second person trying to guess the word by selecting letters until they have either gotten the word or run out of chances.

This game features some rather advanced string manipulation, as well as some good compression for storing the different pieces of the hangman character. Again, try out the game and try to understand and think through the code.



### The Code

```
:"ABCDEFGHIJKLMNOPQRSTUVWXYZ→Str0
:Repeat 33>length(Str1
:ClrHome
:Disp "WORD? (32 CHARS)
:Input "",Str1
:End
:"?→Str2
:For(I,1,length(Str1
:sub(Str1,I,1
:If inString(Str0,Ans:"-
:Str2+Ans→Str2
:End
:sub(Ans,2,length(Ans)-1→Str2
:8→T
:ClrHome
:While Str1≠Str2 and T
:Output(1,1,Str2
:.1{69,67,58,49,47,48,38,38
:Output(iPart(Ans(T)),10fPart(Ans(T)),sub("^^I--IO ",T,1
:Repeat 30<Ans and Ans<94
:getKey
:End
:If Ans=45:Goto Q
:Ans-20-5int(.1Ans)-2(Ans>45→K
:sub(Str0,Ans,1→Str3
:Output(7+(K>14),K+1-13(K>14),Ans
:inString(Str1,Ans→I
:T-not(Ans→T
:While I
:sub(sub(" "+Str2,1,I)+Str3+sub(Str2+" ",I+1,length(Str2)-I+1),2,length(Str2→Str2
:inString(Str1,Str3,I+1→I
:End
:End
:Lbl Q
:Pause "YOU "+sub("LOSE!WIN! ",1+5(Str1=Str2),5
:ClrHome
```

### The Download

In case you want to try the program on your calculator, you can download the program in .8xp format.

- [Hangman](http://tibasicdev.github.io/local--files/hangman/hangman.zip)
