#!/usr/bin/env python3


class MyQueue:
    
    def __init__(self):
        self.data_1 = []
        self.data_2 = []
        
    def is_empty(self):
        if len(self.data_1) == 0 and len(self.data_2) == 0:
            return True
        else:
            return False
            
    def append(self, value):                
        self.data_1.append(value)        
        
    def popleft(self):
        while len(self.data_1) != 0:
                self.data_2.append(self.data_1[-1])
                self.data_1.pop()                
        if len(self.data_2) == 0:
            return None
        else:                
            return self.data_2.pop()            
            
    def size(self):
        return len(self.data_1)
        
    def __str__(self):
        while len(self.data_2) != 0:
                self.data_1.append(self.data_2[-1])
                self.data_2.pop()
                
        return ' '.join(str(i) for i in self.data_1)


def main():
    mq = MyQueue()
    print(mq)
    print(mq.is_empty())
    mq.append(1)
    mq.append(4)
    mq.append(5)
    mq.append(7)
    print(mq)
    print(mq.size())
    print(mq.is_empty())
    x = mq.popleft()
    print(x)
    x = mq.popleft()
    print(x)
    print(mq)
    mq.popleft()
    mq.popleft()
    x = mq.popleft()
    print(x)

#############################################################################

if __name__ == "__main__":
    main()