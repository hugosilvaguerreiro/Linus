import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
sys.path.insert(0, '../tools')
from Intent import *
from Classifier import *
from GreetIntent import *
from SpreadsheetIntent import *
from EmotionIntent import *
from SpamIntent import *
from HumourIntent import *
from BadWordIntent import *
from StorageAccesser import *


class IntentDecoder(Intent):
	def __init__(self, label=None ,file=None):
		Intent.__init__(self, label, file)
		self.label = label
		self.storageAccesser = StorageAccesser()
		self.classifier = Classifier()
		self.intents = {"greet": GreetIntent("greet", "greetings.train", self.classifier), 
						"spreadsheet" : SpreadsheetIntent("spreadsheet", "spreadsheet.train", self.classifier),
						"humour": HumourIntent("humour", "humour.train", self.classifier),
						"badWord": BadWordIntent("badWord", "badWord.train", self.classifier),
						"spam" : SpamIntent("spam")}

	def execute(self, linus, inputReceived):
		label = self.classifier.classify(inputReceived)
		return self.intents[label]

