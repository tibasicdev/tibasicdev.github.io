# Compression Techniques
Compression involves encoding data in an alternative format that has advantages over the un-encoded format. When determining whether to use compression, the main thing you should consider is its effectiveness (i.e., how much size and/or speed gain it results in). Of course, you need to decompress the data before you can use it again.

### Graphing

One of the simplest ways of compressing data is by placing several related command values in a [list](lists.html), instead of listing out each individual command one after the other. A good example of this is when you are displaying a picture on the [graph screen](graphscreen.html) using several [`Pxl-On(`](pxl-on.html) commands. The `Pxl-On(` command has two arguments: an X and Y coordinate. After placing the coordinates in a list, we then just loop through the list with a [`For(`](for.html) loop:

```
:{10,10,25,25,50,50,60,60,35,35
:For(X,1,dim(Ans),2
:Pxl-On(Ans(X),Ans(X+1
:End
```

While this compression is effective, it can be improved upon. If you look at a number, it has an integer and fraction part. These two separate, but related parts can each be isolated using the [`iPart(`](ipart.html) and [`fPart(`](fpart.html) commands respectively.

Relating this back to our previous example, we should combine the two coordinates together, placing the Y coordinate as the integer and the X coordinate as the fraction. This effectively shrinks the list in half. For extracting each coordinate, you simply use the `iPart(` command to get the Y coordinate and multiply the `fPart(` command by 100 ([`E2`](e-ten.html)) to get the X coordinate:

```
:{10.1,25.25,50.5,60.6,35.35
:For(X,1,dim(Ans
:Pxl-On(iPart(Ans(X)),E2fPart(Ans(X
:End
```

This compression technique was possible because the `Pxl-On(` command has two coordinates, but it would not be very effective if we were storing the [`Line(`](line.html) command's four coordinates: X1,Y1,X2,Y2. A better alternative would be to simply put all four coordinates together in the integer of the number. Probably the best example of this technique put to use is Bryan Thomas's [Contra](contra.html) game.

