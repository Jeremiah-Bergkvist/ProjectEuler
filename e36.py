#!/usr/bin/env python
import timeit

def e36():
    s = 0
    n = 1
    while n < 1000000:
        binary = format(n, 'b')
        decimal = str(n)
        if decimal == decimal[::-1] and binary == binary[::-1]:
            s += n
            print "Palindrome: %s[10] - %s[2]" %(decimal, binary)
        n += 2
    print "Sum:", s

def main():
    print "---------- e36() ----------"
    e36()
    print "---------------------------"

if __name__ == "__main__":
    main()
