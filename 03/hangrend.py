#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
FINAL = ["Egyik sem", "Magas", "Mély", "Vegyes"]


def hangrend(word):
    magas = 0
    mely = 0
    for c in word:
        if (c in MAGAS_MGHK):
            magas = 1
        elif (c in MELY_MGHK):
            mely = 2
            
    n = magas + mely
    return FINAL[n]
    

def main():
    word = input("Adjon meg egy szót: ")
    print("Hangrend: ", hangrend(word))


#############################################################################

if __name__ == "__main__":
    main()