##STOPWATCH 3.0
##
##CREATED BY SIDDHARTH KANNAN
##
##WRITTEN ON PYTHON 2.7 AND TKINTER 8.5
##
##OS:WINDOWS XP SP 3


##     This program is free software. It comes without any warranty, to
##     the extent permitted by applicable law. You can redistribute it
##     and/or modify it under the terms of the Do What The Fuck You Want
##     To Public License, Version 2, as published by Sam Hocevar. See
##     http://www.wtfpl.net/ for more details.


from Tkinter  import *
from time import *
from tkFont import *
import tkMessageBox
import tkSimpleDialog
import datetime
now = datetime.datetime.now()

FRAME_WIDTH,FRAME_HEIGHT = 600,700    

class stopwatch(object):
    def __init__(self):
        self.window = Tk()  ##The main window instance
        self.window.title("STOPWATCH")

        
        self.firstTime = True ##Variable keeps track of whether this is the first time that the application is being run

        ##Some fonts for use inside
        self.small = Font(family='Helvetica',size=11)
        self.medium = Font(family='Helvetica',size=15)
        self.big = Font(family='Helvetica',size=24)
        self.veryBig = Font(family='Helvetica',size=72)

        ##Varibales taking care of the check buttons

        self.shown = BooleanVar()

        self.shown.set(True)  ##Pop up shown variable

        self.timeShown  = BooleanVar()

        self.timeShown.set(True)  ##The timing is shown or not

        self.quitted = False

        self.initFrame()

    def createMenu(self,event=None):

        menubar = Menu(self.window)

        filemenu = Menu(menubar,tearoff = 0)

        filemenu.add_command(label='Start',command=self.startrunning,accelerator='S')
        filemenu.add_command(label='Stop',command=self.stoprunning,accelerator='E')
        filemenu.add_command(label='Lap',command=self.endlap,accelerator='L')
        filemenu.add_command(label='Reset',command=self.reset,accelerator='R')
        filemenu.add_command(label='Quit',command=self.quitwin,accelerator='Escape')

        optionsmenu = Menu(menubar,tearoff=0) 

        optionsmenu.add_checkbutton(label='Show timing after the run is completed',command=self.togglePopUp,variable=self.shown,onvalue = True,offvalue = False)
        optionsmenu.add_checkbutton(label='Show the stopwatch running',variable=self.timeShown,onvalue=True,offvalue=False)
        
        helpmenu = Menu(menubar,tearoff=0)

        helpmenu.add_command(label='Help',command=self.showHelp)
        helpmenu.add_command(label='About',command=self.showCredits)

        menubar.add_cascade(label='File',menu=filemenu)
        menubar.add_cascade(label='Options',menu=optionsmenu)
        menubar.add_cascade(label='Help',menu=helpmenu)

        self.window.config(menu=menubar)

    def initFrame(self):

        try:
            self.frame.destroy()

        except AttributeError:
            pass
        
        self.frame = Frame(self.window,width=FRAME_WIDTH,height=FRAME_HEIGHT)  ##The frame instance
        self.frame.pack_propagate(0)  ##Making sure that the window does not shrink
        
        self.frame.pack(fill=None)
        self.initVariables()
        self.initBindings()
        self.createMenu()
        self.initUI()

    def initVariables(self,event=None):

        ##VARIABLES:
        
        self.start = None
        self.stop = None
        self.timeConsumed = None
        self.laps = []
        self.startOfLap = None
        self.endOfLap = None
        self.counterOfLaps = 1

    def initBindings(self,event=None):

        w = self.window

        w.bind('s',self.startrunning)
        w.bind('e',self.stoprunning)
        w.bind('r',self.reset)
        w.bind('l',self.endlap)
        w.bind('<Escape>',self.quitwin)

    def initHelp(self):
        f = self.frame

        info = Message(f,text="You can use the buttons below or \
you can use the following keyboard shortcuts to work with the stopwatch\
                            \n\nPress \'S\' to start running. \
                            \nPress \'E\' to stop running. \
                            \nPress \'R\' to reset the stopwatch. \
                            \nPress \'L\' to end a lap. \
                            \n\nPress escape button to quit this stopwatch\
                            Please note that all the times generated are \
                            being stored in a file \'timings.txt\' from which you can see the timings later.\n\
                            \n\nYou can see this help again by clicking on the help tab in the menu.",\
                            font=self.medium)
        info.pack() 
        
    def initUI(self):

        f = self.frame

        if self.firstTime:
            self.initHelp()
            self.firstTime = False

        start = Button(f,text='START',command=self.startrunning)
        start.pack(side="top")

        stop =Button(f,text='STOP',command=self.stoprunning)
        stop.pack(side="top")

        lap = Button(f,text='LAP',command=self.endlap)
        lap.pack(side='top')

        reset = Button(f,text="RESET",command = self.reset)
        reset.pack(side="top")

        close = Button(f,text="QUIT",bg="black",fg = "red",command=self.quitwin)
        close.pack(side="top")

        ##Changing the font to increase the size of the buttons

        buttons = [start,stop,close,reset,lap]

        for i in buttons:
            i.config(font=self.medium)       

    def startrunning(self,event=None):

        self.reset()

        self.runTime = Frame(self.frame)
        self.runTime.pack()  ##this frame will show the present run time

        self.start = time()
        self.startOfLap = time()

        if self.timeShown.get():

            self.initRunTimeFrame()
        
        r = Frame(self.frame)
        r.pack()

        start = Label(r,text="\nStarted running")
        start.pack()


    def initRunTimeFrame(self,t = ' '):
        
        self.timing = Label(self.runTime,text="",font=self.veryBig)

        self.timing.pack(side='top')

        self.updateRunTimeFrame()

    def updateRunTimeFrame(self):

        t = time()

        now = ' %0.2f' %(t - self.start) 

        self.timing.configure(text=now)

        self.runTime.after(1,self.updateRunTimeFrame)
                

    def stoprunning(self,event=None):
        
        r = Frame(self.frame)
        r.pack()
        self.stop = time()
        self.timeConsumed = self.stop - self.start

        self.runTime.destroy()

        self.timing = Label(r,text='%0.2f' %(self.timeConsumed),font=self.veryBig)

        self.timing.pack(side='top')

        Label(r,text='\nstopped running').pack()
        end = Label(r,text="\nTime consumed is: %0.2f seconds" %self.timeConsumed)
        end.pack(side = "bottom")

        if self.shown.get():
            tkMessageBox.showinfo('Summary of this run','The run was completed in %0.2f seconds' %self.timeConsumed)

        self.writeDataToFile()
        self.initVariables()

    def togglePopUp(self,event=None):
        if self.shown.get():
            tkMessageBox.showinfo('Message','Pop up after run has been switched on')
        else:
            tkMessageBox.showinfo('Message','Pop up after run has been switched off')

    def writeDataToFile(self,event=None):

        inputFile = open('timings.txt','a')

        for i in range(60):
            inputFile.write('-')

        dateNow = 'Date:' + str(now.day) + '-' + str(now.month) + '-' \
                  + str(now.year) \
                  + ', ' + 'Time:' + str(now.hour) + ':' + str(now.minute) \
                  + ':' + str(now.second)

        inputFile.write('\n\n' + dateNow + '\n\n')

        for i in range(len(self.laps)):
            inputFile.write('Lap ' + str(i+1) + ': ' + str('%0.2f' %self.laps[i]) + ' seconds\n')

        if len(self.laps) == 0:
            inputFile.write('No laps recorded')

        inputFile.write('\nSummary of this run:'+str(' %0.2f' %self.timeConsumed) + ' seconds' + '\n')

    def reset(self,event=None):
        self.frame.destroy()

        self.initFrame()

    def endlap(self,event=None):
        self.endOfLap = time()
        timeTakenForOneLap = self.endOfLap - self.startOfLap

        self.laps.append(timeTakenForOneLap)

        r = Label(self.frame,text="Lap " + str(self.counterOfLaps) +" was completed in %0.2f" %timeTakenForOneLap)
        r.pack()
        self.counterOfLaps += 1

        self.startOfLap = time()

        if self.counterOfLaps % 9 == 0:
            self.frame.pack_propagate(1)

    

    def showHelp(self,event=None):

        tkMessageBox.showinfo('Help','Application that emulates a stopwatch with lap timing facility\
                                        \nCopyright(c) 2013 Siddharth Kannan')

        self.firstTime = True

        self.initFrame()

        
    def quitwin(self,event=None):
        self.window.destroy()

        self.window2 = Tk()
        self.window2.title('License and Credits')


        self.window2.bind('<Escape>',self.exit)

        self.frame =Frame(self.window2)
        self.frame.pack()

        self.r = Frame(self.frame)
        self.r.pack()

        r = self.r

        self.big = Font(family='Helvetica',size=24)

        m = Message(r,text="Created by Siddharth Kannan\
                          \nWritten on Python 2.7 and Tkinter 8.5\
                          \nOS: WINDOWS XP SP 3\
                          \nThis software is licensed under the WTFPL license.\
                          \nSee the copying file for more details.\
                          \nPress the quit button below to quit the application\
                          ",font=self.big)

        m.pack()

        b = Button(r,text='QUIT',fg='red',bg='black',command=self.window2.destroy,font=self.big)
        b.pack(side='bottom') 

    def showCredits(self,event=None):

        self.window1 = Tk()
        self.window1.title('License and Credits')
        
        self.frame =Frame(self.window1)
        self.frame.pack()

        self.r = Frame(self.frame)
        self.r.pack()

        r = self.r

        self.big = Font(family='Helvetica',size=24)

        m = Message(r,text="Created by Siddharth Kannan\
                          \nWritten on Python 2.7 and Tkinter 8.5\
                          \nOS: WINDOWS XP SP 3\
                          \nThis software is licensed under the WTFPL license.\
                          \nSee the copying file for more details.\
                          ",font=self.big)

        m.pack()

        b = Button(r,text='OKAY',font=self.big,command=self.window1.destroy)
        b.pack(side='bottom')


    def exit(self,event=None):
        """the function that will kill all the processes and end the application"""

        self.window2.destroy()


stopwatch()
mainloop()
