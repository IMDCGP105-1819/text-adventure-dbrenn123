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

	def __init__(self, name, description, items, joins):
		super().__init__(name, description)

		self._items = items
		self._joins = joins

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

	def add_item(self, item):
		""" Add item to items list

		Parameters
			item (lib.game_item.GameItem)
		"""
		
		self._items.append(item)

	def remove_item(self, item):
		""" Remove item from items list.

		Parameters
			item (lib.game_item.GameItem):
				Item to remove from list.
		"""

		return self._items.remove(item)

	@property
	def joins_list(self):
		retv = []

		for k, v in self._joins.items():
			retv.append((k, v['name']))

		return tuple(retv)

	def get_join_id(self, dir_key):
		return self._joins[dir_key]['id']

	def examine(self):
		""" Perform examine action and get response string """

		NEW_LINE = "\n"

		# Return description of stage followed by list of interactable items.
		return f'''You look around the {self.name}.
				{super().examine()}
				You see the following item(s)...
				{NEW_LINE.join([str(item).capitalize() for item in self.items_list])}

				{NEW_LINE.join([
					f"To the {dir} you see the {name}" for dir, name in self.joins_list
				])}'''
