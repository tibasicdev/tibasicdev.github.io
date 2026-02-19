# Taking Screenshots
Screenshots are one of the best ways to advertise your program at any stage of production. They're also great for explaining a problem you have, explaining how to fix a problem, demonstrating a calculator feature, or being displayed at the top of a TI-Basic Developer page. This tutorial will explain you some easy ways to create still and animated screenshots.

To begin with, you'll need an emulator (a list is available on our [resources](resources.html) page). If you're taking a screenshot of a program on your calculator, you'll need to send it to the computer (see [linking](linking.html)) first, then transfer it to the emulator. Although there are many methods of taking screenshots, I'll only cover a few of them.

## Still Screenshots

These are easy to make with any emulator, even one that doesn't have any screenshot functionality. You can simply use the Print Screen key on your computer to take a screenshot of the entire screen. Then, use any image editor, even one as simple as MS Paint, to remove everything except the emulator's image of the calculator screen. You can also add a border or anything else easily at this point. Save the image and you're done!

Alternatively, you can use TI-Screen Capture, included with TI-Connect. The icon looks like a camera and the software will take a picture of your calculator's screen.

## Animated Screenshots with CalcCapture

[CalcCapture](http://www.ticalc.org/archives/files/fileinfo/290/29024.html) allows you to take an animated screenshot of almost any emulator, with any skin. To begin using it, download CalcCapture, and run it (it doesn't require installation) at the same time as the emulator.

The first time you're using CalcCapture with a particular emulator, press the Configuration button at the top right of the CalcCapture window. Then press New at the top to configure a new emulator. Select the calculator you're emulating, and press the button to the right of the Windows Title field to select the window with the calculator in it. Press Capture to take a screenshot of the window at this moment, and arrange the numbers for the emulator window so that they match the calculator screen. (if it helps, the width and height should be multiples of 96 and 64 respectively — 95 and 63 if you don't want the bottom row and column that you can't access in Basic). Press OK when you're done.

For taking screenshots, the default settings should be sufficient. Choose ANIMATION for the "Capture Type" option, and enter the file name you want. Then press Capture and Stop Capture when you want to take the screenshot (or, you can use a hotkey). The counter at the top right of the screen shows the number of frames that have been captured.

## Animated Screenshots with PindurTI

The emulator PindurTI won't work with CalcCapture because the window title changes constantly, but it has its own screenshotting ability: while using the emulator, you can press Tab to start and then to stop the screenshot, which will be saved as ptiani#.gif in the same place that you put pindurti.exe. This is the so-called "crude screenshot", at 9 frames per second; you can take a "fine screenshot" at 25 frames per second with the Backspace key, but such a screenshot will not be displayed correctly in most browsers — it will be animated almost 3 times slower, giving the impression that your program is slower than it really is. Besides, 9 frames per second is good enough for most programs in any case.

## Some Considerations

When taking animated screenshots, try to plan out what you're going to show before taking the screenshot (if possible, down to the keys you're going to press). Don't include any of the unnecessary detail, like selecting the program out of the menu and pressing ENTER (start in the program itself).

If an actual screenshot is out of the question for one reason or another, consult the [Fake Screenshots](fake-screenshots.html) tutorial.
