from Skill import *

class MimicSkill(Skill):
	def __init__(self, arg=None):
		self.arg = None

	def execute(self, arg, linus):
		linus.sendOutput(arg)
		return arg 