#!/usr/bin/env python3


def summarize(number):
    """
    A fuggveny visszaadja azon 1000-nel kisebb szamok osszeget, 
    melyek 3-nak vagy 5-nek a tobbszorosei.
    
    Parameters
    ----------
    number: int
        Az intervallum, amin belul a szamokat vizsgaljuk.
        
    Returns
    --------- 
    list_of_numbers: int
        List comprehension altal eloalitott lista elemeinek osszege. 
        A lista 3 es 5 tobbszoroseit tartalmazza.
        
    """
    list_of_numbers = sum([n for n in range(number) if ((n % 3) == 0) or((n % 5) == 0)])
    
    return list_of_numbers


def main():
    print(summarize(1000))


#############################################################################

if __name__ == "__main__":
    main()