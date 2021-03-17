#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    A fuggveny visszaadja azokat a karaktereket, amelyek egyarant
    szerepelnek az elso parameterben es az opcionális parameterben is.
    
    Parameters
    ----------
    text: str
        Az elso paramaterket megadott vizsgalni kivant string.
        
    chars: str
        Opcionalis paramater. Ezen karakterekkel lesz osszehasonlitva a text.
        
    Returns
    -------
    final: str
        A vegso stringet azok a karakterek alkotjak, amik egyarant szerepelnek a text-ben és a chars-ban is.
        
    """
    
    final = ""
    for c in text:
        if c in chars:
            final += c
    
    return final


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
    print(valid("MZ/X 1337"))



#############################################################################

if __name__ == "__main__":
    main()