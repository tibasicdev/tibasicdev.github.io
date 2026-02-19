# Computer Setup
> **Note:** Computer setup is only necessary if you want to program on a computer. If you are just interested in programming on your calculator, please skip this page and move on to the [Downloading Programs](sk:downloading-programs.html) page.

While the calculator itself is the predominant place to program TI-Basic, another viable option is programming on a computer. There are several computer tools available, including editors and emulators, which provide a very rich programming environment. In addition, some people don't like using the calculator because it has a small screen that doesn't fit much code, and using its keys to type can be rather cumbersome for writing large programs.

## Connectivity Software

In order to transfer data between your calculator and your computer, you will need some form of connectivity software. This software often allows you to create backups, transfer variables, and even edit variables. A cable is needed to transfer the data. Here are the three common connectivity software.

- [TI-Connect](https://education.ti.com/en/products/computer-software/ti-connect-sw)
- [TI-Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw)
- [TiLP](http://lpg.ticalc.org/prj_tilp/)

The first two (TI-Connect and TI-Connect CE) are developed by TI-Education. TI-Connect is the original linking software TI released. It support the entire TI-83/84 line as well as others. 
TI-Connect CE was released when the TI-84+CE was released. This update retains the same features as TI-Connect while including a modernized UI and a limited TI-Basic editor.
While the first two software are compatible on Windows and Mac, they do not work on Unix platforms. TiLP is a free software was created and is maintained by developers not affiliated with TI-Education. The software supports a multitude of calculators ranging from the TI-73 to the TI-Nspire CX CAS.

## TI-Basic Editors

The first thing you want to get setup is a TI-Basic editor. An editor allows you to make and edit programs and data on the computer, which you can then transfer from your computer to your calculator with a link cable. There is an editor available for each calculator model, so you should download and use the appropriate model:

- [Graph Link](https://education.ti.com/en/software/details/en/a2e9b3dfcb44490dbd5449e05721767d/ti-graph-link-for-windows)
- [TI Connect](https://education.ti.com/en/products/computer-software/ti-connect-sw)
- [JALcc IDE](http://mientki.ruhosting.nl/data_www/pic/jalcc/help/jalcc_ti84_editor.html)
- [TI-Basic Compiler](http://sourceforge.net/projects/tibasic)
- [SourceCoder 3](http://www.cemetech.net/sc/)

If you are using Windows, you probably want to download both TI Connect to transfer programs to and from your calculator and Tokens IDE (which is probably the best TI-83/84 Basic editor out there as of present).  Extract the .zip file you download at the link below and you will be able to run Tokens.

- http://merthsoft.com/Tokens.zip

The first three editors come with automatic installation, so you just follow the on-screen instructions and check boxes to configure them however you want. In addition, the first two editors are made by Texas Instruments, so if you have any problems or questions, you can just go on their [ti.com](http://education.ti.com) website or contact ti-cares@ti.com for support. TI-Basic Compiler is an .exe file and doesn't need installing. If you have problems with figuring out what stands for what, go to [SourceForge.net](http://tibasic.cvs.sourceforge.net/viewvc/tibasic/main.cpp?revision-1.8-view-markup) and scroll down some. There you can find every command you would need. ("Horizontal" is buggy when compiling because of "Horiz")

When using an editor, there will be a calculator keypad displayed to the left of a program edit box (TI-Basic Compiler lets you write the program in NotePad, which gives a little more freedom, but means you have to know exactly how to type everything). Pressing one of the keys on the keypad will bring up the same menus that are on the actual physical calculator, so it is extremely easy to use. If you try typing in some text in the edit box, you will probably note that there is no command syntax checker.

This allows you to type in whatever text you want, including commands, functions, and lowercase and other ASCII characters (such as © or Greek). You just need to be aware that the calculator may not translate a typed command into the actual command when sending the program to your calculator, which will cause the program to crash when you try to run it. So, you should always get the commands and functions from the calculator keypad.

## Calculator Emulators

Once you have installed an editor, now you should install a calculator emulator. An emulator allows you to run a virtual form of your calculator on your computer, which is very convenient when you want to make quick changes to programs, or do any debugging or optimizing.

For example, instead of having to send the program to your calculator, make the changes, and then send the updated program back, you can simply start up your emulator and do everything on your computer. There are several different emulators available for you to use:

- [Virtual TI (VTI)](http://www.ticalc.org/archives/files/fileinfo/84/8442.html)
- [PindurTI (PTI)](http://users.hszk.bme.hu/-pg429/pindurti/)
- [TI Linking Program (TiLP)](http://lpg.ticalc.org/prj_tilp/)
- [TI Linux Emulator (TilEm)](http://lpg.ticalc.org/prj_tilem/index.html)
- [Wabbitemu](http://wabbit.codeplex.com/releases/view/44625)
- [Flash Debugger (SDK)](http://education.ti.com/educationportal/sites/us/productdetail/us_sdk_73_83_84.html)
- [jsTIfied](http://www.cemetech.net/projects/jstified/)

Except for the Flash Debugger emulator, which doesn't need a ROM image, the rest of the emulators need a ROM image before you can use them. A ROM image is simply an instance of your calculator, which tells the emulator that you own your calculator. You just link your calculator to your computer, and then the emulator should be able to download the ROM image off of it.

We just need to mention that you should not give your calculator's ROM image to other people to use, because only one person is supposed to use any one ROM image. If somebody asks you for your ROM image, please do the right thing and tell them no. They should buy their own calculator if they want a ROM image.

## Online Tools

While downloading an editor or emulator is rather simple and easy to do, it is not very useful when you are using someone else's computer, and they don't want you downloading anything. What you can do instead is use one of the online tools that are freely available: [SourceCoder 3](http://www.cemetech.net/sc/) and [Online TI File Converter](http://ti.zewaren.net/). In addition, [jsTIfied](http://www.cemetech.net/projects/jstified/) is an online emulator.

SourceCoder 3 is an online editor that parses TI-Basic code and presents it with the appropriate calculator tokens.  What makes it especially nice is that it will output the code in several different formats, upon your choosing. Programs, AppVars, lists, strings, images, assembly programs, and projects are just some of the several features included. In addition, SourceCoder 3 is implemented with jsTIfied, which makes it easy to test your code in an emulator.

Like its name says, TI File Converter can create and convert several different types of files (includes data, variables, and programs) from the TI-83 series of calculators. After you have created a file, you can download it to your computer to use with an editor or emulator.

You should bookmark both websites, so that you can have them right at your fingertips whenever you need to access them.

<center>

|**[<< Using Your Calc](sk:using-your-calc.html)**|**[Table of Contents](starter-kit.html)**|**[Downloading Programs >>](sk:downloading-programs.html)**|
| --- | --- | --- |

</center>
