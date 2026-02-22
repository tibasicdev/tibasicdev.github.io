![The NewFold Command](68k_newfold/http://tibasicdev.github.io/local—files/template:command/samplescreenshot.gif "The NewFold Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Creates a folder with a specified name|NewFold *folder name*|89/92/T/+/V200|1 byte or 2 bytes|

### Menu Location
Catalog
       
# The NewFold Command
The NewFold command allows the user to create a new folder. It can be run like this:
```
NewFold Hello
//This would make a folder name "hello"
```

## Error Conditions

**[270 - Duplicate variable name](68k:errors.html#e270)** happens when you attempt to create an already made folder.


## Related Commands

Several (around 3) commands have a similar function or are used in a similar context to this command. Make a bulleted list of them, with links to the other commands' pages. It will often be the case that several commands all link to each other.

- [68k:NewData](68k:newdata.html)
- [68k:NewPic](68k:newpic.html)
- [68k:NewProb](68k:newprob.html)
