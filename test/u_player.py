#import mock
#from lib.player import Player

#class TestClass:
#	def t_repr(self):
#		assert repr(Player()) == "<Player()>"

#class TestSetLocation:
#	from lib.room import Room
#	from lib.world import World

#	@mock.patch('lib.world.World.load_room', return_value=Room("Test"))
#	def t_0(self, load_room):
#		p = Player()
#		p.location = load_room()
#
#		assert p.location.name == "Test"

import mock
from xml.etree import ElementTree

import lib.player as player
import lib.world as world

@mock.patch('lib.world._get_document', return_value=ElementTree.parse('test/res/test_world.xml').getroot())
def t_set_stage(mock):
	assert player._current_stage == None
	player.set_stage(0)

	assert player._current_stage.name == "test_00"
