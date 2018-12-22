def execute_command(string):
	cmd = _parse(sting)
	target = _get_target(cmd['target'])

def _parse(cmd):
	'''Parses command string into action and target game-object

	Params
		cmd : string
			Space sperated string tokens.

	Return {action, target}
	'''

	action, target = cmd.upper().rsplit(' ', 1)

	return {"action": action, "target": target}

def _get_target(name):
	NotImplemented
