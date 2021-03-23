#!/usr/bin/env python3


def median(list_of_numbers):

    list_of_numbers = sorted(list_of_numbers)
    
    if len(list_of_numbers) % 2 == 1:
        return list_of_numbers[len(list_of_numbers) // 2]
    else:
        middle1 = list_of_numbers[len(list_of_numbers) // 2]
        middle2 = list_of_numbers[len(list_of_numbers) // 2 - 1]
        return (middle1 + middle2) / 2


def main():

    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 1, 2, 5, 3]
    list3 = [1, 300, 2, 200, 1]
    list4 = [3, 6, 20, 99, 10, 15]
    print(f"Median for list1({list1}) == {median(list1)}")
    print(f"Median for list2({list2}) == {median(list2)}")
    print(f"Median for list3({list3}) == {median(list3)}")
    print(f"Median for list4({list4}) == {median(list4)}")

#############################################################################

if __name__ == "__main__":
    main()