The reason that this works is because a number can have up to 14 digits, so there are plenty of digits available for us to use. To extract each coordinate, you can use a combination of iPart( and fPart(, multiplying by the related power of 10. The following code draws a line for each element in the list:

```
:{15231561,42133313,62186251,48604839
:For(X,1,dim(Ans
:Line(iPart(Ans(X)/ᴇ6),iPart(ᴇ2fPart(Ans(X)/ᴇ6)),iPart(ᴇ2fPart(Ans(X)/ᴇ4)),ᴇ2fPart(Ans(X)/ᴇ2
:End
```

For color calculators, use the following code:

```
:{100100100100,001001001001,050050050050
:For(X,1,dim(Ans
:Line(iPart(Ans(X)/ᴇ9),iPart(ᴇ3fPart(Ans(X)/ᴇ9)),iPart(ᴇ3fPart(Ans(X)/ᴇ6)),ᴇ3fPart(Ans(X)/ᴇ3
:End
```

(Note that the lines may not display correctly if you don't have the right graph screen coordinates, so you should set your calculator to a [friendly graphing window](friendly-window.html) to make all of the coordinates easily-compressible two-digit numbers. In this particular example, the graph screen coordinates are supposed to be X=0…94 and Y=0…62, the standard for grayscale calculators. Color calculators should utilize X=0…264 and Y=0…164 and adjust the coordinates accordingly. Also note that the color version requires 3 digits per coordinate instead of the monochrome's 2 digits)

### Complex Numbers

Besides using the integer and fraction parts of a number, you can also use complex numbers. A complex number has two parts: the real part and the imaginary part. Just like how you were able to separate the integer and fraction part of a number, you can also separate the real and imaginary parts of a complex number:

```
:real(-5+8i   // Returns -5
:imag(-5+8i   // Returns 8
```

While this doesn't have much application because using the integer and fraction part of a number is generally sufficient, it can sometimes be used in place of a 2-by-n matrix; you just use a list of complex numbers, where column 1 is the real part and column 2 is the imaginary part.

Now we'll move on to a different programming situation. In games you sometimes need a switch that tells whether something is in the on or off state. It is fairly common to see beginner programmers utilize two or more variables to keep track of the switch and alternate one variable based on the other's value.

This is an ample place for not only compression but just good logical thinking. If you remember that each variable is considered a Boolean; that means the value indicates either true or false. A false value is zero while a true value is anything else. So, you just need to check to see if the value of the variable is zero:

```
:If not(F    // Check if the flag variable is zero
```

Because the `F` variable can be either true or false, you have the switch built-in for you. To switch the variable, simply use the [`not(`](not.html)} operator:

```
:not(F→F    // Flip the value of the flag variable
```

### Matrices

The most appropriate and needed place for compression is when storing lots of data, such as levels and maps. The most common variable used by people for storing data is matrices. This is because matrices are simple to use and they make sense since they are two-dimensional. However, matrices have one major disadvantage: size.

Instead of using matrices, which take up a large amount of memory, the better approach is to use either lists or strings when storing your levels. To load a level, you can extract the level data from the list and store it in the matrix during gameplay. Afterward, the matrix can be deleted.

#### Compression via Lists

Here is a sample level stored as a list, with each element representing a row to be displayed on the [home screen](homescreen.html):

```
:3→dim(L1
:If L=1:Then    // If level one
:4444→L1(1
:5623→L1(2
:4567→L1(3
:End
```

Using the `iPart(` and `fPart(` commands that we discussed previously, you can break apart each number into its own separate integer and fraction elements. This allows us to then store each number into a specific position in the matrix, looping through it with a couple For loops:

```
:{3,4→dim([B]
:For(Y,1,3
:L1(Y→Z
:For(X,1,4
:iPart(10fPart(Z/10^X→[B](Y,5-X
:End:End
```

#### Compression via Strings

The formula for storing a level as a string and converting it to a matrix is not much different than it was for the list:

```
:If L=1:Then    // If level 1
:"444456234567→Str1
:End
:1→F
:{3,4→dim([A]
:For(A,1,length(Str1
:exp(sub(Str1,A,1→[A]((fPart(A/4)!=0)+iPart(A/4),F
:F(F<4)+(F<4)+(F=4→F
:End
```

While this probably seems like a waste to go through all of this work just to compress a level, it is useful for large or complex level designs.. In addition, the calculator only has a limited amount of memory to begin with, so you need to take advantage of every opportunity to save memory.

### Single Digit Numbers

We can compress a list of up to 14 elements into a single integer whose digits are the elements in reverse. Given an 8-element list stored in `L₁`:

```
{7,0,3,4,1,6,6,2}
```

To compress, use:

```
.1sum(L₁10^(cumSum(1 or L₁
```

which outputs:

```
26614307
```

You'll notice that the digits are in reverse. That might be a bit confusing, but having it in reverse makes it smaller and faster.

So now, we decompress:

```
int(10fPart(Ans/10^(seq(Z,Z,1,8
```

In general, replace 8 with the dimension of your list, or `log(Ans)` if the number of digits is unknown.

There you go. It is decompressed back into Ans. So, now we can compress single-digit data. But what about double-digits?

### Double Digit Numbers

Double digits are a little more complicated, but they are also more useful because they allow up to 100 different positive integers instead of just 10.

Several methods were mentioned previously for decompressing 2-digit numbers, if you paid attention.

So, on to compressing! Say you had this 4-element list stored in `L₁`:

```
{24,47,36,42}
```

To compress it:

```
.01sum(L₁10^(2cumSum(1 or L₁
```

The answer:

```
42364724
```

The decompression:

```
int(E2fPart(Ans/10^(2seq(Z,Z,1,4
```

### Digits of Any Length

One can generalize the above snippets of code to work for any length of digit. Our numbers are stored in `L₁`, and each have length `N`. To compress:

```
10^(-N)sum(L₁10^(NcumSum(1 or L₁
```

And decompress:

```
int(10^(N)fPart(Ans/10^(Nseq(Z,Z,1,1+iPart(log(Ans)/N)
```


However, due to the maximum precision of real variables (14 digits), it is impossible to store more than a couple of large numbers via this method.

### References

- Bryan Thomas and his [Contra](contra.html) game
- Arthur O'Dwyer and his [Complete TI-83 Basic Optimization Guide](http://tibasicdev.github.io/local--files/downloads/83trix.zip) tutorial
- Brandon Green and his [Arrays: The Amazing Data Structure](http://tibasicdev.github.io/local--files/downloads/sicodetutorials.zip) tutorial
- Martin Johansson and his [String Compression](http://tibasicdev.github.io/local--files/downloads/stringcompression.zip) tutorial
