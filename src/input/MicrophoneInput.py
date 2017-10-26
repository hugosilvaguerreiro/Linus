from Input import *
import speech_recognition as sr

class MicrophoneInput(Input):
	def __init__(self, arg="Enter your message\n", timeout=3, phraseTimeLimit=10):
		self.arg = arg
		self.energy_threshold = 4000
		self.recognizer = sr.Recognizer()
		self.recognizer.dynamic_energy_threshold = False
		self.recognizer.energy_threshold = self.energy_threshold
		self.source = sr.Microphone()
		self.timeout = timeout;
		self.phraseTimeLimit = phraseTimeLimit;

	def recognize(audio):
		self.recognizer.recognize_sphinx(audio)
		
	def listen(self, source):
		return self.recognizer.listen(source, timeout= self.timeout, phrase_time_limit= self.phraseTimeLimit)

	def increaseThreshold():
		self.energy_threshold += 100
		self.recognizer.energy_threshold = self.energy_threshold
	def decreaseThreshold():
		if(self.energy_threshold > 200):
			self.recognizer.energy_threshold

	def input(self):

		r = self.recognizer
		r.dynamic_energy_threshold = False
		r.energy_threshold = 4000


		with self.source as source:
			try:
				audio = self.listen(source)
				try:
					print "recognizing..."
					msg =  r.recognize_google(audio)
				except sr.UnknownValueError:
					msg = "Sphinx could not understand audio"
				except sr.RequestError as e:
					msg = "Sphinx error; {0}".format(e)
				return msg
			except sr.WaitTimeoutError:
				print("passing...")
				return "passing"
