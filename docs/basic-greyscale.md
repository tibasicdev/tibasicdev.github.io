# Basic greyscale
## Basic Greyscale

Most people do not know that greyscale can be achieved outside of a extra ASM library like Xlib, greyscale is nothing more than a pixel flashing on and off so quickly that it apperas to be grey. The con of greyscale in Basic is that it can give ERR:MEMoRY when you are using a delay, furthermore, only one grey can be achieved. For instance this hardcoded"block"

```
Repeat 0
Pxl-Change(31,47
Pxl-Change(31,48
Pxl-Change(31,49
Pxl-Change(30,47
Pxl-Change(30,48
Pxl-Change(30,49
Pxl-Change(29,47
Pxl-Change(29,48
Pxl-Change(29,49
Pxl-Change(28,47
Pxl-Change(28,48
Pxl-Change(28,49
End
```

this very simple code will switch the pixels on and off rapidly, a delay could be added using a "for(" loop.
