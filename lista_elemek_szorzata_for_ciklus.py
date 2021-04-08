#!/usr/bin/env python3


def product(numbers):
    prod = 1
    for n in numbers:
        prod *= n
    return prod


def main():
    numbers = [1, 2, 3, 4, 5]
    print("Szorzat:", product(numbers))
    
    
##############################################################################

if __name__ == "__main__":
    main()