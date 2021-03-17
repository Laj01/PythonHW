#!/usr/bin/env python3

# a "K → M, O → Q, E → G" megadásából következtetve a titkosított szöveg
# az angol ABC betűinek 2 pozícióval való eltolásával állt elő.
# Ez közismertebb nevén a Cézár titkosítás (Caesar cipher).
# Az alábbi script ezt a titkosítást próbálja reprodukálni.

MSG = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def decrypt(s):
    shift = 2
    decrypted = ""
    
    for c in MSG:
        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) + ord("A")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            decrypted = decrypted + new_character
        elif c.islower():
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            decrypted = decrypted + new_character
        elif c == "\n":
            decrypted = decrypted + "\n"
        elif c == " ":
            decrypted = decrypted + " "
        elif c == ":":
            decrypted = decrypted + ":"
        elif c == "!":
            decrypted = decrypted + "!"
        
    return decrypted


def main():
    print(MSG)
    print(decrypt(MSG))


##############################################################################

if __name__ == "__main__":
    main()