import sys
sys.path.insert(0, '..')
from defaults import *
from os import listdir
from os.path import isfile, join


class StorageAccesser:
	def __init__(self, path=DEFAULT_STORAGE_PATH):
		self.path = path
	def getFilePath(self, file):
		return self.path + file
	def getAllFiles(self):
		return [f for f in listdir(self.path) if isfile(join(self.path, f))]

	def getAllFilesByFormat(self, sufix):
		allFiles = self.getAllFiles()
		out = []
		for file in allFiles:
			if file.endswith(sufix):
				out += [file]
		return out

	def readFileLines(self, fileName):
		file = open(self.path +fileName, "r")
		data = file.readlines()
		file.close()
		return data