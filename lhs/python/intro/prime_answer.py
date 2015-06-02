#!/usr/bin/python
# This program runs as ./prime_finder (with correct permissions), but
# incorrectly! The program's goal is to list the prime numbers below a certain
# number using the Sieve of Eratosthenes, discovered around 200 BC. 

# Run the file, and mess around with the testing area below. Debug and
# troubleshoot with print() messages

import math     # math.floor(), eg. math.floor(3.2) = 3, math.floor(-3.3) = -4
import sys

# check if 'num' is prime
def is_prime(num):
    # to check, we divide num by all numbers less than it. If num is divisible
    # by any number, we set flag to False
    flag = True
    for elem in range(2,num):
        if (num/elem).is_integer():
            flag = False
    # [print(elem) for elem in range(num)]
    # note this is the same as directly above!
    return flag # let's say flag = True means prime, flag = False means composite

# return a list of prime numbers less than 'bound'
def prime_list(bound):
    # return a list of all of the prime numbers up to 
    return [elem for elem in range(2, bound) if is_prime(elem)]


# testing area
# ------------

print("23 is prime:", is_prime(23))
print("25 is prime:", is_prime(25))
print()

max_num = 200
if len (sys.argv) > 1:
    max_num = int(sys.argv[1])
print(prime_list(max_num))

# end goal: 
# ---------
# prime_list(30) returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# food for thought:
# -----------------
# how fast does this algorithm run?
# could you improve the speed? do you need to check whether n is divisible by
# every number from 1 to n? 

