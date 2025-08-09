class Node:
    def __init__(self,data= None,next = None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(Node):
    def __init__(self):
        self.head = None
    def inserting_at_end(self,data):
        #insert new node at the end- append
        newnode = Node(data=data)
        if not self.head:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
        newnode.prev = last
        
    def inserting_at_beiginning(self,data):
        #inserting newnode at the start
        newnode = Node(data=data)
        if self.head:
            self.head.prev = newnode
            newnode.next = self.head
        self.head = newnode
        
    def remove_by_element(self,data):
        #deleting first element matching data
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next =curr.next
                else:
                    self.head = curr.next
                    
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr= curr.next
            
    def print_DLL_forward(self):
        dll =[]
        curr = self.head
        if not curr:
            print("Doubly Linked list is empty")
            return
        while curr:
            dll.append(curr.data)
            curr= curr.next
        print("Printing Doubly Linked List Forward:",dll)
    def print_DLL_backward(self):
        dll =[]
        curr = self.head
        if not curr:
            print("Doubly Linked List is empty")
            return
        while curr.next:
            curr = curr.next #traversing till end
        while curr:
            dll.append(curr.data)
            curr = curr.prev
        print("Printing Doubly Linked List Backward:",dll)

dll = DoublyLinkedList()
dll.inserting_at_end(10)
dll.inserting_at_end(2)
dll.inserting_at_end(3)
dll.inserting_at_end(4)
dll.inserting_at_end(5)
dll.inserting_at_beiginning(100)
dll.print_DLL_forward()#Printing Doubly Linked List Forward: [100, 10, 2, 3, 4, 5]
dll.remove_by_element(5)
dll.print_DLL_forward()#Printing Doubly Linked List Forward: [100, 10, 2, 3, 4]
dll.print_DLL_backward()#Printing Doubly Linked List Backward: [4, 3, 2, 10, 100]