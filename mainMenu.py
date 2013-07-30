#!/usr/bin/python

from Tkinter import *
from ttk import Treeview

from TestEntry import *

from HardwareTestGUIs import *

class GUIMainMenu(Frame):
    """Main menu for test of Genesi i.MX53 systems"""

    def __init__(self,master=None):
        """Initialize the base class"""
        Frame.__init__(self,master)

        """Set window title"""
        self.master.title("Select System Test")

        """System Tests"""
        self.createTestEntries()

        """Constants"""
        self.TEST_COL=0
        self.STATUS_COL=1
        self.TEXT_ROW=0
        self.TREEVIEW_ROW=1
        self.BUTTON_ROW=2

        """Display main window with padding"""
        self.grid()
        self.createWidgets()

    def createTestEntries(self):
        #TODO must be a better way. Pickle?
        self.tests = [TestInfo("Audio", AudioGUI), TestInfo("Clock", Dummy1),
                      TestInfo("Display", Dummy1), TestInfo("Keyboard", Dummy1),
                      TestInfo("Network", Dummy1), TestInfo("SSD", Dummy1),
                      TestInfo("Video", Dummy2)]
        self.testsLookup = {}
        for te in self.tests:
            self.testsLookup.update({te.name : te})

    def createWidgets(self):
        """Create all the initial widgets for this menu"""
        """Labels"""
        lbl = Label(self, text="Select test below", justify=LEFT)
        lbl.grid(row=self.TEXT_ROW, column=self.TEST_COL)
        
        """Tests"""
        self.trv = Treeview(self, columns=("Status"), displaycolumns='#all')

        for test in self.tests:
            treeviewInsertTest(self.trv, test)

        self.trv.column('#0', width=100)
        self.trv.heading('#0', text="Test")
        self.trv.heading('Status', text='Status')

        self.trv.grid(column=self.TEST_COL, row=self.TREEVIEW_ROW,
                      columnspan=2)

        """Buttons"""
        self.btnOK = Button(self, text="OK", command=self.launchTest)
        self.btnOK.grid(row=self.BUTTON_ROW, column=0)
        self.btnCancel = Button(self, text="Cancel", command=self.quit)
        self.btnCancel.grid(row=self.BUTTON_ROW, column=1)

    def launchTest(self):
        # get the item in focus
        testItem = self.trv.item(self.trv.focus())

        if not testItem['text'] == '':
            testInfo = self.testsLookup[testItem['text']]
            testInfo.launchTest(self)

    def processResults(self, testInfo):
        self.trv.item(testInfo.name, values=(testInfo.status),
                      tag=(testInfo.status))
        # update color notifications
        self.trv.tag_configure('Success', foreground='green')
        self.trv.tag_configure('Failure', foreground='red')

    def withdraw(self):
        """Helpful function to hide window"""
        self.master.withdraw()

    def deiconify(self):
        """Helpful function to restore window"""
        self.master.deiconify()


def treeviewInsertTest(trv, testInfo, pos='end'):
    """Add test to Treeview widget"""
    trv.insert("", pos, iid=testInfo.name,
               text=testInfo.name, values=(testInfo.status))

if __name__ == "__main__":
    root = Tk()
    mainMenu = GUIMainMenu(root)
    root.mainloop()
