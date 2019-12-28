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
            if(slow_p == fast_p):
                self.fistNodeOfLoop(slow_p)
                return 1
        return 0
        
    def createLoop(self):
        
        print('1st and last')
        print(self.head.next.next.next.next.data)
        print(self.head.next.data)
        self.head.next.next.next.next.next = self.head.next
        
    def fistNodeOfLoop(self,loop_node):
        
        p = self.head
        q = loop_node
        
        while( p != q ):
            p = p.next
            q = q.next
            
        print('First Node of the loop is : ' + str(p.data))
        
        
    
        
        
llist = LinkedList()

llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

llist.printList()
llist.createLoop()

if llist.detectLoop():
    print("Loop detected")
else:
    print("No Loop")

