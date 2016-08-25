#!/usr/bin/env python
import timeit
import re
import math

# Positive y -> left
# Negative y -> right
def rotate(l, y=1):
    y = 1
    if len(l) == 0:
        return l
    y = y % len(l)
    return l[y:] + l[:y]

def primes_list(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def all_rotations(n):
    rotations = [n]
    digits = str(n)
    num_rotations = len(digits)
    while num_rotations > 1:
        digits = ''.join(rotate(digits, 1))
        rotations.append(int(digits))
        num_rotations -= 1
    return rotations

def e35_1(limit=1000000):
    # Create a dictionary of primes
    primes = {}
    for prime in primes_list(limit):
        primes[prime] = True
    
    # Process each prime in the dict until only circulars remain
    circulars = {}
    for prime in primes:
        # Skip if already circular
        if prime in circulars:
            continue
            
        # Get a single key from the dict and it's rotations
        rotations = all_rotations(prime)

        # Process each rotation; determine prime eligibility
        circular = True
        for num in rotations:
            if num not in primes:
                circular = False
                break
            
        # Remove non-circular prime
        if circular:
            for prime in rotations:
                circulars[prime] = True

    # Done calculating, show results
    i = 0
    width = 8
    for key in circulars:
        if i % width == 0 and i != 0:
            print ""
        print "%7d" % key,
        i += 1
    if i % width != 0:
        print ""
    print "Entries: ", len(circulars)

def e35_a(limit=1000000):
    # Create a dictionary of primes
    primes = {}
    for prime in primes_list(limit):
        primes[prime] = True
    
    # Process each prime in the dict until only circulars remain
    circulars = 0
    for prime in primes:
        # Get a single key from the dict and it's rotations
        rotations = all_rotations(prime)

        # Process each rotation; determine prime eligibility
        circular = True
        for num in rotations:
            if num not in primes:
                circular = False
                break
            
        # Remove non-circular prime
        if circular:
            circulars += 1

    # Done calculating, show results
    print "Entries: ", circulars

def main():
    print "---------- e35_1() ----------"
    start_time = timeit.default_timer()
    e35_1(1000000)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed
    print "---------- e35_a() ----------"
    start_time = timeit.default_timer()
    e35_a(1000000)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
