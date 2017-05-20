#!/usr/bin/python3

from math import floor, sqrt, ceil

def main():
    n0 = 600851475143
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

if __name__ == "__main__":
    main()
