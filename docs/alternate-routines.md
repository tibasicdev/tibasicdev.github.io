# Alternate Routines
One of the great things about working with TI Basic is that people are always developing new routines.  This page is where you can display code for things that you think could be better than currently accepted routines.
### GetKey Routines
This alternate routine is a size optimization of the usual movement routine used to move a character around the screen (9 bytes less than the regular routine).  It is a replacement for the currently accepted movement routine.  It was discovered by Darkstone Knight and Burr and implemented by Basickevin.

```
:4→A
:8→B
:While 1
:getKey→K
:1
:If K
:" //one space//
:Output(A,B,Ans
:min(8,max(1,A+sum(Δlist(K={25,34→A
:min(16,max(1,B+sum(Δlist(K={24,26→B
:End
```

This is Basickevin's speed optimization of the same routine.  It's about 15% faster, 25 bytes larger, and the variables are all under the finanace window.

```
:4→PMT
:1→FV
:While 1
:getKey→PV
:If PV
:Output(PMT,FV," //one space//
:min(8,max(1,PMT+sum(Δlist(PV={25,34→PMT
:min(16,max(1,FV+sum(Δlist(PV={24,26→FV
:Output(PMT,FV,1
:End
```

## References
- The getKey routine on this page comes from [darkstone knight's post](http://tibasicdev.github.io/forum/t-67037/new-faster-getkey) in the TI|BD forums
