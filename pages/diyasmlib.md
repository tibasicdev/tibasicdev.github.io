# DIY Assembly Library
TI-Basic Developer has a slew of [assembly hexcodes](hexcodes.html) and the list is growing. Though these are often touted as dangerous if used improperly, there are perfectly acceptable ways of combining and creating your own codes *even if you don't know assembly*. This page is focused on how to create your own assembly libraries using the hexcodes on this site.

## Step 1: Select your routines
First, figure out which commands you want to include. Some of the commands will **not** work with this method:
- Sprite
- Fast Keys
- Repeat Keys
These will not work only because they use some constant addresses for routines (basically, it expects a routine to be in a specific place in RAM, so you would need to recalculate the addresses which requires some assembly knowledge).
## Step 2: Organise.
Arrange the commands you selected in some order. We will be accessing them using a number in Ans starting at zero.

## Step 3: Choose a template
These are four basic templates that you can use for your library to start. There are more complicated ones mentioned later for the adventurous.
- If any of your routines require an input in Ans as a number (and none require Ans to be a string):
```
1817              ;skips the first chunk of code
ED5BAF84
7AB3C8
1BED53AF84
2AB184E7
22B184
EFEF4AC9

EFD74A3DC0
EB4E234623
ED43AF84
22B184
CD979D
```
- If any of the routines require Ans as a string (and none require Ans to be a number), we will need to use Str1 instead:
```
1810
EFC541
21AA00
227984
D7
EB4E234623C9
EFD74A
EFEF4A
```
- If any routines require Ans as a number and any routines require Ans as a string:
```
1827              ;skips the first chunk of code
ED5BAF84
7AB3C8
1BED53AF84
2AB184E7
22B184
EFEF4AC9
EFC541
21AA00
227984
D7
EB4E234623C9

EFD74A3DC0
EB4E234623
ED43AF84
22B184
CD979D
```
- If Ans is **not** an input for any of your routines:
```
EFD74AEFEF4A
```
## Step 4: Replace code.
The library needs input in Ans, so naturally there will be a conflict if any of your routines need input in Ans. In this event, if any inputs need to be numbers, we will have to use a two-element list to pass the second argument. This requires you to alter certain parts of code.
<u>Case 1:</u> Ans is **not** an input for any routines.
- No replacing is needed! Go to Step 5.
<u>Case 2:</u> Ans is a number for some inputs and is never a string
- Replace all instances of EFD74AEFEF4A with CD979D (This replaces Ans is a number input)
- Replace all instances of EFDA4AEFEF4A with CD979D (This replaces Y is an input)
- Replace all instances of EFE04AEFEF4A with CD979D (This replaces X as an input)
<u>Case 3:</u> Ans is a **string** for some inputs and is never a number
- Replace all instances of EFD74AFE04C0EB4E234623 with CD979D
- Replace all instances of EFD74AD604C0EB4E234623 with CD979D, if bugs occur, use CD979DAF.
Both of these codes do almost precisely the same thing.
<u>Case 4:</u> Ans is a number in some commands, and could be a string for some commands:
- Replace all instances of EFD74AEFEF4A with CD979D
- Replace all instances of EFDA4AEFEF4A with CD979D
- Replace all instances of EFE04AEFEF4A with CD979D
- Replace all instances of EFD74AFE04C0EB4E234623 with CDAE9D
- Replace all instances of EFD74AD604C0EB4E234623 with CDAE9D

## Step 5: Add your commands.
Now that we have the template for the library setup, we can add in the actual commands. To do this, some byte counting will need to be done.
```
4704
10**
<<code0>>
10**
<<code1>>
10**
<<code2>>
10**
<<code3>>
10**
<<code4>>
...
05C0
<<last code>>
```
The **means you need to count how many bytes are in the routine following. Every two hex digits makes one byte. Every full line in the TI-BASIC editor is 8 bytes since it is 16 chars wide.
So for example, 3E02D310C9 is 5 bytes. Be careful, this value must be in hexadecimal!


Now for my own example. I will use 
ScreenOn : 3E03D310C9
ScreenOff : 3E02D310C9
ScreenToggle : DB10CB6F3E0220013CD310C9
QuickKey : 3A3F84EF8C47EFBF4AC9
LowerCase On : FDCB24DEC9
Lowercase Off : FDCB249EC9
Indicator Off : EF7045C9
Set Contrast : EFD74AEFEF4AC6D8D8D3107B324784C9

Since Set Contrast uses Ans as an input and none of the other routines need Ans as a string, I will use the first starting code:
```
1817              ;skips the first chunk of code
ED5BAF84
7AB3C8
1BED53AF84
2AB184E7
22B184
EFEF4AC9

EFD74A3DC0
EB4E234623
ED43AF84
22B184
CD979D
```
I will need to modify the code for Set Contrast:
**EFD74AEFEF4A**C6D8D8D3107B324784C9 turns into:
**CD979D**C6D8D8D3107B324784C9
And now I need to add this:
```
4704
1005
3E03D310C9
1005
3E02D310C9
100C        ;0C is hexadecimal for 12
DB10CB6F3E0220013CD310C9
100A        ;0A is hexadecimal for 10
3A3F84EF8C47EFBF4AC9
1005
FDCB24DEC9
1005
FDCB249EC9
1004
EF7045C9
05C0
CD979DC6D8D8D3107B324784C9
```

So now here is how to use your program:
- If your program has any commands that use Ans as a string input, the string must be in Str1 instead
- If your program has any commands that use Ans as a number input (or X or Y), the inputs are now passed as list elements.
- If Ans is not needed as a number input by any of the routines, you will simply pass a number to your program

So for example, my program takes a list input. The first element is the command number (I have 8 commands, so use 0 to 7) and the second argument is for any additional inputs the routine may need.
So SetContrast would be {7,<<contrast>>:Asm(prgmLIB
If you omit an argument, the program will read it as 0. So {7} passed to my program will set the contrast to zero. 

So now you have your own, personalised assembly library! Compress it using [AsmComp(](asmcomp.html)and it is ready for release with your games.

## Alternate Templates
If Ans is never a string input for your commands, you can use this code as an alternative. It is bigger, but it has a few perks. Instead of using a one element list, you can simply use the number. For example, {3:Asm(prgmLIB will be read the same as 3:Asm(prgmLIB. Omitted arguments are read as zero, but you can also make your library execute several commands. For example, if 3 and 4 are both separate commands and command 4 has an input, then {3,4,<<arg>>:Asm(prgmLIB will execute the two commands.

**Note:** If a command outputs a value in Ans, make sure it is the last command in the sequence. (otherwise it overwrites the input list!)
```
1818
ED5BAF847AB3C8
1BED53AF842AB184
E722B184EFEF4A37C9
EF524BD7EB
B720050101001806
3DC04E234623
ED43AF8422B184
CDCE9D18FBCD979D3802E1C9
```
