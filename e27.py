#!/usr/bin/env python
import timeit
import sys
import math
'''
Euler discovered the remarkable quadratic formula:

n*n + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41*41 + 41 + 41 is clearly
divisible by 41.

The incredible formula  n*n - 79n + 1601 was discovered, which produces
80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n*n + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
'''

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    
    primes_dict = {}
    for i in xrange(len(sieve)):
        if sieve[i]:
            primes_dict[i] = i
    return primes_dict
    #return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def e27(a_max, b_max):
    primes_list = rwh_primes1(a_max * b_max)
    longest_n = 0
    longest_a = 0
    longest_b = 0
    for a in xrange(-a_max, a_max):
        for b in xrange(-b_max, b_max):
            n = 0
            while abs(n * n + a * n + b) in primes_list:
                n += 1
            if n > longest_n:
                longest_n = n
                longest_a = a
                longest_b = b
    
    # Display result
    print "A sequence of %d primes was generated by %d and %d, the product is %d" % (longest_n, longest_a, longest_b, longest_a * longest_b)
    n = 0
    while abs(n * n + longest_a * n + longest_b) in primes_list:
        print "%4d" %(abs(n * n + longest_a * n + longest_b)),
        if n % 8 == 0:
            print ""
        elif n % 4 == 0:
            print "  ",
        n += 1
    print

def main():
    print "---------- e26 ----------"
    start_time = timeit.default_timer()
    e27(1000, 1000)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
