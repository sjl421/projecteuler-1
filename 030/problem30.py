#!/usr/bin/python2

def main():
    s = 0

    powers = dict((str(x), x**5) for x in range(10))

    for n in xrange(2, 6*(9**5)+1):
        if n == sum(powers[i] for i in str(n)):
            s += n
    return s

if __name__ == "__main__":
    print main()
