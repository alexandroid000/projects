#!/usr/bin/python3

# Needed Modules
# ================

import numpy as np
import matplotlib.pyplot as plt
import scipy.odr.odrpack as odrpack
import sys

# documentation for the odrpack library can be found here:
# "http://docs.scipy.org/doc/scipy/reference/odr.html#id1"

# Functions to fit
# ================

# elements of B are the free parameters for fitting

def fsin(B,x):
    return B[0]*np.sin(B[1]*x)

def fexp(B,x):
    return B[0]*np.exp(B[1]*x)

def fpoly(B,x):
    return B[0]*(x**3) + B[1]*(x**2) + B[2]*(x) + B[3]

# Import data
# ===========

def import_from_csv(data_file):

    x = []
    x_err = []
    y = []
    y_err = []

    with open(data_file, "r") as f:

        # need to remove newlines and commas (for CSVs)
        data = np.array([line.rstrip().split(", ") for line in f])

        # cast to float for computation (copies array)
        data = data.astype(float)

        # if len 4, assume data in [x, x_err, y, y_err] format
        # otherwise transpose
        if len(data) != 4:
            data = np.transpose(data)

        x = data[0]
        x_err = data[1]
        y = data[2]
        y_err = data[3]

    return x, x_err, y, y_err

# Do fit
# ======

# perform orthogonal distance regression for given model f
def do_odr(f, x, xe, y, ye, estimates):

    model = odrpack.Model(f)

    # sx and sy should be the covariances
    data = odrpack.RealData(x, y, sx=xe, sy=ye)

    # can hard-code in guesses for parameters
    #odr = odrpack.ODR(data, model, beta0=[0., 0., 0.])

    # or go with defaults
    odr = odrpack.ODR(data, model, estimates)

    output = odr.run()

    return output

# Plot - required matplotlib
# --------------------------

def plot_fit(x, xe, y, ye, f, betas):

    plt.xlabel('x-label (units)', fontsize = 14) # x-axis label
    plt.ylabel('y-label (units)', fontsize = 14) # y-axis label
    space = 0.1 # desired space as fraction of respective ranges

    xspan = x.max() - x.min() # range of x values
    yspan = y.max() - y.min() # range of y values
    xspace = space * xspan # space on either side of x min/max
    yspace = space * yspan # space on either side of y min/max

    plt.xlim(x.min()-xspace,x.max()+xspace) # x-axis range
    plt.ylim(y.min()-yspace,y.max()+yspace) # y-axis range

    plt.errorbar(x, y, fmt = 'ro', xerr = xe, yerr = ye) # data and error bars

    modelx = np.linspace(x.min()-xspace, x.max()+xspace, 500)

    plt.plot(modelx, f(betas, modelx)) # model

    # save plot to pdf
    #    plt.savefig('myplot.pdf', bbox_inches=0, dpi=600)

    # on screen display of plot
    plt.show()

# Run file
# --------

# need to run with data file as 1st argument
# prints output and shows plot

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Need to supply input file as first argument")

    data_file = sys.argv[1]

    x, xe, y, ye = import_from_csv(data_file)

    sin_ests = [1.0, 1.0]

    sin_fit = do_odr(fsin, x, xe, y, ye, sin_ests)

    print("Estimated Parameters:", sin_fit.beta)
    print("Parameter Standard Errors:", sin_fit.sd_beta)

    plot_fit(x, xe, y, ye, fsin, sin_fit.beta)


