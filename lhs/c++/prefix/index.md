Prefix Calculator
=================

We're going to build a Prefix calculator using C++! It will be great.

Background
----------

So what is a prefix calculator? It's a calculator that accepts inputs in
'prefix' notation. Prefix notation is nice because the order of operations is
unambiguous without needing parentheses.

We are used to 'infix' notation. Infix notation places the operators (such as
'+' and '-') between the two operands (such as '3' or '(5 - 6)'). A prefix
calculator places the operator before the two operands.

```
| Infix:            | Prefix:
| 3 + 5             | + 3 5
| 2 * (a + 4)       | * 2 + a 4
| (3 / 8) + pi      | + / 3 8 pi
```

So, to evaluate a prefix-notation expression, we look at the left-most
symbol. If it's a number, we stop and are done. If it's an operator, we apply
that operator to the two symbols to its right after making the same evaluation
for those symbols. The process looks like this:

```
* 2 + 3 4
^-------- We need to multiply '2' and the result from this '+' operator
* 2 + 3 4
    ^---- So we first evaluate the '+' operator, which has operands '3' and '4'
* 2 7
    ^---- We've replaced the '+' with the result of its operation
* 2 7
^-------- So now we can actually apply the '*' operator to the '2' and the '7'
14
^^------- We replace the '*' with the result of it's operation
```

In the end, the left-most character became a number, so we can stop evaluation.

Preparing
---------

### Compiling

First, we want to setup our development environment. We'll be making one file,
`prefix.cpp`, which we'll compile using `g++` to an executable called `prefix`.
C/C++ are compiled languages, meaning we must compile them before running them.
The command to compile `prefix.cpp` into an executable `prefix` is:

```bash
$ g++ prefix.cpp -o prefix
```

We'll have another terminal open to the same directory where we'll run this
command as well as test out our program.

### Makefile

Instead of compiling from the command line every time, we can create a
`makefile` which stores the compilation commands for us. This can be incredibly
useful when your project starts to grow to multiple files and even directories.

Inside a file called `makefile`, put the lines (note that the space before `g++`
*MUST* be a tab character, *NOT* spaces):

```
all : prefix

prefix : prefix.cpp
    g++ prefix.cpp -o prefix
```

To run this file, we call the command `make`:

```bash
$ make
g++ prefix.cpp -o prefix
```

Make looks through the `makefile` for the rule `all`. We've told it to build
`prefix` for `all` with the first line. The third line is the rule for building
`prefix` - it says "If the file `prefix` is older than the file `prefix.cpp`,
run the following command to update it". The command we supply is `g++
prefix.cpp -o prefix`.

Now, we can just setup our compilation process once for our entire project, and
just type `make` to build the entire thing. Neato!

Procedure
---------

We'll assume that our calculator only deals with integers, making the
programming of it much simpler for us. Division will obviously break.

### Operators

-   Addition            : +
-   Subtraction         : -
-   Multiplication      : *
-   Division            : /
-   Modulus (Remainder) : %

We need to write a function which decides if a character is an operator (simply
compares it to this list of operators). We also need to write a function which
actually runs the calculation for each operator.

-   Write the `is_operator` function which takes a `char` and returns `true` if
    it is an operator and `false` if not.
-   Write the `binary_op` function which takes an operator (`char` type), and
    two operands (`int` types), and returns the resulting integer of the
    calculation.

When writing the second function, `binary_op`, we can use the `switch - case`
syntax of C++ to simplify the whole function. Notice that there is a lot of
repetitive code there - use your knowledge of vim to make developing this
portion of code easier. Write out the `case` statement for one operator, then
yank and paste it several times over to get templates for the others. Then use
vim substitution (`:s/search/replace/g` command) to setup the correct operators
for each.

### Evaluate a Prefix-Notation Expression

In evaluating a prefix-notation expression, we're going to employ a recursive
strategy. In our function `eval_prefix`, we'll look at our current position (the
left-most position), and decide if it's an operator. If it is an operator, we'll
apply that operator to the two operands to the right of it by calling the
`eval_prefix` function on each of those operands recursively.

There are several things we need to check:

-   Are there no more operators/operands left? Then print an error and return 0.
-   Is this a number? Then just return the numer.
-   Is this an operator? Then apply the operator to the two operands to its
    right by calling `eval_prefix` on each of those operands. The same logic
    laid out here will be applied to the evaluation of each of those operands.

### Run the Program

We want our program to accept input of the form:

```bash
$ ./prefix + 2 3
$ ./prefix '*' 2 + 5 6
```

In a C/C++ program, the first chunk of code to be executed will be in the
`main` function, so we need to affect the input-handling logic in this main
fnuction, then call our `eval_prefix` from there. I've supplied a simple sample
`main` function here:

```c
// Main always takes two arguments, `int argc` and `char** argv`, and return int
int main(int argc, char** argv) {
    // Greet user - check for correct arguments
    cout << "Prefix Calculator" << endl;
    if (argc < 2) {
        cerr << "Must supply at least one operand." << endl;
        return 1;
    }

    // Print out what we think the expression is
    cout << "Expression: ";
    for (int i = 1; i < argc; ++i)
        cout << argv[i] << " ";
    cout << endl;

    // Calculate and print the result
    cout << "Result: " << eval_prefix (argc-1, argv+1) << endl;
    return 0;
}
```
