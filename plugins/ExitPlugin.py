from Plugin import *

class ExitPlugin(Plugin):
	def __init__(self, arg=None):
		self.arg = None

	def execute(self, arg):
		if "exit" in arg:
			exit()
		return " "