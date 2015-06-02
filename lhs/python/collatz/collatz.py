#!/usr/bin/python

# Taken from Project Euler: https://projecteuler.net/problem=14
#
#   # Longest Collatz sequence
#
#   The following iterative sequence is defined for the set of positive integers:
#
#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)
#
#   Using the rule above and starting with 13, we generate the following
#   sequence:
#
#       13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#   It can be seen that this sequence (starting at 13 and finishing at 1)
#   contains 10 terms. Although it has not been proved yet (Collatz Problem), it
#   is thought that all starting numbers finish at 1.
#
#   Which starting number, under one million, produces the longest chain?
#
#   NOTE: Once the chain starts the terms are allowed to go above one million.


import sys

# Calculate a single collatz chain
def calc_collatz_chain(start_num):
    if start_num == 0:
        return [-1]
    chain = [start_num]
    while chain[-1] != 1:
        if chain[-1] % 2 == 0:
            chain.append(int(chain[-1] / 2))
        else:
            chain.append(3 * chain[-1] + 1)
    return chain

# Naive approach - re-calculate a chain for every number
def attempt_1(max_num):
    chain_lengths = [len(calc_collatz_chain(start)) \
            for start in range(max_num)]
    # Return index of max value
    return chain_lengths.index(max(chain_lengths))


# Smarter approach - semi-dynamic programming
def attempt_2(max_num):
    chain_lengths = [-1] * max_num
    for i in range(1, max_num):

        # Only calculate a chain if this number hasn't already been calculated
        if chain_lengths[i] == -1:
            curr_chain = calc_collatz_chain(i)

            # Now store the entire calculated chain, not just the first number
            while len(curr_chain) > 0:
                if curr_chain[0] < len(chain_lengths):
                    chain_lengths[curr_chain[0]] = len(curr_chain)
                curr_chain.pop(0)
    # Return index of max value
    return chain_lengths.index(max(chain_lengths))


# Even smarter approach - full dynamic programming
def attempt_3(max_num, chain_lengths=None):
    chain_lengths = [-1] * max_num
    chain_lengths[0] = 1
    chain_lengths[1] = 0
    for i in range(max_num):

        # Calculate the chain up until we hit a number that's already calculated
        curr_num = i
        curr_chain = []
        while curr_num >= max_num or chain_lengths[curr_num] == -1:
            curr_chain.append(curr_num)
            if curr_num % 2 == 0:
                curr_num = int(curr_num / 2)
            else:
                curr_num = 3 * curr_num + 1

        # Add the calculated partial-chain to our list
        add_length = chain_lengths[curr_num]
        count = 0
        while len(curr_chain) > 0:
            count += 1
            if curr_chain[-1] < len(chain_lengths):
                chain_lengths[curr_chain[-1]] = add_length + count
            curr_chain.pop()
    # Return index of max value
    return chain_lengths.index(max(chain_lengths))

# Max number to check up to
if len(sys.argv) < 2:
    sys.exit(1)

# Try different methods
print(attempt_1(int(sys.argv[1])))
print(attempt_2(int(sys.argv[1])))
print(attempt_3(int(sys.argv[1])))
