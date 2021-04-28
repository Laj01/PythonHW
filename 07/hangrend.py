#!/usr/bin/env python3

from enum import Enum, auto

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
    
    
class Hangrend(Enum):
    Semmilyen = auto()
    Magas = auto()
    Mély = auto()
    Vegyes = auto()
    
    
def hangrend(word):
    magas = 0
    mely = 0
    for c in word.lower():
        if (c in MAGAS_MGHK):
            magas = 1
        elif (c in MELY_MGHK):
            mely = 2
            
    n = magas + mely
    return Hangrend(n+1).name
    

def main():
    word = input("Adjon meg egy szót: ")
    print("Hangrend: ", hangrend(word))

#############################################################################

if __name__ == "__main__":
    main()