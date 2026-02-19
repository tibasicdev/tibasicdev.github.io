# Strings
The final data type is the string.  A string is a form of representing a phrase.  Before, you could only use numbers, but a string will hold numbers, letters, and almost every possible character.  This proves very useful because strings can serve multi-functions very easily.  They can be used as variables, outputs in the form of numbers or words, and converters.  Below, we will discuss how to use strings.



## Setting up Strings

There are ten different strings: Str0 to Str9.  Unlike lists or matrices, strings do not use the [dim](dim.html)( command to determine its length.  Also, strings do not have a special [SetUpEditor](setupeditor.html) command.  So, you need to be careful with [archiving](archive.html) or [unarchiving](unarchive.html) strings.  Fortunately, beyond that, there are no special set up requirements.  All you have to be sure of when dealing with strings is whether it is archived or not and whether the string already has something in it.

## Writing Strings

Strings have an infinite dimension as long as it fits in the RAM.  Unlike with lists or matrices, strings are not a way to represent numbers and expressions, but it represents phrases, and phrases are dictated with quotations.  So, when writing a string, you must precede the phrase with quotations.
```
:"HELLO, WORLD"→Str1
```
You can store practically any character into a string, but you cannot store the →.  So, let's say you wanted to store a quadratic equation, 2*x*<sup>2</sup>+4*x*+8, into a string.  Just precede with quotations and write:
```
:"2x²+4x+8"→Str1
```

## Using Strings

Strings are used in various ways. The reason strings are so powerful is that they can be used for many different applications, they are small, and they can be made very large if need be. Strings are commonly used as a form of outputting words or numbers in a prettier fashion, but strings can also be used like a variable, and much more efficiently at that.

### Output

First off, strings are most commonly used for output. For example, programmers would store bits and pieces of information into a string and then display it at the end to get a final output. For example, look at this code. All it is doing is testing a condition (which phrase to store in the string) and acting upon it.
```
:If A=3
:Then
:"You WIN!"→Str3
:Else
:"You LOSE."→Str3
:End
:Disp Str3
```
However, this code seems a little redundant, since all you need to do is simply display the phrase before storing into a string. However, strings have a special little quirk that allows them to be "[added](add.html)" together. What the calculator does is if it finds the addition of two strings, it will combine the strings together into one super phrase, much like what [augment](augment.html)( does with lists. With this in mind, we can actually have initial strings and combine things into the strings depending on some conditions to receive an output. So the above code can be turned into this:
```
:"YOU_"→Str3 //(The _ is a space)
:If A=3
:Then
:Disp Str3+"WIN!"
:Else
:Disp Str3+"LOSE."
:End
```
This stores "YOU" with a space into Str3. Depending on the condition, the program will combine that string with either WIN! or LOSE.

The [sub](sub.html)( command is very useful. It can be used to display YOU WIN or YOU LOSE in a more simple way than previously described. sub( has three arguments, the string to get data out of, the position in that string to start retrieving data, and the length of the string to be extracted. Here is how you would display YOU WIN or YOU LOSE without If-Then statements.
```
Disp "YOU "+sub("WIN LOSE",1+4(A=3),4
```

Also, consider this code.
```
:"_"→Str2
:For(A,1,7)
:A+2(A≥3)(A≤4)-2(A≥5)(A≤6)→A
:Str2+sub("AWESOME",A,1)→Str2
:End
:Disp Str2
```
This code uses strings to unscramble AWESOME. Don't fret...it may look complicated, but it isn't all that hard. We are using a [For](for.html)( loop to run through each letter. The next line changes A to the appropriate position in the messed-up string. The [sub](sub.html)( command then finds the letter indicated by A and stores it into Str2 along with any letter already there. So you see, strings are very powerful!

### Variable Usage
Strings can also be used as a variable. There is a very special command called [expr](expr.html)( that solves the string as if it was an expression. So, if Str4 was defined as "2+2", then expr(Str4) would be the number 4. However, with this new ability, there comes a new type of usage.

A power like this can be used as a variating variable. In other words, you can set the string value to change when other real variables change using expr(. Consider this code.
```
:"A+B"→Str1
:5→A:4→B
:Disp expr(Str1)
:A+0.5B→B
:Disp expr(Str1)
:Disp Str1
```
This code gives an output of 9, 11, and A+B. The whole time, the string remained the same, but when A or B changed, so did expr(Str1). This is an advanced technique known as [Self Modifying Code](smc.html), or at least one variation thereof. You won't be needing this for now, but this just shows you exactly how powerful strings can be. There are so many things you can do such as store coordinates and use sub( to take them out. As you can see, this data type has a lot power within the programming language.

## Cleaning Up

If you don't want the string, you can simply delete it. If you want to keep it, simply archive it for storage.

## Final Notes

That concludes the theory of strings (of course, nothing related to String Theory...) and the end of learning data types. These data types are used widely in BASIC programming, and it is highly recommended you begin practicing with each. As for now, the next lesson delves you into the realm of random numbers, one of the core components of games today.

<center>

|**[<< Data Types (matrices)](sk:matrices.html)**|**[Table of Contents](starter-kit.html)**|**[Random Numbers >>](sk:random.html)**|
| --- | --- | --- |

</center>
