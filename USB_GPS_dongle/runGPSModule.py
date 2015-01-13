#Nathan Neibauer
#runGPSModule.py

from Tkinter import *
from tkFileDialog import *
import time

import GPGGA as gps
import fileOps as store
import serialCom as com

#App class, runs everything and stores local values
class App(object):
	#Initialize the window, most of what is scene here is window layout and a few variable initialization. Storing the dataset, and whether it's collecting data or not
	def __init__(self, master):
		self.master = master
		self.ser = com.serObject()
		self.frame = Frame(master)
		self.frame.pack()
		self.master.title("GPS Data Collection")

		self.pbox = Text(self.frame, height = 1, width = 10)
		self.tbox = Text(self.frame, height = 10, width = 100)
		self.errorBox = Text(self.frame, height = 5, width = 100)
		self.labelPoints = Label(self.frame, text = "Number of Points:")
		self.labelError = Label(self.frame, text = "Error/Notice Messages:")
		self.labelData = Label(self.frame, text = "Current Data Points:")
		self.runningb = Button(self.frame, text = "Start", command = self.start)
		self.connectb = Button(self.frame, text = "Connect", command = self.connect)
		self.saveb = Button(self.frame, text = "Save", command = self.saveData)
		self.openb = Button(self.frame, text = "Open", command = self.openFile)
		self.clearb = Button(self.frame, text = "Clear", command = self.clearData)
		self.refineb = Button(self.frame, text = "Refine", command = self.refineData)
		self.refScale = Scale(master, from_ = 0, to = 100, label = "Refine to % of Points", orient = HORIZONTAL, length = 160)
		self.plotb = Button(self.frame, text = "Plot 3D Data", command = self.plotData)

		self.pbox.grid(column = 1, row = 4)
		self.errorBox.grid(column = 2, row = 6, rowspan = 2)
		self.tbox.grid(column = 2, row = 1, rowspan = 4)
		self.labelPoints.grid(column = 0, row = 4)
		self.labelError.grid(column = 2, row = 5)
		self.labelData.grid(column = 2, row = 0)
		self.runningb.grid(column = 0, row = 0)
		self.connectb.grid(column = 1, row = 0)
		self.saveb.grid(column = 0, row = 1)
		self.openb.grid(column = 1, row = 1)
		self.clearb.grid(column = 0, row = 2)
		self.refineb.grid(column = 1, row = 2)
		self.refScale.pack(side = LEFT)
		self.plotb.grid(column = 0, row = 3)

		self.runWhile = False
		self.connected = False
		self.current = gps.GPGGA()
		self.setState()

	#The setState function -> It tests whether the device is connected, as well as testing whether data is being collected. Based on whether it's connected or collecting, it disables or activates the buttons and interactions in the GUI interface. This function is called at the end of EVERY other function in this class, as in we are resetting the state EVERY TIME anything happens - this also means that the setState function cannot call any other functions in the class for risk of causing infinite recursion
	def setState(self):
		self.connected = self.ser.verify()
		default = ['disabled']*8
		buttonDict = {0:self.runningb.config, 1:self.connectb.config, 2:self.saveb.config, 3:self.openb.config, 4:self.clearb.config, 5:self.refineb.config, 6:self.plotb.config, 7:self.refScale.config}
		if(not self.connected):
			default[1] = 'active'
			if(self.runWhile):
				self.runWhile = False
				self.runningb.config(text = "Start", command = self.start)
				self.errorBox.insert('1.0', "Connection Lost!\n")
				self.errorBox.insert('1.0', "Attempting to Reconnect...(5 second max)\n")
				self.master.update()
				time.sleep(5)
				self.connect()
		if(self.connected):
			default[0] = 'active'
		if(not self.runWhile):
			default[3] = 'active'
			if(len(self.current) > 0):
				default[2] = default[4] = default[6] = 'active'
				if(len(self.current) > 50):
					default[5] = default[7] = 'active'
		for i in range(8):
			buttonDict[i](state = default[i])
		self.pbox.delete('1.0', END)
		self.pbox.insert('1.0', len(self.current))
		self.master.update()

	#This method is the "data collection" method. It runs a loop 'psuedo-infinitely' (really until the variable runWhile is changed to false through some other method, each time trying to collect a data point. Runs when the "Start" button is pressed
	def start(self):
		self.runningb.config(text = "Stop", command = self.stop)
		self.runWhile = True
		self.errorBox.insert('1.0', "Begin Data Collection\n")
		while(self.runWhile and self.connected):
			element, errorTest = self.ser.getGPSData()
			if(not errorTest):
				self.errorBox.insert('1.0', element + '\n')
				self.setState()
			else:
				errorTest = self.current.addElement(element, properForm = False)
				if(errorTest == None):
					self.tbox.insert('1.0', element + '\n')
			self.setState()

	#When the "Stop" button is pressed, this method sets the running state to False, and changes the button to say "Start"
	def stop(self):
		self.errorBox.insert('1.0', "End Data Collection\n")
		self.runningb.config(text = "Start", command = self.start)
		self.runWhile = False
		self.setState()

	#When the "Save" button is pressed, this method will ask for a file name, then pass that name and the data on to the save file method, which will either save it directly, or convert to kml format and save it that way
	def saveData(self):
		filename = asksaveasfilename(filetypes = [('KML Files', '.kml'), ('Data Files', '.dat')])
		if(store.testKMLName(filename)):
			errorTest = store.savef(filename, self.current.kmlForm(), kmlForm = True)
		else:
			errorTest = store.savef(filename, self.current.rawData())
		if(errorTest != None):
			self.errorBox.insert('1.0', errorTest + '\n')
		else:
			self.errorBox.insert('1.0', "File Saved Successfully!\n")
		self.setState()

	#Similar to save, gets a filename, opens the file and reads the data in. Will not support opening KML files
	def openFile(self):
		filename = askopenfilename(filetypes = [('Data Files', '.dat')])
		data, errorTest = store.openf(filename)
		if(errorTest != None):
			self.errorBox.insert('1.0', errorTest + '\n')
		else:
			errorTest = self.current.addList(data, properForm = False)
			if(errorTest != None):
				self.errorBox.insert('1.0', errorTest + '\n')
			for i in self.current.rawData():
				self.tbox.insert('1.0', str(i) + '\n')
		self.setState()

	#Will clear all the windows of output, then reset the data set by setting the data equal to a new instance of GPGGA
	def clearData(self):
		self.errorBox.delete('1.0', END)
		self.tbox.delete('1.0', END)
		self.current = gps.GPGGA()
		self.setState()

	#Will take the parameter value of the slider, then refine the dataset down to the value percent in the slider multiplied by the number of data points
	def refineData(self):
		errorTest = self.current.minimize(pts = self.refScale.get())
		if(errorTest != None):
			self.errorBox.insert('1.0', errorTest + '\n')
		self.setState()

	#Calls the plot3D method on the dataset object, which just displays a simple plot showing the general shape of the current data
	def plotData(self):
		errorTest = self.current.plot3D()
		if(errorTest != None):
			self.errorBox.insert('1.0', errorTest + '\n')
		self.setState()

	#Trys to connect to the GPS device via the serial Object stored in this app, displays error if fails to connect	    
	def connect(self):
		for i in range(100):
			errorTest = self.ser.connect()
			if(errorTest == None):
				self.errorBox.insert('1.0', "Connected Successfully!\n")
				self.setState()
				return
		self.errorBox.insert('1.0', errorTest + '\n')
		self.setState()

#Initialize the window, initialize the application class, start the program running
root = Tk()
app = App(root)
root.mainloop()
