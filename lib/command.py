""" This module handles player input command parsing.

TODO:
	- Implement navigation commands
	- Implement item use/collection/interaction commands
	- Refactor _parse()
"""

import lib.player as player

ACTIONS = ["GO", "LOOK", "EXAMINE", "USE", "COMBINE"]
PREPOSITIONS = ["TO", "AT", "AROUND", "IN", "WITHIN", "WITH", "ON", "UNDER"]
ARTICLES = ["THE"]

class InvalidCommandError(Exception):
	""" Raise when input command does not meet requirements. """
	pass

class MissingActionError(InvalidCommandError):
	""" Raise when initial command token is not a valid action. """
	pass

class InvalidTargetError(InvalidCommandError):
	""" Raise when target item cannot be found """
	pass

class TargetActionMismatchError(InvalidCommandError):
	""" Raise when action is not applicable to target object. """
	pass

def parse(input):
	""" Parse input and return callback function.

	Parameters
		input (string):
			Player input command.

	Return (function)
	"""

	return _parse(*_tokenize(input))

def _tokenize(string):
	""" Split string into token list. """

	tokens = []

	for s in string.split():
		s = s.upper()

		if s in ACTIONS:
			tokens.append({'type': "ACTION", 'value': s})
		elif s in PREPOSITIONS:
			tokens.append({'type': "PREPOS", 'value': s})
		elif s in ARTICLES:
			tokens.append({'type': "ARTICLE", 'value': s})
		else:
			tokens.append({'type': "TARGET", 'value': s})

	return tokens

def _parse(*tokens):
	""" Get command from token list.

	Parameters
		tokens (list[ dict{ str:str, str:str } ]):
			List of tokenized command strings.
	"""

	action = None
	targets = []

	if(tokens[0]['type'] != "ACTION"):
		raise MissingActionError()

	for t in tokens:
		if(t['type'] == "ACTION"):
			action = t['value']
		elif(t['type'] == "TARGET"):
			targets.append(t['value'])

	if(len(targets) == 0):
		# Validate player action
		if action in ["LOOK", "EXAMINE"]:
			return player.get_current_stage().examine
		else:
			raise TargetActionMismatchError()
	else:
		# Validate target item
		for target in targets:
			if(target not in player.get_current_stage().items_list):
				if(action in ["LOOK", "EXAMINE"]):
					return player.get_current_stage().get_item(target).examine
				elif action in ["USE","OPEN"]:
					return player.get_current_stage().get_item(target).use
				else:
					raise TargetActionMismatchError()
			else:
				raise InvalidTargetError()

	raise InvalidCommandError()
