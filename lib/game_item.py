from lib.game_object import GameObject
import lib.player as player

class GameItem(GameObject):
	""" A class representing in game objects that can be interacted with.

	Parameters
		name (string)
		description (string)
	"""

	def __init__(self, name, description):
		super().__init__(name, description)

		NotImplemented

	def examine(self):
		return super().examine()

class Door(GameItem):
	""" A class representing a door allowing the player to navigate stages.

	Parameters
		description (string)

		stage_id (integer):
			ID of stage to which this door will lead.
	"""

	def __init__(self, description, stage_id):
		super().__init__("door", description)
		self._stage_id = stage_id

	def examine(self):
		return super().examine()

	def use(self):
		""" Send player to linked stage. """

		player.set_stage(self._stage_id)

		return f"You go through the door, into {player.get_current_stage().name}"
