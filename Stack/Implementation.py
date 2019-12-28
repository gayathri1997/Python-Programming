class Stack:
    
    def __init__(self):
        self.top = -1
        self.array = []  
        
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
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
        
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.peek())
print(s.isEmpty())    
print(s.top)
print(s.pop())

print(s.top)
print(s.peek())
print(s.pop())
