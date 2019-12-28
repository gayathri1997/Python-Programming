class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

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
            
    def isPalindromeUtil(self,string):
        return (string == string[::-1])
        
    def isPalindrome(self):
        node = self.head
        temp = []
        while(node):
            temp.append(node.data)
            node = node.next
        string = "".join(temp)
        return self.isPalindromeUtil(string)
        
llist = LinkedList() 
llist.push('a') 
llist.push('b') 
llist.push('b') 
llist.push('a') 

llist.printList() 
llist.size()
llist.search(4)

print(llist.isPalindrome())