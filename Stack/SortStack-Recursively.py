'''



'''


class stack:
    def __init__(self):
        self.top = -1
        self.array = []  
        
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        if self.top == -1:
            return -1
        else:
            return self.array[-1]
        
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return '$'

    def push(self,data):
        self.top += 1
        self.array.append(data)
    
    def sortStack(self):
        if not self.isEmpty():
            temp = self.pop()
            self.sortStack()
            self.sortedInsert(temp)
            
    def sortedInsert(self,element):
        if self.isEmpty() or element > self.peek():
            self.push(element)
        else:
            temp = self.pop()
            self.sortedInsert(element)
            self.push(temp)
    
    def printStack(self):
        print(self.array)
        
obj = stack()
obj.push(30)
obj.push(20)
obj.push(40)
obj.push(10)
obj.printStack()

obj.sortStack()
obj.printStack()
