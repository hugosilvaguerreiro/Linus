from Intent import *

class SpamIntent(Intent):
	def __init__(self, label=None):
		self.label = label
	def execute(self, linus, *arg):
		return None