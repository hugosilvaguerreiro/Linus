import sys
sys.path.insert(0, './input')
sys.path.insert(0, './output')
sys.path.insert(0, './intents')
sys.path.insert(0, './skills')
sys.path.insert(0, './storage')
sys.path.insert(0, './tools')

import speech_recognition as sr
import pyttsx
from Linus import *
from BasicOutput import *
from VoiceOutput import *
from RawInput import *
from MicrophoneInput import *
from IntentDecoder import *

linusInputMethod = RawInput()
#linusInputMethod = MicrophoneInput()
# #linusOutputMethod = BasicOutput()
linusOutputMethod = VoiceOutput()
linusIntentDecoder = IntentDecoder()
linus = Linus(linusInputMethod, linusOutputMethod, linusIntentDecoder)

linus.loop()