"""This module manages the game-state of the player."""

import lib.world as world

_current_stage = None
_inventory = []

def init(stage_id):
	"""Initialize player module

		Params:
			stage_id: int - ID of starting stage
	"""

	set_stage(stage_id)

def get_current_stage():
	return _current_stage

def set_stage(id):
	global _current_stage

	_current_stage = world.load_stage(id)
