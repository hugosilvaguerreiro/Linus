class Linus:
    def __init__(self, inputMethod, outputMethod, plugins):
        self.inputMethod = inputMethod
        self.outputMethod = outputMethod
        self.plugins = list(plugins)

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

    def applyPlugins(self, inputReceived):
        outputsAfterApplyingPlugins = []

        for plugin in self.plugins:
            outputsAfterApplyingPlugins.append(plugin.execute(inputReceived, self))

        return outputsAfterApplyingPlugins


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
            pluginsOutput = self.applyPlugins(inputReceived)