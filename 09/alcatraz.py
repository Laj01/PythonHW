#!/usr/bin/env python3

NO_OF_CELLS = 600


def invert(n):
    if n == 0:
        n = 1
    elif n == 1:
        n = 0
    return n


def open_cells(li):
    lock = 0
    while lock < NO_OF_CELLS:
        lock += 1
        for i in range(len(li)):
            if i % lock == 0:
                li[i - 1] = invert(li[i - 1])
                
    finally_open = [i + 1 for i, j in enumerate(li) if j == 1]
    return finally_open


def main():
    cells = [0] * NO_OF_CELLS
    free_murderers = open_cells(cells)
    print(f'Kinyitott cellák:\n{free_murderers}')
    print('\nCellák számának összefűzött stringje:')
    for murderer in free_murderers:
        print(murderer, end='')    

#############################################################################

if __name__ == "__main__":
    main()