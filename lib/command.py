""" This module handles player input command parsing.

TODO:
	- Refactor
"""

import string

import lib.player as player

class CMD:
	GO = 0
	EXAMINE = 1
	USE = 2
	TAKE = 3
	DROP = 4
	COMBINE = 5

	class Type:
		ACTION = 0
		TARGET = 1
		DIR = 2

	type = Type()

ALIASES = {
	CMD.GO: ("GO", "GOTO", "MOVE", "HEAD"),
	CMD.EXAMINE: ("EXAMINE", "LOOK", "VIEW"),
	CMD.USE: ("USE", "OPEN", "INTERACT"),
	CMD.TAKE: ("TAKE", "PICKUP"),
	CMD.DROP: ("DROP"),
	CMD.COMBINE: ("COMBINE"),
	"preposition": ("TO", "AT", "AROUND", "IN", "WITHIN", "WITH", "ON", "UNDER"),
	"article": ("THE", "MY"),
	"direction": ("NORTH", "EAST", "SOUTH", "WEST"),
	"inventory": ("INVENTORY", "INV", "ITEMS", "STUFF")
}

class InvalidCommandError(Exception):
	""" Raise when input command does not meet requirements. """
	pass

class MissingActionError(InvalidCommandError):
	""" Raise when initial command token is not a valid action. """
	pass

class MissingTargetError(InvalidCommandError):
	""" Raise when command that requires target is executed without one """
	pass

class ActionConflictError(InvalidCommandError):
	""" Raise when command contains multiple actions. """
	pass

class InvalidDirectionError(InvalidCommandError):
	""" Raise when player attempts to go where no stage exsists. """
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

def _tokenize(cmd_string):
	""" Split input string into token list.

	Parameters
		cmd_string (string):
			Input string to tokenize

	Return (list[ dict ])
	"""

	tokens = []

	for word in cmd_string.split():
		word = word.translate(str.maketrans('','', string.punctuation)).upper() # Remove punctuation and make uppercase.

		# Check if string token is a command alias.
		for cmd_key, aliases in ALIASES.items():
			if type(cmd_key) is int:
				if word in aliases:
					tokens.append({'type': CMD.type.ACTION, 'val': cmd_key})
					break
			else:
				if cmd_key == "direction":
					if word in aliases:
						tokens.append({'type': CMD.type.DIR, 'val': word.lower()})
						break
				elif word in aliases and cmd_key != "inventory":
					# Ignore prepositions and articles
					break
		else:
			tokens.append({'type': CMD.type.TARGET, 'val': word})

	return tokens

def _parse(*tokens):
	""" Get command from token list.

	Parameters
		tokens (list[ dict{ str:str, str:str } ]):
			List of tokenized command strings.
	"""

	## Validate action
	action_count = _token_type_count(CMD.type.ACTION, tokens)

	# Command must contain only one action, which must be at start.
	if action_count == 0:
		raise MissingActionError(f"{tokens}")
	elif action_count > 1:
		raise ActionConflictError("Too many actions")

	if tokens[0]['type'] != CMD.type.ACTION:
		raise InvalidCommandError(f"Action must come first: {tokens}")

	cmd = tokens[0]['val']
	stage = player.get_current_stage()

	## Validate target(s).
	target_count = _token_type_count(CMD.type.TARGET, tokens)

	if target_count == 0:
		if cmd == CMD.EXAMINE:
			return stage.examine
		elif cmd == CMD.GO:
			# Validate direction.
			if _token_type_count(CMD.type.DIR, tokens) > 1:
				raise ActionConflictError("Cannot go in 2 directions at once")

			# Move player to stage in given direction.
			try:
				dest_stage_id = stage.get_join_id(tokens[1]['val'])
			except KeyError:
				raise InvalidDirectionError()

			return lambda: player.set_stage(dest_stage_id)
		else:
			raise MissingTargetError()
	elif target_count == 1:
		target_name = tokens[1]['val']

		if cmd == CMD.EXAMINE:
			if target_name in ALIASES['inventory']:
				return player.get_items_list_str
			else:
				item = _search(target_name, stage, player)
				return item.examine

		elif cmd == CMD.USE:
			item = _search(target_name, stage)
			return item.use

		elif cmd == CMD.TAKE:
			item = _search(target_name, stage)
			return lambda: player.add_item(item)

		elif cmd == CMD.DROP:
			# TODO - Fix this.
			if target_name in [item.name.upper() for item in player._inventory]:
				item = player.get_item(target_name)

				return lambda: player.drop_item(item)
			else:
				raise InvalidTargetError()
		else:
			raise Exception(f"Command: {tokens} not implemented.")
	elif target_count == 2:
		if cmd == CMD.USE:
			# TODO - Search stage and inventory for targets then use first on second
			NotImplemented

		elif cmd == CMD.TAKE:
			# TODO - Take both from stage
			NotImplemented

		elif cmd == CMD.DROP:
			# TODO - drop both from inventory
			NotImplemented

		elif cmd == CMD.COMBINE:
			# TODO - Search inventory for items and combine.
			NotImplemented

		else:
			raise Exception(f"Command: {tokens} not implemented.")
	else:
		if cmd == CMD.TAKE:
			# TODO - Take all from stage
			NotImplemented
		elif cmd == CMD.DROP:
			# TODO - drop all from inventory
			NotImplemented
		else:
			raise Exception(f"Command: {cmd} not implemented.")

def _token_type_count(type, tokens):
	""" Get total number of tokens of specified type.

	Parameters
		type (integer):
			CMD type to count.

		tokens (list[ dict{ 'type':int } ])

	Return (integer)
	"""

	retv = 0

	for token in tokens:
		if token['type'] == type:
			retv += 1

	return retv

def _search(target_name, *item_containers):
	for container in item_containers:
		if target_name in [name.upper() for name in container.items_list]:
			return container.get_item(target_name)
		else:
			raise InvalidTargetError()
