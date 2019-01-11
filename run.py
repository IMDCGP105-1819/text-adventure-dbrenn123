""" Game cycle.

Parse player input, execute command and print response.

TODO:
	- More helpful InvalidCommandError messages
"""

import re
from shutil import copyfile

import lib.command as command
import lib.player as player
from lib.game_item import Freedom

class _InvalidResponseError(Exception):
	""" Raise when response from callback is incorrect type """
	pass

def init():
	copyfile("res/init_world.xml", "res/world.xml")
	player.init(0)
	print("Use the command (look around) to begin...")

init()

while(Freedom.run):
	CMD = input(">")

	if(CMD.upper() == "QUIT"):
		break
	elif(CMD.upper() == "RESET"):
		start()
	else:
		try:
			callback = command.parse(CMD)
			response = callback()

			print('\n' + re.sub("\t", "", response))
		except command.MissingActionError:
			print("[!] Missing action.")

		except command.MissingTargetError:
			print("[!] Missing target.")

		except command.ActionConflictError:
			print("[!] Too many actions.")

		except command.InvalidTargetError:
			print("[!] Item cannot be found.")

		except command.InvalidDirectionError:
			print("[!] There is nothing that way.")

		except command.TargetActionMismatchError:
			print("[!] You cannot do that with that item.")

		except command.InvalidCommandError:
			print("[!] Invalid command")

		except TypeError:
			raise _InvalidResponseError(f"Invalid response from {callback}. Expected type string. Got type {type(response)}")

		except Exception as e:
			raise e
