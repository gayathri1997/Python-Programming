
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

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

def inorder(root): 
	if root: 
		inorder(root.left) 
		print(root.val) 
		inorder(root.right) 

def height(root):
    if root == None:
        return 0 
    
    leftheight = height(root.left)
    rightheight = height(root.right)
    
    return 1 + max(leftheight,rightheight)

def diameter(root):
    return diameterUtil(root)
    
def diameterUtil(root):
    
    if root == None:
        return 0
        
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldiameter = diameterUtil(root.left)
    rdiameter = diameterUtil(root.right)
    
    return max(lheight + rheight + 1, max(ldiameter,rdiameter))
    
    
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r) 

print('diameter of BST : ', diameter(r))