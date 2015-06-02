---
title: Intro to Python for Physicists
...


Running Python
==============

Python can be run two ways - as a script or as commands typed into the
interpreter. The interpreter is good for testing out small snippets of code or
ideas, while scripts are good for saving programs that you will use regularly.

For this tutorial, you can either create a python script or enter the commands
into the interpreter.

Interpreter
-----------

You can access the Python interpreter by typing `python` at your terminal
prompt:

```bash
% python
```

Once in the interpreter, you can use any commands you would use in python:

```python
>>> print("Hello, world!")
```

Use `python3` instead to explicitly use python 3 (recommended).

One major difference between python2 and python3 is print statements - in
python3 print is a function and requires parenthesis, such as `print("test")`
while in python 2 we can just do `print "test"`.

Script
------

A python script is just a text file with python commands on the lines in the
file. Blank lines are ignored, wherever a line has a `#`, the rest of the line
is a comment and is ignored.

At the first line in the file, place the "sh-bang". Use `python2` or `python3`
if you want to be explicit (instead of `python`).

```python
#!/usr/bin/python3
# This comment is the second line of the file
print("Hello, world!")
```

The appropriate "sh-bang" can be found by running `which python` (or `which
python3`) in your terminal.

To execute the script, you can run the file using the program `python` (or
`python3` as appropriate). Suppose the script is name "myscript.py" (the ".py"
is not required). At your terminal in the appropriate directory run:

```bash
% python myscript.py
```

Or you can make the script executable by running `chmod u+x myscript.py`, then
call it using the `./` syntax. This **requires** the "sh-bang" mentioned above.

```bash
% chmod u+x myscript.py     # Do once to make executable
% ./myscript.py             # Can be run like this every time
```

What was the difference between running our short "Hello, world!" program in the
interpreter versus in a script? In what instances are scripts useful, and when
is the interpreter useful? 

Basic Commands
==============

Try out these commands in the python shell (interpreter). Verify the outputs
shown here.

Assignment and Arithmetic
-------------------------

Assignment uses the `=` operator. The standard arithmetic operators are
supported (`+`, `*`, `-`, `/`) on number types.

```python
>>> a = 5
>>> print (a)
5
>>> a = 15 + 30
>>> print (a)
45
>>> b = 22
>>> print (a, b)
45 22
>>> print (a*b + (b-a))
967
>>> b = a / b
>>> print (b)
2.0454545454545
>>> b = a / b
>>> print (b)
22.0
```

What if we want to perform a `sqrt` or `sin`? We have to import a module which
has that function defined - the `math` module.

```python
>>> import math             # Somewhere before we use `math`
>>> print (math.sqrt(4))
2.0
>>> print (math.sqrt(15))
3.872983346207417
>>> print (math.sin(math.pi / 2))
1.0
```
We often use exponentials, or other complex math functions, when trying to solve
problems with programming. Find e^10, where e is the base of the natural log.
Then, take log(16), then (log(16) base 2). What function do you use, and how do
you call it?  Google will have all the answers.  (google "python exponential",
for example)

You can also write your own modules. Create a python file called `my_module.py`,
then you can import it using `import my_module`. The file `my_module.py` must be
in the same directory you try to use it in.


Lists
-----

Lists are extremely useful in python!

### Construction

To construct a list, we can define it manually using `[element1, ..., elementn]`
syntax. The elements can be of any type, and of heterogeneous types.

```python
>>> test_list = [1,2,3,4,5]
>>> print (test_list)
[1, 2, 3, 4, 5]
>>> names = ["Bob", "Rob", "Robert", "Bobert"]
>>> print (names)
['Bob', 'Rob', 'Robert', 'Bobert']
>>> things = ["Car", 4, 2.23, "Denver"]
>>> print (things)
['Car', 4, 2.23, 'Denver']
```

You can access a specific element of a list using the `my_list[index]` syntax.
The `index`'th element of the list `my_list` will be returned (the first element
is accessed with `index = 0`). A negative `index` will start from the back of
the list.

