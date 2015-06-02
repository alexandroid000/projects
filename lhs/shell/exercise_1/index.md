---
title: Bash Shell Excercise 1
...

Try these excercises out using files from this directory. Have this guide open
in a separate window so you can follow along.


Othello's Lines
===============

This is using file 'othello.txt'.

Objectives
----------

+ Estimate how many lines Othello has, same for Lodovico
+ Print out the first sentence of each of Othello's lines
+ See how many times Othello's name is called in the play

Procedure
---------

Print out the file to get an idea of the structure:

```bash
% cat othello.txt
               Othello, the Moore of Venice
    [1]Shakespeare homepage | [2]Othello | Entire play
    #### Many more lines here ####
       LODOVICO

    [To IAGO] O Spartan dog,
    More fell than anguish, hunger, or the sea!
    Look on the tragic loading of this bed;
    This is thy work: the object poisons sight;
    Let it be hid. Gratiano, keep the house,
    And seize upon the fortunes of the Moor,
    For they succeed on you. To you, lord governor,
    Remains the censure of this hellish villain;
    The time, the place, the torture: O, enforce it!
    Myself will straight aboard: and to the state
    This heavy act with heavy heart relate.

    Exeunt
```

Get Othello's lines using `grep`:

```bash
% grep 'OTHELLO' othello.txt
    OTHELLO
    OTHELLO
    #### Many more lines here ####
    OTHELLO
```

Count Othello's and Lodovico's lines using the '-c' option for `grep`:

```bash
% grep -c 'OTHELLO' othello.txt
296
% grep 'LODOVICO' othello.txt | wc -l
39
```

Print out the first sentence of each of Othello's lines using the '-A' option
for `grep`:

```bash
% grep -A 2 'OTHELLO' othello.txt
    OTHELLO
    #### Many more lines here ###
    OTHELLO

    O fool! fool! fool!
    --
    OTHELLO

    Soft you; a word or two before you go.
    --
    OTHELLO

    I kiss'd thee ere I kill'd thee: no way but this;
```


Random Data File
================

This is using random data file 'data_file.csv'.

Objectives
----------

+ Display the 'Reduced Chai Values' and 'Final Energy Values'
+ Show only the last two 'Reduced Chai Values'
+ Find out how many data lines are in the file
+ Find out how many data points are in the file

Procedure
---------

Get an idea of what the file looks like with `less`. Use the search function of
less (press '/' followed by your search string) to get an idea of the file. Use
the 'n' key to jump to the next match, 'N' to go te previous. Use the keys 'k'
and 'j' to scroll.

```bash
% less data_file.csv
    Reduced Chai Values:
    6575839, 7151022, 7334710, 4978808
    #### Many more lines ####
    Final Energy Values:
    3880766, 14001684, 13718481, 8132653
    #### Many more lines ####
```

Find the 'Reduced Chai Values' and 'Final Energy Values' by calling grep with
the '-A' option. Pipe the second into `less` to be able to scroll through and
search the output.

```bash
% grep -A 1 'Reduced Chai Values' data_file.csv
    Reduced Chai Values:
    6575839, 7151022, 7334710, 4978808
    --
    #### More lines here ####
    Reduced Chai Values:
    9074041, 6222272, 14989142, 5701998

% grep -A 1 'Final Energy Values' data_file.csv | less
    Final Energy Values:
    3880766, 14001684, 13718481, 8132653
    --
    #### More lines here ####
    --
    Final Energy Values:
    10340226, 8981179, 12774173, 8236417
lines 1-65
```

To show only the last two 'Reduced Chai Values', pipe the output of `grep` into
`tail`, and tell `tail` to only output the last 6 lines with the '-n' option.

```bash
% grep -A 1 'Final Energy Values' data_file.csv | tail -n 6
    --
    Final Energy Values:
    12412807, 1170828, 5338510, 9964010
    --
    Final Energy Values:
    11752080, 1137775, 6640678, 7974974
```

