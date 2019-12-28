
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
  
def mirror(root):
    mirrorUtil(root)
    
def mirrorUtil(root):
    if root == None:
        return
    else:
        mirrorUtil(root.left)
        mirrorUtil(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(70)) 

inorder(r)

mirror(r)

inorder(r)