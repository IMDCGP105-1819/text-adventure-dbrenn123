""" This module provides an interface for importing and writing game content from data file. """

from xml.etree.ElementTree import ElementTree

from lib.stage import Stage
from lib.game_item import *

_DATA_PATH = 'res/world.xml'
_TREE = ElementTree()
_TREE.parse(_DATA_PATH)

def _collect_items(stage_element):
	""" Get list of items in stage

	Parameters
		stage_element (xml.etree.ElementTree)

	Return (list[ lib.game_item.GameItem ])
	"""

	items = []

	for item in stage_element.findall("content/*"):
		Item = None

		# Assign item class based on tag name.
		if item.tag == "freedom":
			Item = Freedom
		elif item.tag == "lamp":
			Item = Lamp
		else:
			Item = GameItem

		items.append(Item(*_get_attribs(item, 'name', 'description')))

	for door in stage_element.findall("join/door"):
		items.append(Door(*_get_attribs(door, 'id', 'description', 'dest_id')))

	return items

def _collect_joins(stage_element):
	""" Get directional stage joins

	Parameters
		stage_element (xml.etree.ElementTree)

	Return (dict{ direction: dict{name:str, id:int } })
	"""

	joins = {}

	for join in stage_element.findall("join/*"):
		tag = join.tag

		if tag != "door":
			dest_id = int(_get_attribs(join, 'dest_id')[0])
			dest_name = _get_attribs(_TREE.find(f"stage[@id='{dest_id}']"), 'name')[0]

			joins[tag] = {'id': dest_id, 'name': dest_name}

	return joins

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

def load_stage(id):
	""" Load stage data by ID

	Paremeters
		id (integer):
			ID used to read stage info from data file.

	Return (lib.stage.Stage)
	"""

	stage_element = _TREE.find(f"stage[@id='{id}']")

	return Stage(*_get_attribs(stage_element, 'name', 'description'), _collect_items(stage_element), _collect_joins(stage_element))

def write(xpath, attrib, new_val):
	""" Write new data to document

	TODO:
		-Better API for altering game object data.
	"""

	elem = _TREE.find(xpath)
	old_val = elem.attrib[attrib]

	if new_val != old_val:
		elem.set(attrib, new_val)
		_TREE.write(_DATA_PATH)
