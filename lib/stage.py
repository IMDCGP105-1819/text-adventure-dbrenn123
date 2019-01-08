from lib.game_object import GameObject

class Stage(GameObject):
	""" A class representing an area for the player to explore.

	Parameters
		name (string):
			Name of stage.

		description (string):
			Description of stage.

		items (list[ lib.game_item.GameItem ]):
			List of items which can be interacted with.
	"""

	def __init__(self, name, description, items):
		super().__init__(name, description)

		self._items = items

	@property
	def items_list(self):
		""" Get a list of the names of each item within the stage.

		Return (list[ string ]):
			A list of item names.
		"""
		return [item.name for item in self._items]

	def get_item(self, name):
		""" Get item by name.

		Parameters
			name (string):
				Name of required item.

		Return (lib.game_item.GameItem):
			First item to match name parameter or False if there is no match.
		"""

		for item in self._items:
			if(item.name.upper() == name.upper()):
				return item

		return False

	def examine(self):
		""" Print stage info and interactable item names. """

		print(f"You look around the {self.name}.")
		super().examine()
		print(f"You see the following items...")
		print("\n".join([str(item) for item in self.items_list]))
