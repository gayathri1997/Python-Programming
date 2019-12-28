'''

Following is an algorithm to evaluate postfix expression
1. Create a stack to store operands
2. Scan the given expression and do the following for every scanned element
    2.1 if the element is a number then push it into the stack
    2.2. if the element is a operator then pop operands for the operator from stack.
Evaluate the operator and push the result  back to the stack

3. when the expression is ended then the number in the stack is the final result.

'''

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
        
    def evaluatePostFix(self,exp):
        
        for i in exp:
            
            if( i.isdigit() ):
                self.push(i)
            else:
                a = int(self.pop())
                b = int(self.pop())
                
                if i == '+':
                    self.push(a+b)
                elif i == '-':
                    self.push(a-b)
                elif i == '*':
                    self.push(a*b)
                elif i == '/':
                    self.push(a/b)
                    
        print(self.pop())
                    
        
exp = '12+34+*'
obj = stack()
obj.evaluatePostFix(exp)