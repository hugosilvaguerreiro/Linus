import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
from Intent import *
from StorageAccesser import *
from defaults import *


class GreetIntent(Intent):
	def __init__(self, label=None, file=None, classifier=None):
		Intent.__init__(self, label, file, classifier)
		self.classifier = classifier
		self.storageAccesser = StorageAccesser(DEFAULT_STORAGE_PATH)

	def execute(self, linus, inputReceived):
		return self.respond(inputReceived)