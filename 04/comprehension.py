#!/usr/bin/env python3


def ex_8():
    sentence = "python is an awesome language"
    characters = [word[0] for word in sentence.split()]
    print(sentence, "->", characters)
    
    
def ex_9():
    sentence = "The quick brown fox jumps over the lazy dog"
    tuples = [(word, len(word)) for word in sentence.split()]
    print(sentence, "->", tuples)

def ex_10():
    even = [i for i in range(0, 10, 2)]
    print(even)

def ex_11():
    numbers = [(n*n) for n in range(20) if (n*n) % 2 == 0]
    print(numbers)
    
def ex_12():
    numbers = [(n*n) for n in range(20) if (n*n) % 10 == 4]
    print(numbers)
    

def ex_13():
    alphabet = ["".join(chr(n) for n in range(65, 91))]
    print(alphabet)
    
    
def ex_14():
    words = [' apple ', ' banana ', ' kiwi']
    stripped = [w.strip() for w in words]
    print(stripped)
    
    
def ex_15():
    binary_list = [1, 0, 1, 1, 0, 1, 0, 0]
    binary_string = ["".join(str(binary_list[n-1]) for n in binary_list)]
    print(binary_string)

def main():
    print("-" * 30, "EXERCISE 08", "-" * 30)
    ex_8()
    print("-" * 30, "EXERCISE 09", "-" * 30)
    ex_9()
    print("-" * 30, "EXERCISE 10", "-" * 30)
    ex_10()
    print("-" * 30, "EXERCISE 11", "-" * 30)
    ex_11()
    print("-" * 30, "EXERCISE 12", "-" * 30)
    ex_12()
    print("-" * 30, "EXERCISE 13", "-" * 30)
    ex_13()
    print("-" * 30, "EXERCISE 14", "-" * 30)
    ex_14()
    print("-" * 30, "EXERCISE 15", "-" * 30)
    ex_15()


#############################################################################

if __name__ == "__main__":
    main()