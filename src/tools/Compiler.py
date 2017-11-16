from Tagger import *
from Grammar import *

class Compiler:
	def __init__(self, tags, Grammar):
		self.grammar = Grammar
		self.tagger = Tagger(tags)

	def parseGrammar(self, taggedText):
		rule = ""
		result = []
		for tag in taggedText:
			rule += tag[0] +  " "
		rule = rule[0:-1]
		start = 0
		bestRule = self.grammar.findBestRule(rule)
		bestRule = bestRule.split()
		for tag in bestRule:
			for i in range(start, len(taggedText)):
				if(tag == taggedText[i][0]):
					result += [taggedText[i]]
					start = i + 1
					break
		return result

	def compile(self, text):
		text = text.lower()
		taggedText = self.tagger.tagText(text)
		return self.parseGrammar(taggedText)