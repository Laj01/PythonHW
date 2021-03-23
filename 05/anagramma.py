#!/usr/bin/env python3


def normalize(string):

    normalized_string = ("".join(string.split())).lower()
    return normalized_string
    

def is_anagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    return sorted(list1) == sorted(list2)    


def main():

    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    if is_anagram(normalize(string1), normalize(string2)):
        print("The two strings are anagrams.")
    else:
        print("The two strings are NOT anagrams.")
    
#############################################################################

if __name__ == "__main__":
    main()