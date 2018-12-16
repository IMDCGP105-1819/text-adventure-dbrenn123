from lib.world import World

class Player:
	def __init__(self):
		self._location = None

	def __repr__(self):
		return f"<{self.__class__.__name__}()>"

	@property
	def location(self):
		'''Get the current location of the player

		Returns <Room()>
		'''

		return self._location

	@location.setter
	def location(self, room_id):
		'''Set the current location of the player

		Params
			room_id : int
				ID used to load room object from data file.
		'''

		self._location = World.load_room(room_id)
