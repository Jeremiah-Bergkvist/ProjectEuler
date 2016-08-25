#!/usr/bin/env python
import timeit
from itertools import count

def wpsieve():
    """prime number generator
    call this function instead of roughing or turbo"""
    whlSize = 11
    initPrms, gaps, c = wheel_setup(whlSize)

    for p in initPrms:
        yield p

    primes = turbo( 0, ( gaps, c) )

    for p, x in primes:
        yield p

def prod(seq, factor=1):
    "sequence -> product"
    for i in seq:factor*=i
    return factor

def wheelGaps(primes):
    """returns list of steps to each wheel gap
    that start from the last value in primes"""
    strtPt= primes.pop(-1)#where the wheel starts
    whlCirm= prod(primes)# wheel's circumference

    #spokes are every number that are divisible by primes (composites)
    gaps=[]#locate where the non-spokes are (gaps)
    for i in xrange(strtPt, strtPt+whlCirm+1, 2):
        if not all(map(lambda x:i%x,primes)):continue#spoke 
        else: gaps.append(i)#non-spoke

    #find the steps needed to jump to each gap (beginning from the start of the wheel)
    steps=[]#last step returns to start of wheel
    for i,j in enumerate(gaps):
        if i==0:continue
        steps.append(int(j - gaps[i-1]))
    return steps

def wheel_setup(num):
    "builds initial data for sieve"
    initPrms= roughing(num)#initial primes from the "roughing" pump
    gaps = wheelGaps(initPrms[:])#get the gaps
    c= initPrms.pop(-1)#prime that starts the wheel

    return initPrms, gaps, c

def roughing(end):
    "finds primes by trial division (roughing pump)"
    primes=[2]
    for i in range(3, end+1, 2):
        if all(map(lambda x:i%x, primes)):
            primes.append(i)
    return primes

def turbo(lvl=0, initData=None):
    '''postponed prime generator with wheels (turbo pump)
    Refs:  http://stackoverflow.com/a/10733621
           http://stackoverflow.com/a/19391111'''
    gaps, c = initData
    yield (c, 0)
    compost = {}#found composites to skip
    #store as current value: (base prime, wheel index)
    ps=turbo(lvl+1, ( gaps, c))
    p,x = next(ps)
    psq=p*p
    gapS = len(gaps)-1
    ix=jx=kx=0#indices for cycling the wheel
    def cyc(x):return 0 if x>gapS else x #wheel cycler
    while True:
        c += gaps[ix]#add next step on c's wheel
        ix = cyc(ix+1)#and advance c's index
        bp, jx = compost.pop(c, (0,0))#get base prime and its wheel index
        if not bp:
            if c < psq:#prime
                yield c, ix#emit index for above recursive level
                continue
            else:
                jx = kx#swap indices as a new prime comes up
                bp = p
                p, kx =next(ps)
                psq = p*p
        d = c + bp*gaps[jx]#calc new multiple
        jx = cyc(jx+1)
        while d in compost:
            step = bp*gaps[jx]
            jx = cyc(jx+1)
            d += step
        compost[d]= (bp, jx)
        
def all_shifts(n):
    left_shifts = []
    right_shifts = []
    strnum = str(n)
    
    # Left shifts
    for i in range(1,len(strnum)):
        left_shifts.append(int(strnum[i::]))
    
    # Right shifts
    for i in range(1,len(strnum)):
        left_shifts.append(int(strnum[:i:]))

    return [n] + left_shifts + right_shifts

def primes_list(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def e37_1():
    found = {}
    limit = 1000000
    
    # Generate dictionary of primes
    primes = {}
    for prime in primes_list(limit):
        primes[prime] = True
    for prime in primes:
        if prime < 10:
            continue
        
        valid = True
        shifts = all_shifts(prime)
        for test in shifts:
            if test not in primes:
                valid = False
                break
        if valid:
            found[prime] = True
    
    total = 0
    index = 1
    for trunc in sorted(found):
        total += trunc
        print "%d) %d" %(index, trunc)
        index += 1
    print "Sum is:", total

def e37_a():
    found = {}
    primes = {}
    for prime in wpsieve():
        primes[prime] = True
        if prime < 10:
            continue
        valid = True
        shifts = all_shifts(prime)
        for test in shifts:
            if test not in primes:
                valid = False
                break
        if valid:
            found[prime] = True
        if len(found) == 11:
            break
    
    total = 0
    index = 1
    for trunc in sorted(found):
        total += trunc
        print "%d) %d" %(index, trunc)
        index += 1
    print "Sum is:", total

def main():
    print "---------- e37_1() ----------"
    start_time = timeit.default_timer()
    e37_1()
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

    print "---------- e37_a() ----------"
    start_time = timeit.default_timer()
    e37_a()
    elapsed = timeit.default_timer() - start_time
    print "---------- Elapsed Time: %f ----------\n" % elapsed

if __name__ == "__main__":
    main()
