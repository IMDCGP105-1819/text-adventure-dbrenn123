'''This module provides an interface for importing game locations from data file.'''

from xml.etree import ElementTree
from lib.stage import Stage

def _get_document():
	return ElementTree.parse('res/world.xml').getroot()

def load_stage(id):
	elem = _get_document().find(f"stage[@id='{id}']")
	name = elem.attrib['name']
	description = elem.attrib['description']

	return Stage(name, description)
