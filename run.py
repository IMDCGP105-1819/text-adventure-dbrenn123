""" Game cycle.

Parse player input, execute command and print response.

TODO:
	- More helpful InvalidCommandError messages
"""

import re

import lib.command as command
import lib.player as player

def start():
	player.init(0)

start()

while(True):
	CMD = input(">")

	if(CMD.upper() == "QUIT"):
		break
	elif(CMD.upper() == "RESET"):
		start()
	else:
		try:
			callback = command.parse(CMD)
			response = callback()

			print(re.sub("\t", "", response))
		except command.MissingActionError:
			print("##Missing action")
		except command.TargetActionMismatchError:
			print("##That item cannot do that")
		except command.InvalidCommandError:
			print("##Invalid command")
		except Exception as e:
			raise e
