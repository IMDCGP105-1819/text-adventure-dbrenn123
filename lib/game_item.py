from lib.game_object import GameObject

class GameItem(GameObject):
	""" A class representing in game objects that can be interacted with. """

	def __init__(self, name, description):
		super().__init__(name, description)

		NotImplemented
