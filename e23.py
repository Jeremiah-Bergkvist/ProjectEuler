#!/usr/bin/env python
import timeit
import helper
'''
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
'''

def e23():
    limit = 28123
    start = 12
    
    # Generate abundant numbers dictionary
    abundants = {}
    while start < limit:
        divs = helper.divisors(start)[0:-1]
        nsum = sum(divs)
        if sum(divs) > start:
            abundants[start] = (divs, nsum)
        start += 1
    
    # Check for non abundant sums
    non_abundant_sums = []
    start = 1
    while start <= limit:
        non_abundant_sum = False
        # Subtract an abundant
        for abn in abundants:
            if start - abn in abundants:
                non_abundant_sum = True
                break
        if not non_abundant_sum:
            non_abundant_sums.append(start)
        start += 1
    
    print sum(non_abundant_sums), "should be", 4179871
    

def main():
    print "---------- e23 ----------"
    start_time = timeit.default_timer()
    e23()
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
