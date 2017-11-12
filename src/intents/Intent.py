
from difflib import SequenceMatcher
from random import randint

class Intent:
	def __init__(self, label=None, file=None, classifier= None):
		self.label = label
		self.file = file
		self.classifier = classifier
	def respond(self, inputReceived):
		rawData = self.storageAccesser.readFileLines(self.file)
		data = self.classifier.extractTrainResponsesFileData(rawData)
		bestOption = ""
		bestOptionSimilarity = 0
		for option in data:
			value = self.similar(option, inputReceived)
			if value > bestOptionSimilarity:
				bestOption = option
				bestOptionSimilarity = value

		return data[bestOption][randint(0, len(data[bestOption] ) - 1)]
	def similar(self, a, b):
		return SequenceMatcher(None, a, b).ratio()

	def execute(self, linus, *arg):
		raise NotImplementedError