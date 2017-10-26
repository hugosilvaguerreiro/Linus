import gspread
from oauth2client.service_account import ServiceAccountCredentials
 
DEFAULT_SPREAD_SHEET_NAME = "sopareTest"
DEFAULT_JSON_FILE_NAME = "client_secret.json"

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

if __name__ == "__main__":
	try:
		manager = spreadSheetManager(DEFAULT_SPREAD_SHEET_NAME, DEFAULT_JSON_FILE_NAME)
		print(manager.getAllValues())
	except:
		print "Unable to create spreadsheet manager"