""" This module provides an interface for importing game locations from data file.

TODO:
 - Refactor stage loading
 - Item data. Have items in seperate data file?
 """

from xml.etree import ElementTree
from lib.stage import Stage
from lib.game_object import GameObject

def _get_document():
	""" Get root element of game data XML.

	Return (xml.etree.ElementTree)
	"""

	return ElementTree.parse('res/world.xml').getroot()

def load_stage(id):
	""" Load stage data by ID

	Return (lib.stage.Stage)
	"""

	elem = _get_document().find(f"stage[@id='{id}']")
	name = elem.attrib['name']
	description = elem.attrib['description']
	objects = []

	for obj in elem.findall("content/*"):
		obj_name = obj.attrib['name']
		obj_desc = obj.attrib['description']

		objects.append(GameObject(obj_name, obj_desc))

	return Stage(name, description, objects)
