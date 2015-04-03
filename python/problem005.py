#!/usr/bin/python

"""Problem 5: Smallest multiple"""

from math import log, sqrt
from utils import prime_sieve


def main():
    n = 20

    primes = prime_sieve(n) # prime numbers <= N

    limit = sqrt(n)
    result = 1

    for p in primes:
        exponent = 1 if p > limit else int(log(n)/log(p))
        result *= p ** exponent

    return result

if __name__ == "__main__":
    print(main())