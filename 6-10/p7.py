#!/usr/bin/python3

def largestPrime(ceil):
    '''Returns the number and value of the largest prime <= ceil.'''
    if ceil > 1000000:
        print("Range of max 1000000 is supported.")
        return [78498, 999983]
    nums = [1] * (ceil + 1) # 1 for prime, 0 for non-prime
    nums[0:2] = 0, 0
    idx, p_count, p = 0, 0, 0
    while idx < len(nums) - 1:
        idx += 1
        if nums[idx] == 1:
            p_count += 1
            p = idx
            for i in range(p * 2, len(nums), p):
                nums[i] = 0
    return [p_count, p]


def nthPrime(nth):
    '''Returns the value the nth prime.'''
    if nth > 78498:
        print("Range of max 1000000 is supported.")
        return [78498, 999983]
    nums = [1] * 1000000 # 1 for prime, 0 for non-prime
    nums[0:2] = 0, 0
    idx, p_count, p = 0, 0, 0
    while p_count < nth:
        idx += 1
        if nums[idx] == 1:
            p_count += 1
            p = idx
            for i in range(p * 2, len(nums), p):
                nums[i] = 0
    return [p_count, p]


if __name__ == "__main__":
    n = int(input("Find prime number: "))
    ans = nthPrime(n)
    if n != ans[0]:
        print("Exiting.")
    else:
        print("Prime number %d is %d." % (n, ans[1]))
