#!/usr/bin/python
# This program runs as ./prime_finder (with correct permissions), but
# incorrectly! The program's goal is to list the prime numbers below a certain
# number using the Sieve of Eratosthenes, discovered around 200 BC.

# Run the file, and mess around with the testing area below. Debug and
# troubleshoot with print() messages

# you can import this file into the shell with "import prime_finder" and then
# test individual functions

# end goal:
# ---------
# prime_list(30) returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


import math # so we can use the floor function! called with math.floor(2.33)

# check if 'num' is prime
def is_prime(num):
    # to check, we divide num by all numbers less than it. If num is divisible
    # by any number, we set flag to False
    flag = True

    # use is_integer to tell what sort of data type a number is (useful for
    # divisibility)
    print("ints? ", (4.0).is_integer(), (4.3).is_integer(), '\n')
    # can you implement this same line using modulus (%) instead?

    for elem in range(1,num):
        if elem == 4:
            print("elem is 4")
        print(elem)

    # [print(elem) for elem in range(num)]
    # note this is the same as directly above! 

    return flag # let's say flag = True means prime, flag = False means composite

# return a list of prime numbers less than 'bound'
def prime_list(bound):
    # return a list of all of the prime numbers up to
    return [elem for elem in range(bound) if elem > 10]


# example test commands
# ------------
print("Is 15 prime?")
print(is_prime(15))

print("All primes under 30:")
print(prime_list(30))

# food for thought:
# -----------------
# how fast does this algorithm run?
# could you improve the speed? do you need to check whether n is divisible by
# every number from 1 to n? 

