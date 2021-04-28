#!/usr/bin/env python3

import random
from typing import List, Any

def shuffled(list_of_elements: List[Any]) -> List[Any]:
    shuffled_list = random.sample(list_of_elements, len(list_of_elements))
    return shuffled_list


def main() -> None:
    original_list_numbers = [1, 2, 3, 4, 5]
    original_list_strings = ["egy", "kettő", "három", "négy", "öt"]
    print(f'Shuffled list: {shuffled(original_list_numbers)}')
    print(f'Original list: {original_list_numbers}')
    print(f'Shuffled list: {shuffled(original_list_strings)}')    
    print(f'Original list: {original_list_strings}')

#############################################################################

if __name__ == "__main__":
    main()