Use the '-c' option for `grep` to count the data lines, coupled with the '-v'
option to exclude non-data lines (invert the selection). You can also use the
`wc` command to count the number of lines grep outputs.

```bash
% grep -c -v ':' data_file.csv
5000
% grep -v ':' data_file.csv | wc -l
5000
```

To verify there are four data-points per line, we'll count the data points now.
We'll use the '-v' option for `grep` again to exclude descriptive lines, and
pipe the output into `wc`. This time we'll use the `-w` option with `wc` to
count words, instead of lines. There should be four data-points per line.

```bash
% grep -c -v ':' data_file.csv | wc -w
20000
```

Supercomputer Output Parsing
============================

This is using file 'dextran_qm_dft.out'.

Objectives
----------

+ See the steps and energies for each relaxation of the dextran molecule
+ Print out each geometry along the relaxation path
+ Make an function that does all this for you in one fell swoop
+ Turn the function into a shell script so it can be used a bit more versatily
+ Use the shell script from within vim to create a new file

Procedure
---------

Get a feel for the file by displaying it with `less` (or `vim`). Knowing that
NWChem outputs a '@' at the beginning of a line with energy information on it,
search for '^@'. The '^' is a regular expression that matches the beginning of a
line, so we only get lines what the '@' is at the beginning of the line. Also
search for 'Geometry' to get an idea of what those parts of the file look like.

```bash
% less dextran_qm_dft.out
```

    Please copy the file /lrz/sys/applications/nwchem/6.3/impi/.nwchemrc to your
    home directory.
    This file is necessary for NWChem to find the standard libraries.
     argument  1 = optimize.nw
        #### More lines here ####

    Northwest Computational Chemistry Package (NWChem) 6.3
    ------------------------------------------------------


    Environmental Molecular Sciences Laboratory
    dextran_qm_dft.out lines 1-65/24471 0%

Now that we are familiar with the output format, let's use `grep` to grab only
the lines we need from the file. Once again, the '^' tells `grep` to only match
'@' symbols at the beginning of a line. We can save these energies and deltas by
redirecting the stdout of grep to another file, 'dextran_energies.out'.

```bash
% grep '^@' dextran_qm_dft.out
```

    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
    @    3    -686.93728094 -4.0D-04  0.00183  0.00045  0.02043  0.06471    536.9
    @    4    -686.93765371 -3.7D-04  0.00231  0.00055  0.02664  0.09902    685.2
    @    5    -686.93795400 -3.0D-04  0.00218  0.00046  0.02601  0.08722    834.3
    @    6    -686.93815263 -2.0D-04  0.00214  0.00036  0.02147  0.06602    982.6
    @    7    -686.93820464 -5.2D-05  0.00078  0.00014  0.00714  0.01937   1114.2
    @    8    -686.93823383 -2.9D-05  0.00089  0.00015  0.00618  0.01997   1236.3
    @    9    -686.93825965 -2.6D-05  0.00063  0.00014  0.00684  0.02057   1365.8
    @   10    -686.93828289 -2.3D-05  0.00065  0.00012  0.00676  0.02784   1504.9
    @   11    -686.93829701 -1.4D-05  0.00049  0.00010  0.00514  0.02142   1618.2
    @   12    -686.93830468 -7.7D-06  0.00046  0.00008  0.00443  0.01556   1748.7
    @   13    -686.93830745 -2.8D-06  0.00013  0.00003  0.00102  0.00292   1827.3
    @   14    -686.93830891 -1.5D-06  0.00006  0.00001  0.00100  0.00300   1906.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5

