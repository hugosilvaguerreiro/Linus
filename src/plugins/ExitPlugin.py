from Plugin import *

class ExitPlugin(Plugin):
	def __init__(self, arg=None):
		self.arg = None

	def execute(self, arg, linus):
		if "exit" in arg:
			linus.sendOutput("goodbye master")
			exit()
		return " "