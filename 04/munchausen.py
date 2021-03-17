#!/usr/bin/env python3


def is_munchausen(maximum):
    for i in range(maximum):
        number = i
        powered_number = 0
        for x in str(i):
            if int(x) == 0:
               continue
            powered_number += int(x) ** int(x)
        if number == powered_number:
            print(number)


def main():
    is_munchausen(10000)
#    is_munchausen(440000000)
#   A 440 milliós futásnál a gépem olyan sokáig dolgozott, 
#   hogy sose kaptam vissza a promptot.

#############################################################################

if __name__ == "__main__":
    main()