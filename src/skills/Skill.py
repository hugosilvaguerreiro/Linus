
class Skill:
	def __init__(self, arg=None):
		self.arg = arg

	def execute(self, linus, *arg):
		raise NotImplementedError