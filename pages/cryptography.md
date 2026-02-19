# Cryptography
It is possible to write programs which decode and encode data using ciphers. There are many different kinds of ciphers, some of which are easy to break and some of which are modern and very hard to break. There are two basic kinds of ciphers: substitution ciphers, which substitute some characters for other characters, and transposition ciphers which move characters around. Some ciphers combine those two techniques. Others, such as [DES](http://calccrypto.wikidot.com/algorithms:des) and [AES](http://calccrypto.wikidot.com/algorithms:rijndael), encrypt blocks of data instead of characters.



### Substituting characters
Doing this may seem difficult at first as there are no built-in functions that convert a character to a number or a number to a character. However, it is possible to do that using an "alphabet string" such as:
:"ABCDEFGHIJKLMNOPQRSTUVWXYZ " -> Str1
You can then use the inString function to find the alphabetic position of a letter, and use the sub() function to find the letter at an alphabetic position.

### Caesar Cipher
This is one of the simplest ciphers. The cipher shifts all letters by a constant number. A common special case called ROT13 shifts all characters by 13 (so applying it twice reverses it). It's useless for secure encryption, since you can just try all 25 possible shifts by hand (or [by calculator](http://calccrypto.wikidot.com/crypto:rot-x-breaker)). On the other hand, it's very easy to implement. For example, here is an implementation of ROT13:

```
:"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
:Ans+Ans→Str1
:Disp "ENTER TEXT"
:Input "",Str2
:":"→Str3
:For(P,1,length(Str2))
:inString(Str1,sub(Str2,P,1))→A
:If A:Then
:Str3+sub(Str1,A+13,1)→Str3
:Else
:Str3+sub(Str2,P,1)→Str3
:End
:End
:sub(Str3,2,length(Str2))
```

### Stream Cipher
A stream cipher uses a keystream generator, which is a program that outputs a series of hard-to-predict values after being given a key as an initial input. Each value is then combined with a plaintext letter to produce the ciphertext letter. 
In this cipher, the calculator's random number generator is used as the keystream generator. The alphabet consists of the 26 letters followed by a space. The characters are then shifted over by a "random" integer offset. Here is a sample implementation:

### prgmCIPHER
- usable as a subroutine, taking input in (E, X, Str2) and giving the result in Str3.
```
:"ABCDEFGHIJKLMNOPQRSTUVWXYZ "
:Ans+Ans→Str1
:":"→Str3
:X→rand
:For(P,1,length(Str2),1)
:inString(Str1,sub(Str2,P,1))→A
:If E
:A+int(27rand)→A
:If not(E)
:A+27-int(27rand)→A
:Str3+sub(Str1,A,1)→Str3
:End
:sub(Str3,2,length(Str2))→Str3
```

**prgmCIPHERUI** — usable as a simple interface for the above.
```
:Disp "(0) DECODE","(1) ENCODE"
:Input E
:Input "KEY (NUM)?", X
:Disp "ENTER TEXT"
:Input "",Str2
:ClrHome
:Disp "RESULT:"
:prgmCIPHER
```

- This cipher is secure if and only if the TI random number generator is secure. 
- The same key should not be used for several long messages, since it is possible to subtract the two plaintexts and cancel out the key that way. If you have to do it, add a random number to the key, and tell the other person to do the same. If that is going to be automated in a program, the standard format for that is D:MESSAGE where D is the number.
- AAAAA encrypts to UXGMS if the key is 1, and to NTMZK if the key is 2. Use that to make sure that you got the algorithm right.

### Seed Encryption
I am not familiar with encryption terminology, so please excuse me. The following routine is useful for OS 2.53MP and up. For lower OSes, replace randIntNoRep( with this code:
```
rand(length(Str2→L₂
seq(X,X,0,dim(L₂→L₁
SortA(L₂,L₁
```
So, with these two codes, you can give coded messages to anybody and the only way they can decipher it is if they have a key. The best part is that even looking at the program will not be able to give a way to figure out the key! So pretty much, your code will only be cracked by sheer luck. So here are the two codes and then a combined code that takes care of both:
The codes require Str1 as the string to Decode or Encode. Ans is the decoded or encoded version:
Decode:
```
"ABCDEFGHIJKLMNOPQRSTUVWXYZ .!,0123456789→Str2
Input "KEY:",A
A→rand
randIntNoRep(1,length(Str2→L1
length(Str1→B
".
For(A,1,B
Ans+sub(Str2,sum(cumSum(L1=inString(Str2,sub(Str1,A,1)))),1
End
sub(Ans,2,B
```
Encode:
```
"ABCDEFGHIJKLMNOPQRSTUVWXYZ .!,0123456789→Str2
Input "KEY:",A
A→rand
length(Str2→C
randIntNoRep(1,Ans→L1
length(Str1→B
".
For(A,1,B
Ans+sub(Str2,L1(C-inString(Str2,sub(Str1,A,1))),1
End
sub(Ans,2,B
```
Now to combine them:
```
ClrHome
"ABCDEFGHIJKLMNOPQRSTUVWXYZ .!,0123456789→Str2
Input "KEY:",A
A→rand
length(Str2→C
randIntNoRep(1,length(Str2→L1
length(Str1→B
".
Menu("ZECRYPT","DECRYPT",1,"ENCRYPT",2,"EXIT",Z
Lbl 1
For(A,1,B
Ans+sub(Str2,sum(cumSum(L1=inString(Str2,sub(Str1,A,1)))),1
End
Goto Y
Lbl 2
For(A,1,B
Ans+sub(Str2,L1(C+1-inString(Str2,sub(Str1,A,1))),1
End
Lbl Y
sub(Ans,2,B
Lbl Z
```
