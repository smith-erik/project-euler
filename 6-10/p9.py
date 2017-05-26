#!/usr/bin/python3
from math import sqrt

def findTriplet_withSum(summ):
    '''Returns Pythagorean triplet with a + b + c = sum.'''
    c = 5
    while c < summ // 2:
        for a in range(1, c):
            # If a and c is known, then b = sqrt(c^2 - a^2) and
            # if b is an integer, then [a, b, c] is a valid triple
            b = sqrt(c**2 - a**2)
            if b.is_integer():
                if a + b + c == summ:
                    return [int(a), int(b), int(c)]
        c += 1
    return [0, 0, 0]


if __name__ == "__main__":
    ans = findTriplet_withSum(1000)
    print(ans, end = '')
    print(" - sum is %d." % (ans[0] + ans[1] + ans[2]))
    print("Product a * b * c is %d." % (ans[0] * ans[1] * ans[2]))
