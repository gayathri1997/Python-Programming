class Node:
    def __init__(self,data):
        self.data = data
        self.right = self.left = None
        
class BinaryTree:
    
    root , head = None, None
    
    def BToDll(self, root: Node): 
        if root is None: 
            return
  
        self.BToDll(root.right) 
  
        root.right = self.head 
  
        if self.head is not None: 
            self.head.left = root 
  
        self.head = root 
  
        self.BToDll(root.left)

    def printList(self,temp):
        while(temp is not None):
            print(temp.data, end = ' ' )
            temp = temp.right
            
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(12)
tree.root.left.left = Node(25)
tree.root.left.right = Node(30)
tree.root.right = Node(15)
tree.root.right.left = Node(36)

tree.BToDll(tree.root) 
tree.printList(tree.head)   
