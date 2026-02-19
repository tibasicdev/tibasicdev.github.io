# Assembly Hex Codes
![asmprgm-example.gif](asmprgm-example.gif "")
Example of Inputting Hex Code


There are all sorts of small assembly programs that you can create simply using the calculator's built-in assembly commands (specifically, [AsmPrgm](asmprgm.html)), along with the appropriate hexadecimal code. In order to run a program, you need to use the [Asm(](asm-command.html) command, where Asm(prgmPROGNAME is the program that contains the hexadecimal code.

As a word of caution, when entering in the hexadecimal, you need to be very careful that you type it in exactly as you see it. If there is a single incorrect character, the calculator might crash and reset your RAM when you turn it on again. We have tested the hexadecimal codes to make sure they work, but it's up to you to enter them in correctly.

Also note that these programs may not work on the original TI-83, only the 83+ or higher. Most are harmless, but the last one specifically will crash.

Many of the codes no longer function on the TI-84+CSE or TI-84+CE. The new codes for these calculators can be found [here](84cse:hexcodes.html).



## Toggle Program Mode

```
:AsmPrgm21F8893E02AE77C9
```

When used in a program, it allows you to use [Archive](archive.html) and [UnArchive](unarchive.html) on other programs. Make sure to switch back to "program mode" when you're done by running the program again.

