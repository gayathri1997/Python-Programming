class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def sortedArrayToBST(arr):
    
    if not arr:
        return None
        
    mid = int(len(arr) / 2)
    
    root = Node(arr[mid])
    
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    
    return root
    
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)
        
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
inorder(root)
