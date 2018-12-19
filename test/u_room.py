from lib.room import Room

class TestClass:
	def t_repr(self):
		assert repr(Room("Test")) == "<Room(Test)>"
