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
            
    def sum(self):
        if  self.head == None:
            return 0
        sum = 0
        current = self.head
        while(current.next):
            if current.data > current.next.data:
                sum = sum + current.data
            current = current.next
        if current.data > self.head.data:
            sum = sum + current.data
            
        return sum
        
llist = LinkedList() 
llist.push(5) 
llist.push(2) 
llist.push(3) 
llist.push(4) 

llist.printList() 

print('Sum is : ' + str(llist.sum()))