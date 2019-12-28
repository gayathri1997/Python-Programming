class stack:
    
    def __init__(self):
        self.top = -1
        self.array = []
        self.output = []
        
    def isEmpty(self):
        return True if self.top == -1 else False
        
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
            
    def push(self,i):
        self.top += 1
        self.array.append(i)
        
    def stringReverse(self,exp):
        for i in exp:
            self.push(i)
            
        while not self.isEmpty():
            self.output.append(self.pop())
            
        print("".join(self.output))
        
exp = 'gayathri'
obj = stack()
obj.stringReverse(exp)