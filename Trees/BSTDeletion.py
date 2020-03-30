class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    
    if root:
        inorder(root.left)
        print(root.val, end= " ")
        inorder(root.right)
        
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
    
                
def deleteNode(root, val):
    
    if root is None:
        return None
        
    if root.val > val:
        root.left = deleteNode(root.left, val)
        
    elif root.val < val:
        root.right = deleteNode(root.right, val)
        
    else:
        
        #no child or one child
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp
            
        if root.right is None:
            temp = root.left 
            root = None
            return temp
            
        ## root has to childs
        
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
            
    return root
    
    
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

inorder(r) 
print('\nDelete Node 20 - node with no child')
deleteNode(r, 20)
inorder(r)

print('\nDelete Node 30 -  node with 1 child')
deleteNode(r, 30)
inorder(r)

print('\nDelete Node 70 -  node with 2 childs')
deleteNode(r, 70)
inorder(r)
