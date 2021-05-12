#!/usr/bin/env python3

import sys


def cat(fname):
    try:
        with open (fname, 'r') as f:
            print("---", fname)
            for line in f:
                print(line, end="")
                    
    except ValueError:
        print("----value error", fname)
    except FileNotFoundError as e:
        print("----value error", e)       


def main():
    args = sys.argv[1:]
    for fname in args:
        cat(fname)

#############################################################################

if __name__ == "__main__":
    main()