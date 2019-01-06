'''This module provides an interface for importing game locations from data file.'''

from xml.etree import ElementTree
from lib.stage import Stage
from lib.game_object import GameObject

def _get_document():
	return ElementTree.parse('res/world.xml').getroot()

def load_stage(id):
	elem = _get_document().find(f"stage[@id='{id}']")
	name = elem.attrib['name']
	description = elem.attrib['description']
	objects = []

	for obj in elem.findall("content/*"):
		obj_name = obj.attrib['name']
		obj_desc = obj.attrib['description']

		objects.append(GameObject(obj_name, obj_desc))

	return Stage(name, description, objects)
