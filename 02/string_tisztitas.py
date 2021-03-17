#!/usr/bin/env python3


def cl(s):
    clean = ''.join(s.strip().split()) 
    return clean


def main():    
    raw1 = """192.20.246.138:
    6666"""
    raw2 = """206.130.99.82:
    8080"""
    raw3 = """egy
    ketto
        harom"""
    print(raw1, raw2, raw3, sep="\n")
    print("---Clean strings:---")
    print(cl(raw1), cl(raw2), cl(raw3), sep="\n")


##############################################################################

if __name__ == "__main__":
    main()