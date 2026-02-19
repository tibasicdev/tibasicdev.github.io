![The InputStr Command](68k_inputstr/http://tibasicdev.github.io/local—files/68k:inputstr/InputStr68K.gif "The InputStr Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Stores a string to a variable|InputStr *variable*|TI 89(T)/92|1 byte or 2 bytes|

### Menu Location
In the program editor, press [F3][4]
# The InputStr Command
The InputStr command allows you to input a string to a variable. Since [68k:Input](68k:input.html) doesn't support the storing of strings into variables, you have to use this command to do that. Keep in mind that the inputted variable cannot be the name of a preexisting variable or flash application that is locked, protected, or archived. For example, if you had a program named "a" or "hello", the command wouldn't work because it is already in use.
```
InputStr A
//Here, you would a string to be stored to the variable A

InputStr hello
//This would store the string into the variable "hello".
```
## Related Commands
- [68k:Input](68k:input.html)
- [68k:Prompt](68k:prompt.html)
- [68k:Disp](68k:disp.html)
- [68k:Request](68k:request.html)
## Error Conditions

## Also See
- [Programming Commands](http://tibasicdev.github.io/68k:programming)