When used on the home screen, it allows you to use programming commands like [If](if.html) and [For(](for.html); this has limited utility, but maybe it's useful to check a short bit of code without creating a new program for it.

## Screen to Graph

```
:AsmPrgm214093EF7B4CC9
```

This will put the current screen image on the graph screen.

## Quick Key

```
:AsmPrgm3A3F84EF8C47EFBF4AC9
```

This is a getKey routine that makes all keys repeat, not just arrows and there is no delay between repeats. The key codes are different, so you might need to experiment.

## Text Inverse

```
:AsmPrgm21F5893E08AE77C9
```

This will switch from normal text mode to inverse (white text on black background) and vice versa.

## Lowercase
### Lowercase On
```AsmPrgmFDCB24DEC9
```
### Lowercase Off
```AsmPrgmFDCB249EC9
```
### Lowercase Toggle
```AsmPrgm21148A3E08AE77C9
```
This will toggle lowercase on or off

## Fill Screen
Clear, Black, & Invert Screen
### LCD Clear
```AsmPrgmEF4045C9
```
This only clears the LCD, it doesn't actually clear the graph screen or homescreen
### White
```AsmPrgm210000115F3FEF5C4DC9
```
This fills the graph screen with white pixels. This is not like ClrDraw, as it won't update graphs or plots.
### Black
```AsmPrgm210000115F3FEF624DC9
```
This fills the graph screen with black pixels
### Invert
```AsmPrgm210000115F3FEF5F4DC9
```
This inverts the contents of the screen, drawing it to the graph screen.
### Border
```AsmPrgm210000115F3FEF7D4DC9
```
This draws a border around the graph screen.
### White Border
```AsmPrgm210000115F3FEF864DC9
```
This draws a border of white pixels around the graph screen.
### Black Border, Clear Inside
```AsmPrgm210000115F3FEF8C4DC9
```
This will draw a black border around the graph screen, clearing the contents inside.
## Change contrast level
### Set Contrast
The input is a value between 0 and 39 in [Ans](ans.html) (if you use something else, the program will ignore it), with 0 corresponding to the lowest contrast value, and 39 to the highest. The number displayed by the OS in the top right corner of the screen when you change the contrast with 2nd+UP and 2nd+DOWN is 1/4 of this value, rounded (so a displayed 6 corresponds to a value between 24 and 27 when using this program).

```AsmPrgmEFD74AEFEF4AC6D8D8D3107B324784C9
```

### Get Contrast
This gets the OS contrast level and stores it in Ans:
```AsmPrgm3A4784EF8C47EFBF4AC9
```

### Decrease Contrast
```AsmPrgm2147847ED601D835C6D8D310C9
```
Decrease the contrast by one unit (this will be ignored if the contrast is at minimum already).

### Increase Contrast
```AsmPrgm2147847EC6D9D834D310C9
```
Increase the contrast by one unit (this will be ignored if the contrast is at maximum already).

## Run Indicator
### Run Indicator Off
```AsmPrgmEF7045C9
```
### Run Indicator On
```AsmPrgmEF6D45C9
```
### Toggle Run Indicator
```AsmPrgm21028A3E01AE77C9
```
Note that when this routine turns the run indicator off, it doesn't erase the run indicator, it simply stops it. You can do this yourself — either by outputting something to the top right corner, or by clearing the screen ([ClrDraw](clrdraw.html) or [ClrHome](clrhome.html), doesn’t matter).

## Simulated Key Presses

### Alpha Lock
```AsmPrgmFD361251C9
```
This simulates [2nd][Alpha]
### Alpha Lock (No disable)
```AsmPrgmFD3612D1C9
```
This is the same as the first, but you have to press [2nd][mode] to disable it.
### Lowercase Press
```AsmPrgmFD361231C9
```
This works even if lowercase isn't enabled.
### Lowercase Lock
```AsmPrgmFD361271C9
```
This simulates [2nd][Alpha][Alpha].
### Lowercase Lock (No disable)
```AsmPrgmFD3612B1C9
```
This can only be disabled by pressing [2nd][mode]
### Alpha Off
```AsmPrgm21028A3E0FA677C9
```
Alternatively:
```AsmPrgm3E01FD7712C9
```
### [2nd]
```AsmPrgmFDCB12DEC9
```

An interesting use of these codes can be for prompting user input (If you run Alpha Lock, for example, [Input](input.html) will start with an Alpha press.

If you run the Alpha Lock that can't be disabled at the start of your program and a user presses ON (or an error occurs), you will not be able to select the options, so you are forced to press [2nd][mode].
## Disabling "Done" Message
To disable the "Done" message at the end of a Basic program:
```AsmPrgmFDCB00AEC9
```
## Un-Dirty Graph Screen
```:AsmPrgmFDCB0386C9
```

This will mark the Graph Screen as not dirty.  Using [ClrDraw](clrdraw.html) will mark the Graph Screen as dirty so the next time it is displayed the screen will be cleared. Many ASM libraries (such as [xLIB](xlib.html)) modify the graph buffer without displaying the screen which might be unintentionally cleared.

## Turn Calculator Off

With turning the calculator off, you have options. You can either turn the screen off (your program will continue running, but the calculator will look like it’s turned off) or actually turn the calculator off and wait for the [on] button to be pressed.

### LCD Off
```AsmPrgm3E02D310C9
```

### LCD On
```AsmPrgm3E03D310C9
```

### Toggle LCD Power
```AsmPrgmDB108787879FC603D310C9
```

### Calculator Off
```AsmPrgm3E01D303FB76FDCB09A6C9
```
Turn the calculator off; wait for [on] key before continuing:

Finally, exit the program and turn the calculator off (i.e., once you turn the calculator back on, it will be at the home screen):
**Note, this eats free RAM, so avoid using this!**
```
:AsmPrgmEF0850
```

## Auto Calc

### Auto DMS
```AsmPrgmFD360A06C9
```
Auto DMS displays all decimals in Degrees-Minutes-Seconds on the home screen, automatically.

### Auto Fractions
```AsmPrgmFD360A0CC9
```
Auto Fractions will display decimals as fractions (if it can) on the home screen, automatically.

## Screen Shifting
***Note:*** These routines do not automatically update the LCD. This can be forced by replacing the ending C9 with EF6A48C9.

### Shift Screen Right 1
```
:AsmPrgm2140930E40060CB7CB1E2310FB0D20F5C9
```
This shifts the graph screen right by one pixel. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Left 1
```
:AsmPrgm213F960E40060CB7CB162B10FB0D20F5C9
```
This shifts the graph screen left by one pixel. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Up 1
```
:AsmPrgm214C9311409301F402EDB0EB010C00EF304CC9
```
This shifts the graph screen up by one pixel. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Down 1
```
:AsmPrgm213396113F9601F402EDB823010C00EF304CC9
```
This shifts the graph screen down by one pixel. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Right 4
```
:AsmPrgm2140930E40AF060CED672310FB0D20F5C9
```
This shifts the graph screen right by four pixels. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Left 4
```
:AsmPrgm213F960E40AF060CED6F2B10FB0D20F5C9
```
This shifts the graph screen left by four pixels. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Up 4
```
:AsmPrgm21709311409301D002EDB0EB013000EF304CC9
```
This shifts the graph screen up by four pixels. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

### Shift Screen Down 4
```
:AsmPrgm210F96113F9601D002EDB823013000EF304CC9
```
This shifts the graph screen down by four pixels. See the note [here](http://tibasicdev.github.io/hexcodes#toc42) for updating the screen.

## Memory Functions

### Free RAM
Get the amount of free RAM left in Ans
```AsmPrgmEFE542EF9247EF5641EFBF4AC9
```

### Archiving
```AsmPrgm
EFD74AD604C0   ;Get the pointers to Ans
EB4E234623     ;Get the size and location of the string
117884EDB012   ;Copy it to OP1
EFF142D8       ;Locate the var, exit if it doesn't exist
78B7C0         ;Exit if it is already archived
EFD84FC9       ;Archive it and exit
```
Input: Ans is a string with the name of the variable to archive. The name needs a prefix byte to determine what type of variable it is. Some of them are:
```
 and      Real/Complex
A         List
B         Matrix
C         Equation
D         String
[         Program/Protected program
E         Program/Protected program
F         Program/Protected program
G         Picture
H         GDB
U         Appvar
[[/code]] For example, to archive prgmTEST, any of these inputs will work:
[[code]]
"[TEST
"ETEST
"FTEST
```
### Unarchiving
```AsmPrgm
EFD74AD604C0
EB4E234623
117884EDB0
12EFF142D8
78B7C8         ;Only difference
EFD84FC9
```
Input: See Archiving.
### ToggleArch
```AsmPrgm
EFD74AD604C0
EB4E234623
117884EDB0
12EFF142D8
EFD84FC9
```
Input: See Archiving.
### Reset Defaults
```AsmPrgmEF2851C9
```
### Reset RAM
```AsmPrgmEF4E40C9
AsmPrgmC7
```
### DelVar
```AsmPrgm
EFD74AD604C0
EB4E234623
117884EDB0
12EFF142D8
EFC64FC9
```
Input: See Archiving.

## Miscellaneous

### Remove Cursor
```AsmPrgmFDCB0CE6C9
```
This is harmless, but it stops displaying that blinking cursor :D Just press [2nd][MODE] to put it back to normal. What, jokes are allowed, right?

### Edit Lock/Unlock Program
We are generally an open source community, so this should be fun. To toggle the lock status of a program:
```:AsmPrgmEFD74AFE04C03CEB4E234623117884121CEDB0AF12EFF142D8EE0377C9
```
Please note that you should avoid editing an assembly program using this code. It will likely get messed up and it could cause it to be volatile. The program name will be in Ans, as a string. For example, "HELLO":Asm(prgmLOCK

### Battery Check
This is a "smart" battery check, that detects if the calc is an 84+ or an 83+. If it is a TI-83+, either a 0 or 4 is stored to Ans. If it is a TI-84+, a value from 0 to 4 is stored to Ans. 0 implies a low battery, 4 implies a good battery, and anything in between is just that.
```AsmPrgm
EF6F4C3D280A78FE1E
3805
EF21521808
EFB3503E042001AF
EF8C47EFBF4AC9
```

### ASCII
Display an ASCII character at the last cursor position, using Ans (0 to 255)
```AsmPrgmEFD74AEFEF4AEF0445C9
```
Display a string of ASCII characters using a list in Ans (use values 0 to 255):
```AsmPrgmEFD74A3DC0EB462323C5EF7A41E5EFEF4AEF0445E1C110F1C9
```
An example of using this might be:
```
:65+{7,4,11,11,14
:Asm(prgmASCII
```
That will display "HELLO" and if you change the 65 to a 97, it will disply "hello"

### Error
This code will cause an error to be thrown, based on the value in Ans. The values correspond to the ones found [here](http://www.brandonw.net/calcstuff/ti83plus.txt). Use your browser's search tool to look for "E_Overflow" which is Error 1. By default, there is no Goto option unless you add 128 to the values. So for example, for a divide by zero error with a goto option, use 130 as the error code.
```AsmPrgmEFD74AEFEF4AEFD744C9
```

### Token generator
This code is useful if you want to access an arbitrary [token](tokens.html) given its hex code. For instance, suppose you want to get the [PrintScreen](printscreen.html) token, which has hex code 91. Write
```
:AsmPrgmEFF1423605C9
:91
```
where the last line has the hex code of the token or tokens you want.

To use this, first compile the program with the [AsmComp(](asmcomp.html) command, then run the compiled version with the [Asm(](asm-command.html) command. This will unlock the compiled program for you in the program editor. When you edit it, you'll see a bunch of garbage characters, followed by the token you wanted.

## Advanced
These codes are long and involved, so be careful with putting them in. However, they are very useful.
### CharLength
```
EFD74AD604C0
6F67EB
4E234623EB
C5D5E51A
EFA342F5
EBEF9445
F1E1D109C1
20020B13
0B1378B120E5
EF9247
EF5641
EFBF4A
C9
```
This will return how many characters are in the string (the string is in Ans). For example, "sin(ln(2))" would return 10.
### String Pixel Width
```
EFD74AD604C0
676FEB
4E234623EB
C5D5E51A
EFA342F5
EBEF9445
218D8477EFB44C06004F
F1E1D109C1
20020B13
0B1378B1
20DB
EF9247
EF5641
EFBF4A
C9
```
This returns how wide a string is in pixels.
### ListToVars 1
```
EFD74AFE01C0
1AFE1B38023E1B
EB232347
3E41
C5F5E5F5
EFC541F1
327984
D73003EF0F43
E1010900EDB0
F13CC110E4
C9
```
If Ans is a list, each element will be stored to a Real var, starting with A and incrementing through each var until the list is done. For example, {0,4,3,12,8,24}  will store 0→A, 4→B, 3→C, 12→D, 8→E, 24→F

### ListToVars 2
```
EFC5413EAA327984
D7300F
3E40061B21EC86
3C772310FB
11EA861313D5
EFD74AFE01C0
1AFE1B38023E1B
EB232347
D11A13D5
C5E5F5
EFC541F1
327984
D73003EF0F43
E1010900EDB0
C110E3
D1C9
```
If Str1 contains the list of variables to write to and L1 has the list of values to write, this program will write the values to the variables. For example:
```
 :"ADCZQGB→Str1
 :{0,1,1,2,3,5,8
 :Asm(prgmL2V2
Then result will be:
 :A is 0
 :D is 1
 :C is 1
 :Z is 2
 :Q is 3
 :G is 5
 :B is 8
```

### ExecAns
```
EFD74A
FE04C0
215500 ;55 is the token for "U"
22EC86227984
21F086
EB4E234623
ED43EE86
EDB0
3E05327884
EFF142
3803EFC64F
3E0521EC86
EF3C4C
C9
```
Ans is a string, as input. This will delete prgmU, then copy Ans to prgmU and run it, whether it is assembly or BASIC code.

### RepeatKeys
```
180A
83473A4584323F8478C9
2100807EFE83
2006AF77323F84C9
11979DEB018000EDB0
DB06210080EF664FC9
```
This will set a hook that causes all keys to register very quickly. On top of that, all keys repeat. Note that this will not activate during program execution. Run this program again to deactivate

### FastKeys
```
1809
83473E0132428478C9
2100807EFE83
2006AF77323F84C9
11979DEB018000EDB0
DB06210080EF664FC9
```
This will cause repeating keys (like the arrows or [Del]) to repeat very quickly.

### MultiKeys 2
```
017F07210000545C
CB0179D301E5E1DB012FB720083E08856F10ED180E
C506082C0F30025C6510F8C110DD
7CB720016F
6C62
7BB7280A
444D2909290929292919
EF9247
EF5641
EFBF4A
C9
```
This returns a unique key code for any combination of one or two key presses. Values are 0 to 3191.

### Sprite
```
EFDA4AEFEF4A
626B
19192929E5
EFE04AEFEF4A
1693CBF3E119E5
EFD74AE1FE04C0
1313
010C08
CDCC9DCDCC9D780600094710F3
EF6A48
C9
1AC6C03002D607ED6F13C9
```
This will draw an 8x8 sprite to the graph screen using Ans as the hex string of data, X and Y as coordinates. Y can be anywhere from 0 to 56, X should be 0 to 11 (It draws to every eighth pixel).  The string should be 16 characters long, each character is a hex value that corresponds to the on/off state of 4 pixels.  So the string "3C42A581A599423C" would draw a smiley face.

## References

- Many of these codes (the original ones) come from [DarkerLine's Blog](http://mpl.unitedti.org/?p-18), and the last hex-code in particular for turning off the calculator comes from chipmaster.
- For more opcodes, see the discussions on ASM Programming or Assembly Hex Codes.
- Many codes come from "Zeda's Hex Codes"
