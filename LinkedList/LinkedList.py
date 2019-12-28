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
    
    def size(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        print('size of linked list : ' + str(count))
        
    def search(self,item):
        temp = self.head
        while(temp):
            if temp.data == item:
                print('found : ' + str(temp.data))
            temp = temp.next
        
llist = LinkedList() 
llist.push(1) 
llist.push(2) 
llist.push(3) 
llist.push(4) 

llist.printList() 
llist.size()
llist.search(4)
