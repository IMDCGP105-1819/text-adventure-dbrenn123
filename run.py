import lib.command as command
import lib.player as player

player.init(0)

while(True):
	command.execute(input(">"))