```python
>>> test_list = ["a", "b", "c", "d"]
>>> print (test_list[0])
a
>>> print (test_list[2])
c
>>> print (test_list[-2])
c
>>> print (test_list[-3])
b
```

### Operators and Functions

The `+` operator on two lists extends the first list with the second list.

```python
>>> list1 = [1,2,3]
>>> list2 = [4,5,6]
>>> print (list1, list2, list1 + list2)
[1, 2, 3] [4, 5, 6] [1, 2, 3, 4, 5, 6]
```

The `append` function on a list adds an element to the end of the list:

```python
>>> test_list = [1,2,3]
>>> print (test_list)
[1, 2, 3]
>>> test_list.append(4)
>>> print (test_list)
[1, 2, 3, 4]
```
The `len` function on a list tells you how long it is.

```python
>>> print (len ([1,2,3,4,5]))
5
```

In your shell, create some test lists and compare the behavior of `append` and
`extend`. What happens when you `append` lists to lists?


### Strings

Strings are a special case of a python `list` where the elements are `char`'s.
You can create a `string` in python using quotes (single or double). You can
concatenate strings using the `+` operator.

```python
>>> my_string = "hello"
>>> print (my_string)
hello
>>> string_two = " world"
>>> print (my_string + string_two)
hello world
>>> print (len (my_string))
5
```

In the shell, create a test string. How would you access the first letter of
that string, with list syntax?

### List Slices

List slices can be used to select a certain subset of another list. They use the
`my_list[start:end:inc]` syntax. The new list starts at the `start` index, goes
until the `end` index (but does not include it), making jumps of `inc`. By
default, `start` is `0`, `end` is `len(my_list)`, and `inc` is `1`.

```python
>>> test_list = [1,2,23,2,38,48,54,90]
>>> print (test_list[3:5])
[2, 38]
>>> print (test_list[:7])       # Everything up to element 7
[1, 2, 23, 2, 38, 48, 54]
>>> print (test_list[2:7:2])    # Every second element from 2-7
[23, 38, 54]
>>> print (test_list[::-1])     # Reverse a list
[90, 54, 48, 38, 2, 23, 2, 1]
```

In the shell, try the following:

- reverse elements 1 through 4 in a test list
- use list slices to extract the first 4 letters in a string

Loops
=====

To build lists and perform other calculations, we use loops. A python `for` loop
iterates through a `list` provided by the user. This `list` could be a range of
numbers, or lines in a file, or any list.

```python
>>> for i in [1,2,"hello",4,19]:
...     print (i, i+i)          # Notice extra space before print
...
1 2
2 4
hello hellohello
4 8
19 38
```

Quite often we need to add up numbers in a loop. If we wanted to sum the numbers
from 3 to 5, we need to create a range. The `range(start,end,inc)` function will
produce all numbers up to, but not including, `end` and will increment by `inc`
(1 by default). Also note that we need to initialize the `tot` variable before
the loop. The `tot += elem` operation is shorthand for `tot = tot + elem`.

```python
>>> print (range(3,6))
range(3, 6)                     # Most useless output ever
>>> for i in range(3,6):
...     print (i)               # Don't forget extra space before print
...
3
4
5
>>> tot = 0                         # Let's calculate a total
>>> for elem in range(302,6000):
...     tot += elem
...
>>> print (tot)
17951549
```

Notice that the statements which are "inside" the loop must be indented. There
is no rule saying you have to use spaces or tabs, but you have to be
**consistent**. This enforces easier-to-read code.

Build lists using for loop
--------------------------

### Append method (bad)

This method works best when you don't know how long your list will be, but you
know it will be short. The function `append` is not as efficient as some of the
later methods.

```python
>>> app_list = []
>>> data_to_app = [1,3,5,8,1000]
>>> for elem in data_to_app:
...     app_list.append(elem)
>>> print(app_list)
[1, 3, 5, 8, 1000]
```

In the shell, take the following list of lists and create one flattened list
using a for loop and the `+` operator:

```python
>>> to_flatten = [[1,2,3],["wat"],[0.2,1000]]
```

### Update values of pre-existing list

