def main():
    minimum = 2
    maximum = 100
    terms = {}
    for a in xrange(minimum, maximum+1):
        for b in xrange(minimum, maximum+1):
            terms[a**b] = True
    print len(terms)

if __name__ == "__main__":
    main()
