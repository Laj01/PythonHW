#!/usr/bin/env python3

import json
from pprint import pprint


def main():
    fname = "person.json"
    with open (fname) as f:
        d = json.load(f)
    print(type(d))
    pprint(d, indent=2)
    print(d['salary'])
    
#############################################################################

if __name__ == "__main__":
    main()