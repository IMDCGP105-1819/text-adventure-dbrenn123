class Room:
	def __init__(self, name):
		self._name = name

	def __repr__(self):
		return f"<{self.__class__.__name__}({self._name})>"
		
	@property
	def name(self):
		return self._name
