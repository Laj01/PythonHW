#!/usr/bin/env python3

import sys


def diamond(n):
    if (n % 2 == 0) or (n <= 0):
        print("Error: not a valid number! ")
        sys.exit(-1)
    else:
        dia = []
        i = -1
        middle = (n // 2) + 1
        for e in range(middle):
            i += 2
            dia.append(((i) * "*").center(n))
            dia.append("\n")
        for e in range(middle, n):
            i -= 2
            dia.append(((i) * "*").center(n))
            dia.append("\n")
                
    dia = "".join(dia)    
    return dia  


def main():
    n = int(input("Please enter a positive odd number: "))
    print(diamond(n), end = "")


#############################################################################

if __name__ == "__main__":
    main()