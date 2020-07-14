class PriorityQueue:
    
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return ' '.join([str(i) for i in self.queue]) 
        
    def insert(self,data):
        self.queue.append(data)
        
    def delete(self):
        maxi = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[maxi]:
                maxi = i
        item = self.queue[maxi]
        self.queue.pop(maxi)
        print(item)
        
q = PriorityQueue()
q.insert(1)
q.insert(4)
q.insert(2)
q.insert(3)
q.insert(13)
print(q)

q.delete()
print(q)
