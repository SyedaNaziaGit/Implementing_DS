class Node:
    def __init__(self,data = None,next=None):
        self.data = data    
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node
        
    def print_linkedlist(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head 
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr .next
        print(llstr)
        
    def inserting_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None) 
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data=data,next=None)
    
    def insert_values(self,data_list):
        self.head  = None
        for data in data_list:
            self.inserting_at_end(data)

    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    
    def remove_element_at_index(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Not a Valid Index")
        if index ==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next =itr.next.next
                break
            itr = itr.next 
            count+=1
    
    def insert_element_at_index(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data=data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                print(count)
                node =Node(data=data , next=itr.next)
                itr.next = node
                print(itr.next)
                break   
            itr = itr.next
            count +=1
            
    def insert_after_element(self,data_after,insert_data):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data = insert_data,next=self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data=insert_data,next=itr.next)
                break
            itr = itr.next
            
    def remove_by_element(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data ==  data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList()

    #ll.insert_at_begining(5)
    #ll.insert_at_begining(9)
    #ll.inserting_at_end(69)
    #ll.inserting_at_end(80)
    ll.insert_values(["b","ca","do","egg","fun"])
    ll.print_linkedlist()
    #ll.remove_element_at_index(2)
    #ll.remove_element_at_index(20)
    ll.print_linkedlist()
    ll.insert_element_at_index(index=0,data="hat")
    ll.print_linkedlist()
    ll.insert_element_at_index(index=2,data="ink")  
    ll.print_linkedlist()
    ll.insert_after_element("ca","jump")
    ll.print_linkedlist()
    ll.remove_by_element("do")
    ll.print_linkedlist()
    print("length of the linked list:",ll.get_length())