import mock
import lib.command as cmd

class TestTokenization:
	def t_0_target_cmd(self):
		t = cmd._tokenize("look around")
		assert len(t) == 2
		assert t[0]['type'] == "ACTION"
		assert t[0]['value'] == "LOOK"

	def t_1_target_cmd(self):
		t = cmd._tokenize("Look at thing")
		assert len(t) == 3
		assert t[0]['type'] == "ACTION"
		assert t[0]['value'] == "LOOK"
		assert t[1]['type'] == "PREPOS"
		assert t[1]['value'] == "LOOK"
		assert t[2]['type'] == "TARGET"
		assert t[2]['value'] == "THING"

	def t_2_target_cmd(self):
		t = cmd._tokenize("Combine thing with otherThing")
		assert len(t) == 4
		assert t[0]['type'] == "ACTION"
		assert t[0]['value'] == "COMBINE"
		assert t[1]['type'] == "TARGET"
		assert t[1]['value'] == "THING"
		assert t[3]['type'] == "TARGET"
		assert t[3]['value'] == "OTHERTHING"

class TestParse:
	def t_(self):
		p = cmd._parse({'type': "ACTION", 'value': "LOOK"})
		assert p == 123
