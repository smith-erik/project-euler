#!/usr/bin/python3

def findSmalletDivisibleSlow(startHere, belowThis):
    count = startHere
    while count < belowThis:
        for i in range(2,21):
            if count % i != 0:
                break
            elif i == 20:
                return count
        count += 20
    return None


def findSmalletDivisibleSlow2(startHere):
    i = startHere
    while (i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or i % 6 != 0 or i % 7 != 0 or \
        i % 8 != 0 or i % 9 != 0 or i % 10 != 0 or i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 !=0 or \
        i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0):
        i += 20
    return i

primes20 = [3, 5, 7, 11, 13, 17, 19]
start = 1
for i in primes20:
    start *= i
print(str(start))
x = findSmalletDivisibleSlow2(start)
print(str(x))
