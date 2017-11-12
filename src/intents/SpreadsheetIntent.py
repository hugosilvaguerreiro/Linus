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
from defaults import *
from Compiler import *

units = [
			"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
			"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen", "nineteen",
		]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
scales = ["hundred", "thousand", "million", "billion", "trillion"]

tags = {"remove":["remove", "take", "taking", "removing"],
		"add": ["add", "adding", "put", "putting", "place"],
		"find": ["is", "there", "find", "where", "do", "we", "have"],
		"number": units + tens + scales,
		"noun":[]
		}
rules = [ "remove number noun",
			"remove noun",
			"add number noun",
			"add noun",
			"find noun"
		]
class SpreadsheetIntent(Intent):
	def __init__(self, label=None, file=None, classifier = None):
		Intent.__init__(self, label, file, classifier)
		self.label = label
		self.spreadSheetSkill = SpreadsheetSkill()
		self.values = self.spreadSheetSkill.getValues()
		for value in self.values:
			tags["noun"] += value[0].split()
		self.compiler = Compiler(tags, Grammar(rules))
		self.text2int = TextToIntSkill()
	#def add(self, order):

	#def find(self, order):
	def add(self, order):
		value = 0
		noun = None
		if len(order) == 1 and order[0][0] == "noun":
			value = 1
			noun = order[0][1]
		elif len(order) == 2 and order[0][0] == "number":
			if not order[0][1].isdigit():
				value = self.text2int.execute(order[0][1])
			else:
				value = eval(order[0][1])
			noun = order[1][1]
		if(noun != None):
			self.spreadSheetSkill.addValue(noun, value, self.values)
			return "adding " + str(value) + " " + noun + " to the inventory"
		else:
			return "Sorry. i could not complete your add request"

	def remove(self, order):
		value = 0
		noun = None
		if len(order) == 1 and order[0][0] == "noun":
			value = 1
			noun = order[0][1]
		elif len(order) == 2 and order[0][0] == "number":
			if not order[0][1].isdigit():
				value = self.text2int.execute(order[0][1])
			else:
				value = eval(order[0][1])
			print(value)
			noun = order[1][1]
		if( noun != None):
			self.spreadSheetSkill.addValue(noun, -1*value, self.values)
			return "removing " + str(value) + " " + noun + " from the inventory"
		else:
			return "Sorry. i could not complete your removal request"

	def execute(self, linus, inputReceived):
		simpleCompiledText = self.compiler.compile(inputReceived)
		if len(simpleCompiledText) > 0:
			order = simpleCompiledText[0][0]
			if order == "remove":
				return self.remove(simpleCompiledText[1:])
			if order == "add":
				return self.add(simpleCompiledText[1:])
		return "Sorry. i did not understand your spreadsheet request"

