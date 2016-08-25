#!/usr/bin/env python
import timeit
import re

def fraction_to_decimal(dividend, divisor):
    quotient, remainder = divmod(dividend, divisor)
    remainders = [remainder]
    quotients = [quotient]
    rep_start = 0
    
    # Not evenly divided
    while remainder > 0:
        remainder *= 10
        quotient, remainder = divmod(remainder, divisor)
        quotients.append(quotient)
        if remainder in remainders:
            rep_start = remainders.index(remainder)+1
            break
        remainders.append(remainder)
    
    # Format a pretty answer
    solution = str(quotients[0])
    if len(quotients) > 1:
        solution += "."
        
    for i in xrange(1, len(quotients)):
        if i == rep_start:
            solution += "("
        solution += str(quotients[i])
    if rep_start > 0:
        solution += ")"
    
    return solution

def e26(limit):
    regex = re.compile(r'\((\d+)\)')
    longest = [0,""]
    
    for divisor in xrange(1, limit+1):
        r = fraction_to_decimal(1, divisor)
        m = re.search(regex, r)
        if m:
            if len(m.group(1)) > len(longest[1]):
                longest[0] = divisor
                longest[1] = m.group(1)
    print "The divisor of %d has the longest repeating value of %d numbers" %(longest[0], len(longest[1]))
    print longest[1]

def main():
    print "---------- e26 ----------"
    start_time = timeit.default_timer()
    e26(1000)
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
