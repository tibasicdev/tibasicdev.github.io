# Text Adventure
> **Note:** This page was originally created by AtionSong on the TI-Basic wiki, and has been added here because TI-Basic wiki is in the process of being merged with this wiki. In addition to this page, only those pages which weren't already duplicated on this wiki were added.

![tgmscreen.jpg](tgmscreen.jpg "")

### Text Adventures

**Needed Commands:** [Goto/Lbl](goto.html), [Menu(](menu.html), [ClrHome](clrhome.html), [Output(](output.html), and [Pause](pause.html) *Some additional commands used in demo for demonstration purposes*

#### Structure

A Text Adventure game can easily be made on a graphing calculator using many Output( commands to advance a story and Menu( for choices. To see how a small RPG Game might be made, see the following diagram:

```
                     -Go Back
                     -Climb Tree     - Go Back
           - Go Left -Cut down tree  - Burn Bridge
Crossroads - Go Forward -------------- Cross Bridge
           - Go Right - Go Back
                      - Knock on door
                      - Break into house
                      - Burn house down
```

There are 3 sections or levels to this game (choice groups). The first level offers 3 choices of how to proceed along the crossroads. The second level allows for interaction with the object found, based on the direction chosen in level 1. In our demo, level 3 has no choices, but in a full game, the choice made from level 3 would impact what happens in level 4.

#### Actual Game

In this game, the user is told that they are a mighty warrior with an ax and a match. To set up the game, we will start with an opening screen:

```
prgmRPGGAME
:ClrHome
:Output(1,1,"-/-/-/-/-/-/-/-/
:Output(2,3,"WARRIOR GAME
:Output(3,1,"-/-/-/-/-/-/-/-/
:Output(5,1,"PROGRAMMED BY
:Output(6,1,"TI-BASIC WIKI
:Pause
:ClrHome
```

After the opening screen, we want to set the scene for the player, so they know their "role" in this role playing game:

```
:Lbl 1
:Output(1,1,"YOU ARE TIB, A 
:Output(2,1,"MIGHTY WARRIOR.
:Output(3,1,"ON YOUR TRAVELS
:Output(4,1,"YOU COME TO A
:Output(5,1,"CROSSROADS.
:Pause
:ClrHome
```

Now, we create the first screen where the first set of choices (outlined above) is presented. We give the user 1 match, using the [→](store.html) command.

```
:1→M
:Menu("CHOOSE:","LEFT <-",2,"FORWARD ^",3,"RIGHT ->",4)
```

We then create the second level in the same was as the first, with explanations, followed by choices, as in level 1.

```
:Lbl 2
:Output(1,1,"YOU COME TO AN
:Output(2,1,"OLD OAK TREE.
:Pause
:ClrHome
:Menu("CHOOSE:","GO BACK",1,"CLIMB TREE",5,"BURN TREE",6)
:Lbl 3
:Output(1,1,"YOU COME TO A
:Output(2,1,"WOODEN BRIDGE.
:Output(3,1,"THERE'S A CAVE ON
:Output(4,1,"THE OTHER SIDE.
:Pause
:ClrHome
:Menu("CHOOSE:","GO BACK",1,"BURN BRIDGE",7,"CROSS BRIDGE",8)
:Lbl 4
:Output(1,1,"YOU COME TO A
:Output(2,1,"LOG CABIN WITH
:Output(3,1,"A LIGHT ON.
:Pause
:ClrHome
:Menu("CHOOSE","GO BACK",1,"KNOCK",9,"BREAK IN",10,"BURN HOUSE",11)
```

To continue the game, additional Labels would be made for each of the other choices. We will only go over one: the Label for an event using a match to show how item possession is used. Let's use the Label 6 "BURN TREE" example:

```
:Lbl 6
:If M>0:Then
:M-1→M
:Output(1,1,"YOU BURNED THE
:Output(2,1,"TREE DOWN.
:Pause
:ClrHome
:Menu("CHOOSE:"...
:End
:Else
:Output(1,1,"YOU DO NOT HAVE
:Output(2,1,"A MATCH!
:Pause
:ClrHome
:Goto 2
:End
```

Checking to see if M is greater than 0, then subtracting 1 will allow for additional matches to be collected, and still be used. Using → and If/Then statements, you can create an intricate item possession system as well as restrict certain events to people with certain items or skill levels above a certain amount.

If you want to continue this game on your own, feel free to write your own storyline. Will burning the bridge prohibit you from reaching another area? Or will it save you from being attacked by a bear that lives in a cave? You can decide if you choose to make your own Text Adventure RPG!
