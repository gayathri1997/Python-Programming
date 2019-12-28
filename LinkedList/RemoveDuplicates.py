class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
            
    def removeDuplicates(self):
		p = self.head
		while(p):
			q = p
			while(q.next):
				if(p.data == q.next.data):
					q.next = q.next.next
				else:
					q = q.next
			p = p.next
			    
        
llist = LinkedList() 
llist.push(4)
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(4) 

llist.printList() 
print('After removing duplicates')
llist.removeDuplicates()
llist.printList()







