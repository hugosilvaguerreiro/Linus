class Intent:
	def __init__(self, label=None):
		self.label = label
	def execute(self, linus, *arg):
		raise NotImplementedError