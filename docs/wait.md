![The Wait Command](wait/http://tibasicdev.github.io/local—files/wait/waitexample.gif "The Wait Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Suspends execution for a specified amount of time|Wait [seconds]|TI-84+ CE OS 5.2 or higher|2 bytes|

### Menu Location
2ND CATALOG to enter the Catalog.
W to go to commands starting with W.
       
# The Wait Command

The Wait command was introduced in TI-OS 5.2 for the TI-84+CE. The Wait command tells the calculator to wait for a specified number of seconds before continuing. The specified amount of seconds can be a decimal, as it is not limited to whole numbers. This command can be useful for displaying information momentarily before proceeding in a program. The Wait command functions similarly to the [Pause](pause.html) command, but without the extra arguments.

```
:Disp "WAIT FOR IT!
:Wait 4
:Disp "Surprise
```

## Advanced Uses

The Wait command is useful for facilitating automatic linking within programs. Since the [Get(](get.html) and [GetCalc(](getcalc.html) commands only work when the sending calculator is in a preemptible state, including a small Wait delay will allow the other calculator to receive data.

Because the Wait command is relatively new, it may be advisable to avoid using it to ensure compatibility with older operating systems. Similar functionality can be achieved with the second optional argument to the [Pause](pause.html) command.

## Optimization

Traditionally it was recommended to use either a For( loop or the rand( command to create a delay within a program. The For( loop takes more space, and the rand( command uses more memory during execution.

```
:rand(100
can be
:Wait 1
```


## Error Conditions

- **[ERROR: INVALID](errors.html#invalid)** is thrown if the Wait command is executed on the home screen.

## Related Commands

- [Pause](pause.html)
- [Menu(](menu.html)
