class Node:
    
    def __init__(self,key):
        
        self.key = key
        self.left = None
        self.right = None
        
def lowestCommonAncestor(root, n1, n2):
    
    if root is None:
        return None
        
    if root.key == n1 or root.key == n2:
        return root
        
    left = lowestCommonAncestor(root.left, n1, n2)
    right = lowestCommonAncestor(root.right, n1, n2)
    
    if left is not None and right is not None:
        return root
        
    if left is None and right is None:
        return None
        
    return left if left is not None else right
    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 

print('lowestCommonAncestor of 4 and 6 is :', lowestCommonAncestor(root,4,5).key)
