class HashTable:
    def __init__(self):
        self.Max =10
        #self.arr = [None for i in range(self.Max)]
        #solving collsion problem using linear chaining
        self.arr = [ [] for i in range(self.Max)]
        
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return (hash % self.Max)
    
    def __getitem__(self,key):
        hash = self.get_hash(key= key)
        for ele in self.arr[hash]:
            if ele[0] == key:
                return ele[1]
    
    def __setitem__(self,key,value):
        hash = self.get_hash(key=key)
        found = False
        #check if key exists in Linkedlist
        for idx, ele in enumerate(self.arr[hash]):
            if len(ele) ==2 and ele[0] == key:
                self.arr[hash][idx] = (key,value)
                found = True
                break
        #if key not in linkedlist 
        if not found :
            self.arr[hash].append((key,value))
    
    def __delitem__(self,key):
        h = self.get_hash(key=key)
        for index , ele in enumerate(self.arr[h]):
            if ele[0] == key:
                del self.arr[h][index]