# Binary Data Compression
|Routine Summary|Inputs|Outputs|Variables Used|
|--- |--- |--- |--- |
|Bitwise operations on a decimal representation of binary data|*D* —  the Decimal that represents the binary data<br>*I* — the Index of the bit you will check/change|*Ans* the checked bit or the changed decimal representation|*D*, *I*, *Ans*|

When you have a program with lots of bivalent information — for example, a RPG with open/closed doors, defeated/undefeated bosses, completed/uncompleted quests, etc. — you could store all of this data in a list. However, lists tend to become rather large, so compression is vital.

First let's have a glance at how this will work. For example, there are six locations in a RPG that a player might have visited or not, which is stored as 1 or 0, respectively. As a list, we would have something like this:

```
:{1,0,0,1,1,0
```

But if you know a thing about binary, you know that 100110b equals 38d in decimal notation (if this confuses you, please read through the [binary and hexadecimal](binandhex.html) page first). We can store up to 44 "bits" of information in just one variable! The reason we can store a maximum of 44 bits in one variable is because of the internal rounding that the calculator does.
 
So imagine at a given moment the game needs to know if the player has been to area four. Continuing our example from above, we take the number 38 as the current value, which we know represents 100110, and for the sake of optimization we need to index this binary number as follows: 1<sub>5</sub>0<sub>4</sub>0<sub>3</sub>1<sub>2</sub>1<sub>1</sub>0<sub>0</sub>.

Using following routine, we extract the value of the bit with index I from its decimal representation D. In our example, I=4 and D=38

```
:int(2fPart(.5D/2^I
```

Ans will now contain the value of the bit with index I from the decimal notation D. In our example, Ans would be 0, location 4 was not yet visited by the player. Now all we need is ways to change that bit. If the player visits this location it would have to be changed to 1.

This routine deals with that, assuming Ans is the value of the flag (either one or zero, returned from the previous routine):

```
:D+2^Inot(Ans→D        //if Ans=1, nothing needs to be changed, and 0 is added to D
                       //if Ans=0 it needs to become 1, so 2^I is added to D, effectively setting the bit with index I to 1
```

Next routine does the exact opposite: it changes the value to 0

```
:D-Ans2^I→D
```

Finally, the last routine changes whatever value is in the current bit: 0 becomes 1 and 1 becomes 0.

```
:D+2^I(1-2Ans→D        //(1-2Ans) sets the sign: -1 if Ans was 1 and +1 if Ans was 0
```

## Error Conditions

- **[ERR:DATA TYPE](errors.html#overflow)** is thrown if D or I is imaginary.
- **[ERR:OVERFLOW](errors.html#overflow)** is thrown if I>333 (though I shouldn't be this large with only 44 bits).

- No errors will be thrown if I≥44 or D≥2<sup>44</sup>, but data will get corrupted in the lower indexes because of rounding if D is changed.
- No errors will be thrown if I<0, but D will become decimal if it gets changed.
- No errors will be thrown if I or D are not whole, but data will be corrupted.
