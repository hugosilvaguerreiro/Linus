from Output import *
import subprocess

class VoiceOutput:
	def __init__(self, arg=None):
		self.arg = None
		
	
	def sendOutput(self, arg):
		print(arg)
		subprocess.call(["espeak", "-s", " 180", "-p", "25","-a","70", arg])