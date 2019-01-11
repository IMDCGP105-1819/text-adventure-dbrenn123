import lib
import lib.player as player
from lib.game_object import GameObject

class GameItem(GameObject):
	""" A class representing in game objects that can be interacted with.

	Parameters
		name (string)

		description (string)
	"""

	def __init__(self, name, description):
		super().__init__(name, description)

	def examine(self):
		return super().examine()

class Door(GameItem):
	""" A class representing a door allowing the player to navigate stages.

	Parameters
		description (string)

		dest_id (integer):
			ID of stage to which this door will lead.
	"""

	def __init__(self, id, description, dest_id):
		super().__init__(f"door{id}", description)
		self._dest_id = dest_id

	def use(self):
		""" Send player to linked stage. """

		player.set_stage(self._dest_id)

		return f"You go through the door, into {player.get_current_stage().name}..."

class Freedom(GameItem):
	""" A class representing an object which triggers end game. """
	run = True # False will exit game cyle.

	def __init__(self, name, description):
		super().__init__(name, description)

	def use(self):
		""" Finish game. """

		Freedom.run = False

		return f"You run off into the sunset and live happily ever after. The End."

class Lamp(GameItem):
	""" A class representing a lamp object. Can reveal hidden secrets.

	Parameters
		name (string)

		description (string)
	"""

	def __init__(self, name, description):
		super().__init__(name, description)

	def use(self):
		""" Reveal item description """
		lib.world.write(".//item[@id='1']", 'description', "Méphistophélès dans les airs - 1828")

		return f"You turn on the light..."
