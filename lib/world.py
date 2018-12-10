class World:
	__instance = None

	@classmethod
	def getInstance(cls):
		if cls.__instance == None:
			cls()

		return cls.__instance

	def __init__(self):
		if self.__class__.__instance != None:
			raise Exception(f"Class {repr(self)} can only be instantiated once")
		else:
			self.__class__.__instance = self

	def __repr__(self):
		return f"<{self.__class__.__name__}()>"
