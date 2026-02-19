# Numerically Index Words
|Routine Summary|Inputs|Outputs|Variables Used|Author|Authors|
|--- |--- |--- |--- |--- |--- |
|Retrieves a word from an indexed string of words with an index number.|*A* - The word's index number<br>*Str0* - The index of words|*Str1* - The word|A, Str0, Str1|ADeadBody|ADeadBody|

```
:"000Word......001another..."→Str0    
:sub(Str0,3+inString(Str0,sub("0123456789",iPart(A/100)+1,1)+sub("0123456789",10fPart(iPart(A/10)/10)+1,1)+sub("0123456789",10fPart(A/10)+1,1)),10)→Str1
```

The routine converts the number into a string then searches for that in the string of words and stores the characters that follow it. Input in some 3 digit number ex: 001 would correspond to word 001.  102 would correspond to word 102.  The routine itself can store up to 1000 10 letter words.  I developed this for the purpose of storing and retrieving Pokemon names in the game I am developing but I am sure that there are other uses.

- **Acceptable inputs**:   zero, positive integers up to 999
- **Error inducing inputs**: decimals, negative numbers, numbers over 1000

This example of the routine would display "helloworld", 
```
:1→A
:"000worldhello001helloworld"→Str0
:sub(Str0,3+inString(Str0,sub("0123456789",iPart(A/100)+1,1)+sub("0123456789",10fPart(iPart(A/10)/10),1))+1,1)+sub("0123456789",10fPart(A/10)+1,1)),10)→Str1
:Disp Str1
```

If A were 0 instead of 1, then the output would be "worldhello".
In this modified version of the code it would output "helloworlditsme" a 15 letter code while still only displaying 10 letter words for any other input.  You can see how by looking at the end of the 3rd line of programming it adds a value of 5 to the length of the outputted string under the condition of A being equal to 1
```
:1→A
:"000worldhello001helloworlditsme002helloworld"→Str0
:sub(Str0,3+inString(Str0,sub("0123456789",iPart(A/010)+1,1)+sub("0123456789",10fPart(iPart(A/10)/10),1))+1,1)+sub("0123456789",10fPart(A/10)+1,1)),10+5(A=1))→Str1
:Disp Str1
```

## Error Conditions

- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown when the input number is either over 999 or under 0

## Related Routines
