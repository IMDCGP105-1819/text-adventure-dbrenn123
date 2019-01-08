class GameObject:
	""" Abstract game object class

	Parameters
		name (string):
			...

		description (string):
			...
	"""

	def __init__(self, name, description):
		self._name = name
		self._description = description

	def __repr__(self):
		return f"<{self.__class__.__name__}({self._name})>"

	@property
	def name(self):
		return self._name

	@property
	def description(self):
		return self._description

	def examine(self):
		""" Print description of object """

		print(self.description)
