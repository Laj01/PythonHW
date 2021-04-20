#!/usr/bin/env python3

from collections import deque


class Sor:
    
    def __init__(self):
        self.data = deque([])
        
    def ures(self):
        if len(self.data) == 0:
            return True
        else:
            return False
            
    def betesz(self, value):
        self.data.append(value)        
        
    def kivesz(self):
        if len(self.data) == 0:
            return None
        else:    
            return self.data.popleft()              
                
    def meret(self):
        return len(self.data)
        
    def __str__(self):
        return ' '.join(str(i) for i in self.data)


def main():
    s = Sor()
    print(s)
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # [1 4 5
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 5
    print(s)         # [1 4
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)

#############################################################################

if __name__ == "__main__":
    main()