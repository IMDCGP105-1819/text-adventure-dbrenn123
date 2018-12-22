def execute_command(cmd):
	cmd = _parse(cmd)
	target = _get_target(cmd['target'])

	if(target == None):
		return _invalid_target(cmd)

	action = _get_action(cmd['action'], target)

	if(action == None):
		return _invalid_action(cmd)

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

def _invalid_target(cmd):
	print(f"There is no {cmd['target']}")

	return False

def _invalid_action(cmd):
	print(f"Cannot {cmd['action']} {cmd['target']}")

	return False
