# Reverse String
**Inputs**

*string* - A string

**Outputs**

The reversal of the input string, or an empty string if the input is not a string.

**Variables Used**

s, temp, i
All are created locally in the program.

**Calculator Compatibility**

TI-89/92/+/V200



```
:reverse(s)
:Func
:Local i,temp
:""→temp
:If getType(s)=getType(temp) Then
: For i,1,dim(s)
:  mid(s,i,1)&temp→temp
: EndFor
:EndIf
:EndFunc
```

This function requires the user to enter a string as an argument. Many would object that a "return" is needed at the end. This is not true, because, if there is no "return" statement, the calculator automatically returns the last value that it calculated.

## Error Conditions

None
