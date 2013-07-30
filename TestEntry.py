from Tkinter import *

class TestInfo():
    def __init__(self, name, guiTest, status="Incomplete", logfile=None):
        self.name = name
        self.guiTest = guiTest
        self.status = status
        self.logging = (logfile == None)
        self.logfile = logfile

    def launchTest(self, root):
        root.withdraw()
        self.guiTest(root, self)
        # left to guiTest to reiconify

class GUITest(Toplevel):
    def __init__(self, root, testInfo):
        Toplevel.__init__(self)
        
        self.master = root
        self.testInfo = testInfo

    def cleanup(self):
        # report progress to master
        # then return focus to main menu
        self.master.processResults(self.testInfo)
        self.master.deiconify()

    def destroy(self):
        self.cleanup()
        Toplevel.destroy(self)

    def quit(self):
        self.cleanup()
        Toplevel.quit(self)

    def finishSuccess(self):
        self.testInfo.status="Success"
        self.destroy()

    def finishFailure(self):
        self.testInfo.status="Failure"
        self.destroy()
