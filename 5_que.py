 #Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

class Stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.stack3=[]
    
    def push1(self,data):
        self.stack1.append(data)
    
    def pop1(self):
        if len(self.stack1)==0:
            return "Empty stack1"
        return self.stack1.pop(len(self.stack1)-1)
    
    def push2(self,data):
        self.stack2.append(data)
    
    def pop2(self):
        if len(self.stack2)==0:
            return "Empty stack2"
        return self.stack2.pop(len(self.stack2)-1)
    
    def push3(self,data):
        self.stack3.append(data)
    
    def pop3(self):
        if len(self.stack3)==0:
            return "Empty stack3"
        return self.stack3.pop(len(self.stack3)-1)
    
    def peek(self):
        return self.stack3[len(self.stack3)-1]
        

obj=Stack()
obj.push1(3)
obj.push1(2)
obj.push1(1)
#  retrive from stack1 (3)
value=obj.pop1()
# push into stack2 3
obj.push3(value)


val=obj.pop1()

obj.push2(val)


value=obj.pop3()

obj.push2(value)

value=obj.pop1()
obj.push3(value)

value=obj.pop2()
obj.push1(value)

value=obj.pop2()
obj.push3(value)

value=obj.pop1()
obj.push3(value)


    
