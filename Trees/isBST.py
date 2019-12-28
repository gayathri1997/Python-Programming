
int_min = -1000
int_max = 1000

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

def isBST(root):
    return isBSTUtil(root, int_min, int_max)
    
def isBSTUtil(root, mini, maxi):
    
    if root == None:
        return True

    if root.val < mini or root.val > maxi:
        return False
        
    return (isBSTUtil(root.left,mini,root.val-1) and isBSTUtil(root.right,root.val+1,maxi))

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r) 

print('IS BST : ', isBST(r))