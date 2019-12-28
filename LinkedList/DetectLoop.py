class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self,new_data):
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
            
    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("loop found")
                return
        print("No loop")
        
    def createLoop(self):
        self.head.next.next.next.next.next.next = self.head.next 
            
llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)


llist.printList()
llist.detectLoop()

llist.createLoop()
llist.detectLoop()
