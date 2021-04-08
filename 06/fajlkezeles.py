#!/usr/bin/env python3


def main():
    with open('string1.py', 'r') as f, open('string1_clean.py','w') as to:
        for line in f:            
            if line.strip().startswith('#') or line.strip().startswith("\n"):
                continue
            to.write(line)
        print("File: String1_clean.py created.")

#############################################################################

if __name__ == "__main__":
    main()