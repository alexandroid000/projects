Mathematica Scripting
=====================

A guide to writing Mathematica scripts (no GUI required).


Basic Script
------------

You can save the commands for a Mathematica script in a text file and call it
directly (if made executable).

Script: 'math_script.m'

```mathematica
#!/usr/local/bin/MathematicaScript -script
X=InputString[];
SetDirectory[X];
Export["mathTest.dat",2];
```

Called as:

```bash
$ math_script.m
```

Asks for a string, stores it in X, sets that as the working directory, and saves
the number '2' in the file 'mathTest.dat' at that directory.


Standard Input/Output
---------------------

You can send input to it via standard input and capture standard output as well.

Script: 'math_script.m'

```mathematica
#!/usr/local/bin/MathematicaScript -script
X=InputString[];
Print[X<>" world!"];
```

Called as:

```bash
$ echo 'hello' | math_script.m | grep 'world'
> hello world!
```


Arguments
---------

You can also accept arguments in the script from the command line.

Script: 'math_script.m'

```mathematica
#!/usr/local/bin/MathematicaScript -script
a=$ScriptCommandLine
WriteString[$Output,a[[2]]<>" world!\n"];
WriteString[$Output,"Who am "<>a[[3]]<>"?\n"];
```

Called as:

```bash
$ mathscriptTest hello I
> hello world!
> Who am I?
```
