#!/usr/bin/env python3


def main():
    tmp_min = 0
    tmp_max = 0
    checksum = 0
    with open('day02.txt', 'r') as f:
        for line in f:
            line = line.strip("\n").split()
            tmp_list = [int(n) for n in line]
            tmp_min = min(tmp_list)
            tmp_max = max(tmp_list)
            checksum += tmp_max - tmp_min
    print(checksum)

#############################################################################

if __name__ == "__main__":
    main()