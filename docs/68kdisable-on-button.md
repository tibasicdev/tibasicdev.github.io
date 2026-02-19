# Disable On Button [68k OnBlock]
THIS TIP IS FROM TIPRGMZ9K

TIP IS MOSTLY FOR BASIC PROGRAMS.

Ok. Want to prevent people from pressing the "break" button
accidentally during a Dialog or Text session? Here's how:

```
Prgm
Lbl x
Try
flib("breakoff")
Dialog
Title "Test"
Text "You can't break me!"
EndDlog
Else
Goto x
EndTry
Endprgm
```

Note: This requires the [[[http://www.ticalc.org/archives/files/fileinfo/27/2788.html|flib](http://www.ticalc.org/archives/files/fileinfo/27/2788.html-flib)] library, which includes commands to disable the [ON] key.

It does not have to be Lbl x. This should prevent people from "breaking" the program and exiting the current program in session. This tip might not work all the time.

## Credits
Credits to burr, he made everything here.
