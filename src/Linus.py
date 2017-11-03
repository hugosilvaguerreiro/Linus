class Linus:
    def __init__(self, inputMethod, outputMethod, intentDecoder):
        self.inputMethod = inputMethod
        self.outputMethod = outputMethod
        self.intentDecoder = intentDecoder
        self.errorMsg = {"NotImplementedIn": "ERROR: THE INPUT METHOD IS NOT VALID",
                         "NotImplementedOut": "ERROR: THE INPUT METHOD IS NOT VALID",
                         "IOErrorIn": "ERROR: CANNOT RECEIVE INPUT", 
                         "IOErrorOut": "ERROR: CANNOT OUTPUT THE MESSAGE"}

    def getInput(self):
        try:
            return self.inputMethod.input()
        except IOError:
            return self.errorMsg["IOErrorIn"]
        except  NotImplementedError:
            return self.errorMsg["NotImplementedIn"]

    def sendOutput(self, msg):
        try:
            self.outputMethod.sendOutput(msg)
        except IOError:
            return self.errorMsg["IOErrorOut"]
        except  NotImplementedError:
            return self.errorMsg["NotImplementedOut"]

    def loop(self):
        while True:
            inputReceived = self.getInput()
            intent = self.intentDecoder.execute(self, inputReceived)
            output = intent.execute(self, inputReceived)
            if(output != None):
                self.sendOutput(output)
            else:
                self.sendOutput("sorry i could not understand")