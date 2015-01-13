#Everett Hildenbrandt
#GPGGA.py

from GPSDataStructure import *
from scipy import interpolate as ip
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Class defined for only the GPGGA position data from a GPS Dongle. Overloads necessary functions in the generic GPSDataSet class. Offers minimization of the dataset, as well as conversion to the KML format for creating a file for uploading to map software.
#[time, latitude, longitude, altitude, gps quality, numer of satellites, horizontal dilution, geoidal separation]
class GPGGA(GPSDataSet):
	#Initialization of the object, calls the parent initializer, then sets some other values properly, such as the classType
	def __init__(self, dataSet = None, properForm = False, extLen = 200, verify = None):
		if(verify == None):
			verify = [None]*15
		super(GPGGA, self).__init__(dataSet = dataSet, properForm = properForm, extLen = extLen, verify = verify)
		self.classType = "GPGGA"

	#Method which specifically takes a string data input, checks if it is a valid GPGGA code, and then breaks it into a list of float values which we can use/operate on. Notice that not only can it take a raw GPGGA code, it can take a .dat file line as a string and split it up into data points
	def stringToData(self, dataPt):
		dataPos = [1, 2, 4, 9, 6, 7, 8, 11]
		returnPt = [None]*8
		try:
			if(dataPt[0] == '$'): #If it's a raw GPGGA code from the serial input
				strList = dataPt.split(',')
				if(len(strList) < 12 or strList[0] != '$GPGGA'):
					return None, "Incorrect Data Format for Data Conversion - Error in GPGGA.stringToData"
				for i in range(8):
					if(strList[dataPos[i]] == ''):
						returnPt[i] = 0
					else:
						returnPt[i] = float(strList[dataPos[i]])
				returnPt[1] /= 100.
				returnPt[2] /= 100.
				if(strList[3] == 'S' or strList[3] == 's'):
					returnPt[1] *= -1
				if(strList[5] == 'W' or strList[5] == 'w'):
					returnPt[2] *= -1
			elif(dataPt[0] == '['): #If it's from a .dat file saved by this program
				strList = dataPt.strip('[]').split(',')
				for i in range(8):
					returnPt[i] = float(strList[i])
			else:
				return None, "Unsupported Data Import Type - Error in GPGGA.stringToData"
		except TypeError:
			return None, "Incorrect Data Format, Unable to Convert from String to Float - Error in GPGGA.stringToData"
		except IndexError:
			return None, "Datapoint with Incorrect Length, Indexing Error - Error in GPGGA.stringToData"
		return returnPt, None

	#Method to overload the convertInput method of the GPSDataSet class in order to call the convertToString method of the GPGGA class.
	def convertInput(self, dataPt):
		selfTest = None
		try:
			dataPt, selfTest = self.stringToData(dataPt)
		except:
			selfTest = "Data Could not be Converted to the Proper Form - Error in GPGGA.convertInput"
		return dataPt, selfTest

	#Overloaded verify method which verifies data based on whether it has any matching data points to the filter.
	def verify(self, dataPt, filt = None):
		if(filt == None):
			filt = self.verifyObj
		try:
			lenPt = len(dataPt)
			if(lenPt < 8):
				return False
			else:
				for i in range(lenPt):
					dataValue = float(dataPt[i]) #This is a hack to force the try: except: block to throw an error for strings
					if(dataPt[i] == filt[i]):
						return False
		except (IndexError, TypeError):
			return False
		return True

	#Method to return a numpy array which has the latitude, longitude, and altitude data in a dataset for manipulation, useful for plotting, or for saving to a kml file
	def posArray(self):
		try:
			selfTest = self.removeNones()
			if(selfTest != None):
				return None, selfTest
			posArray = np.zeros((3, self.length))
			for i in range(3):			
				for j in range(self.length):
					posArray[i, j] = self.data[j][i + 1]
			return posArray, None
		except IndexError:
			return None, "Index Error when Numpy Position Array - Error in GPGGA.posArray"
		

	#Minimize the number of data points that are stored
	def minimize(self, pts = 50, smoothVal = 3.):
		if(pts >= 100):
			return "Points Specified for Refinement Either as long as or longer than DataSet - Error in GPGGA.minimize"
		elif(pts == 0):
			return "Will Not Refine All Points Out Of Existence - Error in GPGGA.minimize"
		dependArray = np.array(range(self.length)) #Create an x-axis to create the cubic splines over
		splineArray, selfTest = self.posArray() #Get only the latitude, longitude, and altitude
		if(selfTest != None):
			return selfTest
		sVal = (self.length)**(1./smoothVal) #Set our smoothing value parameter
		if(sVal <= 3.): #It has to be greater than k = 3 (for cubic splines)
			sVal = 4.

		#Here, we create the spline interpolation of the data, which returns it as knots to be used for the spline evauluation function later
		splineRep2nd = [ip.splrep(dependArray, splineArray[0], s = sVal, k = 3), ip.splrep(dependArray, splineArray[1], s = sVal, k = 3), ip.splrep(dependArray, splineArray[2], s = sVal, k = 3)]
		#Here, we evaluate the spline's first and second derivative (needed for the curvature) at all of the data points in dependArray
		splineDer1 = np.transpose([ip.splev(dependArray, splineRep2nd[0], der = 1), ip.splev(dependArray, splineRep2nd[1], der = 1), ip.splev(dependArray, splineRep2nd[2], der = 1)])
		splineDer2 = np.transpose([ip.splev(dependArray, splineRep2nd[0], der = 2), ip.splev(dependArray, splineRep2nd[1], der = 2), ip.splev(dependArray, splineRep2nd[2], der = 2)])
		
		#Initialize the curvature, and using the curvature formula as well as data regarding the first and second derivative of the path, calculate the curvature at every point along the path, then set the curvature at the ends to the highest -> keeps endpoints		
		curv = np.zeros(self.length)
		for i in xrange(self.length):
			curv[i] = (np.linalg.norm(splineDer1[i])**3.)/np.linalg.norm(np.cross(splineDer1[i], splineDer2[i]))
		curv[0] = curv[-1] = max(curv)

		#Create a priority queue which tells us which points to take or not
		priority = self.priorityList(curv)
		self.length = self.trimData(priority, int(round(self.length * (float(pts)/100.))))
		return None

	#Finds the priority of a list - returns a list with the first position specifying the position of the maximum element, then subsequent positions specifying the subsequent maximums
	def priorityList(self, curv):
		lenD = len(curv)
		keys = range(lenD)
		d = dict(zip(keys, curv))
		priority = sorted(d, key = lambda k: d[k], reverse = True)[:lenD]
		return priority

	#Truncates the priority que to only the number of points desired, then sorts it so that the data will be brought onto the new trimmed list in the same order as the original data
	def trimData(self, priority, points):
		priority = sorted(priority[0:points])
		trimmedData = []
		for i in priority:
			trimmedData.append(self.data[i])
		self.data = trimmedData
		return len(trimmedData)

	#Plots the latitude, longitude, and altitude data in 3D, gives an idea what it looks like.
	def plot3D(self):
		plotData, selfTest = self.posArray()
		if(selfTest != None):
			return selfTest
		fig = plt.figure()
		ax = fig.gca(projection = '3d')
		ax.plot(plotData[0], plotData[1], plotData[2])
		plt.show()
		return None
	
	#Return a list of strings in the kml file format
	def kmlForm(self):
		selfTest = self.removeNones()
		returnList = None
		if(selfTest != None):
			return returnList, selfTest
		try:
			returnList = [None]*self.length
			for i in range(self.length):
				returnList[i] = str((self.data[i][2])) + ',' + str((self.data[i][1])) + ',' + str((self.data[i][3]))
		except IndexError:
			returnList = None
			selfTest = "Error Converting the Data Points to KML Format, Index Error - Error in GPGGA.kmlForm"
		return returnList, selfTest
