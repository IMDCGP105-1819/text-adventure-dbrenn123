""" This module manages the game-state of the player.

TODO:
	- Inventory functionality
"""

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
		id (int):
			ID used to load stage data.

	TODO:
		- Handle invalid ID
	"""

	global _current_stage

	_current_stage = world.load_stage(id)
