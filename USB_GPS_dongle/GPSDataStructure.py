#Everett Hildenbrandt
#GPSDataStructure.py
#Data Structure for inputting data from a GPS. For our purposes, we only want the position data out of the GPGGA codes, but written here is a generic class for any data type which comes in as a string. For the position data, we don't want to store it as a string, so methods that are specific to it being a string are overloaded in the subclass GPGGA. Similarly, functionality can be extended to other NMEA codes via creating a different subclass and overloading the parent functions appropriately. As they stand, they work very generically.

#Very generic definition of a GPS Data Input class. Will not work for specific operations other than general dataset manipulation. Possible extensions - A remove method to delete a specific datapoint from the set. It seems to me that this method would never be used or serve any specific purpose. With GPSData, at least to me, it seems that you never want to remove a specific point, but always ordered sets of points, which the trim() or filterSet() functions offer to an extent.
class GPSDataSet(object):
	#Initialization Method: Should be fairly good at initializing sub-classes as well provided the proper methods are over-loaded properly in the subclasses. Can accept a generic dataset, convert it to the proper format (based on either the generic function provided with this super class or over-loaded in the sub-class), and check it for errors. In general, it is good to call this method in sub-class initialization methods.
	def __init__(self, dataSet = None, properForm = False, extLen = 200, verify = '$'):
		self.classType = "GPSDataSet"
		self.extendLength = extLen
		self.data = []
		self.length = 0
		self.verifyObj = verify
		if(dataSet != None):
			selfTest = self.addList(dataSet, properForm = properForm)
			secondTest = self.filterSet(self.verifyObj)
			if(selfTest != None or secondTest != None):
				print str(selfTest), '\n', str(secondTest), "\nObject may not have been instantiated correctly - Error in GPSDataSet.__init__"

	#Storage in this class and sub-classes is done in a list (kept generic). When elements need to be added to the list, they are appended to the end, which is slow if done on large data-sets many times. So, we only extend the list by a pre-defined amount every once in a while, just overwriting the None values in the interim. Care must be taken to keep the length of the data set correct - if the list is extended past a bunch of None values and the length does not take this into account, you'll overwrite your extended data. This method does not need over-loaded in general.
	def extendSet(self, amount = None):
		if(amount == None):
			self.data.extend([None]*self.extendLength)
			return
		self.data.extend([None]*amount)

	#Checks if the list is long enough, if not, it extends it. If the extension does not work, it passes back an error message. If it does work, it sets the next open data point (which it assumes to be at position self.length) to the incoming data point. This method does not need overloaded in general.
	def addElement(self, element, properForm = True):
		selfTest = None
		if(self.length >= len(self.data)):
			self.extendSet()
		if(not properForm):
			element, selfTest = self.convertInput(element)
		if(selfTest != None):
			return selfTest
		try:
			if(self.verify(element, filt = self.verifyObj)):
				self.data[self.length] = element
				self.length = self.length + 1
			else:
				selfTest = "Data Point not of Correct Format/Type, Not Added - Error in GPSDataSet.addElement"
		except IndexError:
			selfTest = "Dataset Not Long Enough - Error in GPSDataSet.addElement"
		return selfTest

	#Accepts a list of elements as input and uses the addElement method to store each individually in the dataset. This method does not need over-loaded in general
	def addList(self, listElements, properForm = True):
		selfTest = None
		try:
			notAdd = 0
			for dataPt in listElements:
				tempTest = self.addElement(dataPt, properForm = properForm)
				if(tempTest != None):
					notAdd += 1
					selfTest = "[x" + str(notAdd) + "] " + tempTest
		except TypeError:
			selfTest = "List to Append is not of Type List - Error in GPSDataSet.addList"
		return selfTest

	#This method looks through the list of data for all the None values, which may arise when extending the list or if a None element is added for any reason. It will remove those None values, and reset the list length to the full length of the list. Then it looks through for other None values, and if any are found it returns an error message. This method does not need over-loaded in general
	def removeNones(self):
		try:
			noneLeft = True
			while(noneLeft):
				try:
					self.data.remove(None)
				except ValueError:
					noneLeft = False
			self.length = len(self.data)
			return None
		except IndexError:
			return "Index Problem Removing Nones - Error in GPSDataSet.removeNones"

	#A generic trimming method. Syntactically similar to the range() function. Options include whether you want to remove the Nones from the list before applying the trim, as well as specifying the place to start the trim, stop the trim, and the interval between points to take. Defaults are starting the trim at the beginning of the list, stopping at the length of the data set (not necessarily the length of the list), and taking every point. Default is also to not remove the None values before performing the trim. This method can be overloaded if you're looking for a more specific sort of trim, but it seems useful to keep it around anyway.
	def trim(self, stop = None, start = 0, interval = 1, removeNone = False):
		if(stop == None):
			stop = self.length
		if(removeNone == True):
			selfTest = self.removeNones()
			if(selfTest != None):
				return selfTest
		try:
			tempData = []
			for i in xrange(start, stop, interval):
				tempData.append(self.data[i])
		except IndexError:
			return "Specified Trimming Conditions out of Dataset Range - Error in GPSDataSet.trim"
		self.data = tempData
		self.length = len(self.data)
		return None

	#A method to convert an input data-set (usually for when the data is initialized) to the proper form for the object it's being stored as. Here, it just tries to convert every element into a string (for the generic storage class). This method SHOULD ALWAYS be over-loaded if you plan to store your data as anything other than a string literal for every data point.
	def convertInput(self, dataPt):
		selfTest = None
		try:
			dataPt = str(dataPt)
		except:
			selfTest = "Data Could not be Converted to String - Error in GPSDataSet.convertInput"
		return dataPt, selfTest

	#This method will look through the data set, given a filtering parameter (optional), and only keep data points that match the filtering parameter. It's described very generically because the specifics of filtering are meant to be put into the verify() method, specified below. This method does not generally need overloaded because of that generality.
	def filterSet(self, filt = None, removeAll = True):
		if(filt == None):
			filt = self.verifyObj
		selfTest = self.removeNones()
		if(selfTest != None):
			return selfTest		
		tempData = []
		for dataPt in self.data:
			if(self.verify(dataPt, filt = filt)):
				tempData.append(dataPt)
		tempLength = len(tempData)
		if(tempLength <= 0):
			selfTest = "No Data Matching Filter Found, Dataset Unaltered - Notice in GPGGA.filterSet"
			if(not removeAll):
				return selfTest
			self.Test = None
		if(filt == self.verifyObj and tempLength != len((self.data))):
			selfTest = "Filter on " + str(filt) + " Removed Some Invalid Items - Notice in GPSDataSet.filterSet"
		self.data = tempData
		self.length = tempLength
		return selfTest

	#This method will verify that the datapoint is of the correct form. It returns True if it is, False if not. It should almost always be overloaded in sub-classes
	def verify(self, dataPt, filt = None):
		if(filt == None):
			filt = self.verifyObj
		try:
			filtLen = len(filt)
			if(dataPt[:filtLen] == filt):
				return True
		except:
			return False
		return False

	#Oveload the __getitem__ method
	def __getitem__(self, index):
		try:
			return (self.data[index])
		except IndexError:
			print "Index out of Range of Data - Error in GPSDataSet.__getitem__"
			return None

	#Overload the __setitem__ method
	def __setitem__(self, index, dataPt):
		try:
			if(self.verify(dataPt)):
				self.data[index] = dataPt
				return
		except IndexError:
			print "Index out of Range of Data - Error in GPSDataSet.__setitem__"

	#Overload the __len__ method
	def __len__(self):
		return self.length

	#This method returns the datalist itself. Nothing fancy. Does not need to be over-loaded for sub-classes.
	def rawData(self):
		selfTest = self.removeNones()
		if(selfTest != None):
			return None
		return self.data

	#This method returns the class type, for checking whether it's filtered or not
	def getClassType(self):
		return self.classType
