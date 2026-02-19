![Xor](nspire_xor/sample.png "Xor")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|
|--- |--- |--- |
|Exclusive or statement. Returns the truth value of value1 or value2, but not both, being true.|value1 xor value2|If this is only available on certain versions of the nspire|

### Menu Location
Describe how to get the command from a menu.

# Xor

 **xor** takes two numbers of expressions and checks to see if *exactly one* is True.  If both are True or both are False, it returns 0.
```1 xor 0
           1

:2 xor (3 xor 0)    (after evaluating 3 xor 0, it simplifies into True xor True.)
           0

:0 xor (1-1)^2
           0
```
### Table of Results
For reference, the following true/false table shows what gets returned when you use different combinations of 1 (true) and 0 (false):

| xor | 1 (true) | 0 (false) |
| --- | --- | --- |
| 1 (true) | 0 (false) | 1 (true) |
| --- | --- | --- |
| 0 (false) | 1 (true) | 0 (false) |
| --- | --- | --- |

## Related Commands

- [nspire:and](nspire:and.html)
- [nspire:or](nspire:or.html)
- [nspire:not(](nspire:not.html)
