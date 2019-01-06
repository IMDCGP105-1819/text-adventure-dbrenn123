import sys
import io

from lib.game_object import GameObject
from lib.stage import Stage

def t_props():
	s = Stage("Qwert","Zap", [GameObject("Test_1", "Desc_1"), GameObject("Test_2", "Desc_2"), GameObject("Test_3", "Desc_3")])

	assert s.name == "Qwert"
	assert s.description == "Zap"
	assert len(s.objects_list) == 3

def t_get_object():
	go = GameObject("Test_2", "Desc_2")
	s = Stage("Qwert","Zap", [GameObject("Test_1", "Desc_1"), go, GameObject("Test_3", "Desc_3")])

	assert s.get_object("Test_2") is go

def t_examine():
	capturedOutput = io.StringIO()
	sys.stdout = capturedOutput

	s = Stage("Test Stage", "test", [GameObject("obj", "test")])
	s.examine()

	sys.stdout = sys.__stdout__

	assert len(capturedOutput.getvalue()) == 74
