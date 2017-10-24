from Output import *
import pyttsx


class VoiceOutput:
	def __init__(self, arg=None):
		self.arg = None
		
	
	def sendOutput(self, arg):
		engine = pyttsx.init()
		engine.say(arg)
		engine.runAndWait()