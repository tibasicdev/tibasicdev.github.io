# Tips & Tricks
**Eliminate Annoying Things**

If you want you to get rid of the “Done” message after you exit your program you can place some text or just a single double-quote on the last line of your program. Another option is to use the [Output(](output.html) command, which has the benefit of not moving the cursor to the second line.

```
:ClrHome
:Output(4,4,"Some Text
:"
```

Something to be aware of about this, however, is that because there is no Stop command, Return is implied. This is okay if your program runs independently, but be careful if your program was called by another program- it will return to the previous one instead of quitting.

Another annoying thing is the run indicator that appears in the upper right corner of the screen. You can get rid of the run indicator by using Text(-1,0,90," " or Output(1,16," " (on the home screen) in a [getKey](getkey.html) loop:

```
:Repeat Ans
:Text(-1,0,90," // 1 space
:getKey→K
:End
```

**Home Screen Text on Graph Screen**

To get home screen font on the graph screen (except on the regular TI-83) you should place '-1' at the beginning of the [Text(](text.html) command:

```
:Text(-1,Y,X,"Text
```

**Digits in a Number**

To find out the number of digits in a whole number (i.e., a number without decimals), use the [log(](log.html) function. An [abs(](abs.html) function prevents a domain error when taking the logarithm of a negative number:

```
:1+int(log(abs(#
```

**Empty Variables**

You can create an empty string with "→Str1, and an empty list with the [ClrList](clrlist.html) command.

**Displaying Quotes and Store**

Without storing them to a special string, you cannot usually display quotation marks (") and the [store](store.html) command (→). However, you can mimic these respectively in the [Text(](text.html) command by using two apostrophes (' '), and two subtract signs and a greater than sign (—>).

**Right Triangle Hypotenuse**

You can get the hypotenuse of a right triangle by using [R►Pr(](r-pr.html)a,b), where a and b are the legs of a right triangle, or [abs(](abs.html)a+b*i*, where a and b are the legs of a right triangle and *i* is the imaginary i.

**Dividing by 100**

Using the program editor, you can place the [%](percent.html) symbol directly into the code as a replacement for dividing by 100. This saves a few bytes each time you use it.

Using the [sub(](sub.html) command, if only one argument is given and it contains an expression that evaluates to a real, complex, or list of numbers, the argument will be divided by 100.

```
:sub(225
    2.25
```

**Turn the Screen Black**

If your window is set up so that Xscl < ΔX and Yscl < ΔY, you can use [GridOn](gridon.html) to make the entire screen black. You should note, however, that is rather slow.
You can also use [Shade(](shade.html) to go faster.

```
:Shade(Ymin,Ymax
```

**Inputting Coordinates**

Most programmers know the normal syntax for Input, but it can be used alone without any arguments. This simply displays a little "+" on the graph screen, along with the coordinates on the bottom. The plus symbol can be moved horizontally or vertically to a certain coordinate, and the command ends by pressing ENTER. The coordinates are then stored to x and y, respectively.

```
:Input
```
**Faster Circles**

On the TI-83+ and above, the [Circle(](circle.html) command has an alternate syntax. When a complex list such as {i} is added as the 4th argument, "fast circle" mode will be turned on, which uses the symmetries of a circle to save on trig calculations, and draws a circle in only 30% of the time it would normally take.

```
:Circle(0,0,5,{i
```

**Extra Characters**

Although the extra characters are only available through an [assembly](assembly.html) program, once you have them you can store them to a string and then use the string in a program with no problems. The characters include lowercase letters and ASCII characters (such as @, &, #, $, and international characters like ä).

**Strange Control Flow**

There are a few cases of strange [control flow](controlflow.html), where you can use [If](if.html) conditionals by themselves, or together with [loops](while.html) and/or [DelVar](delvar.html), to create some interesting results. The Disp commands tell the input conditions under which they will be executed. 

- The dangling else (i.e, the executed statement itself is a conditional)

```
:If A:If B:Disp "B or not(A)
```

```
:If A:Then
:Disp "A
:If B:Else
:Disp "not(A) or not(B)
:End
```

- Misusing the [DelVar](delvar.html) bug that occurs when chaining an [If](if.html), [Else](else.html), or [End](end.html) command to the end

```
:If A:DelVar XIf 0
:Disp "not(A)
```

```
:If A:Then
:Disp "A
:If B:DelVar XElse
:Disp "A and not(B)
:End
```

**Running Programs from Assembly Shells**

As a matter of convenience, you can run your TI-Basic program from an [assembly shell](asmshells.html). DoorsCS 6 will automatically display all programs, but you need to place a colon (":") as the first line of your program for MirageOS to recognize it. However, it should be noted that there is no guarantee that your program will work correctly when run by a shell.

**Moving Setup to Program End**

If you have a large program where speed is at a premium, then you want the main program loop as close to the beginning of the program as possible. Since [program setup](setup.html) is usually the code that is at the beginning of the program, this means that you should move it to the end of the program and then jump to it using a [Goto](goto.html).

```
:99→I
:Goto 0
…
:Lbl 0
:ClrDraw
:ZStandard
:ZInteger
:Menu(" FROGGER v1.0 ","PLAY",1,"HELP",2,"EXIT",3
```

**Extra Variables**

If you are out of variables (A-Z and theta) to use in a program, there are actually 8 more that can be used in the same way as the others (although they do have functions of their own in certain situations). However, none of them appear in the memory menu. They are: 

```
n
```

This can be typed using the [X,T,theta,n] button when in sequential mode, or by using the catalog and jumping to n. You can use the DelVar command on this, but you cannot call it if it is not defined like you can other variables.

```
ℕ, I%, PV, PMT, FV, P/Y, C/Y
```

These can all be typed using [Apps][Finance...][Vars]. You cannot use the DelVar command on these, however you can call them if they are not defined (they will come up as 0).

This allows for use of up to 35 variables instead of 27.

More Information on the last 7 of these can be found at the bottom of the [System Variables](system-variables.html) page.

<center>

|**[<< Downloads](downloads.html)**|**[Table of Contents](starter-kit.html)**|**[Variable Tips >>](sk:variable-tips.html)**|
| --- | --- | --- |

</center>
