#!/usr/bin/python3

from math import floor, sqrt, ceil

def slow(n0):
    maxprime = ceil(sqrt(n0))
    print("Ceil of square root of 600851475143 is %d." % maxprime)
    for i in range(maxprime - 1, 1, -1):
        if n0 % i == 0 and isPrimeSlow(i):
            print(str(i))
            return
    print("Reached end of loop.")


def isPrimeSlow(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def fasterLargest(n0):
    n, largest, counter = n0, 0, 2
    while counter * counter <= n:
        if n % counter == 0:
            n //= counter
            largest = counter
        else:
            counter += 1
    if n > largest:
        largest = n
    return largest


def fasterFactors(n0):
    factors = []
    n, largest, counter = n0, 0, 2
    while counter * counter <= n:
        if n % counter == 0:
            n //= counter
            largest = counter
            factors.append(counter)
        else:
            counter += 1
    if n != 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    #print(str(slow(600851475143)))
    #print(str(fasterLargest(600851475143)))
    factors = fasterFactors(600851475143)
    for i in factors:
        print(i, end=' ')
    print()