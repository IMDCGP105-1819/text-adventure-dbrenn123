import mock
import pytest
from xml.etree import ElementTree

import lib.world as world

class TestClass:
	@mock.patch('lib.world._get_document', return_value=ElementTree.parse('test/res/test_world.xml').getroot())
	def t_load_stage(self, mock):
		assert world.load_stage(0).name == "test_00"
		assert world.load_stage(1).name == "test_01"
