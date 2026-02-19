# Glossary
[A](#A) | [B](#B) | [C](#C) | [D](#D) | [E](#E) | [F](#F) | [G](#G) | [H](#H) | [I](#I) | [K](#K) | [L](#L) | [M](#M) | [N](#N) | [O](#O) | [P](#P) | [R](#R) | [S](#S) | [T](#T) | [U](#U) | [V](#V)


### A {#A}



: **Argument** : One of the values that a [command](#command) acts on.

: **Array** : A collection of numeric [variables](#variable) arranged in a [list](#list) or [matrix](#matrix) for processing by the calculator. Each element in an array is referenced by its [index](#index) - position in the array.

: **ASCII** : The American Standard Code of Information Interchange. It uses 1 [byte](#byte) (8 [bits](#bit)) to hold a [character](#character), and thus is limited to 256 different characters. The calculator uses a modified version of ASCII internally to store characters (see [68k:Character Codes](68k:character-codes.html)), but the TI-Basic interpreter deals with tokens instead.

: **Assembly** : The other programming language built-in to the TI graphing calculators, apart from [TI-Basic](#tibasic). It is much more difficult to learn and program in, but at the same time it is much more powerful, and can be used to create very sophisticated games and [programs](#program). You can also compile [C](#c) into an assembly program.



### B {#B}



: **Binary** : The two-digit ([bit](#bit)) [number system](#number-system) based on 0 and 1, similar to the way the normal [decimal](#decimal) system is based on the numbers 0-9. For example the number 10101 in binary represents 1*2<sup>4</sup>+0*2<sup>3</sup>+1*2<sup>2</sup>+0*2+1, or 21 in decimal. To enter a number in binary on a [TI-68k](#ti-68k) calculator, write 0b followed by the number.

: **Bit** : A [binary](#binary) digit (0 or 1).

: **Branch** : A departure from the sequential performance of program statements. An unconditional branch causes the calculator to jump to a specified place in the program each time the branching statement is encountered. A conditional branch transfers program control based on the result of some logical [condition](#condition).

: **Breakpoint** : A point in a program where program execution can be suspended, used when [debugging](#debugging) the program. In [TI-Basic](#tibasic), such breakpoints can be created with the [Text](text.html) command.

: **Bug** : An error in a [program](#program) (see also [Debugging](#debugging)).

: **Byte** : A string of eight [bits](#bit). The calculator uses one byte of information to encode the letter "A", as well as most [tokens](#token). Bytes (or kilobytes - one kilobyte is 1024 bytes) are used to measure the amount of memory a program or variable takes up on the calculator.



### C {#C}



: **C** : A popular programming language on many platforms. Using [TIGCC](http://tigcc.ticalc.org), C programs can be compiled to [assembly](#assembly) for the [TI-68k](#ti-68k) calculators.

: **Character** : A letter, number, punctuation symbol, or special graphics symbol. They are encoded in [ASCII](#ascii) format internally, but the [TI-Basic](#tibasic) interpreter uses [tokens](#token) instead.

: **Clock cycle** : The unit of time in a [CPU](#cpu). It is so small that even the most primitive [assembly](#assembly) instructions take several clock cycles to run; the amount of clock cycles it takes for a single [TI-Basic](#tibasic) command can be in the millions.

: **Command** : A word or token that tells the calculator to do something. Examples: [68k:RclPic](68k:rclpic.html), [68k:For](68k:for.html), [68k:max()](68k:max().html), etc. They are sometimes subdivided into [functions](#function) and [instructions](#instruction)

: **Concatenation** : Joining two or more [strings](#string) together to make a longer string. The ampersand — & — is the concatenation operator. For example, "TI-"&"Basic"="TI-Basic".

: **Condition** : A logical expression that the calculator can evaluate to be true or false. 

: **Constant** : A specific number, [list](#list), [matrix](#matrix), or [string](#string) that is given as a fixed value in the program (such as 9.024 or "Hello"), rather than contained in a [variable](#variable).

: **CPU (Central Processing Unit)** : The "brain" of the calculator, where the calculator controls the processing and execution of everything.

: **Cursor** : A small, flashing square showing where a typed character will appear. A cursor (in the form of a crosshair) is also used on the graph screen to input a point from the user.



### D {#D}



: **Data** : Information, often numerical in form. When data is used by a calculator program, it can be [hardcoded](#hardcode) or [softcoded](#softcode).

: **Debugging** : Fixing a [program](#program) to remove [bugs](#bug), or mistakes. There are many [techniques](68k:debugging.html) for debugging, some universal, some specific to calculator programming.

: **Decimal** : A base 10 [number system](#number-system) using the symbols 0-9. It is the default number system used by the calculator.

: **Default** : A standard characteristic or value which the calculator assumes without specification. For example, the [68k:RclPic](68k:rclpic.html) displays a picture at the coordinate (0,0) by default (the top left corner). This can be overwritten with further [arguments](#argument) to specify the coordinate to display at.

: **Dialog** : A message box displayed on the screen for [input](#input) and [output](#output).



### E {#E}



: **Execute** : Another name for running a program or command. 

: **Exponent** : A number indicating the power to which a number or expression is to be raised, usually written at the right and above the number. For example, 2<sup>6</sup> = 2x2x2x2x2x2. In scientific notation, the power of ten which the mantissa is multiplied by to calculate the actual number.



### F {#F}



: **Flash** : The ROM/archive memory on the [TI-68k](#ti-68k) calculators where applications are stored.

: **Floating point** : The format used in TI-Basic for storing decimals. It uses [scientific notation](#scientific-notation) to display all numbers.

: **Flow Chart** : A diagram of geometric shapes connected by arrows that show the progression of a program. Flow charts are handy for developing complicated programs and illustrating how programs work.

: **Function** : The word Function has several meanings in the context of TI-Basic programming. It can mean a type of [command](#command) that returns a value - such as [68k:gcd()](68k:gcd().html) or [68k:sin()](68k:sin().html). Or it can mean a type of user-defined program that returns a value.



### G {#G}



: **Graphics** : Any sort of visual display on the screen, such as graphs, patters, and drawings, both stationary and animated.



### H {#H}



: **Hardcode** : Hardcoded [data](#data) is information used by the program that results from the logic of its [commands](#command). It is very easy for the program to read, but can be impossible to change.

: **Hardware** : The circuit boards and other electronic parts which make up a calculator.

: **Hexadecimal** : A base 16 [number system](#number-system) using 16 symbols, 0-9 and A-F. It is used as a convenient shorthand way to express [binary](#binary) code, because every four bits of binary have a corresponding hexadecimal symbol. To enter a number in hexadecimal on a [TI-68k](#ti-68k) calculator, write 0h followed by the number.



### I {#I}



: **Index** : A position in an [array](#array). In TI-Basic, arrays are indexed starting with 1 (so that the first element in a [list](#list) is numbered 1, the second 2, and so on). In some other languages, they are indexed starting with 0.

: **Input** : The means by which data is entered into the calculator by the [user](#user), primarily through the calculator's keys (though the link port is also a form of input).
 
: **Instruction** : In the case of TI-Basic programming, this is often used to indicate a type of [command](#command) that does not return a value, but stands alone: for example, [68k:Line](68k:line.html), or [68k:Input](68k:input.html). It is also sometimes used to describe commands in general.

: **Integer** : A whole number, positive or negative (or 0). Usually in TI-Basic, a number is an integer by default, which means all of its digits are stored exactly. You can also use [floating point](#floating-point) numbers for approximate calculations with decimals.

: **Interpreter** : The algorithm stored inside the calculator that runs a [TI-Basic](#tibasic) program by executing the appropriate system routines.

: **Iteration** : One repetition of a [loop](#loop). For certain [commands](#command), the calculator has an internal loop for which the total number of iterations is relevant, and affects accuracy.



### K {#K}



: **Keypad** : The panel of keys used to enter [programs](#program) and [data](#data) into the calculator.



### L {#L}



: **List** : A sequence of [variables](#variable) which can be accessed and modified by their position. In TI-Basic, lists can have any mix of variable types.

: **Loop** : A group of one or more consecutive program lines which are performed repeatedly, either a specific number of times, or until a [condition](#condition) is met.



### M {#M}



: **Mantissa** : The basic numeric portion of a number expressed in scientific notation. In 3.264E + 4, the mantissa is 3.264.

: **Matrix** : A two-dimensional grid of [variables](#variable) which can be accessed and modified by their position. In TI-Basic, lists can have any mix of variable types.

: **Memory** : The two different places (RAM and ROM) where calculator [programs](#program) and [data](#data) are stored. All variables and programs take up part of memory to store, which makes the size of a program or variable very important.

: **MHz** : The speed the calculator [CPU](#cpu) runs at. It ranges from 10MHz to 16MHz on the [TI-68k](#ti-68k) calculators. It's measured in millions of [clock cycles](#clock-cycle) per second.



### N {#N}



: **Number system** : A way of writing down a number. Two common systems used by people are the [decimal](#decimal) (Arabic) system, and the Roman numeral system. The calculator uses the [binary](#binary) system internally, but the decimal system is what it usually displays.




### O {#O}



: **Operator** : A symbol used in calculations (numeric operators) or in relationship comparisons (related operations). The math operators are +, -, *, /, ^. The relational operators are >, <, =, ≥, ≤, ≠. The logic operators are and, or, xor, not.

: **Optimization** : The process of improving the running time, length, or memory usage of a program.

: **Output** : Information sent from the calculator, e.g. graphics on the screen. Also, the means by which data leaves the calculator, through either the link cable, graph link, or USB cable.

: **OS (Operating System)** : The internal program that runs the calculator and includes all the functionality needed to use the calculator.



### P {#P}



: **Program** : The list of instructions that tells the calculator what to do to perform a task.

: **Programmer** : A person who writes programs.

: **Programming Language** : Numeric or alphabetic commands which the calculator can understand, and execute.



### R {#R}



: **RAM (Random Access Memory)** : A temporary memory, i.e. one in which data is stored so long as electrical power is applied. Data in RAM can be accessed or changed and is lost if the batteries are removed from the calculator. 

: **Recursion** : A program that calls itself as a subroutine (or a function that's defined in terms of itself). See [recursion](#recursion).

: **ROM (Read Only Memory)** : Certain instructions for the calculator are permanently stored in ROM and can be accessed but cannot be changed. [Data](#data) in ROM is not lost if batteries are removed.



### S {#S}



: **Scientific Notation** : A method of expressing very large or very small numbers by using a base number ([mantissa](#mantissa)) times ten raised to some power ([exponent](#exponent)).

: **Scroll** : Shifting part of the screen to give the illusion of seeing only part of an image larger than the screen.

: **Softcode** : Softcoded [data](#data) is information stored in an [array](#array) at the beginning of the program, and read from it later. It is usually slower to read than [hardcoded](#hardcode) data, but the advantage is that the same code can often used for different data stored in the same way.

: **Sprite** : A small image which is moved around the screen using code and/or repeated multiple times on the screen.

: **Statement** : A single line of a program containing a single instruction such as [68k:Text](68k:text.html), [68k:RclPic](68k:rclpic.html), [68k:max()](68k:max().html), etc. Usually synonymous with [command](#command).

: **String** : A variable type that stores text as a series of characters.

: **Subprogram** : A program segment which can be used more than once during the execution of a program, such as a complex set of calculations or a print routine. You can make subprograms using the [68k:Define](68k:define.html) command.



### T {#T}



: **TI (Texas Instruments)** : The makers of the TI graphing calculators. In addition to graphing calculators, they also make a large assortment of other electronic devices.

: **TI-68k** : The unofficial name for the TI calculators that have a 68k processor: the TI-89, TI-89 Titanium, TI-92, TI-92 Plus, and Voyage 200. These are the calculators described in this section of TI|BD.

: **TI-Basic** : The unofficial name of the programming language found on TI calculators.

: **Token** : A single instruction or symbol in [tokenized](68k:tokenization.html) TI-Basic that takes up 1 to 3 bytes and is used to encode TI-Basic programs.



### U {#U}



: **User** : When talking about the effect of a program or command, it is the person running the program or command on his/her calculator.



### V {#V}



: **Variable** : A name given to a value which may vary during program execution. A variable is a memory location where values can be replaced by new values during program execution.
