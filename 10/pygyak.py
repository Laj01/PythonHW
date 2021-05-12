#!/usr/bin/env python3

import urllib.request

def get_page(url):
    response = urllib.request.urlopen("https://konnektor.org/")
    raw = response.read()    
    html = raw.decode("utf-8")
    return html
    
#############################################################################

if __name__ == "__main__":
    main()