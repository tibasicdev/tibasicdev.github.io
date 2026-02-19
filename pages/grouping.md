# Grouping A Program
Your friend just asked you to transfer a program on your calculator over to his calculator so that he can play it in class whenever he wants to. You say sure, and he gets his link cable out and you start the transfer process. What you thought was going to be a simple transfer turns out to involve some serious headaches.

The program he wants not only has several subprograms that go with it, but multiple list and matrix variables as well as a few pictures. Unfortunately, you aren't aware of this until later after he tries to run the main program without the necessary subprograms, variables, and pictures.

When he asks you why the program won't work like it did on your calculator, you don't have an answer. You decide to start transferring over other programs and variables and whatever else to try to make the program work, but the program still doesn't cooperate. Finally you just give up and tell him that there must be something wrong with his calculator.

While this seems like a rather difficult problem to fix, there is in fact a simple solution: group files. Groups store files together in a package, where the file can be almost anything, whether it is a program, variable, picture, etc. Because groups reside in the archive, you never have to worry about a RAM clear deleting your group.

## Advantages

Several files that go together can be put in one group, making it easy to transfer the files together — whether between two calculators, or a calculator and a computer.

On a TI-83+ or higher, group variables are stored in the archive, which means that a rogue RAM clear won't delete your files.

Groups are also great for backing up a version of a program being worked on before making major changes to it - even if the program is very large, or split between several files.

Finally, putting several parts of a released program in a group avoids the issue of users that forget to transfer a necessary file (although you should explain how groups work in a readme file).

## Limitations

A group must contain more than one variable. It's possible to get around this by providing a dummy variable in the group (use a variable such as X that probably doesn't hold anything important).

TI-Basic programs cannot modify groups. You will have to recreate the group if you want to change its contents. Usually, this isn't too much trouble.

It's also been reported that in large enough groups, the calculator may change a bit in the data when ungrouping — in practice, this might result in an error when running the newly-ungrouped program. To be on the safe side, you should check that a group "works" before deleting the original files. It's also possible that splitting the large group in two (if this is feasible) will fix the issue. 

## References

- The idea for this grouping article came from Jon Pezzino and Kerm Martian's "The Elite Guide to TI-BASIC". It is a good read with lots of useful knowledge and tips/tricks. You can find the link to it on the [Resources](resources.html) page.
