![Gettime](68k_gettime/gettime.png "Gettime")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|returns a list formatted as {hours, minutes, seconds}|getTime()<br>getTime()|This command works on all calculators.|~8 byte(s)|
       
### Menu Location
In catalog under G for supported devices and operating systems.
# Gettime

Returns the current system time as a list of hour, minute, second values. This function was introduced in AMS 2.07 as per tigcc. 

```
getTime()
          {4 26 30}
```

## Advanced Uses

------

Can be used to determine the length of program execution. 

## Optimization

## Error Conditions

## Related Commands
## References 
[estack tag reference listing getTime tags as requiring AMS 2.07](http://tigcc.ticalc.org/doc/estack.html#exttags)
