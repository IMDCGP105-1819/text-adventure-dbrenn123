import mock

from lib.command import CMD, _tokenize, _token_type_count

class TestHelperFunctions:
	def t_token_type_count(self):
		assert _token_type_count(CMD.type.TARGET, [{'type': CMD.type.ACTION}, {'type': CMD.type.TARGET}, {'type': CMD.type.TARGET}]) == 2
		assert _token_type_count(CMD.type.ACTION, [{'type': CMD.type.ACTION}, {'type': CMD.type.TARGET}, {'type': CMD.type.TARGET}]) == 1

class TestTokenization:
	def t_action(self):
		for test_str in ("examine", "EXAMINE", "EXAMINE!-@#"):
			msg = f"Test string: {test_str}"
			tokens = _tokenize(test_str)

			assert len(tokens) == 1, msg
			assert tokens[0]['type'] == CMD.type.ACTION, msg
			assert tokens[0]['val'] == CMD.EXAMINE, msg

	def t_action_alias(self):
		assert _tokenize("look")[0]['val'] == CMD.EXAMINE

	def t_action_with_target(self):
		test_str = "use object"
		msg = f"Test string: {test_str}"
		tokens = _tokenize(test_str)

		assert len(tokens) == 2, msg
		assert tokens[0]['type'] == CMD.type.ACTION, msg
		assert tokens[0]['val'] == CMD.USE, msg
		assert tokens[1]['type'] == CMD.type.TARGET, msg
		assert tokens[1]['val'] == "OBJECT", msg

	def t_action_with_two_targets(self):
		test_str = "combine object1 object2"
		msg = f"Test string: {test_str}"
		tokens = _tokenize(test_str)

		assert len(tokens) == 3, msg
		assert tokens[1]['type'] == tokens[2]['type'] == CMD.type.TARGET, msg

	def t_action_with_many_targets(self):
		test_str = "drop object1 object2 object3"
		msg = f"Test string: {test_str}"
		tokens = _tokenize(test_str)

		assert len(tokens) == 4

	def t_direction(self):
		test_str = "go north"
		msg = f"Test string: {test_str}"
		tokens = _tokenize(test_str)

		assert tokens[1]['type'] == CMD.type.DIR
		assert tokens[1]['val'] == "NORTH"

	def t_prepos_artic(self):
		test_str = "look at the thing"
		msg = f"Test string: {test_str}"
		tokens = _tokenize(test_str)

		assert len(tokens) == 2
		assert tokens[0]['type'] == CMD.type.ACTION
		assert tokens[1]['type'] == CMD.type.TARGET
