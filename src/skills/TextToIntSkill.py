from Skill import *

class TextToIntSkill(Skill):
	def __init__(self, arg=None):
		self.units = [
			"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
			"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
			"sixteen", "seventeen", "eighteen", "nineteen",
		]
		self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

		self.scales = ["hundred", "thousand", "million", "billion", "trillion"]
		self.arg = arg
		
	def findNumWords(self, text):
		prev = False
		out = []
		numwords = {}
		numwords["and"] = (1, 0)
		for idx, word in enumerate(self.units):    numwords[word] = (1, idx)
		for idx, word in enumerate(self.tens):     numwords[word] = (1, idx * 10)
		for idx, word in enumerate(self.scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)
		for word in text.split():
			if word in numwords:
				if prev:
					out[-1] += " " + word
				else:
					out += [word]
				prev = True
			else:
				prev = False
		return out

	def execute(self, textnum, linus):
		numwords = {}
		numwords["and"] = (1, 0)
		for idx, word in enumerate(self.units):    numwords[word] = (1, idx)
		for idx, word in enumerate(self.tens):     numwords[word] = (1, idx * 10)
		for idx, word in enumerate(self.scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

		current = result = 0
		for word in textnum.split():
			if word not in numwords:
			  raise Exception("Illegal word: " + word)

			scale, increment = numwords[word]
			current = current * scale + increment
			if scale > 100:
				result += current
				current = 0

		return result + current
	