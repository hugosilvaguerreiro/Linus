import gspread
from Plugin import *
from oauth2client.service_account import ServiceAccountCredentials
 
DEFAULT_SPREAD_SHEET_NAME = "sopareTest"
DEFAULT_JSON_FILE_NAME = "client_secret.json"



class SpreadSheetPlugin(Plugin):
	def __init__(self, arg=None):
		self.arg = None
		self.manager = spreadSheetManager(DEFAULT_SPREAD_SHEET_NAME, DEFAULT_JSON_FILE_NAME)

	#command format
	def execute(self, arg, linus):
		commands = arg.split()
		if "spreadsheet" in commands or "inventory" in commands:
			if "list" in commands:
				linus.sendOutput("Do you want me to read the list?")
				linusIn = linus.getInput()
				while linusIn not in ["yes", "no"]:
					linus.sendOutput("Please respond with yes or no ")
					linusIn = linus.getInput()
				if linusIn == "yes":
					listOfThings = self.manager.getAllValues()
					linus.sendOutput("In your spreadsheet you have")
					for thing in listOfThings:
						linus.sendOutput(str(thing[0]) + " " + str(thing[1]))
		return ""


class spreadSheetManager:
	def __init__(self, spreadSheetName, jsonFileName):
		self.scope = ['https://spreadsheets.google.com/feeds']
		self.spreadSheetName = spreadSheetName
		self.jsonFileName = jsonFileName
		self.creds = ServiceAccountCredentials.from_json_keyfile_name(jsonFileName, self.scope)
		self.client = gspread.authorize(self.creds)

		self.sheet = self.client.open(spreadSheetName).sheet1 #add more sheets if the file has more sheets

	def getAllValues(self):
		return self.sheet.get_all_values()

	def getAllRecords(self):
		return self.sheet.get_all_records()

	def editValue(self, key, newValue):
		self.sheet.update_cell(1, 1, "test") #TODO
		return None
