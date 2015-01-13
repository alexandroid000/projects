#Alli Nilles
#fileOps.py

def testKMLName(fName):
	if(fName[-3:] == 'kml'):
		return True
	return False

#Accepts a file object and reads the data and formats it for the program to use, turning all the strings into floats and separating the data into individual data points
def openf(fName):
	try:
		if(fName == ''):
			return None, "No File Selected, No Data Loaded - Notice in fileOps.openf"
		#kmlForm = testKMLName(fName) - Not supporting opening of KML files yet, just .dat
		f = open(fName, 'r')
		data = f.read()
		data = data.split('\n')
		f.close()
		return data, None
	except:
		pass
	return None, "Problem Opening File for Input - Error in fileOps.openf"

#Accepts a file object and a list of data, converts the data into a useful format for storage, and then stores the data
def savef(fName, dataList, kmlForm = False):
	try:
		if(fName == ''):
			return "No File Selected, No Data Saved - Notice in fileOps.openf"
		f = open(fName, 'w')
		saveString = ''
		if(kmlForm):
			saveString = createKML(dataList)
		else:
			for dataPoint in dataList:
				saveString = saveString + str(dataPoint) + '\n'
		f.write(saveString)
		f.close()
		return None
	except:
		return "Problem Opening File for Saving - Error in fileOps.savef"

#Same as the save function above, but saves in the KML format instead
def createKML(dataList):
	if len(dataList) == 2:
		dataList = dataList[0]
	header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n  <Document>\n    <name>Paths</name>\n    <description>Examples of paths. Note that the tessellate tag is by default      set to 0. If you want to create tessellated lines, they must be authored      (or edited) directly in KML.</description>\n  <Style id=\"yellowLineGreenPoly\">\n      <LineStyle>\n        <color>7f0000ff</color>\n        <width>4</width>\n      </LineStyle>\n      <PolyStyle>\n        <color>7f0000ff</color>\n      </PolyStyle>\n    </Style>\n    <Placemark>\n      <name>Absolute Extruded</name>\n      <description>Transparent green wall with yellow outlines</description>\n   <styleUrl>#yellowLineGreenPoly</styleUrl>\n     <LineString>\n        <extrude>1</extrude>\n        <tessellate>1</tessellate>\n        <altitudeMode>absolute</altitudeMode>\n        <coordinates>\n"
	footer = "        </coordinates>\n      </LineString>\n    </Placemark>\n  </Document>\n</kml>"
	for i in range(len(dataList)):
		header = header + dataList[i] + '\n'
	fileData = header + footer
	return fileData
