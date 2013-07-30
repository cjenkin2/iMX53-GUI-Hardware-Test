class TestEntry():
    def __init__(self, name, action, status="Incomplete", logfile=None, strpad=10):
        self.name = name
        self.action = action
        self.status = status
        self.logging = (logfile == None)
        self.logfile = logfile
        
        # bad separation of concerns
        # but it gets the job done
        self.strpad=strpad 

    def getStr(self):
        return self.name + "\t(" + self.status + ")"
