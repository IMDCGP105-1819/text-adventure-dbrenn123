import re

import lib.command as command
import lib.player as player

player.init(0)

while(True):
	input = input(">")

	try:
		print(re.sub("\t", "", command.parse(input)()))
	except command.MissingActionError:
		print("##Missing action")
	except command.TargetActionMismatchError:
		print("##That item cannot do that")
	except command.InvalidCommandError:
		print("##Invalid command")
	except Exception as e:
		raise e
