The enclosed figures demonstrate the functionality of the program.
It accepted a list of 816 elements and performed operations to compute the standard deviations of a subset of the list.
It plots the coordinates against time, and the number of satellites.
It plots the standard deviation of the coordinates against time, and the number of satellites.

It should be noted that this program requires numpy for array operations, matplotlib.pyplot for plotting functions, Pylab,
and it requires the special GPGGA class designed specifically for this project.

As a stand-alone program, the error analysis is a class that organizes data according to coordinate and builds lists of
standard deviations in each coordinate, as well as the proper reference coordinates to map the standard deviation coordinates
with. It contains a simple error function that computes relative error.