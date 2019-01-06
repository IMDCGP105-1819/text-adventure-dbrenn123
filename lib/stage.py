from lib.game_object import GameObject

class Stage(GameObject):
	"""Object representing an area for the player to explore

		Params:
			name: string - Name of area
			description: string - Description of area
			objects: [] - List of objects contained which can be interacted with
	"""

	def __init__(self, name, description, objects):
		super().__init__(name, description)

		self._objects = objects

	def __repr__(self):
		return f"<{self.__class__.__name__}({self._name})>"

	@property
	def objects_list(self):
		"""Get list of names of each object within stage

			Returns string[]
		"""
		return [obj.name for obj in self._objects]

	def get_object(self, name):
		"""Get instance of specified object

			Params:
				name: string - Name of required object

			Returns first object to match name parameter, False if there is no
			match.
		"""
		for obj in self._objects:
			if(obj.name.upper() == name.upper()):
				return obj

		return False

	def examine(self):
		print(f"You look around the {self.name}.")
		super().examine()
		print(f"You see the following objects...")
		print("\n".join([str(obj) for obj in self.objects_list]))
