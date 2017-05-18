print("Sum of even-valued terms less than four million in the Fibonacci sequence:")
a, b, sum = 1, 1, 0
while b < 4000000:
    sum += b if b % 2 == 0 else 0
    a, b = b, a + b
print(sum)
