
def main():
    # Maximum value needed to get calculate
    # 9**5 == 59049
    # 59049 * 5 == 295245
    power = 5
    start = 2
    stop = power * 9**5
    matches = []
    for x in xrange(start, stop+1):
        xstr = str(x)
        xsum = 0
        for y in xrange(len(xstr)):
            xsum += int(xstr[y]) ** power
            if xsum > x:
                break
        if xsum == x:
            matches.append(xsum)
    xsum = 0
    for x in xrange(len(matches)):
        print "[!]", matches[x]
        xsum += matches[x]
    print "sum", xsum

if __name__ == "__main__":
    main()