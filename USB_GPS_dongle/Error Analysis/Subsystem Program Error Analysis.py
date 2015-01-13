#Matt Jones
#Subsystem Program Error Analysis.py

import numpy as np
import matplotlib.pyplot as plt
import pylab
import GPGGA

## note: reference coordinate = time coordinate or # of satellites --> used to refer to an instance of an event (like when standard deviation was lowest or higest
## note: coordiante = latitude, longitude, elevation

## This is the error analysis class, which organizes data and builds lists of standard deviations and another list of reference coordinates.
class analysis:
    def __init__(self, data, step):
        self.d = data
        self.s = step
        self.organize = data.transpose()
        self.satellites = self.organize[5]
        self.satellplot = []
        self.tcoord(self.satellites, self.satellplot)
        self.lat = self.organize[1]
        self.latavg = np.average(self.organize[1])
        self.latdev = []
        self.dev(self.lat, self.latdev)
        self.longi = self.organize[2]
        self.longiavg = np.average(self.organize[2])
        self.longidev = []
        self.dev(self.longi, self.longidev)
        self.elev = self.organize[3]
        self.elevavg = np.average(self.organize[3])
        self.elevdev = []
        self.dev(self.elev, self.elevdev)
        self.time = self.organize[0]
        self.timeplot = []
        self.tcoord(self.time, self.timeplot)

    ## This function accepts a coordinate and an empty list. It computes the standard deviation of a subset of the primary list given a step, s
    def dev(self, coord, devlist):
        for i in range(len(coord)/self.s):
            dev = (1/np.sqrt(self.s))*np.std(coord[i*self.s:(i+1)*self.s], axis = 0)    ## Computes the standard deviation of the mean of a subset of a coordinate list. For example, if the step is 50 points,
            devlist.append(dev)                                     ## then this function would compute the standard deviation of a subset of the list from 0 to 50, from 50 to 100 and so forth.

    ## This function accepts a coordinate and an empty list. Its primary function is to keep track of the reference coordinates (time and # satellites)
    ## in order to plot the standard deviations against time or the # of satellites.
    def tcoord(self, coord, coordplot):
        for i in range(len(coord)/self.s):
            t = coord[i*self.s]
            coordplot.append(t)    ## Appends an empty list with the i*step time or satellite coordinate --> new compiled list used heavily in plotting

    ## A general plotting function that accepts a coordinate, a reference coordinate, a plot title, x and y axes titles. It plots the coordinate and the reference coordinate
    def plotgen(self, coord, time, title, axisy, axisx):
        plt.plot(time, coord)
        plt.title(title)
        plt.xlabel(axisx)
        plt.ylabel(axisy)
        plt.show()

    ## An error function that accepts a position to check the data set against. It computes the average of a particular coordinate and compares it to the accepted value.
    def error(self, USGS):
        USGS = USGS.transpose()
        lat_error = self.latavg - USGS[1]      ## Calculates absolute error
        longi_error = self.longiavg - USGS[2]
        elev_error = self.elevavg - USGS[3]
        rel_lat_error = np.abs(float(lat_error)/USGS[1])    ## Calculates relative error
        rel_longi_error = np.abs(float(longi_error)/USGS[2])
        rel_elev_error = np.abs(float(elev_error)/USGS[3])
        return rel_lat_error, rel_longi_error, rel_elev_error

## Expected Data Format: [UTC of Position (0), Latitude in degrees (1), Longitude in degrees (2), Elevation in meters (3), ... , Number of Satellites as an integer (5)]
f = open("stationaryData.dat")
data = f.read()
data = data.split("\n")
test = GPGGA.GPGGA(dataSet = data)
data  = test.rawData()
a = np.array(data)
USGS = np.array([[0., 4120.8963, 08150.6838, 1, 05, 1.5, 279.0, -32.0]])
a = analysis(a,50)

## Plots against Time
a.plotgen(a.elev, a.time, "Elevation vs Time", "Elevation - Meters", "Time - Seconds")
a.plotgen(a.lat, a.time, "Latitude vs Time", "Latitude - Degrees", "Time - Seconds")
a.plotgen(a.longi, a.time, "Longitude vs Time", "Longitude - Degrees", "Time - Seconds")
a.plotgen(a.satellites, a.time, "# Satellites vs Time", "# Satellites - Integer", "Time - Seconds")

## Deviation Plots against Satellites
#a.plotgen(a.elev, a.satellites, "Elevation vs Satellites", "Elevation - Meters", "# Satellites - Integer")
a.plotgen(a.latdev, a.satellplot, "Latitude SDOM vs # Satellites", "Latitude Deviation - Degrees", "# Satellites - Integer")
a.plotgen(a.longidev, a.satellplot, "Longitude SDOM vs # Satellites", "Longitude - Degrees", "# Satellites - Integer")
a.plotgen(a.elevdev, a.satellplot, "Elevation SDOM vs # Satellites", "Elevation - Meters", "# Satelltes - Integer")

## Scatter Plot Elevation vs Satellites
plt.scatter(a.satellites, a.elev)
plt.title("Elevation vs # Satellites")
plt.xlabel("# Satellites - Integer")
plt.ylabel("Elevation - Meters")
plt.show()

## Deviation Plots against Time
a.plotgen(a.latdev, a.timeplot, "Latitude SDOM vs Time", "Latitude - Degrees", "Time - Seconds")
a.plotgen(a.longidev, a.timeplot, "Longitude SDOM vs Time", "Longitude - Degrees", "Time - Seconds")
a.plotgen(a.elevdev, a.timeplot, "Elevation SDOM vs Time", "Elevation - Meters", "Time - Seconds")


