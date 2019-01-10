import mock
from xml.etree import ElementTree

import lib.world as world

'''class TestClass:
	@mock.patch('lib.world._get_document', return_value=ElementTree.parse('test/res/test_world.xml').getroot())
	def t_load_stage(self, mock):
		assert world.load_stage(0).name == "test_00"
		assert world.load_stage(1).name == "test_01"

	@mock.patch('lib.world._get_document', return_value=ElementTree.parse('test/res/test_world.xml').getroot())
	def t_stage_properties(self, mock):
		assert world.load_stage(0).name == "test_00"
		assert world.load_stage(1).name == "test_01"

		assert world.load_stage(2).description == "test_description"
		assert len(world.load_stage(2)._objects) == 1
		assert world.load_stage(2)._objects[0].name == "obj_03"

		assert len(world.load_stage(3)._objects) == 2
		assert world.load_stage(3)._objects[0].name == "obj_04"
		assert world.load_stage(3)._objects[1].name == "obj_05"
'''
class TestHelperFunctions:
	def t_get_attribs(self):
		elem = ElementTree.parse('test/res/test_world_helpers.xml').getroot().find("test")
		attribs = world._get_attribs(elem, 'test_0', 'test_1', 'test_2')

		assert attribs == ("qwerty", "zap", "asdf")

class TestStageLoading:
	def t_collect_items(self):
		stage_elem = ElementTree.parse('test/res/test_world_items.xml').getroot().find("stage[@id='0']")
		items = world._collect_items(stage_elem)

		assert len(items) == 2
		# TODO assert len(items[1].get_items()) == 2

	@mock.patch('lib.world._get_document', return_value=ElementTree.parse('test/res/test_world_joins.xml').getroot())
	def t_collect_joins(self, mock):
		stage_elem = ElementTree.parse('test/res/test_world_joins.xml').getroot().find("stage[@id='0']")
		joins = world._collect_joins(stage_elem)

		assert "north" in joins
		assert "east" in joins
		assert "south" in joins
		assert "west" not in joins
		assert list(joins.values())[0] == {'id': 1, 'name': 'test_01'}
