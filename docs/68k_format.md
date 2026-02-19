![The format() Command](68k_format/format.png "The format() Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Converts a number to a string with specified formatting.|format(*number*[,*options*])|This command works on all calculators.|3 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press D to enter the Strings submenu.
- Press 9 to select format(.
       
# The format() Command

E[[/size]]]]

The format() command is a more advanced version of [68k:string()](68k:string().html) specifically intended to convert numbers (usually, floating-point numbers) to strings. It can override settings like Display Digits and Exponential Format, and instead lets the user input these options and more in a string. Since it converts even integer input to floating-point, it also doesn't depend on the Base setting.

The format string can have the following values (not case-sensitive):
- **F*[number]*** overrides Display Digits to fixed-point with *[number]* digits after the decimal; *[number]* can be omitted to use the default, which is 12; it must be between 0 and 12.
- **S*[number]*** does this and also overrides Exponential Format to scientific.
- **E*[number]*** does this and also overrides Exponential Format to engineering.
- **G*[number][character]*** does this and also separates the digits to the left of the decimal into groups of three, with *[character]* as the separator. The default for *[character]*, if it is omitted, is a comma. If you make the separator a period, then the decimal point will become a comma.

To all of these, you can also append **R*[character]*** to replace the decimal point with *[character]*. Only 'symbols' are allowed for *[character]*, which is a bit vague: numbers and letters are not allowed, nor are some international characters.

```
:format(π,"F")
           "3.14159265359"
:format(2^25,"S6")
           "3.355443e7"
:format(2^25,"E6")
           "33.55443e6"
:format(2^25,"G0")
           "33,554,432."
:format(2^25,"G0 R ")
           "33 554 432 "
```

If the format string is empty, or if the argument is omitted entirely, format() will convert the number to a decimal, but otherwise will work just like [68k:string()](68k:string().html)

## Error Conditions



## Related Commands

- [68k:string()](68k:string().html)
- [68k:expr()](68k:expr().html)
