# Queue
A queue is an abstract data structure that stores objects in a First In First Out basis. The two main operations that can be performed on a queue are *enqueue* and *dequeue*. *Enqueue* adds an element to the bottom of a queue. *Dequeue* removes the top element from the queue, and returns it. A queue can be visualized as a line of people waiting to get on a bus. The first person there gets on first, and the last person there gets on last.

Queues are widely used in the TI-83+ operating system, and are found in most computer systems.

## Implementation in TI-Basic

TI-Basic does not have a queue data structure by default, but depending on what needs to be stored, a stack can be implemented as either a list or a string. 

### Lists

In a list, the top can be considered the first element of the list or the last element of the list. Both approaches are valid, and either may be more appropriate depending on the situation.

#### First element as top

To make a queue using a list, one can create a list for which one assumes that the first element is the top of the queue. In order to enqueue one would do:
```
:N→L₁(1+dim(L₁
```
This adds N to the end of the list. Dequeue is done by getting the value of the first element and then using [ΔList(](deltalist.html) in conjuntion with [cumSum(](cumsum.html) to remove the first element of the list. This can be done with the following code:
```
:L₁(1→N
:ΔList(cumSum(L₁→L₁
```
If the queue is empty, then the list will be empty and dim(L₁) will return 0. In this implementation, adding an element to the queue is fast, whereas removing an element is slow.

#### Last element as top

To make a queue using a list, one can create a list for which one assumes that the last element is the top of the stack In order to enqueue onto the stack one would do:
```
:augment({N},L₁)→L₁
```
This stores N into the first element of the list. Dequeue is done by getting the value of the last element and then decreasing the list size by one. This can be done with the following code:
```
:L₁(dim(L₁))→N
:dim(L₁)-1→dim(L₁
```
If the queue is empty, then the list will be empty and dim(L₁) will return 0. Here, adding an element is slow, but removing one is relatively fast.

### Strings

To make a queue using a string one has to store values into a string with a specified delimiter. The delimiter is a one or two token string that will *not* appear in any of the data items being put into the queue. This delimiter will change depending on what you are storing in the queue. To begin, store one instance of the delimiter (for this example, "::") into a string which will be the stack. To push on to the string, simply add the new data and a delimiter to the end of the string (for this example Str0).
```
:Str0+Str1+"::"→Str0
```
To dequeue from the string, use the inString( function for find the first instance of the delimiter and remove it from the queue.
```
:inString(Str0,"::")→N
:sub(Str0,1,N-1)→Str1
:sub(Str0,N+2,length(Str0)-N-1)→Str0
```
If the queue is empty, the string will contain one delimiter and length(Str0) will return the length of the delimiter (in this case 2).
