#!/usr/bin/env python3


def main():
    characters = ["aa", "", "aa", "a"]
    number = int("".join([str(len(c)) for c in characters]))
    print(number)


#############################################################################

if __name__ == "__main__":
    main()