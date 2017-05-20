#!/usr/bin/python3

def findSmalletDivisibleSlow(maxLoops):
    count = 1
    while count < maxLoops:
        for i in range(2,21):
            if count % i != 0:
                break
            elif i == 20:
                return count
        count += 1
    return None

x = findSmalletDivisibleSlow(1000000)
print(str(x))
