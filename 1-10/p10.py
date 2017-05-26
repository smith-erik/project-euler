#!/usr/bin/python3

def primesBelow(ceil):
    '''Returns all primes less than or equal to ceil.'''
    if ceil > 10000000:
        print("Range of max 10'000'000 is supported.")
        return None
    nums = [1] * (ceil + 1) # 1 for prime, 0 for non-prime
    nums[0:2] = 0, 0
    pList = []
    idx, p = 0, 0
    while idx < len(nums) - 1:
        idx += 1
        if nums[idx] == 1:
            p = idx
            pList.append(p)
            for i in range(p * 2, len(nums), p):
                nums[i] = 0
    return pList


if __name__ == "__main__":
    n = int(input("Enter ceiling (inclusive) to sum primes to: "))
    summ = sum(primesBelow(n))
    print("Sum of primes less than or equal to %d is %d." % (n, summ))
