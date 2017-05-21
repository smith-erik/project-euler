#!/usr/bin/python3

"""Make sure all factors of numbers 1 to 20 are included and then multiply."""

from p3 import fasterFactors

primes20 = [2, 3, 5, 7, 11, 13, 17, 19]
factors = primes20
build_these = set(range(2, 21)) - set(primes20)
for n in build_these:
    n_factors = fasterFactors(n)
    for i in n_factors:
        diff = n_factors.count(i) - factors.count(i)
        if diff > 0:
            for times in range(diff):
                factors.append(i)
answer = 1
for factor in factors:
    answer *= factor
print(str(answer))
