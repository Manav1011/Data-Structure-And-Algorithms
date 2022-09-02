from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def reverse_string(self,value):
        for i in value:
            self.container.append(i)
        for i in range(len(self.container)):
            print(self.container.pop())
            
    
s=Stack()
s.reverse_string("Manav shah")