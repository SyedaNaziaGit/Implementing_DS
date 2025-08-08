''''
#list in python as a queue
wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)
print(wmt_stock_price_queue)#op -[135, 132.12, 131.1]
wmt_stock_price_queue.pop()
print(wmt_stock_price_queue)#op -[135, 132.12]
#list in python is dynamic array, if it exceeds its capacity it will allocate new area again with the previous data and hence it is expensive
#hence we use double ended queue- deque from the collections module in python for the implementation 
#queue is FIFO- first in first out Data structure
'''
#Queue class Implementation
from collections import deque
q= deque()
q.appendleft(1)
q.appendleft(10)
q.appendleft(100)
print(q)#op[100,10,1]
q.pop()#op -1
print(q)#op[100,10]

#class implementations
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) ==0
    def size(self):
        return len(self.buffer)
qq = Queue()
qq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
qq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
qq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
print(qq.size())#op- 3
qq.dequeue()
print(qq.is_empty())#op - False