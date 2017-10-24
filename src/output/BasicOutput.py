from Output import *

class BasicOutput(Output):
	def __init__(self, arg=None):
		self.arg = None
	
	def sendOutput(self, arg):
		print(arg)