```bash
% grep '^@' dextran_qm_dft.out > dextran_energies.out
% cat dextran_energies.out
```

    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
    @    3    -686.93728094 -4.0D-04  0.00183  0.00045  0.02043  0.06471    536.9
    @    4    -686.93765371 -3.7D-04  0.00231  0.00055  0.02664  0.09902    685.2
    @    5    -686.93795400 -3.0D-04  0.00218  0.00046  0.02601  0.08722    834.3
    @    6    -686.93815263 -2.0D-04  0.00214  0.00036  0.02147  0.06602    982.6
    @    7    -686.93820464 -5.2D-05  0.00078  0.00014  0.00714  0.01937   1114.2
    @    8    -686.93823383 -2.9D-05  0.00089  0.00015  0.00618  0.01997   1236.3
    @    9    -686.93825965 -2.6D-05  0.00063  0.00014  0.00684  0.02057   1365.8
    @   10    -686.93828289 -2.3D-05  0.00065  0.00012  0.00676  0.02784   1504.9
    @   11    -686.93829701 -1.4D-05  0.00049  0.00010  0.00514  0.02142   1618.2
    @   12    -686.93830468 -7.7D-06  0.00046  0.00008  0.00443  0.01556   1748.7
    @   13    -686.93830745 -2.8D-06  0.00013  0.00003  0.00102  0.00292   1827.3
    @   14    -686.93830891 -1.5D-06  0.00006  0.00001  0.00100  0.00300   1906.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5
    @   15    -686.93830931 -4.1D-07  0.00005  0.00001  0.00041  0.00128   1978.5

So we have the electronic energies at each relaxation step (as well as position
deltas between steps) saved to a file. Now we need to get the geometry at each
relaxation step. Here, we'll use the '-A' option for `grep` to print out the
lines following our matches. At first, we may not know how many lines to print
out, so we'll try something excessive, perhaps 40? Then narrow it down (or
expand it) to make sure you get all the atoms. Once we're satisfied that we're
getting the results we want, we can redirect the output to a file for saving.

```bash
% grep -A 40 'Geometry "geometry"' dextran_qm_dft.out
```

                                 Geometry "geometry" -> ""
                                 -------------------------

     Output coordinates in angstroms (scale by  1.889725989 to convert to a.u.)

      No.       Tag          Charge          X              Y              Z
     ---- ---------------- ---------- -------------- -------------- --------------
        1 C                    6.0000    -1.46614374     1.14413858     0.20689570
        2 C                    6.0000    -0.06510930     1.71491488     0.52712986
        3 C                    6.0000     1.01933089     0.89126609    -0.19986268
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

          Atomic Mass
          -----------

          C                 12.000000
          O                 15.994910
          H                  1.007825


     Effective nuclear repulsion energy (a.u.)     827.3774954752

Looks like we overshot by 10 lines

```bash
% grep -A 30 'Geometry "geometry"' dextran_qm_dft.out
```

                                 Geometry "geometry" -> ""
                                 -------------------------

     Output coordinates in angstroms (scale by  1.889725989 to convert to a.u.)

      No.       Tag          Charge          X              Y              Z
     ---- ---------------- ---------- -------------- -------------- --------------
        1 C                    6.0000    -1.46614374     1.14413858     0.20689570
        2 C                    6.0000    -0.06510930     1.71491488     0.52712986
        3 C                    6.0000     1.01933089     0.89126609    -0.19986268
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

```bash
% grep -A 30 'Geometry "geometry"' dextran_qm_dft.out > dextran_geometries.out
```

Now we want to define a bash function which runs all these commands on the file.
The function should be able to handle and NWChem output file (for ease of use),
as well as any number of atoms. Here, we have 24 atoms, and had to use '-A 30'
with `grep` to get the correct lines, so we need to add 6 to our number of atoms
and pass that number to `grep`. We'll setup our function so it can take the file
to use and the number of atoms as arguments (parameters). This is done with the
'$N' notation - '$1' stores the first argument, '$2' stores the second, etc...

