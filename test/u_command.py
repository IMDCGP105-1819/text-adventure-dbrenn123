import mock
import lib.command as cmd

class TestParse:
	def t_parser(self):
		c = cmd._parse("Test Command")
		assert c['action'] == "TEST"
		assert c['target'] == "COMMAND"
