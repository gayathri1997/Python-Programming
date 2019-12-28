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
            
    def deleteeven(self):
        while(self.head.data%2 == 0):
            self.head = self.head.next
        
        current = self.head
        while(current):
            if(current.next.data%2==0):
                prev = current
                current = current.next.next
                prev.next = current
            else:
                current = current.next
        
llist = LinkedList() 
llist.push(4)
llist.push(5) 
llist.push(2) 
llist.push(3) 
llist.push(4) 

llist.printList() 

print('for deleting even nodes : ')
llist.deleteeven() 
llist.printList() 
