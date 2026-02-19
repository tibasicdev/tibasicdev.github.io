![The → Command](68k_store/ "The → Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Stores a value to a variable.|*value*→*variable*|This command works on all calculators.|1 byte|
       
### Menu Location
Press the STO> key to insert →.
       
# The → Command

The `→` operator assigns a value to a variable.

Initially, a variable such as 'x', 'lastname', or 'cube' is undefined. When used in an expression, they will be treated as unknowns: 3*x-x may be simplified to 2*x, but will otherwise be left alone.

Once a value is assigned to a variable, that value will be substituted for the variable every time you use it. For example, you might store 5→x. Now, if you write 3*x-x, the answer won't be 2*x, but 10.

Any kind of value — a simple number, an expression, a string, list, or matrix, or even a function can be stored to a variable with →. The following are all valid:
```
:5→x
           5
:"Alighieri"→lastname
           "Alighieri"
:n^3→cube(n)
           Done
```

As a special case, you can even store to a single element of a list or matrix. For example:
```
:{1,2,3,4,5}→list
           {1  2  3  4  5}
:99→list[3]
           99
:list
           {1  2  99  4  5}
```

## Advanced Uses

Using the # ([`68k:indirection`](68k:indirection.html)) operator, you can store a value to a variable given its name, in a string.

## Optimization

There are alternatives to `→` such as [`68k:Define`](68k:define.html) or [`68k:CopyVar`](68k:copyvar.html); they have their uses in special situations, but `→` is better (smaller and easier to understand) in other cases.

## Error Conditions



## Related Commands

- # ([`68k:indirection`](68k:indirection.html))
- [`68k:Define`](68k:define.html)
- [`68k:DelVar`](68k:delvar.html)
