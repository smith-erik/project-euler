
def main():
    n0 = 600851475143
    n = n0
    while (n > 1):
        n = n - 1
        if n0 % n == 0 and isPrime(n):
            print(n)

def isPrime(x):
    for i in range(1, x):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()
