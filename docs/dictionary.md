# Dictionary
A dictionary (also known as a map) is a data structure in which one piece of data maps to another piece of data, and the first datum (the key) maps to and only to the second datum (the value), much like how a word in a dictionary maps to a definition.  However, there can be multiple keys for the same value. The major operations for a dictionary are *put*, *contains*, *get*, and *remove*. *Put* adds a key and a value to the dictionary. *Contains* indicates whether or not a key is to be found within the dictionary. *Get* retrieves the value associated with the given key. *Remove* removes a key and value pair based on a given key.

## Implementation in TI-Basic

The most easily created dictionary in TI-Basic is implemented using a string. The string would have many keys and values, separated by delimiters (similar to the string implementations of [stacks](stack.html) and [queues](queue.html)). The string can have keys and values of any length so a delimiter must be used to separate the keys and values from each other. For dictionaries, it useful to have two delimiters; one which separates keys from their values, and another which separates one entry from other entries. These delimiters can be any short string that will **never** appear in any of the entries. Here, we will use the standard ":" and "," delimiters.
To create a dictionary store an instance of the entry delimiter into the string. This is because in TI-Basic, one cannot add to empty strings, and for our implementation, each key and value **must** be surrounded by a delimiter on either end. The reason for this will become clear soon. We must also add a padding character at the front of the string; this will be to eliminate special cases for the remove operation.
```
:"?,"→Str0
```

It does not matter onto which end we *put* data because we can get and remove data from any point in the dictionary so for this instance, we're going to add to the end of the dictionary.
```
:"KEY"→Str1
:"VALUE"→Str2
:Str0+Str1+":"+Str2+","→Str0
```

To find whether a key is contained with in the dictionary (*contains*) use [inString(](instring.html). If it returns 0, the key is not in the dictionary.
```
:"KEY"→Str1
:inString(Str1+":")→N
```

To *get* a value, we first have to find the location of the key using the [inString(](instring.html) function. Then we add to that the length of the key and the lengths of the two surrounding delimiters. We now know the location of the first character of the value. To find the length of value use inString( starting at that location and subtract it from the first location.
```
:"KEY"→Str1
:inString(Str0,Str1+":")→N
:If Ans:Then
:inString(Str0,",",N)→M
:sub(Str0,N,M-N)→Str2
:End
```

To *remove* a value, we have to use the same code as above to locate the end of the key-value segment of the string. We then concatenate the part of the string before the key-value combination and the part of the string after the key-value combination. This is why we added the initial character ("?"), because we can't concatenate with an empty string in TI-Basic.

```
:"KEY"→Str1
:instring(Str0,Str1+":")→N
:If Ans:Then
:inString(Str0,",",N)→M
:sub(Str0,1,N-2)+sub(Str0,M,length(Str0)-M+1)→Str0
:End
```

## Advanced Dictionary Operations

The four basic dictionary functions, *put*, *get*, *contains*, and *remove*, can be chained together to create more advanced commands. A few are listed below, namely, *pop*, *update*, *keys*, and *values*. A basic function will be denoted as a subprogram within each code block, using the same arguments as above.

To *pop* a key, we simply read the value of the key, then remove the key.
```
:"KEY"→Str1
:prgmGET
:prgmREMOVE
```

To *update* the dictionary with a new key-value pair, there are two possibilities: 1) The key does not exist in the dictionary, so we *put* it on the end, or 2) The key does exist, so we must *remove* the old key and *put* the new one. This chain of commands becomes:
```
:"KEY"→Str1
:"VALUE"→Str2
:prgmCONTAINS
:If N :prgmREMOVE
:prgmPUT
```

*Keys* allows to get a list of all the keys in the dictionary on their own. The "list" will actually be a string of keys, separated by the entry delimiter ",".
```
:2→N
:",→Str3
:While N<length(Str0)
:inString(Str0,":",N)→M
:Str3+sub(Str0,N,M-N)+","→Str3
:1+inString(Str0,",",M→N
:End
```

Similarly, *values* obtains a list of the dictionary's values. This can be done by simply using *get* on each key from *keys*.
```
:2→N
:",→Str4
:prgmKEYS
:While N<length(Str3)
:inString(Str3,",",N)→M
:sub(Str3,N,M-N)→Str1
:prgmGET
:Str4+Str2+","→Str4
:M+1→N
:End
```
