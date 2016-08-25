#!/usr/bin/env python
import timeit

'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25      1               1 * 1   dis 1
20  7  8  9 10      3 5 7 9         3 * 3   dis 2
19  6  1  2 11      13 17 21 25     5 * 5   dis 4
18  5  4  3 12
17 16 15 14 13      101

43 44 45 46 47 48 49    1
42 21 22 23 24 25 26    3 5 7 9         3*3     dis 2
41 20  7  8  9 10 27    13 17 21 25     5*5     dis 4
40 19  6  1  2 11 28    31 37 43 49     7*7     dis 6
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31    261


It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def e28_a(spiral):
    end = spiral * spiral
    
    n = 3
    w = 3
    a = 2
    t = 1
    
    while n <= end:
        t += n
        n += a
        if n >= w * w:
            w += 2
            a += 2
    return t


def e28_1(spiral):
    s=0;
    for i in xrange(0, 501):
        s += 4*(2*i+1)*(2*i+1)-12*i;
    return s-3;

def main():
    print "---------- e28_a ----------"
    start_time = timeit.default_timer()
    print e28_a(1001)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed
    
    print "---------- e28_1 ----------"
    start_time = timeit.default_timer()
    print e28_1(1001)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
