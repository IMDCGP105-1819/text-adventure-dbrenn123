def parse(cmd):
	'''Parses command string into action and target game-object

	Params
		cmd : string
			Space sperated string tokens.

	Return {action, object}
	'''

	action, object = cmd.rsplit(' ', 1)

	return {"action": action, "object": object}
