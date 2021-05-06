#!/usr/bin/env python3

def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except (KeyboardInterrupt, EOFError):
            print()
            break
        except (ValueError):
            print("Az adott értékkel nem végezhető matematikai művelet!")
            break
        except (ZeroDivisionError):
            print("Nullával való osztás, érvénytelen művelet!")
            break
#####

if __name__ == "__main__":
    main()