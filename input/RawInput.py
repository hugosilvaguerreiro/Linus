from Input import *

class RawInput(Input):
	def __init__(self, arg="Enter your message\n"):
		self.arg = arg

	def input(self):
		return raw_input(self.arg)
