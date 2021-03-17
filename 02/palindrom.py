#!/usr/bin/env python3

from collections import deque


def is_palindrome_trivial(s):
    return s == s[::-1]


def is_palindrome_iterate(s):
    word = deque(s)
    i = len(word)
    if len(word) <= 1:
        return True
    while i > 1:
        return word.popleft() == word.pop()
        i -= 2
        

def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])


def main():
    s = input("Please enter a string: ")
    print("Trivial palindom?", is_palindrome_trivial(s))
    print("Itarative palindom?", is_palindrome_iterate(s))
    print("Recursive palindom?", is_palindrome_recursive(s))

##############################################################################
if __name__ == "__main__":
    main()