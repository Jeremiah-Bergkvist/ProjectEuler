def ispan(num):
    if len(num) != 9:
        return False
    nums = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    for digit in str(num):
        nums[digit] += 1
    for num in nums:
        if nums[num] > 1 or nums["0"] > 0:
            return False
    return True

def main():
    used_multipliers = {}
    pan_digitals = {}
    n1 = 1
    # 1 digit * 4 digit
    while n1 < 9:
        n2 = 9876
        while n2 > 1000:
            n3 = n1 * n2
            if ispan( str(n1) + str(n2) + str(n3) ):
                pan_digitals[n3] = (n1, n2)
                print n1, n2, n3
            n2 -= 1
        n1 += 1

    # 2 digit * 3 digit
    n1 = 10
    while n1 < 100:
        n2 = 1000
        while n2 > 100:
            n3 = n1 * n2
            if ispan( str(n1) + str(n2) + str(n3) ):
                pan_digitals[n3] = (n1, n2)
                print n1, n2, n3
            n2 -= 1
        n1 += 1
    
    print pan_digitals
    print "Unique entries :", len(pan_digitals)
    total = 0
    for key in pan_digitals:
        total += key
    print "Sum of products:",  total

if __name__ == "__main__":
    main()
