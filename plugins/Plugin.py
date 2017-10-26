
class Plugin:
	def __init__(self, arg=None):
		self.arg = None

	def execute(self, arg):
		raise NotImplementedError