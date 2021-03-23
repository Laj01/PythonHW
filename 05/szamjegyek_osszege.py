#!/usr/bin/env python3

NUMBER = 2


def main():

    power = int(input("Number 2 on the power of.... (add a number): "))
    sum_of_numbers = 0
    for i in str(NUMBER ** power):
        sum_of_numbers += int(i)    
    
    print(f"\n{NUMBER ** power}")
    print(f"\nSum of the numbers of {NUMBER} ^ {power}: {sum_of_numbers}")

#############################################################################

if __name__ == "__main__":
    main()