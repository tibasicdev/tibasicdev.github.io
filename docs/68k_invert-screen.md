# Invert Screen
**Routine Summary**

This routine uses the PxlHorz function to invert the graph screen.

**Inputs**

None

**Outputs**

The graph screen is inverted as a result of this program.

**Variables Used**

i - a counter variable
size - the size of the graph screen window in pixels
All of these are locally declared.

**Calculator Compatibility**

TI-89/92/+/V200


```
:invert()
:Prgm
:Local i,size
:when(getConfg()[10]=160,76,102)→size
:For i,0,size
: PxlHorz i,-1
:EndFor
:EndPrgm
```

The -1 at the end of PxlHorz is a flag that tells the system to invert all pixels along the line. I chose PxlHorz because this requires less lines to be drawn than PxlVert does.

## Error Conditions

None
