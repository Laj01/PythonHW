#!/usr/bin/env python3


def product(numbers):
    prod = 1
    if len(numbers) == 0: 
        return prod
    else:
        i = 0
        while i < len(numbers):
            prod = prod * numbers[i]
            i += 1
        return prod


def main():
    numbers = [1, 2, 3, 4, 5]
    print("Szorzat:", product(numbers))
    
    
##############################################################################

if __name__ == "__main__":
    main()