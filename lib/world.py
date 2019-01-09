""" This module provides an interface for importing game locations from data file.

TODO:
 - Refactor stage loading
 - Item data. Have items in seperate data file?
 """

from xml.etree import ElementTree
from lib.stage import Stage
from lib.game_item import GameItem, Door

def _get_document():
	""" Get root element of game data XML.

	Return (xml.etree.ElementTree)
	"""

	try:
		return ElementTree.parse('res/world.xml').getroot()
	except ElementTree.ParseError as e:
		raise Exception("Parse Error: Check res/world.xml for unclosed tags")
	except Exception as e:
		raise e

def load_stage(id):
	""" Load stage data by ID

	Return (lib.stage.Stage)
	"""

	elem = _get_document().find(f"stage[@id='{id}']")
	name = elem.attrib['name']
	description = elem.attrib['description']
	items = []

	for item in elem.findall("content/*"):
		item_name = item.attrib['name']
		item_desc = item.attrib['description']

		items.append(GameItem(item_name, item_desc))

	for door in elem.findall("join/door"):
		door_desc = door.attrib['description']
		door_stage_id = door.attrib['id']

		items.append(Door(door_desc, door_stage_id))

	return Stage(name, description, items)
