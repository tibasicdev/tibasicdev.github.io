# Highlighting Text
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Highlights text, displaying it in white on a black background.|*Str1* - text to be displayed<br>*A* - row coordinate of the text<br>*B* - column coordinate of the text<br>*W* - pixel width of the text|None|Str1, A, B, C, W|[file highlighttext.zip]|

```
:Text(A,B,Str1
:For(A,A,A+6
:For(C,B-1,B+W
:Pxl-Change(A,C
:End:End
```

First, we display the string using [Text(](text.html) on the graph screen. This displayed it normally, using black on white. To switch it to white on black, we need to flip the pixels from white to black and black to white — this can be done using [Pxl-Change(](pxl-change.html). We chose the pixel command over the point command for two reasons: first, it is slightly faster, and second, it uses the same coordinate system as Text( — pixels (if we used Pt-Change, we'd need to convert from pixels to points to be sure of drawing in the same location).

We loop A from above to below the text, and C from just before the text to immediately after it. Note that because of the way the [For(](for.html) loop works — it saves the lower and upper bound before doing the loop — we can reuse the variable A. But we can't reuse B in the same way in the second For( loop, because the loop is done multiple times — it would work correctly the first time, but then B would have changed for the second.

Since Text( uses variable-width font, we need the W variable to tell us how long the string is in pixels. For uppercase letters, the width is 4 pixels; for spaces, the width is 1 pixel, and for lowercase letters, the width varies from 2 to 6 pixels.

Because Pxl-Change( must not go off the screen, check to see that the string fits on the screen entirely (with a border of 1 pixel around it) before displaying it.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if the string does not fit on the screen entirely.

## Related Routines

- [Wordwrapping Text on the Graphscreen](wordwrap-text.html)
