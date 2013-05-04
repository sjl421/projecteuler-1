#!/usr/bin/python2
# coding=utf-8

from math import sqrt

def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return wrapper

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True # we have already excluded 4, 6 and 8
    elif n % 3 == 0:
        return False
    else:
        limit = int(sqrt(n))
        k = 5
        while k <= limit: # check through all the numbers of the form 6k ± 1
            if n % k == 0:
                return False
            if n % (k+2) == 0:
                return False
            k += 6

        return True


# returns the prime numbers <= limit
# implements The Sieve of Eratosthenes
def prime_sieve(n):
    if n <= 1:
        return []

    bound = (n-1)/2 # last index of the sieve
    sieve = [True]*(bound+1)

    for i in xrange(1, int(sqrt(n)/2)+1):
        if sieve[i]: # 2*i+1 is a prime, mark multiples
            for j in xrange(2*i*(i+1), bound+1, 2*i+1):
                sieve[j] = False
    primes = [2]
    for i in xrange(1, bound+1):
        if sieve[i]:
            primes.append(2*i+1)
    return primes


# returns prime factors of an integer
def prime_factors(n):
    if n == 1:
        return [(1, 1)]

    primes = prime_sieve(int(sqrt(n)))
    prime_factors = []

    for p in primes:
        if p*p > n:
            break

        e = 0
        while n % p == 0:
            e += 1
            n //= p

        if e > 0:
            prime_factors.append((p, e))

    if n > 1:
        prime_factors.append((n, 1))

    return prime_factors

# http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
def sum_of_divisors(n):
    return reduce(lambda x,y: x * (y[0]**(y[1]+1)-1)/(y[0]-1), prime_factors(n), 1)

def sum_of_proper_divisors(n):
    return sum_of_divisors(n) - n


# returns the factors of an integer
def factor(n):
    a, r = 1, [1]
    while a * a < n:
        a += 1
        if n % a:
            continue
        b, f = 1, []
        while n % a == 0:
            n //= a
            b *= a
            f += [i * b for i in r]
        r += f

    if n > 1:
        r += [i * n for i in r]
    return r


# The function used for the problems 18 & 67
# the number of rows in the triangle and the number's index in the array are calculated using the formulas
# for the sum of the members of an arithmetic progression
def calc_max_total(nums):
    nrows = (-1 + sqrt(1+4*2*len(nums))) / 2

    @memoize
    def calc_total(rownum, idx):
        n = nums[ ((1 + (rownum-1))*(rownum-1))/2 + idx ]
        return n if rownum == nrows else n + max(calc_total(rownum+1, idx), calc_total(rownum+1, idx+1))

    return calc_total(1, 0)
