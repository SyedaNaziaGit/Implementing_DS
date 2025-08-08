'''
#Weblinks vistied in list s
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')
print(s)
s.pop()
print(s)

#as list in python is a dynamic array- it will multiply list and extend memory allocation- for millions of data it is expensive
#hence we use deque from collections in python to implement stack
from collections import deque
stack = deque()
stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')
print(stack.pop())
'''
from collections import deque
class Stack:
    def __init__(self):
        self.container =deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

s = Stack()
s.push(10)
s.peek()
s.pop()
print(s.is_empty())
s.push("x")
s.push("y")
print(s.size())