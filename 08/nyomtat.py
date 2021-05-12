#!/usr/bin/env python3

from typing import List, Any


def printer(data: Any) -> List[int]:
    individual_pages = set()
    data = data.split(',')
    for e in data:
        page = e.split('-')
        individual_pages.update([page for page in range(int(page[0]),int(page[-1])+1)])
    return list(individual_pages)


def main() -> None:
    pages = input("Adja meg a nyomtatni kívánt oldalakat: ")
    print(printer(pages))

#############################################################################

if __name__ == "__main__":
    main()