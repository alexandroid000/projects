#!/usr/bin/python3

# generates data from some user-defined function
# adds (uniform) random deviations to each data point
# creates spreadsheet with data for fitting

import math
import random

# Generating Functions
# --------------------

def my_sine(x):
    return 5*math.sin(.5*x)

def add_rand(x, err_range = 1):
    return x + random.uniform(-err_range,err_range)

# Generate data
# -------------

def gen_dat(f, xs = range(1,20)):

    ys = [f(x) for x in xs]

    # seeds with system time - not necessary, but good to think about
    random.seed()

    # can have different error in x and y
    x_eval = .2
    y_eval = .3

    # generate data with randomness
    xs = [add_rand(x, x_eval) for x in xs]
    ys = [add_rand(y, y_eval) for y in ys]

    x_err = [x_eval]*len(xs)
    y_err = [y_eval]*len(xs)

    return xs, x_err, ys, y_err

def write_data (name, x, x_err, y, y_err):
    with open(name + ".dat", "w") as fo:
        for (xi,xe,yi,ye) in zip(x, x_err, y, y_err):
            fo.write(str(xi) +", "+ str(xe) +", "+ str(yi) +", "+ str(ye) +"\n")

# Running this file generates data for a couple different curves
if __name__ == "__main__":

    curves = [math.exp, math.sin, my_sine]

    for c in curves:
        x, xe, y, ye = gen_dat(c)
        write_data(c.__name__, x, xe, y, ye)
