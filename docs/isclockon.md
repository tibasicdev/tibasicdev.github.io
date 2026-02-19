![The isClockOn Command](isclockon/ISCLOCKON.GIF "The isClockOn Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Returns whether the clock on the TI-84+/SE is on or off.|isClockOn|TI-84+/SE|2 bytes|

### Menu Location
This command can only be found in the catalog. Press:
1. 2nd CATALOG to enter the command catalog
1. i to skip to commands starting with I
1. Scroll down to isClockOn and select it
       
# The isClockOn Command

The `isClockOn` command returns whether the clock on the TI-84+/SE calculators is on or off. The command will return 1 if the clock is enabled and 0 if it is not. You can store it to a [variable](variable.html) for later use, or use it in [conditionals](conditionals.html) and [loops](loops.html) as part of the condition. For example, here is how you would check to see if the clock is on:

```
:If isClockOn
:Then
  (code if clock is on)
:Else
  (code if clock is off)
:End
```

## Related Commands

- [`ClockOff`](clockoff.html)
- [`ClockOn`](clockon.html)
