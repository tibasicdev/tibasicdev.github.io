# Releasing Your Program
|**This article is part of the releasing stage of the [development](development.html) cycle.**|
| --- |

Many programming guides give you excellent advice on programming, but stop at the point when the program is finished, tested, and optimized. After all, most people can manage to release a program somewhere, one way or another. But in reality, an inexperienced programmer may well release his work quietly and in an unassuming form, which people will simply glance over without stopping. This tutorial will tell you how to avoid this, and make your program get all the attention it deserves.

## Where to Release

First, it's important to know where to go to upload your program to the Internet. Although you might want to create your own website and release all your games there, that alone will not get your program noticed. Sure, having your own site might get you some publicity, but the best way to get your game noticed is by releasing it at one (or all!) of the large program archives.

- [ticalc.org](http://www.ticalc.org)
- [CalcGames.org](http://www.calcgames.org)
- [United-TI](http://www.unitedti.org)
- [TI-Basic Developer](http://tibasicdev.github.io/archives)
- [Cemetech](http://www.cemetech.net)

Of these, ticalc.org is by far the largest (and most popular), but it's also likely you'll spend longer waiting for your program to be put up there.  With CalcGames and United-TI, you only have to wait a day or two.  With TI-Basic Developer, you only have to wait a few minutes, or you could do it yourself.

## What to Release

There's more you'll want to submit than just the program itself. Here are the elements you'll want to put together — some of these are called optional by the file archive websites, but they are mandatory if you want the program to be successful.

**The program itself (obviously)**

If you were programming on the calculator, you'll need to transfer the program to your computer to submit it. You'll need a calculator-to-computer cable, and software such as TI-Connect. If you don't know where to get these, or have problems using them, see [linking](linking.html).

Now, you have one or more files from your calculator on the computer. If there's only one, you're good to go. If there are several files involved, you should consider combining them in a [group](grouping.html) file (usually .83g or .8xg). Or keep them like they are, but then make sure to mention what each file is for, in the readme.

Although, if you don't want to worry about having to ungroup, or group the files, another option for monochrome calculators is [Basic Builder.](basicbuilder.html)  Basic Builder packages your programs, in an app.  More information, is given at [this page.](basicbuilder.html)

**The readme**

A critical step in submitting a program. Make sure to read our tutorial on [writing a readme](documentation.html) if you've never done it before (and possibly even if you have). Usually, longer is better than shorter (it's worse if someone doesn't understand how your program works, than if they have what they already know explained to them again) — unless it's a five-act play, in which you might consider removing the nonessentials. Generally, the longer and better your program, the longer your readme can be; you don't need any more than the minimum for, say, a quadratic solver.  For a huge program, a 2-4 page plain text file is appropriate.

Also, please don't make the readmes in Microsoft Word 7 file format! A .txt file is sufficient, and in fact recommended.  However, if you're just itching to put screenshots, pictures, and format your whole paragraph accordingly, a .pdf file would be a good idea.  PDF files can be read by most computers automatically, but if not, Adobe reader, is free.  It might be a good idea, to put a file with a link to an adobe download station.  Most likely http://get.adobe.com/reader/ will be the link to get adobe reader.  You might also want to mention that it's free.  Make sure you have that .txt file that gives the information on where to find adobe.


**The screenshot**

All four websites listed above let you add a still or animated screenshot of your program. This is very easy to do — see the [making a screenshot](screenshots.html) page — and goes a long way toward making your program look good (if it actually is good). An attractive screenshot will encourage visitors to download your program more than the most flowery prose. Show your program at its most impressive here.

Getting a screenshot is easy using TI Connect. In 1.7 and 1.6, the screenshot button should look like a camera.  Click it.

**The title**

The title will tell visitors what your program is all about. One common mistake is making the title the same as the 8-character name of the program. Don't do this — the title is the first thing people will see, and you want to make it clear. Of course, if the program is called prgmTETRIS it's okay to call it Tetris (though Grayscale Tetris, if that's the case, could be even better). But if the program is called prgmQUADSOLV, *please* make the title Quadratic Solver instead!

**The description**

Don't forget this! It should have three parts:
- What the program is about. "Solves all quadratic equations over the complex numbers."
- The program's best qualities. "A grayscale interface at the low size of 13 bytes!"
- Any requirements. "Requires xLIB, Omnicalc, Symbolic, and DAWG to work correctly. Also, create and unarchive GDB7."

The first two parts are positive; the third is negative, but necessary (imagine if your program crashes without warning if GDB7 is not created. 99% of your users will be lost, even if this is explained in the readme, and write negative reviews). You want to make this section as short as possible, and the best way to do this is to avoid the requirements in the first place.  Even if your game is in the "games for xLib" category, the one who is looking for a game might not see this, and not download, or install xlib.

**Putting this together**

The program and the readme should be combined in a .zip archive: this is a community-wide standard. The file upload form (this is different for all websites, but contains the same basic information to be entered) should have fields where you can submit everything else. You might also consider adding the screenshot to the .zip archive, **in addition** to its normal location.

Here are the links to the file upload forms of all the websites mentioned on this page.
- [Ticalc.org's form](http://www.ticalc.org/cgi-bin/file_upload.pl)
- [United-TI's form](http://www.unitedti.org/index.php?act-downloads-do-add)
- [CalcGames.org's form](http://design.calcgames.org/uploadform.php?tmplt-14)
- [TI-Basic Developer's form](http://tibasicdev.github.io/archives:upload)
- [Cemetech’s form](https://www.cemetech.net/programs/upload.php)

*Note: You need to create an account at the respective website before you can upload files there.*

## Marketing

Marketing your program can start as early as when you first get the idea for your program, although many people won't take you seriously until you have at least a basic engine to show for your efforts. Other good points at which to advertise the program include a beta-testing period before you release it to the masses, and of course when it's finally released. For more marketing tips, see our [marketing](marketing.html) tutorial.

<center>

|**[<< Marketing](marketing.html)**|**[Overview](development.html)**|**[Creating New Program Versions >>](creating-new-program-versions.html)**|
| --- | --- | --- |

</center>
