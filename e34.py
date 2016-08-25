#!/usr/bin/env python
import timeit
import re
import math

def e34():
    n = 3
    t = 0
    while n < 200000:
        s = 0
        for d in map(int, str(n)):
            s += math.factorial(d)
        if n == s:
            print "Digit Factorial: %d == %d" %(n, s)
            t += n
        n += 1
    print "Sum of all: %d" % t

def main():
    print "---------- e34() ----------"
    start_time = timeit.default_timer()
    e34()
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
