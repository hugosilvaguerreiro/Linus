from difflib import SequenceMatcher
from Grammar import *
class Tagger:
	"""tags: dictionary of the form {tag1: [<word1>,<word2>,...,<wordn>], ..., tagn: ...}"""
	def __init__(self, tags):
		self.tags = tags

	def tagText(self, rawText, hasNumber = True):
		text = rawText.split()
		previousTag = ""
		result = []
		for word in text:
			print(word)
			if hasNumber and word.isdigit():
				if previousTag == "number":
						result[-1][1] += " " + word
				else:
					previousTag = "number"
					result += [["number", word]]
			else:
				for i in self.tags:
					if word in self.tags[i]:
						if previousTag == i:
							result[-1][1] += " " + word
						else:
							previousTag = i
							result += [[i, word]]				


		print(result)
		return result

	

