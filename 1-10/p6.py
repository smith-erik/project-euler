#!/usr/bin/python3
ceil = int(input("Please enter range ceiling (inclusive)\n"))
summ, sum_of_square = 0, 0
for n in range(1, ceil + 1):
    summ += n
    sum_of_square += n**2
square_of_sum = summ**2
diff = abs(sum_of_square - square_of_sum)
print("Sum of squares is %d and square of sum is %d."
                                        % (sum_of_square, square_of_sum))
print("Difference is %d." % diff)
