import mock
from xml.etree import ElementTree

import lib.world as world

class TestClass:
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
