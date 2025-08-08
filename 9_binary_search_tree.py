#Binary Tree:
'''
Every Node has 2 child nodes
They follow order -all LHS nodes are less than parent node and RHS > parent node
elements are always unique
Binary Search Tree- can be used 
Search complexity is O(logn)
Inserting in BT the complexity is O(logn)
Two approaches - Traversal techniques:
Breadth first search, depth first search -Inorder traversal,preorder traversal, post order traversal
'''
#implementing Binary Search Tree- Inorder traversal
class  BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left =  None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            #add data to self subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    def in_order_traversal(self):
        ele =[]
        #in inordertraversal we  first visit left subtree and then base node and then right subtree
        #visiting left subtree
        if self.left:
            ele += self.left.in_order_traversal()
        #visit base node
        ele.append(self.data)
        #visiting right subtree
        if self.right:
            ele += self.right.in_order_traversal()
        return ele
    
    def search_ele(self,val):
        if self.data == val:
            return True
        if val < self.data:
            #val might b in left subtree
            if self.left:
                return self.left.search_ele(val)
            else:
                return False
        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search_ele(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
            else:
                return None
        elif val > self.data:
            if self.right:
                self.right.delete(val)
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
#helper method
def buildTree(elements):
    root = BinarySearchTree(elements[0])#adding first element in BST
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    num = [17,4,1,20,9,23,18,34]
    btree = buildTree(num)
    print(btree.in_order_traversal())#sorted list - removes duplicates and acts like a set
    #op-[1, 4, 9, 17, 18, 20, 23, 34]
    print(btree.search_ele(20))#True
    print(btree.search_ele(41))#False
    #we acihieve(logn) complexity 
    print("Before Delete:",btree.in_order_traversal())
    btree.delete(20)
    print("After deleteing ele :" ,btree.in_order_traversal())#op -[1, 4, 9, 17, 18, 23, 34]