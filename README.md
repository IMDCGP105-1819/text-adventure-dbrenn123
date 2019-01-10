# Start

To start, execute the run file from the project directory:

```
python run.py
```

## Commands

Command syntax is `<action> [<target_object>...]`.

Valid actions include:
- `go|goto|move <north|east|south|west>` 	- Move player to new area.
- `examine|look|view [<item>]` 				- Print description of item. Omit item to describe current location and list interactable items.
- `reset`									- Re-initialize game.
- `quit`									- End game.


###### TODO:-
- `use|open|interact <item>` 				- Perform action specific to item.
- `take|pickup <item>...`					- Take item into inventory.
- `drop <item>...`							- Drop item from inventory.
- `combine <item> <item>`					- Combine two items.

- Extract game messages into separate string file.
- Make grammar of game messages responsive to subject word.
- Modify data resource file to keep track of changes made by player.

# Testing

## Requirements:

pytest<br/>
pytest-cov

## Run Tests

Run full suite or specify test file path.

```
pytest [--cov --tb=<level> <path> -k <test>]
```
```--cov``` 			- Show test coverage.<br/>
```--tb=<no|line>``` 	- Hide traceback.
```-k <test>```			- Specify test function to run.
