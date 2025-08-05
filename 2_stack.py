from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,value):
        self.container.append(value)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

st = Stack()

st.push(5)
print(st.is_empty())
print(st.pop())
print(st.is_empty())

st.push(111)
st.push(555)
st.push(777)
st.push(333)

print(st.peek())

print(st.pop())
