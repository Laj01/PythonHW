#!/usr/bin/env python3

import urllib.request


def main():
    response = urllib.request.urlopen("https://konnektor.org/")
    raw = response.read()
    #print(type(raw))
    #print(raw)
    
    html = raw.decode("utf-8")
    #print(type(html))
    print(html)
    

#############################################################################

if __name__ == "__main__":
    main()