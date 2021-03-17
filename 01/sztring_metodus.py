#!/usr/bin/env python3

# Az alábbi script a felhasználó által megadott szavak kezdőbetűit 
# alakítja nagybetűssé.

import sys


def main():
    s = input("Kérem adja meg a nevét: ").title()
    print("Az Ön neve: " + s)


if __name__ == "__main__":
    main()