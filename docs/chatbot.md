# Chatbot
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Simulates a simple AI chatbot.|None|None|Str1, A|alexrudd|[file chatbot.zip]|

```
:ClrHome
:Disp "What is your pro","blem?
:Repeat Str1="Shut up
:Input ">",Str1
:int(3rand→A
:">Can you say tha","t in a different","way?
:If A=1:">Can you explain ","in more detail, ","please?
:If not(A:">And how does tha","t make you feel?
:Output(1,1,Ans
:End
```

A [Chatbot](https://en.wikipedia.org/wiki/chatterbot) is a type of AI which is able to simulate an intelligent conversation with a person. A typical conversation consists of the person asking the chatbot questions, and the chatbot giving relevant responses. The way the chatbot determines a response is by breaking down the person's statements into the individual words and phrases, and looking up an appropriate response in its database (where its "knowledge" is stored).

Obviously, the more sophisticated a chatbot is, the larger the database of words and phrases needs to be, and likewise the larger the chatbot logic will be. In our simple chatbot, there are only three phrases that the chatbot will say, and the phrases are determined purely by random chance.

When you type in a statement, the chatbot will respond back with its own statement. You can keep "talking" with the chatbot for however long you want, but all you need to type to have it quit is just "Shut up". Because the routine uses Str1, you should [clean it up](cleanup.html) at the end of your program.
