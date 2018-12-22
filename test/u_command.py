import mock
import lib.command as cmd

class TestParse:
	def t_parser(self):
		c = cmd._parse("test command")
		assert c['action'] == "TEST"
		assert c['target'] == "COMMAND"

	def t_invalid_cmd(self):
		assert cmd.execute_command("Test Invalid") == False
