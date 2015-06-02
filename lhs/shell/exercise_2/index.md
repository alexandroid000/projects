---
title: Bash Shell Excercise 2
...

Try these excercises out using files from the current directory. Have this guide
open in a separate window so you can follow along. You'll need an internet
connection for parts of this guide.


Paramater Sweep
===============

This will be using the program 'tsp.py' from the directory 'media/tsp', with
input files 'tsp_n.in'. We'll be 'submitting' our jobs to the 'supercomputer'
using the file 'submit_template'. The program 'tsp.py' takes a file with integer
coordinates on each line and attempts to find the shortest path that travels
to each point in the file exactly once.

Objectives
----------

-   Write a SLURM submission script which calles `tsp.py` on an input file
-   Write a wrapper script which submission scripts for you
-   Write a second wrapper which modifies the input file instead

Procedure
---------
