#!/usr/bin/python2

cache = {}
longest = 0
num = 0

def get_chain_length(n):
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = length = 1 + get_chain_length(n/2 if n % 2 == 0 else 3*n+1)
    return length

for i in xrange(2, 1000000):
    length = get_chain_length(i)

    if length > longest:
        longest = length
        num = i

print num