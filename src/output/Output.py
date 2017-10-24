class Output:
	def __init__(self, arg=None):
		self.arg = None
	
	def sendOutput(self, arg):
		raise NotImplementedError
