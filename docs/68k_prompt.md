![The Prompt Command](68k_prompt/Prompt68k.gif "The Prompt Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Prompts the user to assign a value to a variable|Prompt *var1,var2...*|TI 89(T)/92|2 bytes|

### Menu Location
In the program editor, press [F3][5]
       
# The Prompt Command
The Prompt command functions much like the [68k:Input](68k:input.html) command. It allows you to type a value to be stored to a variable. You can also prompt multiple values at the same time. For example:
```
Prompt A
//This will ask the user to type a value for A

Prompt A,B,C
//This will ask for a value for variables A,B, and C
```
You can also ask for input in user-made variables
```
Prompt cool
//This asks for a value for the variable "cool"
```

## Related Commands
- [68k:Input](68k:input.html)
- [68k:Disp](68k:disp.html)
