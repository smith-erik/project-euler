#!/usr/bin/python3

ceiling = int(input('Enter ceiling: '))
sum = 0
for i in range(1, ceiling + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("The sum of natural numbers less than %d that are multiples of 3 or 5 is:\n%d" % (ceiling, sum))
