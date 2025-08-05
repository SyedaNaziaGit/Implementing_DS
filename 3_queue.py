from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self,value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
aq = Queue()
aq.enqueue({'company':'Walmart','timestamp':'1 july 11.01','price':131.10})
aq.enqueue({'company':'Walmart','timestamp':'1 july 11.10','price':132.19})
aq.enqueue({'company':'Walmart','timestamp':'1 july 11.21','price':135.12})    

print(aq.buffer)
print(aq.size())
print(aq.is_empty())
print("------------")
print(aq.dequeue())