In this example, we allocate all the memory for the list ahead of time and
update values after. This is more efficient than appending to an existing list
every time (the lists memory only needs to be allocated once). The syntax
`[0]*num` creates a list of `0`'s that is `num` long.

```python
>>> xs = [1,3,5,10,15]
>>> vs = [0]*(len(xs)-1)            # Allocate memory for velocities
>>> dt = 1
>>> for t in range(len(vs)):
...     dx = xs[t+1] - xs[t]
...     vs[t] = dx/dt
...
>>> print(vs)
```

The loop above took a list of positions and, assuming constant time intervals,
created a list of velocities. On your own, take that list of velocities and make
a loop to calculate a list of accelerations, including allocating memory before
the loop. Your resulting list should be `[0.0, 3.0, 0.0]`.


### List comprehensions

This is the most compact and "pythonic" way to build lists. It is also usually
the fastest. List comprehensions need to be used with an existing list to build
from, which can be a built-in like the `range(start, stop, inc)` function.

Here are some examples of list comprehensions. Notice that you can evaluate
general expressions (even calling functions) in the list comprehension.

```python
>>> simple_range = [x for x in range(5)]
>>> print (simple_range)
[0, 1, 2, 3, 4]
>>> squared = [i*i for i in simple_range]
>>> print (squared)
[0, 1, 4, 9, 16]
>>> import math
>>> sqrts = [math.sqrt(element) for element in range(12, 15)]
>>> print (sqrts)
[3.4641016151377544, 3.605551275463989, 3.7416573867739413]
```

We can also add conditional statements, for example to grab all multiples of
five. The `%` operator - called `modulus` - calculates the remainder after
division (eg. `5 % 3 == 2`, `17 % 7 == 3`, `10 % 2 == 0`).

```python
>>> simple_range = [x for x in range(44) if x % 5 == 0]
>>> print (simple_range)
[0, 5, 10, 15, 20, 25, 30, 35, 40]
>>> squares_under_fifty = [n*n for n in range(51) if n*n <= 50]
>>> print (squares_under_fifty)
[0, 1, 4, 9, 16, 25, 36, 49]
```

We can do mathematical operations within the list comprehension. In the shell,
write your own list comprehension which is all the integers from 10 to 20,
squared.

As a final example, let's write a quick `flatten` function which takes a list of
lists and creates a list with one less level of nesting:

```python
>>> list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
>>> flattened = [x for sublist in list_of_lists for x in sublist]
>>> print (flattened)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This is some crazy syntax, so take a while to think about how this works. It
might help to see the equivalent `for` + `append` loop expression:

```python
>>> list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
>>> flattened = []
>>> for sublist in list_of_lists:   # Appears first in nested comprehension
...     for x in sublist:           # Appears second
...         flattened.append(x)
...
>>> print (flattened)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

List comprehensions are much faster than for loops + append, especially for
larger lists!


Functions
=========

We can define functions to encapsulate a general computation. Functions are
useful for creating modular easy-to-maintain and easy-to-test code. Never write
the same code in two or more places in a program! Create small generic functions
that work on a variety of inputs, and use them all together to write your
program. This will lead to more readable and reliable code.

Remember, consistent indentation is important in python functions!

Remember your `my_module.py` file you created? Copy the following function into
it, then save and run `import my_module` in a python shell in the same
directory. Now, you should be able to call `my_module.sum_ints`. Try running
this function with different integers for "beginning" and "end" and see what it
prints.

```python
>>> def sum_ints(beginning, end):
...     tot = 0
...     for elem in range(beginning, end+1):
...         tot += elem
...     return tot
...
>>> sum_ints(3, 5)
12
>>> sum_ints(1, 100)
5050
>>> sum_ints(1000, 1243)
273646
```

Now write a function, `f(x,y) = x^2 + y*x`.

```python
>>> def f (x, y):
...     # Some code here to return `x^2 + y \times x`
...
>>> f(3,3)
18
>>> f(3,4)
21
>>> f(2,4)
12
>>>
```

Write a function which takes two vectors (lists of numbers) and returns the
dot-products of them - `dot_prod (A, B) = A . B`.

