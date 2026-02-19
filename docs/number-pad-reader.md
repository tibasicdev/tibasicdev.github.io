# Key Code to Number (Number Pad Reader)
|Routine Summary|Inputs|Outputs|Authors|
|--- |--- |--- |--- |
|Outputs the number corresponding to a keypress.|*None*|*Ans* - The number pressed.|Unknown, Toothless the Night Fury|

```
:Repeat Ans≤9
:Repeat Ans
:getKey
:End
:Ans(102≠Ans)-13int(Ans/13(2>abs(5-abs(5-abs(Ans-83
:End
```

The routine waits for a key that corresponds to a number 0-9. All magic is on the lengthy line.

An alternate method to this is an adaptation of the Key Code to Letter routine, written below. Both methods share very extremely fast speeds, but the alternate method uses slightly more bytes. However, it does have the advantage of converting keycodes to strings instead of numbers, has the added period, and can be easily converted to numbers (through expr) if needed (unlike the other way around).

```
:Repeat Ans>71 and min(Ans≠{75,81,85,91,95
:getKey
:End
:sub("789  456  123  0.",Ans-36-5int(.1Ans),1
```

## Modifications
- You can delete the :Repeat Ans<=9 :End loop to not wait
- Delete the (102≠Ans) if you don't need the 0 number
- Fixed from "Outputs the letter corresponding to a keypress." to "Outputs the number."
- Added alternate method and general cleanup.

## Error Conditions
None known.

## Related Routines
- [Key Code Retriever](key-code-retriever.html)
- [Key Code to Letter](key-code-to-letter.html)
