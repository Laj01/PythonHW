#!/usr/bin/env python3

def reverse(n):
    r = n[::-1]
    return r


def main():
    print("Kérem adjon megy egy egész számot: ")
    n = input()
    print(reverse(n))
    

if __name__ == "__main__":
    main()