```python
>>> def dot_prod (A, B):
...     # Generate vector `C = A . B` first
...     # Then sum the elements of that vector
...
>>> dot_prod([1,2,3],[4,5,6])   # A . B = (1*4) + (2*5) + (3*6)
32
>>> dot_prod([1,0,0],[0,1,0])   # Orthogonal vectors
0
>>> dot_prod([1,0,0,1,1],[0,1,1,0,1]) # Near orthogonal
1
```

Now write a function which multiplies a matrix (vector (row) of vectors
(columns)) with a column vector (list). We want the function
`mat_by_vect (A, x) = A . x`.  The result of `A . x` is a vector where each
element is the corresponding row element `a` of `A` dot-producted with `x`.
Remember, you just wrote a dot_prod function which you can use here!

```python
>>> def mat_by_vect (A, x):
...     # Return `A . x`, which is a vector
...
>>> mat_by_vect ([[1,0],[0,1]], [1,3])
[1, 3]
>>> mat_by_vect ([[0,1],[1,0]], [1,3])
[3, 1]
>>> mat_by_vect ([[.5,.5],[2,3]], [1,3])
[2.0, 11]
```

Now write a function to multiply two matrices togother - `mat_by_mat (A, B)`.
Assume that you are given matrix `A` as a list of rows, and matrix `B` as a list
of columns. You should return the resultant matrix as a list of columns.

```python
>>> def mat_by_mat (A, B):
...     # Return a matrix (list of lists) `C = A . B`
...     # You should use the function `mat_by_vect`
...
>>> mat_by_mat ([[1,0],[0,1]], [[2,3],[5,8]])   # Identity
[[2, 3], [5, 8]]
>>> mat_by_mat ([[0,1],[0,1]], [[2,3],[5,8]])   # Second row
[[3, 3], [8, 8]]
>>> mat_by_mat ([[0,-1],[1,0]], [[2,3],[5,8]])  # Rotate 90
[[-3, 2], [-8, 5]]
```

Now write a function `transpose` which takes in a matrix defined as a list of
columns and returns it defined as a list of rows. We may need to transpose a
matrix to multiply it with another matrix.


Conditionals
============

Conditional expressions are useful for controlling operations. `if` statements
will only execute if their condition evaluates to `True`.

```python
>>> def eq(a, b):
...     if (a == b):
...         print("Values are equal!")
...     else:
...         print("Values are not equal!")
...
>>> eq (3,2)
Values are not equal!
>>> eq (3,3)
Values are equal!
```

We can add `elif` statements after the `if` and before the `else` to check more
conditions. `if` conditions can stand on their own, without an `else` clause.

For practice, write a piecewise function using `if`, `elif`, and `else`.

    f(x) =
        x,      if x < 10
        x^2     if 10 <= x < 100
        2*x     otherwise

```python
>>> def f(x):
...     # Use `if - elif - else` statement
...     # for three separate cases.
...
>>> f(3)
3
>>> f(30)
900
>>> f(300)
600
```

Dictionaries
============

Want to store your data and access it with something other than integer
indices? For example, you have a table of excitation energies and you want to
be able to look up the energy by element name. You can store data in a
dictionary, which looks like this:

```python
elem_dict = {"hydrogen":1, "helium":1.23, "carbon":1.45}
```
We can access elements of the dictionary with its keys, the values before the
colons. Accessing a dictionary with a key returns the corresponding value, the
data after the colon. So `elem_dict["carbon"]` will return 1.45. Assigning a
value to a key in a dictionary will overwrite the previous value, if it exists,
or will add a new `key:value` pair if the key does not exist. So we can add a
value to our previous dictionary with:

```python
>>> elem_dict["iron"] = 2
```

We can use the function keys() to access a list of all the keys in a dictionary,
such as with `elem_dict.keys()`.


Command-line Arguments
======================

What if we want to run our program with different values from the command line?
To do this, we need to `import sys`, which gives us access to system
information. Try adding these following lines to your python file and running
your script from the command line with different arguments. What's the first
element of the arguments list?

```python
print("Num arguments: ", len(sys.argv))
print("Arguments:     ", sys.argv)
```

```bash
% python my_module.py "test" "arguments" 5
```
