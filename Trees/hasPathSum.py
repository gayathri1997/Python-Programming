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
		print(root.val, end=" ") 
		inorder(root.right) 

def hasPathSum(node, s): 
	
	# Return true if we run out of tree and s = 0 
	if node is None: 
		return (s == 0) 

	else: 
		ans = 0
		
		# Otherwise check both subtrees 
		subSum = s - node.val 
		
		# If we reach a leaf node and sum becomes 0, then 
		# return True 
		if(subSum == 0 and node.left == None and node.right == None): 
			return True

		if node.left is not None: 
			ans = ans or hasPathSum(node.left, subSum) 
		if node.right is not None: 
			ans = ans or hasPathSum(node.right, subSum) 

		return ans 
		
		
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

inorder(r) 

print(hasPathSum(r,100))
