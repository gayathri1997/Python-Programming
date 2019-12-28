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
            
    def reverse(self):
        prev = None
        current = self.head
        next = None
        
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        self.head = prev
			    
        
llist = LinkedList() 
llist.push(1)
llist.push(2) 
llist.push(3) 
llist.push(4) 
llist.push(5) 

llist.printList() 
print('Reversed LinkedList')
llist.reverse()
llist.printList()







