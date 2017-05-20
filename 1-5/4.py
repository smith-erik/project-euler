# imports here

def main():
    basenum_length, largest = 3, 0
    maxnum = 10 ** basenum_length - 1
    maxprod = maxnum ** 2

    print("Maximum number is %d." % maxprod)
    for a in range(maxprod, 1, -1):
        for b in range(maxprod, a, -1):
            if isPalindrome(a * b) and a * b > largest:
                largest = a * b
    print("%d is the product of %d and %d." % (a * b, a, b))


def isPalindrome(x):
    if x < 10 or x % 10 == 0:
        return False
    x_str = str(x)
    for i in range(len(str(x)) // 2):
        if x_str[i] != x_str[-i - 1]:
            return False

if __name__ == "__main__":
    main()
