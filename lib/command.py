def parse(cmd):
	'''Parses command string into action and target game-object

	Params
		cmd : string
			Space sperated string tokens.

	Return {action, target}
	'''

	action, target = cmd.upper().rsplit(' ', 1)

	return {"action": action, "target": target}
