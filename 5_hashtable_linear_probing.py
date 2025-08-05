#Hash Table implementation using Linear probing
class HashTable:
    def __init__(self,size):
        self.size = size
        self.keys = [None for  i in range(size)]
        self.values = [None for i in range(size)]
    
    def get_hash(self,key):
        return hash(key)%self.size
    
    def __getitem__(self,key):
        index = self.get_hash(key)
        start_index = index
        
    def __setitem__(self):
        pass
    
    def __delitem__(self):
        pass