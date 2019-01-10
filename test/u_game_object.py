import io
import sys

from lib.game_object import GameObject

def t_props():
	go = GameObject("Test", "Desc")

	assert go.name == "Test"
	assert go.description == "Desc"

def t_examine():
	go = GameObject("Test", "Desc")
	go.examine()

	assert go.examine() == "Desc"
