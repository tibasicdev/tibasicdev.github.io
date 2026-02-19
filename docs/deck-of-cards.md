# Deck of Cards
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Simulates a standard 52-card deck of cards.|None|*∟DECK* - the cards, in the format:<br><br>Value.Suit<br><br>Value is 1..13<br>Suit is 0, .25, .5, .75|L₁, ∟DECK|[file deckofcards.zip]|

**Creating the deck**

```
seq(X/4,X,4,55→DECK
```

**Shuffling the deck**

```
rand(52→L₁
SortA(L₁,∟DECK
```

**Accessing individual cards**

```
∟DECK(I
Disp "VALUE:",sub("A23456789TJQK",int(Ans),1 
Disp "SUIT:",sub("SHCD",4fPart(Ans)+1, 1
```

The cards in the deck are stored in the form Value.Suit, where the value of the card (Ace through King) is encoded as a number 1 through 13; and the suit of the card is the fractional part, encoded as one of 0, 0.25, 0.5, or 0.75. In the above code (accessing individual cards), the convention is that 0=Spades, 0.25=Hearts, 0.5=Clubs, 0.75=Diamonds; however, you can pick any order as long as you're consistent.

Since any value from 1.00 to 13.75, that's 1/4 of an integer, is a valid card, we can generate the entire deck as 1/4 of the values {4,5, ..., 54, 55}.

When shuffling the deck, we generate a random list in L₁, then use [SortA(](sorta.html) to sort ∟DECK by the values in L₁. Since the values in L₁ are random, this has the effect of sorting ∟DECK in a random order.

The main overhead of this shuffling method, however, is that generating a random list might take a long time (around a second or two). To avoid this, you can generate individual elements of L₁ randomly in a [getKey](getkey.html) loop, while waiting for a key, then use L₁ to shuffle later. Since shuffling isn't done often, by the time you need to shuffle, L₁ will most likely be fully randomized already.

Finally, accessing the cards is done using [fPart(](fpart.html) and [int(](int.html). If a variable X is encoded in the same way that we encode cards, int(X) will return its value (1-13) and 4fPart(X)+1 will return its suit as a number 1-4.
