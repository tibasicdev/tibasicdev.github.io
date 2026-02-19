# Fake Home Screen
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Fakes the home screen.|Str1,A,(B)|none|Str1,A|Adm. Wiggin|[file fakehomescreen.zip]|

```
:Repeat 0
:Input "",Str1
:Disp randInt(1,E3
:End
```

This routine allows you to mess with people who aren't very knowledgeable about the calculator, and don't know how to exit out of an infinite loop. The routine is very simple in that it fakes the home screen, giving the user the appearance that they can operate the calculator as usual.

When the user inputs a number or some text (both are acceptable because it is being stored to a [string](strings.html)), the calculator randomly selects a number between 1 and 1000, and displays it on the screen. This process will be repeated over and over again until the user either presses [ON] or [2nd][QUIT]. In any case, this should provide you with some basic humor for a minute or two.

Another way to do this, that allows for results closer to the actual answer, is to store the input to a real variable. With large calculations it is virtually undetectable and rarely give the right answer, but if the user tries to enter in anything other than a number, it will cause the program to crash.

the code for this is 

```
:ClrHome
:While 1
:Input "",A
:Disp A+randInt(-50,50
:End
```

Alternatively, to guarantee that the correct answer will never be displayed, the following code can be used:

```
:ClrHome
:While 1
:Input "",A
:A→B
:While A=B
:A+randInt(-50,50→B
:End
:Disp B
:End
```


Or if you really want to be tricky, you can modify the answer only if it is a decimal and/or number larger than 1000 sometimes and sometimes give the right answer. This way people will have less of a chance of noticing that the calculator is displaying the wrong answer.

```
:ClrHome
:While 1
:Input "",A
:Disp A+randInt(-1,1)(fPart(A)rand+randInt(-10,10)(A>1000
:End
```
