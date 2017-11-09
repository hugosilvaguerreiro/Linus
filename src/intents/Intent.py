
from difflib import SequenceMatcher

class Intent:
	def __init__(self, label=None):
		self.label = label

	def similar(self, a, b):
		return SequenceMatcher(None, a, b).ratio()

	def execute(self, linus, *arg):
		raise NotImplementedError