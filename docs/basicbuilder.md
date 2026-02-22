# Basic Builder
There is a computer application for the purpose of turning a BASIC program(s) into a Flash application. It is known as Basic Builder (BB for short). There are several pros and cons, so in the end, it is just a personal choice, and dependent on how large the programs are.


**Pros:**
- Your programs are compressed, allowing more programs in an app than regular archived programs
- It will be run from the archive
- People can't edit it (sometimes is a con)
- Apps look more professional


**Cons:**
- If your program takes up very little space, it is a waste of archive to turn it into an app
- BB can only make single page applications (16384 bytes), so there is a limit to the size of your program(s). For games including programs that always remains in the archive memory and that are only copied into the RAM when needed (such as with Resource or [xLIB](xlib.html) app), you still need to keep these programs separate from the BasicBuilder app, which partially defeats its purpose.
- [Picture](pictures.html) files must be separate from the app if they are going to be used by [Omnicalc](omnicalc.html), [xLIB](xlib.html) or Celtic III commands. Else, you will need to create installation code that is only ran the first time you run your program that will copy all pictures from BasicBuilder to the picture slots you want.
- You can't [GOTO](goto.html) an error (sometimes good)
- You can't delete variables inside the app, although there is a [workaround](basicbuilder:delvar.html).


## Using Basic Builder

> TO-DO: Add some screenshots of the steps to go along with the word instructions.

These are step-by-step instructions on using Basic Builder.

### Obtaining Basic Builder and Other Equipment

The most recent version of Basic Builder can be found [here](http://www.ticalc.org/archives/files/fileinfo/321/32127.html). You will need Wappsign to sign the app you create, which can be found with the 83+ Flash Debugger, which can be found [here](https://archive.org/details/ti-83sdk1.0b28).

### Installation

All you need to install is the Flash Debugger, so open that file and follow the installation instructions.

### Building the Application Hex

The instructions for generating the hex are in the BB readme, steps 1~8, but I have the instructions below.

1. Ensure that all needed files (programs, subprograms, and pictures) are available. It is easier if they are in the same directory
2. Start up the BB executable
3. There are four fields on the right. Change 'Application name' to the name of your app, and 'Outputfile' to '<app name>.hex'. Leave the other two fields alone for now
4. Press the upper left button, the one with a sheet of paper and a green '+'

To understand the next few things, you have to understand what BB actually does. It creates an app, that when started, will normally just execute the main program. However, if you want the user to be able to execute multiple things from the beginning, you can create multiple menu items. These will be shown in the format of the [Menu(](menu.html) command. An example of this is a pack with several games that you want the user to choose from. You have several menu options and the user is free to decide which one.

1. After you pressed that button, you should have seen a field appear in the left. That is the menu entry for the horde of files you will now turn into some hex
2. Change that field from program name to the text that you want shown for that menu option when BB is started
3. Click 'Add program' on the right. Find your program. Do this over and over until you have all the necessary programs. Do the same for 'Add picture'
4. If you want more menu options, click the paper-and-plus button in the upper-left and repeat
5. Click 'Generate' in the lower-right

You should now have a .hex file in the BB directory.=, along with a small pop-up giving how much space was saved/how much space is left. But you can't do anything with this hex file... Yet.

### Signing the Hexfile

1. Click on Start -> All programs -> TI-83 Plus Flash Debugger -> Wappsign
2. You should have a small program running, called Wappsign. There should be four check boxes on the right. Check the upper two and un-check the lower two.
3. On the right of the 'Application' field, there should be a '...' button. Click it.
4. Browse for your hexfile.
5. Click 'Sign'.

Congratz! You should now have an application in the same directory as the hexfile!
