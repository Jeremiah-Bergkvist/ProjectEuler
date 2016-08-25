#!/usr/bin/env python
import timeit

def e31(target=200):
    matches = []
    for one_p in xrange(0, 200+1):
        for two_p in xrange(0, 100+1):
            if one_p + two_p * 2 > target:
                break
            for fiv_p in xrange(0, 40+1):
                if one_p + two_p * 2 + fiv_p * 5 > target:
                    break
                for ten_p in xrange(0, 20+1):
                    if one_p + two_p * 2 + fiv_p * 5 + ten_p * 10 > target:
                        break
                    for twe_p in xrange(0, 10+1):
                        if one_p + two_p * 2 + fiv_p * 5 + ten_p * 10 + twe_p * 20 > target:
                            break
                        for fif_p in xrange(0, 4+1):
                            if one_p + two_p * 2 + fiv_p * 5 + ten_p * 10 + twe_p * 20 + fif_p * 50 > target:
                                break
                            for one_P in xrange(0, 2+1):
                                if one_p + two_p * 2 + fiv_p * 5 + ten_p * 10 + twe_p * 20 + fif_p * 50 + one_P * 100 > target:
                                    break
                                for two_P in xrange(0, 1+1):
                                    total = one_p
                                    total += two_p * 2
                                    total += fiv_p * 5
                                    total += ten_p * 10
                                    total += twe_p * 20
                                    total += fif_p * 50
                                    total += one_P * 100
                                    total += two_P * 200
                                    if total == target:
                                        matches.append((one_p, two_p, fiv_p, ten_p, twe_p, fif_p, one_P, two_P))
    return matches

def main():
    print "---------- e31 ----------"
    start_time = timeit.default_timer()
    print len(e31())
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
