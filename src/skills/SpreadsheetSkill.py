import gspread
import sys
sys.path.insert(0, '../storage')
sys.path.insert(0, '..')
from StorageAccesser import *
from Skill import *
from TextToIntSkill import *
from oauth2client.service_account import ServiceAccountCredentials
from defaults import *

class SpreadsheetSkill(Skill):
	def __init__(self, spreadSheetName = DEFAULT_SPREAD_SHEET_NAME, 
					   jsonFileName = DEFAULT_JSON_FILE_NAME):
		self.storage = StorageAccesser()
		self.scope = ['https://spreadsheets.google.com/feeds']
		self.spreadSheetName = spreadSheetName
		self.jsonFileName = self.storage.getFilePath(jsonFileName)
		self.creds = ServiceAccountCredentials.from_json_keyfile_name(self.jsonFileName, self.scope)
		self.client = gspread.authorize(self.creds)

		self.sheet = self.client.open(spreadSheetName).sheet1 #add more sheets if the file has more sheets
	
	def getAllValues(self):
		return self.sheet.get_all_values()

	def getAllRecords(self):
		return self.sheet.get_all_records()

	def findItem(self, key, values = None):
		if values == None:
			values = self.sheet.get_all_values()
		for i in range(0,len(values)):
			if key == values[i][0]:
				return i + 1
		return None

	def addValue(self, key, addValue, values=None):
		if values == None:
			values = self.sheet.get_all_values()
		location = self.findItem(key, values)
		self.editValue(key, values[i][1] + addValue, values)

	def editValue(self, key, newValue, values= None):
		if values == None:
			values = self.sheet.get_all_values()
		keyIndex = self.findItem(key, values)
		if keyIndex != None:
			self.sheet.update_cell(keyIndex, 2, newValue)
			return True
		return False

	def execute(self, arg, linus):
		return ""
