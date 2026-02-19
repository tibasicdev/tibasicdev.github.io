# Artificial Intelligence
![neural network](http://neuralnetworksanddeeplearning.com/images/tikz10.png "")
## Introduction
Artificial intelligence, often abbreviated AI, is a branch of computer science concerning the intelligence of machines. More specifically, artificial intelligence is the ability of inorganic automaton to perceive their environment and make rational decisions based on data acquired. Used in applications with dynamic environments, as opposed to static, AI attempts to provide solutions to problems without the need of human interaction. The entire purpose behind utilizing AI is to allow automata to make decisions as if it were human. In essence, AI is an effort to emulate the human mind in settings where a real human would be impossible or impracticable to use.



## Characteristics of AI
In the game industry, AI allows a CPU to compete against a human player (or another CPU) under the rules governing the game. For example, a chess AI will analyze the game and attempt to make moves which will maximize its success. Other examples of AI include speech recognition used in cell phones, automatic thermostat controls, and the navigation system used in autonomous robotic vacuum cleaners. In each of these applications, AI combines multiple elements together to complete a task based on the data presented. Breaking the AI into individual qualities allows these elements to be characterized.

In order for a system to be considered artificially intelligent, it must exhibit at least three established characteristics. These characteristics are referred to as the “three A’s”; acquire, analyze, action.

### Acquire
An AI system has the ability to make observations about its environment.
Whether the observations are physical or purely numerical, they represent data acquired by the AI.

### Analyze
An AI system has the ability to evaluate the data acquired and arrive at a conclusion. A chess AI will analyze board piece locations to determine a set of possible actions which will maximize its probability of winning the game.

### Action
An AI system has the ability to make rational choices based on the conclusion of the analysis. This characteristic is especially important as it represents the AI’s function as an agent. In other words, the AI has the ability to choose its course of action, doing so in a rational manner.

The three A’s were specifically chosen in order to differentiate true AI from what is otherwise an automated entity performing a predetermined set of tasks. Industrial robots may appear to have AI; however, they are simply machines following programmed instructions. They do not have the ability to acquire nor analyze environmental data. Another misleading use of the word AI is toward game opponents. Often, game opponents that give the impression of being artificially intelligent are nothing more than controlled systems abiding by a set of rules according to the current situation. An example would include Goombas and Koopa Troopas commonly found throughout many Mario series. They do not have AI since they do not possess the defining characteristic of action. In other words, they do not have the ability to make choices. Although Goombas and industrial robots do not have AI, this doesn’t mean that they could not utilize AI.

For example, the industrial robot could be equipped with a humidistat and sound level meter in order to collect data about environmental humidity and decibel levels respectively. The robot could then analyze the information and make decisions based on the results of the analysis. A possible action may be to activate evaporation fans if the humidity rises above a certain level or to reduce operation speed if the environment decibel levels exceed regulation. While less independent, as may be associated with AI, the industrial robot in this proposed setting abides by the rules established for characterizing artificial intelligence. The robot has the ability to acquire, analyze, and take action based on environmental data, making rational decisions towards achieving a goal.

## Understanding AI
Developing artificial intelligence involves critical thinking and requires an interrogative approach towards its application. It is often necessary to analyze human thought patterns when designing an AI. The process through which an individual arrives at a conclusion in a game of checkers is likely similar to the sequence of steps an AI should take to maximize competency. Thus to better understand artificial intelligence, it is worthwhile to consider the entity from which it is being modeled, the human brain.

With estimated 50-100 billon neurons and approximately 100 trillion synaptic connections linking the neurons, the human brain is arguably the most powerful computer in existence.

## Prerequisites
### Logic

In order to take action based on what it analyzes, an AI must use logical and conditional statements pertaining to the operation it has been programmed to do. For example, in a game of "Tic Tac Toe", the AI must be able to use logic statements to determine where to place the next 'X' or 'O' in order to either block its opponent or complete a 3-in-a-row for itself. Logic statements can also be used to put certain actions at a higher priority than others. For example, a "Tic Tac Toe" AI will attempt to complete its own 3-in-a-row before blocking the opponent, because if it has already won, then the game is over and there is no chance of the opponent winning.

### Procedural Programming
### Control Flow
### Data Structures
## Environment
### Code Structure
### Gather Variables
## Components
### Thinking like AI

To program an AI you must think like one. As a human, you can base your actions on your assessment of the situation — which move would be more strategic, which might result in a better outcome for you — while an AI cannot do this. It can only do what your code tells you to do, nothing more.
### Conditionals

Conditionals are programming objects that check if an event is true and run a section of code if it is. In Ti Basic, the most applicable conditional for AI is [If](if.html), and less common, [While(](while.html), [Repeat(](repeat.html),
 [For(](for.html), [IS>(](is.html), and [DS<(](ds.html). Conditionals are the easiest way to reach an action from input information (it represents Analyze of the "three A's").

### Probability

In a game that contains random elements as a mechanic, such as dice, cards, and spinners, a good AI must account for them in a logical manner. One way to implement this would be to do a weighted average of all the possible options, based on the likelihood of each outcome and a calculable value for how well the game is going.

## Methods

There are many methods that an AI can use to calculate a move, each with their own strengths and weaknesses. These are some of the most popular.

### MiniMax

MiniMaxing is a method of AI in which each possible move is plotted on a tree, the computer finds the most achievable end state, and takes moves to reach that state. Note that the end state does not have to be the best possible state; for example, a MiniMax "Tic Tac Toe" AI won't try to attempt 3 in a row assuming that its opponent won't try to stop it. Instead, a MiniMax AI assumes that its opponent will make the best possible moves, and then find moves that lead to the worst possible 'best' moves: in other words, the minimum maximum. MiniMaxing is suited for AI that should play perfectly, and thus might not be a good fit for a fun game opponent. This approach works best for smaller, shorter games like "Tic Tac Toe" where there aren't too many moves to plot, and the number of possible moves decreases over time. MiniMaxing in a game such as "Chess" is much more difficult, due to there being an increasing, large number of moves, so much so that such an endeavor is currently infeasible. MiniMaxing also doesn't work well for real-time games where each 'turn' happens every interactable frame.

### Decision Tree

The decision tree AI is the most common and the most applicable AI in video games (and is also the easiest to implement on a graphing calculator). A decision tree's foundation is the conditional. The programmer codes in certain events, has the computer check if those events are true, and then has it run code if it is true. For the game "Tic Tac Toe", the programmer might have the computer check if it has a 2 in a row on the board. If so, then they will have it choose the 3rd empty tile. This approach to AI is the best suited for games due to its logical, predictable, and easy to implement system of conditionals. Because of the decision tree's simple nature, it is by far the best choice for TI Basic.
 
### Self-Learning

First of all, letting a calculator *learn* is not really possible, though it is possible to let it remember and compare, thus creating the illusion of learning. Let's look at an example, "Tic Tac Toe": in this game it could be possible for the program to store all the games it's played in lists, whenever the program can't figure a *good* move using the *normal* routine it can refer back to the lists and compare the list with the actual situation, now if the situation matches it could give a *good* move based on what it did *good* or *bad* in the list it is comparing to. This way of learning would prevent the human player from applying the same tactic over and over again, ergo, the machine seems to have *learned* what to do when this "tactic" appears. A good example of self-learning is Deep Blue, an AI developed by IBM that won a deciding chess game against the best human chess player at the time.

[[embedvideo]]
<object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/NJarxpYyoFI&hl=nl&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/NJarxpYyoFI&hl=nl&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object>
[[/embedvideo]]

## Conclusion

*work in progress*
