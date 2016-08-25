import math

'''from decimal import Decimal
from decimal import getcontext
getcontext().prec = 1000'''

        # Move up to previous line and clear it
def up_clear():
    sys.stdout.write("\033[F\033[2K")

def find_recurring_sequences(s):
    length = len(s)
    max_width = length // 2
    matches = []
    width = 1
    while width <= max_width:
        index = 0
        while index + width < length:
            if s[index:index+width] == s[index+width: index+width+width]:
                #print "[%d] (%d, %d) (%s, %s) %s == %s" % (width, index, index+width-1, index+width, index+width+width-1, s[index:index+width], s[index+width: index+width+width])
                matches.append(s[index:index+width])
                break
            index += 1
        width += 1
    return matches

def shortest_common_string(s):
    seqs = find_recurring_sequences(s)
    if len(seqs) < 2:
        return None
    while len(seqs) > 1:
        rep = len(seqs[1]) / len(seqs[0])
        if seqs[0] * rep == seqs[1]:
            seqs.pop(1)
        else:
            seqs.pop(0)
    return seqs[0]

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def appendEs2Sequences(sequences,es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result

def cartesianproduct(lists):
    """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
    return reduce(appendEs2Sequences,lists,[])

def primefactors(n):
    '''lists prime factors, from greatest to smallest'''  
    i = 2
    while i<=math.sqrt(n):
        if n%i==0:
            l = primefactors(n/i)
            l.append(i)
            return l
        i+=1
    return [n]

def factorGenerator(n):
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors

def divisors(n):
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[map(lambda x:k**x,range(0,factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors
