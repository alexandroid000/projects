---
title: Linux Shell Commands Cheatsheet
...


Basic Commands
==============

Navigation, file/directory manipulation
---------------------------------------

```bash
% ls    # list files (`ls -lah` for more info)
% cd    # change directory (`cd ..` for parent directory)
% mv    # move/rename files
% mkdir # make directories
% touch # create empty file
% rm    # remove files (`rm -r` for directories)
```

Viewing a file
--------------

```bash
% cat   # display whole file
% less  # page whole file (`j` and `k` to navigate, `/` to search)
```

Editing a File
--------------

```bash
% nano  # basic
% vim   # advanced
% emacs # advanced
```

Accessing servers (supercomputers, school computers)
----------------------------------------------------

```bash
% ssh   # Secure shell - login to remote server
% scp   # Secure copy - copy file to remote server
```

For Windows, you can use "Putty.exe" and "PSCP.exe". I don't know if these are
the best ones, but they are simple and standalone (don't require and install).


Shell
=====

Piping and Redirection
----------------------

```bash
% command > file        # command stdout to file (overwrite)
% command >> file       # command stdout to file (append)
% command < file        # file to command stdin
% command1 | command2   # command1 stdout to command2 stdin
```

Loops
-----

```bash
# For loop
% for i in literal $variable ${array[@]}; do
    > echo $i
    > done
% j="10"
% while [[ "$j" != "0" ]]; do
    > echo $j
    > let i=$j-1
    > done
```

Useful Commands
===============

Select Output
-------------

```bash
% grep 'regexp' # print stdin lines which match 'regexp'
% tail -n45     # display the last 45 lines of stdin
% head -n38     # display the first 38 lines of stdin
```

Manipulate Output
-----------------

```bash
% sort -k3      # sort stdin by third field
% cut -d' ' -n3 # print only third field of stdin
% tr -d '\n'    # delete every newline '\n' of stdin
% tr 'search' 'replace'     # replace 'search' of stdin with 'replace'
% sed 's/search/replace'    # replace 'search' in stdin with 'replace'
```

Misc utilities
--------------

```bash
% xargs -I item command item    # call 'command' for each 'item' on stdin
% rename "s" "r" file           # replace 's' with 'r' in 'file's filename
% htop              # display running processes/cpu usage
% top               # htop not available (less good)
% ps                # display running process info
% pkill proc_name   # kill proc_name process
```
