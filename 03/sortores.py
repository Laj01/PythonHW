#!/usr/bin/env python3

import sys
import random as r

UPTO = 100


def main():
    counter = 0
    for i in range(UPTO):
        counter += 1
        print(r.randint(0, 9), end="")
        if counter == 10:
            print()
            counter = 0
    

#############################################################################

if __name__ == "__main__":
    main()