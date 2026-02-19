![The GraphColor( Command](graphcolor/@ "The GraphColor( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Changes the color of a certain function.|GraphColor(function#,color#)|TI-84+ CSE/CE|2 bytes|

### Menu Location
Press:
1. 2ND 0 to access catalog.
1. TAN to get to the G index
1. Scroll down to find GraphColor(, then ENTER to paste.

Graph colors can also be changed under Y=.
       
# The GraphColor( Command

The `GraphColor(` command will change the color of any function from `Y<sub>0</sub>` to `Y<sub>9</sub>`. So, for example, to change the color of `Y<sub>3</sub>` to NAVY, do:
```
GraphColor(3,NAVY
```
Notice, you must use the number of the function, rather than the entire function name, which would be `Y<sub>3</sub>`.

As you may know, you can also use the value of the color, which can be any integer between 10 and 24. So, our last command could also be:
```
GraphColor(3,17
```



## Related Commands

- [`GraphStyle(`](graphstyle.html)
- [`BorderColor `](bordercolor-.html)
