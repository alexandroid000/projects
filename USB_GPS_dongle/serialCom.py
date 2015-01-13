#Kento Okomoto
#serialCom.py

import serial
import glob

#Define the serial object class we will be using
class serObject(object):
	#Initialize the class, creating a verify string (to check if it's the right data coming in, not some other serial device that's connected), and set the actual object to an empty object for now
	def __init__(self, vStr = '$'):
		self.serObj = None
		self.verifyString = vStr

	#This method is LINUX SPECIFIC. The glob module is not available on Windows (according to many sources, it may be that a port exists). It just returns a list of the devices in the folder, in this case we specify it so that we can get USB devices and Serial Com devices
	def scanPorts(self):
		return glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyS*')

	#This method attempts to connect to the correct serial device. It gets a list of ports first, then cycles through them trying to connect to them. Once it connects to one, it reads in a data point and checks if it is of the correct format for us (starts with a '$'). Returns None for no error if it connects.
	def connect(self, baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1, xonxoff = 0, rtscts = 1, timeout = 5):
		portsAvail = self.scanPorts()
		if(len(portsAvail) <= 0):
			return "Error Opening Serial Port, No Ports Available - Error in serObject.connect"
		for i in portsAvail:
			try:
				self.serObj = serial.Serial(i, baudrate = baudrate, bytesize = bytesize, parity = parity, stopbits = stopbits, xonxoff = xonxoff, rtscts = rtscts, timeout = timeout)
				if(self.verify()):
					return None
			except serial.SerialException:
				pass
		return "Error Opening Serial Port - Error in serObject.connect"

	#This method reads a single line from the serial port, stripping it of it's newlines and other baggage. It returns both the line it reads (if succesful), and a state of success (True or False) to be used for verifying connection
	def getGPSData(self):
		try:
			for i in xrange(100):
				inputLine = self.serObj.readline().strip('\n\r')
				if(inputLine[0] == self.verifyString and (inputLine.count('\n') + inputLine.count('\r') == 0)):
					return inputLine, True
		except:
			pass
		return "Error Obtaining a Data Value from Serial Device - Error in serialObject.getGPSData", False

	#This method calls getGPSData() in such a way that it can determine if it's connected to a GPS device or not
	def verify(self):
		return self.getGPSData()[1]
		
