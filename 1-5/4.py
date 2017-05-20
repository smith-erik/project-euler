#!/usr/bin/python3

def main():
    basenum_length, largest = 3, 0
    maxnum = 10 ** basenum_length - 1
    x, y = 0, 0
    for a in range(maxnum, 1, -1):
        for b in range(a, 1, -1):
            if isPalindrome(a * b) and a * b > largest:
                largest = a * b
                x, y = a, b
    print("%d is the product of %d and %d." % (largest, x, y))


def isPalindrome(x):
    if x < 10 or x % 10 == 0:
        return False
    x_str = str(x)
    for i in range(len(str(x)) // 2):
        if x_str[i] != x_str[-i - 1]:
            return False
    return True

if __name__ == "__main__":
    main()
