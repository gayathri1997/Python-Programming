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
    return heightUtil(root)
    
def heightUtil(root):
    if root == None:
        return 0 
    
    leftheight = heightUtil(root.left)
    rightheight = heightUtil(root.right)
    
    return 1 + max(leftheight,rightheight)

def isBalanced(root):
    if root is None:
        return True
        
    lh = height(root.left)
    rh = height(root.right)
    
    if (abs(lh-rh) <=1 and isBalanced(root.left) is True and isBalanced(root.right) is True):
        return True
    return False
    
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r) 

print('Height of BST : ', height(r))

if isBalanced(r):
    print('Balanced')
else:
    print('Not Balanced')
