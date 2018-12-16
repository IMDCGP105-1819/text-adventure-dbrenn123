import mock
from lib.player import Player

class TestClass:
	def t_repr(self):
		assert repr(Player()) == "<Player()>"

class TestSetLocation:
	from lib.room import Room
	from lib.world import World

	@mock.patch('lib.world.World.load_room', return_value=Room("Test"))
	def t_0(self, load_room):
		p = Player()
		p.location = load_room()

		assert p.location.name == "Test"
