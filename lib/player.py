""" This module manages the game-state of the player. """

import lib.command
import lib.game_item
import lib.world as world

_current_stage = None
_inventory = []

def init(stage_id):
	""" Initialize player module.

	Parameters
		stage_id (integer):
			ID of starting stage.
	"""

	set_stage(stage_id)

def get_current_stage():
	""" Get current stage object.

	Return (lib.stage.Stage):
		...
	"""

	return _current_stage

def set_stage(id):
	""" Set current stage by stage ID.

	Parameters
		id (integer):
			ID used to load stage data.

	TODO:
		- Handle invalid ID
	"""

	global _current_stage

	_current_stage = world.load_stage(id)

	return f"You enter the {get_current_stage().name}."

@property
def items_list():
	""" Get a list of the names of each item within the player inventory.

	Return (list[ string ]):
		A list of item names.
	"""

	return [item.name for item in self._inventory]

def get_item(name):
	""" Get item from inventory by name.

	Parameters
		name (string):
			Name of required item.

	Return (lib.game_item.GameItem):
		First item to match name parameter or False if there is no match.
	"""

	for item in _inventory:
		if(item.name.upper() == name.upper()):
			return item

	return False

def get_items_list_str():
	retv = ""

	for item in _inventory:
		retv += item.name.capitalize() + "\n"

	if retv == "":
		return "[Empty]"
	else:
		return retv[:-1]

def add_item(item):
	""" Add item to inventory.

	Parameters
		item (lib.game_item.GameItem)
	"""

	if item.__class__ is lib.game_item.GameItem and item.__class__ is not lib.game_item.Door:
		_current_stage.remove_item(item)
		_inventory.append(item)

		return f"{item.name.capitalize()} added to inventory."
	else:
		raise lib.command.TargetActionMismatchError()

def drop_item(item):
	""" Drop item from inventory and back into the stage

	Parameters
		item (lib.game_item.GameItem)
	"""

	# TODO - fix this -> _inventory.remove(item) property object not iterable
	for i in range(len(_inventory)):
		print(i)
		if item is _inventory[i]:
			del _inventory[i]

	_current_stage.add_item(item)

	return f"{item.name.capitalize()} removed from inventory"
