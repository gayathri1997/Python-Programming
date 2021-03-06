class Queue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self,data):
        
        while(len(self.s1) != 0):
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        self.s1.append(data)
        
        while(len(self.s2) != 0):
            self.s1.append(self.s2[-1])
            self.s2.pop()
        
        
    def dequeue(self):
        if len(self.s1) == 0:
            print('Q is empty')
        else:
            print(self.s1[-1])
            self.s1.pop()
            
q = Queue()

q.enqueue(1)
q.enqueue(3)
q.enqueue(5)

q.dequeue()
q.dequeue()
q.dequeue()

q.dequeue()
