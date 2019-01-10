import collections.abc

import lib.player
import lib.command as command

lib.player.init(0)

class TestCMDS:
	def t_go(self):
		cmd_strings = ("GO north", "GOTO north", "MOVE north")

		for test_str in cmd_strings:
			callback = command.parse(test_str)

			assert isinstance(callback, collections.abc.Callable)

	def t_examine(self):
		cmd_strings = ("LOOK", "LOOK item", "EXAMINE", "EXAMINE item", "VIEW", "VIEW item")

		for test_str in cmd_strings:
			callback = command.parse(test_str)

			assert isinstance(callback, collections.abc.Callable)

	def t_use(self):
		cmd_strings = ("USE item", "OPEN door", "INTERACT with item")

		for test_str in cmd_strings:
			callback = command.parse(test_str)

			assert isinstance(callback, collections.abc.Callable)

	def t_take(self):
		cmd_strings = ("TAKE item", "TAKE item item item", "PICKUP item", "PICKUP item item item")

		for test_str in cmd_strings:
			callback = command.parse(test_str)

			assert isinstance(callback, collections.abc.Callable)

	def t_drop(self):
		cmd_strings = ("DROP item")

		for test_str in cmd_strings:
			callback = command.parse(test_str)

			assert isinstance(callback, collections.abc.Callable)
