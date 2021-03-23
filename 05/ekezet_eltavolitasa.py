#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""

rovid = "aeiooouuuAEIOOOUUU"
hosszu = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"


def main():
    for c in TEXT:
        pos = hosszu.find(c)
        if pos >= 0:
            print(rovid[pos], end = "")
        else:
            print(c, end = "")

#############################################################################

if __name__ == "__main__":
    main()