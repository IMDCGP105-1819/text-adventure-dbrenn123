""" This module handles player input command parsing and execution.

TODO:
	- Implement navigation commands
	- Implement item use/collection/interaction commands
	- More helpful InvalidCommandError messages
"""

import lib.player as player

ACTIONS = ["GO", "LOOK", "EXAMINE", "USE", "COMBINE"]
PREPOSITIONS = ["TO", "AT", "AROUND", "IN", "WITHIN", "WITH", "ON", "UNDER"]
ARTICLES = ["THE"]

class _InvalidCommandError(Exception):
	""" Raise when input command does not meet requirements. """
	pass

class _MissingActionError(_InvalidCommandError):
	""" Raise when initial command token is not a valid action. """
	pass

class _TargetActionMismatchError(_InvalidCommandError):
	""" Raise when action is not applicable to target object. """
	pass

def execute(input):
	""" Parse and execute input.

	After a command has been executed, a response will be printed informing the
	player of the results. If an invalid command is attempted, a message will be
	printed explaining the error.

	Parameters
		input (string):
			Player input command.
	"""

	try:
		# Parse tokenized input and execute.
		_parse(*_tokenize(input))()
	except _MissingActionError:
		print("##Missing action")
	except _TargetActionMismatchError:
		print("##That object cannot do that")
	except _InvalidCommandError:
		print("##Invalid command")
	except Exception as e:
		raise e

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
		raise _MissingActionError()

	for t in tokens:
		if(t['type'] == "ACTION"):
			action = t['value']
		elif(t['type'] == "TARGET"):
			targets.append(t['value'])

	if(len(targets) == 0):
		# Check for player action
		if action in ["LOOK", "EXAMINE"]:
			return player.get_current_stage().examine

	raise _InvalidCommandError()
