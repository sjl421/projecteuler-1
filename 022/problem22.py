#!/usr/bin/python2

import os

def main():
    datafile = os.path.join(os.path.dirname(__file__), "names.txt")
    names = open(datafile).read().split(",")

    names.sort()

    s = 0

    for i, name in enumerate(names):
        s += sum(ord(c) - 64 for c in name if c != '"') * (i+1)

    return s

if __name__ == "__main__":
    print main()
