#!/usr/bin/python
# shebang - tells shell how to run program. Find path with "whereis python"

import sys # gives us access to system information (files, arguments, etc)
import math
import random as r
import timeit as ti


# Compare Function (For Testing Speeds)
# =====================================
def compare_funcs (funcs, random_size = 1000, number = 10000):
    # (Notice line continuation `\`, `setup_str` is defined across two lines
    setup_str = "import intro_to_python as ip; import random as r;" \
            + "xs = [r.randint(1,100) for i in range("+str(random_size)+")];"
    for func in funcs:
        print (func + ":",
            ti.timeit("ip."+func+"(xs)", setup = setup_str, number = number))


# Simple Loop
# ===========
def simple_loop(beginning, end):
    sum = 0
    # range is exclusive of end - range(1,3) produces [1,2]
    for elem in range(beginning, end):
        sum += elem
    print("Sum from",beginning,"to",end-1,"is",sum)


# Using Function from a Module (math.sqrt)
# ========================================
def check_square(val):
    # math.sqrt will return float, cast to int
    sqrt = int(math.sqrt(val))
    if sqrt*sqrt == val:
        return True
    # if we rounded in cast to int, square won't be reconstructed
    else:
        return False


# Creating Lists
# ==============

# Append Method (not as good)
# ---------------------------
def list_append(data_to_app = [1,3,5,8,1000]):
    app_list = []
    for elem in data_to_app:
        app_list.append(elem)
    return app_list

# List Comprehension (faster)
# ---------------------------
def list_comp(data_to_comp = [1,3,5,8,1000]):
    ret_list = [elem for elem in data_to_comp]
    # Same thing, but only take even numbers
    #ret_list = [i for i in data_to_comp if i % 2 == 0]
    # Same thing, but square only the numbers divisible by 7
    #ret_list = [num*num for num in data_to_comp if num % 7 == 0]
    return ret_list


# Compare the speeds
# ------------------
def compare_lists():
    compare_funcs (["list_append", "list_comp"])


# Numeric Differentiation
# =======================

# Append Method (Not as good)
# ---------------------------
def num_diff_1(xs = [1,3,5,10,15], dt = 1):
    velocities = []         # Empty list
    # Loop over our x_vals/t_vals
    for t in range(len(xs) - 1):
        dx = xs[t+1] - xs[t]
        velocities.append(dx/dt)
    return velocities

# List Comprehension Method (better)
# ----------------------------------
def num_diff_2(xs = [1,3,5,10,15], dt = 1):
    velocities = [(x1 - x0)/dt for (x0,x1) in zip (xs[:-1], xs[1:])]
    return velocities

# Compare the speeds
# ------------------
def compare_diffs():
    compare_funcs(["num_diff_1", "num_diff_2"])


# Flatten a list of lists
# =======================
def flatten(list_o_lists):
    flattened = [x for sublist in list_o_lists for x in sublist]
    return flattened


# Handling Command line arguments
# ===============================
print("Num arguments: ", len(sys.argv))
print("Arguments:     ", sys.argv)
#if len(sys.argv) < 3:
#    print("Need two command-line arguments, beginning and end of range")
#    sys.exit(1)
