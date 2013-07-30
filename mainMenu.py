#!/usr/bin/python

from Tkinter import *
from ttk import Treeview

from TestEntry import *

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
        self.tests = [TestEntry("Audio", None), TestEntry("Clock", None),
                      TestEntry("Display", None), TestEntry("Keyboard", None),
                      TestEntry("Network", None), TestEntry("SSD", None),
                      TestEntry("Video", None)]

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
        self.btnOK = Button(self, text="OK", command=None)
        self.btnOK.grid(row=self.BUTTON_ROW, column=0)
        self.btnCancel = Button(self, text="Cancel", command=self.quit)
        self.btnCancel.grid(row=self.BUTTON_ROW, column=1)
        

def treeviewInsertTest(trv, testEntry, pos='end'):
    """Add test to Treeview widget"""
    trv.insert("", pos, text=testEntry.name, values=(testEntry.status),
               tag=testEntry.name)

if __name__ == "__main__":
    mainMenu = GUIMainMenu()
    mainMenu.mainloop()
