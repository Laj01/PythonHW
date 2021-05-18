#!/usr/bin/env python3

import urllib.request
import json


def main():
    url = "https://jsonip.com/"
    fname = "my_ip.json"
    urllib.request.urlretrieve(url, fname)
    with open (fname) as f:
        d = json.load(f)
        
    print(d['ip'])

#############################################################################

if __name__ == "__main__":
    main()