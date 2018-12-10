from lib.player import Player

class TestClass:
	def t_repr(self):
		p = Player()
		assert repr(p) == "<Player()>"
