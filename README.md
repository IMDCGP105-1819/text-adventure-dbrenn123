# Start

To start, execute the run file from the project directory:

```
python run.py
```

## Commands

Command syntax is `<command> [<arg>...]`.
Input is not case sensitive and prepositions and articles are ignored i.e.- `Look at the thing` = `look thing`.

Command|Args|Description
-|-|-
`Go`|(**north**&#124;**east**&#124;**south**&#124;**west**)|Sets stage in given direction to current stage.
`Examine`|[(<**item**>&#124;**inventory**)]|Prints name and description of given item. Omitting item prints name and description of current stage, lists items within stage and lists joined stages and their direction. Examining inventory will list all items within players inventory.
`Use`|<**item**>|Perform action specific to item.
`Take`|<**item**>|Take item from stage and store it in player inventory. Only certain items can be picked up.
`Drop`|<**item**>|Remove item from inventory and put it back into stage.
`Reset`||Restarts game.
`Quit`||Ends game

Command|Aliases
-|:-:
`Go`|(**Goto**&#124;**Move**)
`Examine`|(**Look**&#124;**View**)
`Use`|(**Open**&#124;**Interact**)
`Take`|(**Pickup**)
`Inventory`|(**Inv**&#124;**Items**)

# Walkthrough

```
Use the command (look around) to begin...
>look around

You look around the atrium.
There is nothing out of the ordinary.
You see the following item(s)...
Lamp
Chandelier
Desk
Paperclip

To the north you see the hallway
>look at paperclip


Could be useful...
>take paperclip

Paperclip added to inventory.
>go north

You enter the hallway.
>look

You look around the hallway.
It is a spooky hallway. There is something out of the ordinary.
You see the following item(s)...
Painting
Door1

To the south you see the atrium
>examine the painting

It's too dark to see.
>head south

You enter the atrium.
>look lamp

It is a nice lamp.
>use lamp


You turn on the light...
>go north

You enter the hallway.

>look painting

Méphistophélès dans les airs - 1828
>use door1

You go through the door, into cellar...
>look

You look around the cellar.
It is dark and damp.
You see the following item(s)...
Shovel
Door1
Door2



>use door2


You go through the door, into passage-way...
>look

You look around the passage-way.

You see the following item(s)...
Shoe
Door2

To the west you see the outside
>take shoe

Shoe added to inventory.
>drop shoe
0

Shoe removed from inventory
>go west

You enter the outside.
>look around


You look around the outside.

You see the following item(s)...
Trees
Freedom


>look at the trees

The trees sway gently in the wind.
>use freedom

You run off into the sunset and live happily ever after. The End.
```

###### TODO:-
- `combine <item> <item>`					- Combine two items.


- Unify item management for player inventory and stage contents
- Extract game messages into separate string file.
- Make grammar of game messages responsive to subject word.
- Modify data resource file to keep track of changes made by player.
- Read-back command when InvalidCommandError is raised.
- Examine individual inventory items.
- Condense command parsing.

# Testing

## Requirements:

pytest<br/>
pytest-cov

## Run Tests

Run full suite or specify test file path.

```
pytest [--cov --tb=<level> <path> -k <test>]

--cov			  	Show test coverage.
--tb=<no|line> 		Hide traceback.
-k <test>		  	Specify test function to run.
```
