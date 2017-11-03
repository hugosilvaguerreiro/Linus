import sys
sys.path.insert(0, '../skills')
from Intent import *

class GreetIntent(Intent):
	def __init__(self, storageAccesser, label=None):
		self.label = label

	def execute(self, linus, *arg):
		return "hi"