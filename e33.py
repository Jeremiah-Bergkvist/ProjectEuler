#!/usr/bin/env python
import timeit
import fractions

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def e33_1():
    # Track wasted loops
    wasted = 0
    fractions = []
    
    # Generate all 2 digit numerators
    for numerator in range(10, 99):
        n1, n2 = divmod(numerator, 10)

        # Skip "trivial" examples
        if n2 == 0:
            continue

        # Denominator generator
        for d1 in range(n2, 10):
            for d2 in range(n1+1, 10):
                denominator = d1 * 10 + d2
                if n2 == d1:
                    if n1 / float(d2) == numerator / float(denominator):
                        fractions.append((numerator, denominator))
                        #print "%d/%d == %d/%d | %f" %(numerator, denominator, n1, d2, n1 / float(d2))
                    else:
                        wasted += 1
                else:
                    wasted += 1
    print "Wasted Loops:", wasted

    r_n = 1
    r_d = 1
    for fraction in fractions:
        n, d = fraction
        r_n *= n
        r_d *= d
        print "%d/%d" %(n, d)
    c = gcd(r_n, r_d)
    r_n /= c
    r_d /= c
    print "----> %d/%d" %(r_n, r_d)


def main():
    print "---------- e33_1() ----------"
    start_time = timeit.default_timer()
    e33_1()
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
