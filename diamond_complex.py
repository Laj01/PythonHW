#!/usr/bin/env python3

import sys


def diamond(n):
    if (n % 2 == 0) or (n <= 0):
        print("Error: not a valid number! ")
        sys.exit(-1)
    else:
        for i in range(-n + 1, n + 1, 2):
            print(((n - abs(i)) * '*').center(n))      


def main():
    n = int(input("Please enter a positive odd number: "))
    diamond(n)


#############################################################################

if __name__ == "__main__":
    main()