#!/usr/bin/env python3


def main():
    sum_of_numbers = 0
    for number in range(1_000_000):
        if str(number) == str(number)[::-1]:
            binary = str(bin(number))[2:]
            if binary == binary[::-1]:
                sum_of_numbers += number
    print(sum_of_numbers)

#############################################################################

if __name__ == "__main__":
    main()