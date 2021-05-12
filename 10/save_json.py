#!/usr/bin/env python3

import json

def read_string():
    s = """{
    "last": "Arnold",
    "first": "Swarzenegger",
    "age": 70,
    "sex": "M",
    "registered": true,
    "salary": 1000000
}"""

    d = json.loads(s)
    print(d)
    #return d
    
def main():
    read_string()
    
#############################################################################

if __name__ == "__main__":
    main()