#!/usr/bin/env python
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3,
4, and 5, giving the pandigital, 918273645, which is the concatenated
product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n)
where n > 1?
'''

def pandi_validate(n):
    counts = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
    }
    for digit in str(n):
        counts[digit] += 1
        if counts[digit] > 1:
            return False
    for key in counts:
        if counts[key] != 1:
            return False
    return True

def pandi_potential(n):
    counts = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
    }
    if len(n) > 9:
        return False
    
    for digit in str(n):
        counts[digit] += 1
        if counts[digit] > 1:
            return False
    
    return True

def main():
    n = 1
    n_max = 987654321

    for n in xrange(1, n_max+1):
        n 

if __name__ == "__main__":
    main()