```bash
    #Define a function called 'extract_data'
% extract_data() {
> file="$1"
> n_atoms="$2"
> let n_atoms=$n_atoms+6
> echo "Relaxation Data"
> grep --color=auto '^@' "$file"
> echo
> echo "Geometry Data"
> grep --color=auto -A "$n_atoms" 'Geometry "geometry"' "$file"
> }
```

Test out the function

```bash
% extract_data dextran_qm_dft.out 24
```

    Relaxation Data
    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

Save the output to a file

```bash
% extract_data dextran_qm_dft.out 24 > dextran_all_data.out
```

Awesome! Now we have a function which we can apply to any NWChem geometry
relaxation output from a run on the supercomputers to extract exactly the data
we need. However, if we log out and log back in to the supercomputer, our
function definition will be gone! Redifining this function everytime we login is
tedious, but we can put it in our '.bashrc' to force it to be redefined every
time. Edit your '.bashrc' and add the function definition to it somewhere.

```bash
% vim .bashrc

    # Add the lines
extract_data() {
    file="$1"
    n_atoms="$2"
    let n_atoms=$n_atoms+6
    echo "Relaxation Data"
    grep --color=auto '^@' "$file"
    echo
    echo "Geometry Data"
    grep --color=auto -A "$n_atoms" 'Geometry "geometry"' "$file"
}

    # Save and close (:wq)
```

Now logout and log back into your remote computer (if doing this locally, simply
close your terminal and open a new one). Verify that `extract_data` is defined
by calling it on the 'dextran_qm_dft.out' file.

```bash
% extract_data dextran_qm_dft.out 24
```

    Relaxation Data
    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

Neato! So we can write these little single-purpose scripts which help our data
collection as functions in our '.bashrc'. This can greatly simplify working with
the supercomputers. However, what if we want to call this script from inside
`vim`? `vim` doesn't look at functions we've defined for the shell when running
commands, only at the '$PATH' variable for the shell. To make this functionality
available to call from within vim, we'll have to make it into a script. Make the
directory '~/bin' if it doesn't exist, and add it to your path.

```bash
    #Check the contents of our $PATH
% echo $PATH
/usr/local/bin:/usr/bin:/bin:/opt/bin:/sbin:/usr/sbin

    # Make '~/bin'
% mkdir ~/bin

    # Edit '~/.bashrc'
% vim ~/.bashrc

    # Add the line (somewhere towards the end is fine)
export PATH="$PATH:$HOME/bin"

    # Save and close, close your terminal (or logout) and open a new one
% echo $PATH
/usr/local/bin:/usr/bin:/bin:...:/usr/sbin:/home/ehildenb/bin
```

Now the folder '~/bin' can contain executables which we can call from the
command line. Nifty! So we'll make a new script in 'bin' called `extract_data`
with the same commands as our function, then make that script executable for our
user using `chmod`.

```bash
% vim ~/bin/extract_data

    # Add the lines that follow
    # Put a 'shebang' here by running ':read !which bash'

file="$1"
n_atoms="$2"
let n_atoms=$n_atoms+6
echo "Relaxation Data"
grep --color=auto '^@' "$file"
echo
echo "Geometry Data"
grep --color=auto -A "$n_atoms" 'Geometry "geometry"' "$file"

    #Save and close the file, now mark it as executable with `chmod`
% chmod u+x ~/bin/extract_data

    #Make sure Bash sees it
% which extract_data
/home/ehildenb/bin/extract_data

    #Test it out
% extract_data dextran_qm_dft.out 24
```

    Relaxation Data
    @ Step       Energy      Delta E   Gmax     Grms     Xrms     Xmax   Walltime
    @ ---- ---------------- -------- -------- -------- -------- -------- --------
    @    0    -686.92664205  0.0D+00  0.02562  0.00530  0.00000  0.00000    124.6
    @    1    -686.93572937 -9.1D-03  0.00495  0.00123  0.05800  0.21419    230.6
    @    2    -686.93688173 -1.2D-03  0.00371  0.00079  0.03159  0.12217    377.7
        #### More lines here ####
       20 H                    1.0000    -0.60963072    -2.48793956     1.59468758
       21 H                    1.0000    -1.82931112    -2.81641725     0.34650697
       22 H                    1.0000     1.71835792    -2.27555426    -0.39890742
       23 H                    1.0000     2.96714682     0.88238211    -0.22383765
       24 H                    1.0000    -0.14249451    -3.77623236    -0.91338242

