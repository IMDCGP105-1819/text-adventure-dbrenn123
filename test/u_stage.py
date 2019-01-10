import sys
import io

from lib.game_object import GameObject
from lib.stage import Stage

def t_props():
	s = Stage(
		"Qwert",
		"Zap",
		[GameObject("Test_1", "Desc_1"), GameObject("Test_2", "Desc_2"), GameObject("Test_3", "Desc_3")],
		{"north": {'id': 1, 'name': "test"}}
	)

	assert s.name == "Qwert"
	assert s.description == "Zap"
	assert len(s.items_list) == 3

def t_get_object():
	go = GameObject("Test_2", "Desc_2")
	s = Stage(
		"Qwert",
		"Zap",
		[GameObject("Test_1", "Desc_1"), go, GameObject("Test_3", "Desc_3")],
		{"north": {'id': 1, 'name': "test"}}
	)

	assert s.get_item("Test_2") is go

def t_joins_list():
	s = Stage("Test Stage", "test", [GameObject("obj", "test")], {"north": {'id': 1, 'name': "test1"}, "south": {'id': 2, 'name': "test2"}})

	assert s.joins_list == (('north', 'test1'), ('south', 'test2'))

def t_get_join_id():
	s = Stage("Test Stage", "test", [GameObject("obj", "test")], {"north": {'id': 1, 'name': "test"}})

	assert s.get_join_id('north') == 1

def t_examine():
	s = Stage("Test Stage", "test", [GameObject("obj", "test")], {"north": {'id': 1, 'name': "test"}})
	assert len(s.examine()) == 83
