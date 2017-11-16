import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
from Intent import *
from StorageAccesser import *
from defaults import *

class EmotionIntent(Intent):
	"""@params:
			string: label - The label given to this intent
			string: file - Filename of the train file of this intent
			Classifier: classifier - A classifier to access the data of the train file
	"""
	def __init__(self, label=None, file=None, classifier=None):
		Intent.__init__(self, label, file, classifier) # calls the super method to initialize it
		self.label = label #label is the label of this intent
		self.classifier = classifier #Classifier is used to extract data from .train files and to classify inputs
		self.storageAccesser = StorageAccesser(DEFAULT_STORAGE_PATH) #storageAccesser is used to access/read/write files from the storage

	def execute(self, linus, inputReceived):
		return self.respond(inputReceived) #respond is implemented in the class Intent