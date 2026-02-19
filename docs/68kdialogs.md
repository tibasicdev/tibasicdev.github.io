# Dialogs
Although input on the I/O screen (with commands such as [68k:Input](68k:input.html) and [68k:InputStr](68k:inputstr.html)) can be useful for some programs, dialog boxes are usually more effective. A dialog box is a typical message box that is displayed on top of whichever screen you're currently on, but without overwriting anything (so the background is restored when the dialog box is exited).



## The Basics

A dialog can be created by inserting a [68k:Dialog](68k:dialog.html)..EndDlog block into a program. The dialog will be displayed when that part of the program runs; after the dialog is exited, the program will resume after the EndDlog.

Just Dialog:EndDlog would give an empty dialog box, and in fact causes an error. To provide content for the dialog box, use the following commands:

: [68k:Title](68k:title.html) : Gives the dialog a title. There can be at most one title. If there is no title, the top of the dialog box will be blank.
: [68k:Text](68k:text.html) : Adds a line of text to the dialog. The text must be a string, so use the [68k:string()](68k:string().html) command to display any other data type.
: [68k:Request](68k:request.html) : Adds a text entry box to the dialog. Request takes two arguments, a line of text and a variable to store to.
: [68k:DropDown](68k:dropdown.html) : Adds a dropdown menu to the dialog. DropDown takes three arguments: a line of text, a list of strings for the dropdown, and a variable to store to.

Text and Request can be used by themselves, giving a dialog box with no other elements in it.

## Advanced Details

### Cancelling Dialogs

At the bottom of a dialog box, there are two "buttons": ENTER=OK and ESC=CANCEL. If the ESC key is used to get out of a dialog, the dialog is indeed cancelled: the variables that would've been affected by Requests and DropDowns are left as they were (usually, undefined).

Fortunately, there's a way to check if this happened. The system variable [ok](68k:system-variables.html#ok) keeps track of the way that the last dialog was exited. It does this in a somewhat unusual way: if ENTER was pressed, its value is the floating-point value 1.0, and if ESC was pressed, its value is 0.0 (maybe this is a holdover from TI-83 series calculators, which stored all truth values in this way).

The variable ok isn't affected by a Text instruction outside Dialog..EndDlog (which can also be exited using ESC, but doesn't have two buttons), nor by a [68k:PopUp](68k:popup.html) menu. It *does* work when a Request instruction is used by itself outside Dialog..EndDlog.

### Alpha-lock Request

Request always stores a string to its variable, but it's meant to be used for all kinds of input. As a result, there's an option to turn off the alpha-lock for it, if you're going to be inputting a number. To do this, add a third argument to Request which evaluates to 0.

This functionality was only added with OS version 2.07, which might be an issue. It also doesn't actually *do* anything on the widescreen calculators (since those have a QWERTY keyboard and don't need alpha-lock). However, it's still there on widescreen calculators for compatibility, and just doesn't affect anything.

Unfortunately, if there are several Requests in a single Dialog..EndDlog block, they can't have different alpha-lock settings. Either they all have alpha-lock or none of them do (the setting for the first Request command is used, and the rest are ignored).

### Compatibility

If the text in one of the elements of a dialog is too long to fit in one line, the dialog gives a [Dimension](68k:errors.html#e230) error. However, the allowed length of text varies from the TI-89 and TI-89 Titanium to the other, widescreen calculators. Thus, a dialog that works on one calculator may give an error on another.

You might think that more text fits on a widescreen calculator, but that's actually not the case, because they use a different font for everything except titles. The actual limits are given in the following table:

| Command  | Widescreen (TI-92/+/V200) | Standard (TI-89/Titanium) |
| --- | --- | --- |
| Title | 50 chars | approx. 39 chars |
| Text (Dialog) | 38 chars | approx. 39 chars |
| Text (simple) | 34 chars | approx. 37 chars |
| Request | 20 chars | 20 chars |
| DropDown | 35 chars | approx. 35 chars |

Note: "approx." means that due to the variable width of a font used, the actual upper limit varies. For DropDown, the upper limit is on the total length of the description and the longest option.

It makes sense to write Dialog boxes with text that fits both sets of requirements at the same time. Then, there is no risk of the Dialog ever crashing!

### Default Values

If the variables being stored to by Request or DropDown aren't undefined, they're used as default values:
- For Request, *if* the variable's value is a string, it's pre-entered and highlighted in the request box.
- For DropDown, *if* the variable's value is a number, the corresponding option is the one initially chosen.
This can be useful for changing menu options. Alternatively, you can use it for instructions or custom default values, for example:
```"Enter the answer here"→answer
Request "Ans:",answer
```

If the variable has the wrong type, it doesn't show up, as though it were undefined.

## Dialog Snippets

These are some common code snippets involving dialogs, that could come in handy in almost any program. Of course, the text may be customized to your needs.

### Confirmation Dialog

```
:Dialog
: Title "Are you sure?"
: Text "Unsaved data will be lost!"
:EndDlog
:If ok=1 Then
: © Continue
:Else
: © Abort
:EndIf
```

### Load/Save File

```
:"main"→fold
:Dialog
: Title "Load file"
: Request "Folder",fold
: Request "Variable name",var
:EndDlog
:If ok=0
: © Abort
:#(fold&"\"&var)→file © to save a file, instead do :file→#(fold&"\"&var)
```

It's a good idea to ask for the folder and variable name separately, because it clears up questions about syntax. Also, if you move :"main"→fold to an earlier part of the program, a folder that was loaded from once will be a default value in the dialog. In fact, for this purpose, you might want to keep two variables for saving and loading files, to allow for different default values.

### Error Dialog

```
:Try
: © main program code
:Else
: © if an error occurred
: © handle expected errors, then
: Dialog
:  Title "Error"
:  Text "An unexpected error occurred."
:  Text "Error code: "&string(errornum)
:  Text "Continue with program?"
: EndDlog
: If ok=1 Then
:  ClrErr
:  Goto start
: Else
:  © clean up vars
:  PassErr
: EndIf
:EndTry
```

A dialog box like this will ensure that a bug in your code isn't as bad an outcome as it would be otherwise - a professional approach to handling errors. You might also want to add something like "Please mail <email address> with a bug report" to the message.

Replace PassErr with something like ClrErr:Goto quit if you don't want to let the user see the error message, under any circumstances.

<center>

|**[<< Assembly](68k:assembly.html)**|**[Overview](68k:techniques-overview.html)**|**[Sprites >>](68k:sprites.html)**|
| --- | --- | --- |

</center>
