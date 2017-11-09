import sys
sys.path.insert(0, '../skills')
sys.path.insert(0, '../storage')
sys.path.insert(0, '..')
from Intent import *
from SpreadsheetSkill import *
from ClassifierSkill import *
from TextToIntSkill import *
from StorageAccesser import *
from defaults import *

class SpreadsheetIntent(Intent):
	def __init__(self, label=None, classifier = None):
		self.label = label
		#self.spreadSheetSkill = SpreadsheetSkill()
		self.classifier = ClassifierSkill(0.2, DEFAULT_STORAGE_PATH + "spreadsheetCommands/")
		self.storageAccesser = StorageAccesser(DEFAULT_STORAGE_PATH + "spreadsheetCommands/")

	def add(self, inputReceived):
		text2int = TextToIntSkill()
		rawData = self.storageAccesser.readFileLines("add.train")
		data = self.classifier.extractTrainFileData(rawData)
		inputReceived = inputReceived.split()
		for i in range(len(inputReceived)):
			if inputReceived[i] in data:
				break
		while text2int.isNumber(inputReceived[i]):
			i += 1
		item =  inputReceived[i:]
		numbers = text2int.findNumWords(inputReceived)
		if len(numbers) == 0:
			number = 1
		else:
			for num in numbers:
				number += text2int.execute(num)
		self.spreadSheetSkill.addValue(item, number)
		return item + " updated on the inventory"

	# def remove(self, inputReceived):
	# 	text2int = TextToIntSkill()
	# 	inputReceived = inputReceived.split()
	# 	for i in range(len(inputReceived)):
	# 		if inputReceived[i] == 
	# 	numbers = text2int(inputReceived)

	def find(self, inputReceived):
		return None
	def execute(self, linus, inputReceived):
		label = self.classifier.classify(inputReceived)
		print label
		if label == "add":
			self.add(inputReceived)
		elif label == "remove":
			#self.remove(inputReceived)
			return None
		else:
			return None