Cool. We've achieved the same thing as before with the function, only this time
we used a shell script. Now, we can call that script from within `vim` (using the
':!' or ':read !' syntax) to get that data into a file we already have open. Try
it out!

```bash
    #Open vim with the filename you want to save the data as (should start empty)
% vim 'data.out'

    #Type this command in
:read !extract_data dextran_qm_dft.out 24

    #Now suddenly your buffer will have the output of that command in it.
```


Selecting Multiple Files with Globbing
======================================

This is using the the files in directory 'plots'.

Objectives
----------

+ Select only the 'CCFreq' and 'CCTime' plots
+ Select only the 'tmax-140' plots
+ Select only the 'CCFreq' and 'tmax-140' plots zip them up for emailing

Procedure
---------

Select all the 'CCFreq' files or 'CCTime' files using 'globbing', or
'wildcards'. A wildcard is a `*` on the command line, which tells Bash to try to
match anything there. Let's try it. Examine the output of these commands:

```bash
% ls CCFreq*
% ls CCFreq_*
% ls CCFreq_* CCTime_*
```

Notice how the `*` character acts like a wildstar. It will match anything.

Now create a directory and copy the selected files into that directory:

```bash
% mkdir final_plots
% cp  CCFreq_* CCTime_* final_plots
% ls final_plots/
```

    CCFreq_L-8_tmax-10_dt-0.1.png   CCFreq_L-8_tmax-30_dt-0.2.png
    CCTime_L-8_tmax-140_dt-0.5.png  CCFreq_L-8_tmax-10_dt-0.2.png
    CCFreq_L-8_tmax-50_dt-1.png     CCTime_L-8_tmax-140_dt-1.png
    CCFreq_L-8_tmax-120_dt-1.png    CCTime_L-8_tmax-10_dt-0.1.png
    CCTime_L-8_tmax-30_dt-0.2.png   CCFreq_L-8_tmax-140_dt-0.2.png
    CCTime_L-8_tmax-10_dt-0.2.png   CCTime_L-8_tmax-50_dt-1.png
    CCFreq_L-8_tmax-140_dt-0.5.png  CCTime_L-8_tmax-120_dt-1.png
    CCFreq_L-8_tmax-140_dt-1.png    CCTime_L-8_tmax-140_dt-0.2.png

So we can create a directory and using 'globbing' move exactly the files we want
into that directory. Now, try selecting for only the 'tmax-140' plots, including
all three of 'CCFreq', 'CCTime', and 'Board'

```bash
% ls *_tmax-140_*
```

    Board_L-8_tmax-140_dt-0.2.png  CCFreq_L-8_tmax-140_dt-0.2.png
    CCTime_L-8_tmax-140_dt-0.2.png Board_L-8_tmax-140_dt-0.5.png
    CCFreq_L-8_tmax-140_dt-0.5.png CCTime_L-8_tmax-140_dt-0.5.png
    Board_L-8_tmax-140_dt-1.png    CCFreq_L-8_tmax-140_dt-1.png
    CCTime_L-8_tmax-140_dt-1.png

Now select for all the 'CCFreq' and 'tmax-140' plots, copy them into a new
directory called 'presentation_plots', then zip it up using the `zip` command so
you can email it. Make sure to pass the '-r' option to the `zip` command so that
it zips the entire 'presentation_plots' directory.

```bash
% mkdir presentation_plots
% cp CCFreq_*_tmax-140* presentation_plots
% zip -r presentation_plots.zip presentation_plots/
```
