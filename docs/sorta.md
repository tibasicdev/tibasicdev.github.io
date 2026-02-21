![The SortA( Command](sorta/SORTA.GIF "The SortA( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Sorts a list in ascending order.<br><br>For more than one list, sorts the first, and reorders other lists accordingly.|SortA(*list1* [,*list2*, ...])|TI-83/84/+/SE|1 byte|

### Menu Location
Press:
1. 2nd LIST to access the list menu.
2. RIGHT to access the OPS submenu.
3. ENTER to select SortA(.
       
# The SortA( Command

The SortA( command sorts a list in ascending order. It does not return it, but instead edits the original list variable (so it takes only list variables as arguments).

SortA( can also be passed multiple lists. In this case, it will sort the first list, and reorder the others so that elements which had the same indices initially will continue having the same indices. For example, suppose the X and Y coordinates of some points were stored in ∟X and ∟Y, so that the Nth point had coordinates ∟X(N) and ∟Y(N). Then SortA(∟X,∟Y) would sort the points by their x-coordinates, still preserving the same points.

However, SortA( is not stable: if several elements in the first list are equal, then the corresponding elements in the subsequent lists may still end up being in a different order than they were initially.

## Algorithm

The algorithm used by SortA( and [SortD(](sortd.html) appears to be a modified selection sort. It is still O(n<sup>2</sup>) on all inputs, but for some reason takes twice as long on a list with all equal elements. It is not stable.

## Related Commands

- [SortD(](sortd.html)
