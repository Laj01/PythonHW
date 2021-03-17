#!/usr/bin/env python3

import sys


def converter(number):
    binary = []
    if number <= 0:
        print("Required decimal number MUST be positive!")
        sys.exit(-1)
        
    while number >= 1:
        binary.append(str(number % 2))
        number = number // 2
        
    binary = "".join(binary[::-1])
    return binary


def main():
    decimal = int(input("Enter a decimal number: "))
    print("Number converted to binary:", converter(decimal))


#############################################################################

if __name__ == "__main__":
    main()