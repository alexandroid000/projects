Developed By:

Everett Hildenbrandt
Nathan Neibauer
Alexandra Nilles
Kento Okomoto
Matt Jones

Files Contained:
runGPSModule.py - Nathan Neibauer
fileOps.py - Alexandra Nilles
serialCom.py - Kento Okomoto
Error Analysis - Matt Jones
GPSDataStructure.py - Everett Hildenbrandt
GPGGA.py - Everett Hildenbrandt

Operating Systems Supported:
Linux (specifically run on Ubuntu 12.04 LTS)
(We did not have time to support Windows or Mac OS)

Package Dependencies:
python - Version 2.7.3
time
scipy - 0.9.0
numpy - 1.6.1
matplotlib - 1.1.1rc
Tkinter - Revision: 81008
tkFileDialog
serial
glob
mpl_toolkits.mplot3d

Internal Dependencies:
runGPSModule.py needs:
 Tkinter
 tkFileDialog
 GPGGA.py
 fileOps.py
 serialCom.py

GPGGA needs:
 interpolate from scipy
 numpy
 Axes3D from mpl_toolkits.mplot3d
 GPSDataStructure.py
 
serialCom needs:
 serial
 glob

Instructions for use of the program are provided in the Final Report (found in this directory). Proof that the program works is placed throughout the report via various images and text. Additionally, if you look at the Usage Images directory, and read the README.txt file in that directory, you'll see a more concise (though less thourough) version of the proof of working.

The code presented here is a more up-to-date version of the code used to provide images for the Report, so the GUI interface will look different and some functionality is added to the code provided here. All of the functions have been tested, in as many logical orders as we could derive, and no bugs have been found. That's not to say there aren't bugs, just that we haven't found them. The program, during the debugging process, has been known to hang occasionally, though the most recent version has not.

In a sub-directory labeled "Usage Images", there are several images demonstrating the program in use, as well as some plots of data points onto Google Maps. More thourough descriptions are contained in the README.txt in that directory.

As a quick demonstration of how to use the program (provided you meet the system specs):
In the python shell type:
>>>import runGPSModule
The GUI will show, if you have a GPS dongle you can connect to it, otherwise click the "Open" button to open the data set "dataLong.dat".
After loading in the data set, it should print it out to the screen, and you can manipulate it with the full functionality of the program.

This program was actually tested with two different GPS devices and shown to work with both of them. The second one (the newer one) was a bit more finicky in that sometimes after pressing Start, it wouldn't start collecting, but you could get it to by clicking Stop and Start again. Also, the second GPS unit tended to disconnect randomly, which we took care of by writing a reconnect script which waits for 5 seconds then tries to reconnect.

Matt Jones' subsystem is in a separate folder, Error Analysis, with it's own documentation. It is run as a separate program on the datasets in order to analyze the accuracy of the GPS against a known data point.
