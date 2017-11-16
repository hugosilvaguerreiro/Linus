import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
from Intent import *
from StorageAccesser import *
from defaults import *
from random import randint

class BadWordIntent(Intent):
	def __init__(self, label=None, file=None, classifier=None):
		Intent.__init__(self, label, file, classifier)
		self.label = label
		self.classifier = classifier
		self.storageAccesser = StorageAccesser(DEFAULT_STORAGE_PATH)

	def execute(self, linus, inputReceived):
		return self.respond(inputReceived)