#!/usr/bin/env python3


def summarizeDigits(x):
    digits = 0
    while (x != 0):
        digits += x % 10
        x = x // 10
     
    return digits


def summarizeAll():
    n = 100
    result = 0
    for x in range(n + 1):
        result += summarizeDigits(x)
        
    return result


def main():

    print(summarizeAll())

#############################################################################

if __name__ == "__main__":
    main()