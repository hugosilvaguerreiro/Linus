from Skill import *

class ExitSkill(Skill):
	def __init__(self, arg=None):
		self.arg = None

	def execute(self, arg, linus):
		if "exit" in arg:
			linus.sendOutput("goodbye master")
			exit()
		return " "