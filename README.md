# Start

To start, execute the run file from the project directory:

```
python run.py
```

## Commands

Command syntax is `<action> [<target_object>...]`.

Valid actions include:
- `examine|look|view [<item>]` 	- Print description of item. Omit item to describe current location and list interactable items.
- `use|open|interact <item>` 	- Perform action specific to item.

# Testing

## Requirements:

pytest<br/>
pytest-cov

## Run Tests

Run full suite or specify test file path.

```
pytest [--cov] [<path>]
```
