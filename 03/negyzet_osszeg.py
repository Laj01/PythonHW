#!/usr/bin/env python3


def squared_of_sum():
    result_1 = (sum(range(101))) ** 2
    return result_1


def sum_of_squared():
    result_2 = sum((i) ** 2 for i in range(101))        
    return result_2


def main():
    print(squared_of_sum() - sum_of_squared())


#############################################################################

if __name__ == "__main__":
    main()