import pytest
from lib.world import World

@pytest.fixture(autouse=True)
def drop_instance():
    World._World__instance = None

class TestClass:
	def t_repr(self):
		assert repr(World()) == "<World()>"

class TestInstance:
	def t_inst_exception(self):
		World()
		try:
			World()
			assert False, f"{repr(World.getInstance())} was instantiated twice"
		except AssertionError as e:
			raise e
		except Exception as e:
			pass

	def t_get_inst(self):
		assert World.getInstance() is World.getInstance()
