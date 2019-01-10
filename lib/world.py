""" This module provides an interface for importing game locations from data file. """

from xml.etree import ElementTree

from lib.stage import Stage
from lib.game_item import GameItem, Door

def _get_document():
	""" Get root element of game data XML.

	Return (xml.etree.ElementTree)
	"""

	try:
		return ElementTree.parse('res/world.xml').getroot()
	except Exception as e:
		raise e

def load_stage(id):
	""" Load stage data by ID

	Paremeters
		id (integer):
			ID used to read stage info from data file.

	Return (lib.stage.Stage)
	"""

	stage_element = _get_document().find(f"stage[@id='{id}']")

	return Stage(*_get_attribs(stage_element, 'name', 'description'), _collect_items(stage_element), _collect_joins(stage_element))

def _get_attribs(element, *attrib_keys):
	""" Get attribute values from element data

	Parameters
		element (xml.etree.ElementTree):
			Document element tree to read from.

		attrib_keys (string)...:
			Each attribute to return.

	Return (tuple( <string>... )): Tuple of attribute values in same order as args.
	"""

	attrib_vals = ()

	for key in attrib_keys:
		attrib_vals += (element.attrib[key],)

	return attrib_vals

def _collect_items(stage_element):
	""" Get list of items in stage

	Return (list[ lib.game_item.GameItem ])
	"""

	items = []

	for item in stage_element.findall("content/*"):
		items.append(GameItem(*_get_attribs(item, 'name', 'description')))

	for door in stage_element.findall("join/door"):
		items.append(Door(*_get_attribs(door, 'description', 'dest_id')))

	return items

def _collect_joins(stage_element):
	""" Get directional stage joins

	Return (dict{ direction: dict{name:str, id:int } })
	"""

	joins = {}

	for join in stage_element.findall("join/*"):
		tag = join.tag

		if tag != "door":
			dest_id = int(_get_attribs(join, 'dest_id')[0])
			dest_name = _get_attribs(_get_document().find(f"stage[@id='{dest_id}']"), 'name')[0]

			joins[tag] = {'id': dest_id, 'name': dest_name}

	return joins
