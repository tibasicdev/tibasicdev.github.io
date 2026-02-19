# Instant Messenger
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|A simple instant messaging program.|Str3|None|A, Str1, Str2, Str3|James Kanjo|[file im.zip]|

```
:"→Str1
:"→Str2
:GetCalc(A
:not(A→A
:Lbl M
:ClrHome
:Menu("IM","READ",R,"SEND",S,"QUIT",Q
:Lbl S
:Input "SEND MESSAGE:   ",Str3
:If A:Str3→Str1
:If not(A:Str3→Str2
:Goto M
:Lbl R
:If A:Then
:GetCalc(Str1
:Str1
:Else
:GetCalc(Str2
:Str2
:End
:Output(1,1,Ans
:Pause :Goto M
:Lbl Q
```

An "Instant Messaging" program, is a program that allows you to have an "instant" conversation with another person via a computer of some sort. With this program, you must connect two calculators via the calculator-calculator cable (it's about 22 centimetres long) before initiating the program on both calculators. Using this program means that you can be massive 22 centimetres away from a friend, and STILL be able to have conversations with them.

Obviously this is a silly program, but its real purpose is to demonstrate the calculator's capacity to communicate with other calculators — and it's a great 'learning program'.

Firstly, the program resets the Str1 and Str2 variables, which are used to later display "received messages", and executes the [getcalc(](getcalc.html) command to retrieve variable A from the connected calculator. Then the program does something tricky; it checks to see if the variable A is equal to [π](pi.html) ([pi](pi.html)). If so, then it sets variable A to *[e](e-value.html)*. If A does not equal π, then π is stored to A. This is a complicated process which gives each calculator it's own identity — a vital part of [cross-calculator programs](multiplayer.html).

The menu then appears giving the user options to "receive" a message, "send" a message and to "quit". When the user tries to send a message, the program retrieves the user's input and temporarily stores it into Str3. The program then stores Str3 to variables Str1 or Str2, depending on the value of A. When the user goes to retrieve a message, depending on the value of A, it selectively retrieves Str1 or Str2 from the other calculator, which is the message that the other user has "sent".

Of course, this isn't true instant messaging, but is at the least a simulation of it. Because the GetCalc( command retrieves data from another calculator, the other calculator needs to be idle to be able to send it. This program works because both calculators are always idle — in the menu, when typing a message and when reading a message. This routine uses Str1, Str2 and Str3, which you should [clean up](cleanup.html) at the end of your program.
