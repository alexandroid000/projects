// Prefix Calculator in C/C++

#include <cstdlib>
#include <iostream>
using namespace std;

// Check if a character is an operator
bool is_operator (char op) {
    bool result = false;
    if (op == '+' || op == '-' || op == '*' || op == '/' || op == '%')
        result = true;
    return result;
}

// Applies an operation to two numbers
int binary_op (char op, int n1, int n2) {
    int result = 0;
    switch (op) {
        case '+':
            result = n1 + n2;
            break;
        case '-':
            result = n1 - n2;
            break;
        case '*':
            result = n1 * n2;
            break;
        case '/':
            result = n1 / n2;
            break;
        case '%':
            result = n1 % n2;
            break;
        default:
            cerr << "Invalid operation " << op << endl;
            break;
    }
    return result;
}

// Evaluate a position
int eval_prefix (int len_expr, char** argv) {
    int result = 0;

    // If there are no more operands left, print error and return 0
    if (len_expr < 1)
        cerr << "No more operands. Check your expression." << endl;

    // If it's an operator, evaluate the two expressions to the right and apply
    else if (is_operator(argv[0][0])) {
        int num1 = eval_prefix (len_expr-1, argv+1);
        int num2 = eval_prefix (len_expr-2, argv+2);
        result = binary_op (argv[0][0], num1, num2);
    }

    // Otherwise, it's just a number, return the number
    else
        result = atoi(argv[0]);

    // Return the result
    return result;
}

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
