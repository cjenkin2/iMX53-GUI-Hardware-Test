#!/usr/bin/python

import sys
import subprocess

from Tkinter import *

from TestEntry import *

def mkTextPage(text, root):
    lines = text.splitlines()

    tkText = Text(root, wrap=WORD, width=reduce(max, map(len, lines))+1,
                  height=len(lines)+1)
    tkText.insert('end', text)
    tkText.config(state=DISABLED)
    return tkText

class AudioGUI(GUITest):
    def __init__(self, root, testInfo):
        GUITest.__init__(self, root, testInfo)

        self.createPg1()

    def proceedPart1(self):
        self.withdraw()
        self.pg1.grid_forget()

        # TODO parameterize?
        subprocess.call("./audio-01-pink", shell=True)

        self.createPg2()
        
        self.deiconify()

    def proceedPart2(self):
        #cleanup, logging from part 1
        self.withdraw()
        print "Part 1 of audio test finished: ", self.part1Status.get()

        if self.part1Status.get() == "normal":
            self.testInfo.status = "Success"
        else:
            self.testInfo.status = "Failure"

        self.destroy()

    def createPg1(self):
        # Text for first page
        tmptxt = """   This is a test of the i.MX53 audio input / output systems. There are three parts to the test.
You will be asked to report the results of each after each part finishes.

    The first part will play 'pink' noise for ~12 seconds. Pink noise is designed to sound as though 
no specific tone is being played. If you hear a distinct tone, or hear no noise at all, please report
this as an error.

    The second part will play a familiar sound clip. If the sound is distorted (or if there is no sound)
please report this as an error.

    The third and last part will record a short audio clip using the available audio input and then play
the clip back. Pleae speak or make some noise when you are prompted.

    To begin, press 'OK'. To return to the main menu, press 'Cancel'."""

        self.pg1 = Frame(self)
        
        pg1Text = mkTextPage(tmptxt, self.pg1)
        pg1Text.grid(row=0, column=0, columnspan=2)

        btnOK = Button(self.pg1, text="OK", command=self.proceedPart1) #TODO command
        btnOK.grid(row=1, column=0)
        btnCancel = Button(self.pg1, text="Cancel", command=self.destroy)
        btnCancel.grid(row=1, column=1)

        self.pg1.grid(row=0,column=0)

    def createPg2(self):
        self.pg2 = Frame(self)

        # radiobutton section
        pg2lb = Label(self.pg2, text="Indicate the outcome of the test by selecting one of the options below")
        pg2lb.grid(row=0, column=0, columnspan=3)

        self.part1Status = StringVar()
        self.part1Status.set("normal")

        pg2rsucc = Radiobutton(self.pg2, variable=self.part1Status, value="normal",
            text="Normal audio")
        pg2rsucc.grid(row=1, column=0)

        pg2rweird =Radiobutton(self.pg2, variable=self.part1Status, value="problem",
            text="Problems with audio")
        pg2rweird.grid(row=1, column=1)

        pg2rsilent=Radiobutton(self.pg2, variable=self.part1Status, value="none",
            text="No audio playback")
        pg2rsilent.grid(row=1, column=2)

        # text entry section
        pg2lb2 = Label(self.pg2, text="Please leave additional comments in the text area below")
        pg2lb2.grid(row=2, column=0, columnspan=3)

        self.pg2text = Text(self.pg2, wrap=WORD)
        self.pg2text.grid(row=3, column=0, columnspan=3)

        pg2btnSubmit = Button(self.pg2, text="Proceed", command=self.proceedPart2)
        pg2btnSubmit.grid(row=4, column=2)

        self.pg2.grid(row=0, column=0, columnspan=3)


class VideoGUI(GUITest):
    def __init__(self, root, testInfo):
        GUITest.__init__(self, root, testInfo)

        self.createPg1()

    def createPg1(self):
        tmptxt = """    This is a test of the i.MX53 video processing device (VPU).

    For this test a 30 second video clip will play. You will be asked to report the result 
after the clip is finished.

    To begin press press 'OK'. To return to the main menu press 'Cancel'."""

        self.pg1 = Frame(self)

        pg1text = mkTextPage(tmptxt, self.pg1)
        pg1text.grid(row=0, column=0, columnspan=2)

        btnOK = Button(self.pg1, text="OK", command=self.launchVideoTest)
        btnOK.grid(row=1, column=0)
        btnCancel = Button(self.pg1, text="Cancel", command=self.destroy)
        btnCancel.grid(row=1, column=1)

        self.pg1.grid(row=0, column=0, columnspan=2)

    def createPg2(self):
        self.pg2 = Frame(self)

        lbl1 = Label(self.pg2, text="Indicate the outcome of the test by selecting one of the options below")
        lbl1.grid(row=0, column=0, columnspan=3)

        pg2btnSubmit = Button(self.pg2, text="Proceed", command=self.proceedPart2)
        pg2btnSubmit.grid(row=4, column=2)

        self.pg2.grid(row=0, column=0)
        

    def launchVideoTest(self):
        # cleanup
        self.withdraw()
        self.pg1.grid_forget()

        subprocess.call("timeout 30 totem big_buck_bunny_720x576_surround.clip2.avi", shell=True)

        self.createPg2()
        self.deiconify()

    def proceedPart2(self):
        # cleanup
        self.withdraw()

        self.testInfo.status="Success"

        self.destroy()
        
class Dummy1(GUITest):
    def __init__(self, root, testInfo):
        GUITest.__init__(self, root, testInfo)

        lb = Label(self, text="Tests go here")
        lb.grid(row=0, column=0)
        btn = Button(self, text="OK", command=self.finishSuccess)
        btn.grid(row=0, column=1)

class Dummy2(GUITest):
    def __init__(self, root, testInfo):
        GUITest.__init__(self, root, testInfo)

        lb = Label(self, text="Tests go here")
        lb.grid(row=0, column=0)
        btn = Button(self, text="OK", command=self.finishFailure)
        btn.grid(row=0, column=1)
