---
title: Longest Collatz Sequence
...

Taken from Project Euler: https://projecteuler.net/problem=14

Problem
=======

The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Preparation
===========

We should practice our development practice a bit here. Write this program using
vim (or emacs or another similarly powerful editor). Have a second terminal open
for testing the script.

We also want to be able to call the script with any input number as our maximum
number to search up to. In Python, we can do this using `sys.argv`.

```python
#!/usr/bin/python
import sys
print("Num arguments: ", len(sys.argv))
print("Arguments:     ", sys.argv)
```

Assuming the above file is called `test.py`, we can call it with various
arguments and see what it outputs.

```bash
$ ./test_py
Num arguments:  1
Arguments:      ['./test_py']

$ ./test_py 1
Num arguments:  2
Arguments:      ['./test_py', '1']

$ ./test_py 1 hello
Num arguments:  3
Arguments:      ['./test_py', '1', 'hello']

$ ./test_py 1 hello world
Num arguments:  4
Arguments:      ['./test_py', '1', 'hello', 'world']
```

Other languages have similar constructs - in C or C++ we can use the `int argc`
and `char** argv` variables passed to main. In sh-based languages (Bash, zsh,
etc...) we can use position parameters - `$@`, `$1`, `$2` ...

-   First write the above program and play around with it until you feel
    comfortable with how arguments work in Python. We'll use this as a way to
    rapidly test our program.
-   Make sure you have a second terminal opened to the same directory you're
    working in - switch to the second one for testing and back to the first for
    development.

Procedure
=========

Approach 1
----------

We can start by just calculating the Collatz chain for every number between 0
and 1000000, then just figuring out which one is the longest. This solution will
work every time, but is extremely slow. Start by coding this solution and trying
it out on several numbers.

-   Write a function called `attempt_1` which takes a single parameter `max_num`
    and finds the starting number below `max_num` with the longest chain. Have
    it cycle through each number below `max_num` and calculate the Collatz
    chain, storing the final length of it in our final array of lengths.

Approach 2
----------

As stated above, the Collatz chain for 13 is:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

What about the Collatz chain for 20? Perhaps:

    20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Notice anything? It's exactly the same as the tail of the Collatz chain for 13,
which makes sense. Perhaps we can utilize this repetitive nature of the
calculation to speed up the process?

This approach is called 'Dynamic Programming' - instead of re-calculated
intermediate results over and over again we'll tabulate them, allowing us to
calculate them once then just look them up when needed later. This approach
actually isn't quite perfect dynamic programming as we'll see with [#Approach 3]
below, but it's much better than [#Approach 1].

-   Take the code from [#Approach 1] which generates Collatz chains and move it
    into its own function: `calc_collatz_chain`.
-   Write a new function, `attempt_2`, which again cycles through all the
    numbers from 0 to `max_num` and calculates their Collatz chain. This time
    though, have it store the chain-length for every number in the calculated
    chain. Additionally, have it check if the Collatz chain of a number has
    already been calculated, avoiding re-calculations.

Approach 3
----------

Our previous attempt still re-calculates lots of values. We avoid recalculating
a Collatz chain for a number that already has a length assigned to it, but we
still calculate each Collatz chain completely. What if we could stop calculating
a Collatz chain as soon as we hit even just one number that is already defined?

Here, we are accomplishing ideal dynamic programming - we never recalculate an
intermediate result so each number below `max_num` only needs to be hit once for
the entire calculation.

-   Write a new function, `attempt_3`, which cycles through each number from 0
    to `max_num` and generates the Collatz chain for that number. Have the
    chain-generation stop as soon as a number that has already been calculated
    is reached.

Solution
========

The supplied file, `collatz.py` contains the three solutions described here.
