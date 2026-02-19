# Key Code To Letter
|Routine Summary|Inputs|Outputs|Authors|Download|
|--- |--- |--- |--- |--- |
|Outputs a letter corresponding to a keypress.|*None*|*Ans* - the letter as a string|Weregoose|*https://www.dropbox.com/s/iqpl210jax3bo3n/Routines.8xg?dl=0 Routines.8xg|

```
:Repeat Ans>34 and min(Ans≠{44,45,105
:getKey
:End
:sub("ABC**DEFGHIJKLMNOPQRSTUVWXYZθ'* :?",Ans-5int(.1Ans+4),1
```

The Repeat loop makes sure good input is passed.
The last line takes from the string the letter according to the keycode.

## Error Conditions
None.

## Related Routines
- [Key Code Retriever](key-code-retriever.html)
- [Number Pad Reader](number-pad-reader.html)
