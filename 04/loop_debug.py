#!/usr/bin/env python3

DEBUG_1 = "Ciklus kezdete: \n"
DEBUG_2 = "Ciklus vége."


def loop(number, debug = False):
    string = " ".join([str(i+1) for i in range(number)])    
    if debug == True:
        print(f"{DEBUG_1}{string}\n{DEBUG_2}")
    else:
        print(string)
        

def main():
    print("-" * 20 + "Printing WITHOUT debug:" + "-" * 20)
    loop(5)
    print("-" * 20 + "Printing WITH debug:" + "-" * 20)
    loop(5, debug = True)


#############################################################################

if __name__ == "__main__":
    main()