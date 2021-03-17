#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 3:
        print("HIBA! Nem adott meg megfelelő számú argumentumot!")
        print("Kérem adjon meg két számot argumentumként.")
    final = int(sys.argv[1]) + int(sys.argv[2])
    print("A két szám összege:", final)


if __name__ == "__main__":
    main()