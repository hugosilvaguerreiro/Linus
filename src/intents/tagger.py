from difflib import SequenceMatcher
from Grammar import *
class Tagger:
	"""tags: dictionary of the form {tag1: [<word1>,<word2>,...,<wordn>], ..., tagn: ...}"""
	def __init__(self, tags):
		self.tags = tags

	def tagText(self, rawText):
		text = rawText.split()
		previousTag = ""
		result = []
		for word in text:
			for i in self.tags:
				if word in self.tags[i]:
					if previousTag == i:
						result[-1][1] += " " + word
					else:
						previousTag = i
						result += [[i, word]]
		return result

	def parseGrammar(self, Grammar, taggedText):
		rule = ""
		result = []
		for tag in taggedText:
			rule += tag[0] +  " "
		rule = rule[0:-1]
		start = 0
		bestRule = Grammar.findBestRule(rule)
		bestRule = bestRule.split()
		for tag in bestRule:
			for i in range(start, len(taggedText)):
				if(tag == taggedText[i][0]):
					result += [taggedText[i]]
					start = i + 1
					break
		return result

