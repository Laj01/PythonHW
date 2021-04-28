#!/usr/bin/env python3
    
import math
    

def is_prime(number: int) -> bool:
    if(number <= 1):
        return False
    if(number <= 3):
        return True
    if(number % 2 == 0 or number % 3 == 0):
        return False     
    for i in range(5,int(math.sqrt(number) + 1), 6):
        if(number % i == 0 or number % (i + 2) == 0):
            return False     
    return True

    
def is_prime_palidrom(number: int) -> int:
    prime = number - 1
    found = False
    if (number <= 1):
        return 2         
    while(not found):
        prime += 1 
        if(is_prime(prime) == True and str(prime) == str(prime)[::-1]):
            found = True
    return prime
  

def main() -> None:
    print(f'is_prime_palidrom(31) == {is_prime_palidrom(31)}')
    print(f'is_prime_palidrom(130) == {is_prime_palidrom(130)}')
    print(f'is_prime_palidrom(131) == {is_prime_palidrom(131)}')
    print(f'is_prime_palidrom(1977) == {is_prime_palidrom(1977)}')

#############################################################################

if __name__ == "__main__":
    main()