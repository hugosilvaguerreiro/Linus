import sys
sys.path.insert(0, '../storage')
sys.path.insert(0, '..')
import random
from textblob.classifiers import NaiveBayesClassifier
from Skill import *
from StorageAccesser import *
from defaults import *


class Classifier:
	def __init__(self, spam=0.7, path=DEFAULT_STORAGE_PATH, trainFiles="all"):
		self.spam = spam
		self.storage = StorageAccesser(path)
		self.trainFiles = trainFiles
		if self.trainFiles == "all":
			self.trainFiles = self.storage.getAllFilesByFormat(".train")
		self.classifier = self.trainClassifier()

	def trainClassifier(self):
		rawData = self.storage.readFileLines(self.trainFiles[0])
		train = self.extractTrainFileData(rawData)
		cl = NaiveBayesClassifier(train)
		for i in range(1, len(self.trainFiles)):
			rawData = self.storage.readFileLines(self.trainFiles[i])
			train = self.extractTrainFileData(rawData)
			cl.update(train)
		return cl

	def extractTrainFileData(self, rawData):
		label = rawData[1][3:-1]
		prefix = "\t> "
		train = []
		for i in range(2, len(rawData)):
			if rawData[i].startswith(prefix):
				train += [(rawData[i][3:-1], label)]
		return train

	def extractTrainResponsesFileData(self, rawData):
		label = rawData[1][3:-1]
		prefixIn = "\t> "
		prefixOut = "\t< < "
		train = {}
		currentPhrase = None

		for i in range(2, len(rawData)):
			if rawData[i].startswith(prefixIn):
				train[rawData[i][3:-1]] = []
				currentPhrase = rawData[i][3:-1]
			if rawData[i].startswith(prefixOut) and currentPhrase != None:
				train[currentPhrase] += [rawData[i][5:-1]]
		return train


	def classify(self, text):
		label = self.classifier.classify(text)
		prob = self.classifier.prob_classify(text)

		if prob.prob(label) < self.spam:
			return "spam"
		else:
			return label
		label = cl.classify(test)

	def execute(self, linus, text):
		return self.classify(text)



		