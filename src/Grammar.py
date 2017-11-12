from difflib import SequenceMatcher
class Grammar:
	def __init__(self, rules=[]):
		self.rules = rules

	def addRule(self, rule):
		self.rules += [rule]

	def similar(self, a, b):
		return SequenceMatcher(None, a, b).ratio()

	def findBestRule(self, tentativeRule):
		bestRule = ""
		bestSim = 0
		for rule in self.rules:
			value = self.similar(rule, tentativeRule)
			if(value > bestSim):
				bestRule = rule
				bestSim = value
		return bestRule