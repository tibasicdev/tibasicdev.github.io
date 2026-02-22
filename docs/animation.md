# Animation
Animation is the rapid display of images on the screen to create an appearance of movement: it works by displaying an image and then moving it to a new location after a short delay has occurred. While there are many different things that you can do for animation (the possibilities are practically infinite; heck, there is an entire program directory at ticalc.org devoted to animations), almost every animation depends on [For(](for.html) loops.

A For( loop is a special kind of [While](while.html) loop, with all of the loop construction built-in, it has the the variable that the loop uses, the starting value, the ending value, and the increment. This is important because you can use all of those things to dictate how many times the animation is displayed, the speed of the animation, and even the animation itself (using the For( loop variable as the coordinates or the text that is displayed).

Animation is commonly used at the beginning of a program or on loading screens to add some visual pop or pizazz, which gives a program an edge over similar programs. At the same time, this does not mean that you can't go overboard with animation; too much animation becomes annoying and lengthy after a while. Selective animation — where it makes sense and complements the program — has the best impact in a program.

You also want to keep in mind the calculator that the animation is running on. If you created your animation on the TI-83+SE or TI-84+SE, then the animation probably won't display as you intended on a TI-83 or TI-83+ calculator (calculators that have a much slower processor; 6MHZ and 8MHZ respectively are slower compared to 15MHZ for the TI-83+SE and TI-84+SE). Of course, there are a few other things that you need to consider, so you should read the [portability](portability.html) page for more information.

### Animation Examples

This is an example of moving text: the variables of the X or Y coordinate of the text are changed by the for( command. 
The spaces before "looks" and after "huh?" are needed to delete the old text.
```
ClrDraw
AxesOff
For(A,1,20
Text(A,40,"This
End
For(A,1,19
Text(28,A+9," looks
Text(28,69-A,"cool
End
For(A,50,35,-1
Text(A,40,"huh?
Text(A+6,40,"<16 spaces>
End
```

Running this code gives this program:
![http://tibasicdev.github.io/local—files/animation/Text_example_looped.gif ](http://tibasicdev.github.io/local—files/animation/Text_example_looped.gif  "")

You can also draw and erase shapes and lines. 

```
ClrDraw
For(A,1,10)
Line(30,40,40,40
Line(40,40,40,30
Line(40,30,30,30
Line(30,30,30,40
Line(30,40,40,40,0
Line(40,40,40,30,0
Line(40,30,30,30,0
Line(30,30,30,40,0
End
```

> TODO: Add more examples
> * Using pictures
> * Drawing/Erasing text (changing position, size, letter by letter)
> * Drawing/Erasing shapes (changing position, size, color)

One of the most common examples of animation that you see in games is wiping the graph screen (you can certainly wipe the home screen as well). This is usually done at the end of the game, after the player has lost, or as a transition from one level of the game to the next.

Wiping the screen involves using one or more [Line(](line.html) or [Horizontal](horizontal.html)/[Vertical](vertical.html) commands, and then displaying the line from one side of the screen to the other:

```
:For(X,Xmin,Xmax,ΔX
:Vertical X
:End
```

As you can see, a vertical line is displayed from the left side of the screen to the right side, effectively shading the entire screen.  Since it uses Xmin ,Xmax, and ΔX, it will work on any screen.

Another common example is displaying text. This is commonly used on the title screen of a game to make the game stand out to the user. There are several different ways that you can display text, but some of the most common are: letter by letter, sliding it in from the screen side, overlapping each letter, and displaying the large text behind the small text.

Displaying text letter by letter involves placing the text in a string, and then displaying the respective substring based on where you are in the For( loop. More plainly stated, display each character by itself at the respective time.

The code for this is fairly simple:

```
:For(X,1,5
:Output(1,X,sub("HELLO",X,1
:End
```

### Animation Length

The two different options for animation length are timed and infinite:  timed means the animation lasts for a set amount of loop iterations, while infinite means the animation will go on indefinitely with no end (or at least until the user finally presses the ON key).

The way you go about making a timed animation is by simply using an additional For( loop enclosed around the animation. For example, if you want the animation from before to be displayed five times, you can just do:

```
:For(I,1,5
...
:End
```

There are actually three different ways to make an infinite animation: use a For( loop with a really large ending value (such as E5) or use an infinite While 1 or Repeat 0 loop. The infinite While or Repeat loop is the smaller of the two, but the For( loop has the advantage that it still allows the user to exit out of the animation.

Of course, the really long For( loop is not a true infinite loop, since it will eventually end at some point. For our purposes, however, it works quite well because the calculator will actually power down after a certain amount of inactivity (the TI-83+ and above have a built-in APD feature).

The last way is adding [prgm](prgm.html) and then your program name, which you put at the end of your program. This makes it loop itself infinitely, until you press the ON key. This does use a little bit of storage every time, so use this one sparingly. Example:

```
PROGRAM:HI
:Disp "HI."
:prgmHI
```

### Adding a Delay

If you try out any of the examples that have been shown so far, one of the things you will probably notice is that they display so quickly that you can barely see them being displayed until they are almost done. This behavior is acceptable for some animations, such as where there is lot of things being animated at one time, but it can cause havoc for a lot of animations. The way you fix this problem is by adding a delay.

There are two basic ways to create a delay: use a [For(](for.html) loop or use the [rand](rand.html) command. The For( loop is just an empty loop, meaning there are no commands or functions inside of it. The rand command's alternate syntax — rand( — generates a list of random numbers, which is a rather time-consuming operation. Both of these delay methods can be worked so that they create a small or large delay simply by changing the size of the For( loop and the number of random numbers generated respectively.

For an example, here is the text animation from before, where the word HELLO is displayed letter by letter on the first line on the home screen, with each of the two respective delay methods added to it:


```
:For(X,1,5
:Output(1,X,sub("HELLO",X,1
:For(I,1,20:End
:End
```


```
:For(X,1,5
:Output(1,X,sub("HELLO",X,1
:rand(10
:End
```


Each delay method has its own advantages and disadvantages. The For( loop has the advantages that using it still allows the user to do something during the delay, and it does not have any additional memory overhead like rand does. The rand command has the advantage that it is smaller in size than the For( loop.

The rand command does use some additional memory for storing the temporary list of random numbers in Ans, which may be undesirable. To avoid this, you simply have to use this somewhat longer line: If dim(rand(#. Despite the presence of an [If](if.html) statement, you don't have to worry about the next line being skipped, since dim(rand(#)) will always be true.

The other concern when using the rand command is that if the number is large enough, the program will run out of memory from trying to generate such a large list, and subsequently return a [ERR:MEMORY](errors.html#memory) error. What number is too large is dependent on how much free RAM is available on the calculator, so for some people it might be 100 while for others it might only be 50. So, if you want to use a large delay, it might be better to go with a For( loop instead of a rand command.

Related to that concern is the issue of [portability](portability.html): a delay may be appropriate on your calculator, but it won't be on another calculator. For example, if you have a TI-83 and you use a delay for twenty iterations of a For( loop, that would be almost unnoticeable on the much speedier TI-83+SE and TI-84+SE calculators. Conversely, if you write your program on a TI-83+SE, the delay would be much longer on a TI-83 and TI-83+, to the point that the animation would slow to a crawl.

With exception to [assembly libraries](assembly-libraries.html), there is no viable way to check what calculator a program is being run on. A good alternative is to find the appropriate delay for each calculator, and then take the average for the delay that you use. This happy medium is just a simple fix, and really all you can do is just keep the other calculators in mind when deciding how much delay to use.

### Allowing User Exiting

One of the main considerations that you have to make when using animation in a program is whether the user can exit the animation at any time they want. This applies to animations of any length, but it especially applies to long animations. This is because the user has to wait until the entire animation is finished before they can move on to the rest of the program, which is extremely annoying from the user's point of view (see [program usability](usability.html) for more information).

There are a couple different ways you can fix this problem. The first way is to add some [getKey](getkey.html)'s throughout the animation to check for user key presses; and if you find any, you exit the animation.

Since the animations use For( loops, and we want to exit out of them before they have finished, you can do this by storing something at least equal to the end value to the variable used in the For( loop. For example:

```
:For(C,61,32,-1
:Pxl-On(C,47
:If getKey:32→C
:End
```

While this approach works quite well if your animation only consists of one For( loop, it doesn't work when you have two or more For( loops that you need to exit out of. The problem is that if you exit out of the first loop early, you then need to skip the rest of the For( loops in the animation.

Unfortunately, there is no real easy way to go about doing this. One option is to use [branching](branching.html) to jump out of the For( loops to go to a While 0 loop [internal subprogram](subprograms.html). The reason for doing this, of course, is to avoid creating a memory leak.

Because using branching can get rather messy, another option is using an additional variable to act as a flag. You just set the variable to an off state (zero is the standard value), and then change it to an on state (achieved by inverting the flag variable's value) when the user has pressed a key.

For example, here is an animation that displays the word HELLO letter by letter, and then erases each letter starting from the "O". If the user doesn't exit the animation early, it will be played 100 times before it is finally finished. Note the first example uses the branching while the second example uses the A variable as a flag.


```
:For(I,1,E2
:For(X,1,5
:Output(1,X,sub("HELLO",X,1
:If getKey:Goto A
:rand(10
:End
:For(X,1,5
:Output(1,6-X," "
:If getKey:Goto A
:rand(10
:End:End
:While 0:While 0
:Lbl A
:End:End
```


```
:DelVar A
:For(I,1,E2not(A
:For(X,1,5not(A
:Output(1,X,sub("HELLO",X,1
:If getKey:not(A→A
:rand(10
:End
:For(X,1,5not(A
:Output(1,6-X," "
:If getKey:not(A→A
:rand(10
:End
:End
```


Those two options should generally suffice for most animations, but a third option available is to simply rewrite the animation. There is no hard and fast way to rewrite an animation, but it generally just involves thinking about the animation and seeing if there is an alternative way of implementing it.

One common way to rewrite animations where you are moving back and forth (or displaying and erasing text) is by combining the two For( loops into one, and using some additional variables to keep track of the current direction (or if it should be displayed or erased). When an edge is reached, you then just invert the variables values from negative to positive and vice versa.
