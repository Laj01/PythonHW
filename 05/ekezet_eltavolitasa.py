#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""

rovid = "aeiooouuuAEIOOOUUU"
hosszu = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"

d = {
    'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ö':'o', 'ő':'o',
    'ú':'u', 'ü':'u', 'ű':'u', 'Á':'A', 'É':'E', 'Í':'I',
    'Ó':'O', 'Ö':'O', 'Ő':'O', 'Ú':'U', 'Ü':'U', 'Ű':'U'
    }

def main():
    print("\n============Replace without dictionary============")
    for c in TEXT:
        pos = hosszu.find(c)
        if pos >= 0:
            print(rovid[pos], end = "")
        else:
            print(c, end = "")
    
    print("\n============Replace with dictionary===============")
    new_text = TEXT
    for k, v in d.items():
        new_text = new_text.replace(k, v)
    print(new_text)

#############################################################################

if __name__ == "__main__":
    main()