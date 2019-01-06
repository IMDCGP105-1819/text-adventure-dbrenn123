import io
import sys

from lib.game_object import GameObject

def t_props():
	go = GameObject("Test", "Desc")

	assert go.name == "Test"
	assert go.description == "Desc"

def t_examine():
	capturedOutput = io.StringIO()
	sys.stdout = capturedOutput

	go = GameObject("Test", "Desc")
	go.examine()

	sys.stdout = sys.__stdout__
	assert capturedOutput.getvalue() == "Desc\n"
