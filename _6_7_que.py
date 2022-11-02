#6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression and 
# Q7. Write a program to convert prefix expression to infix express

"""
Infix   :-  a+b
Postfix :-  ab+
Prefix  :-  +ab
"""

class Stack :
    def __init__(self):
        self.stack = []


    def push(self,value):
        self.stack.append(value)
        print("Successfully Added ")

    def pop(self):
        if len(self.stack)==0:
            print("Stack is empty !!")
            return
        value=self.stack.pop()
        return value
    
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty !!")
            return
        return self.stack[len(self.stack)-1]
    
    def postfix_to_prefix(self,exp):
        str=""
        for i in range(len(exp)):
            
            if i==len(exp)-1:          
                while len(self.stack) != 0:
                        value1=self.pop()
                        value2=self.pop()
                        print("yes")
                        str=str+exp[i]+value2+value1
                        return str
        
            elif exp[i].isalpha():
                 self.push(exp[i])
                
            elif exp[i]=='/' or exp[i]=='+' or  exp[i]=='*' or exp[i]=='-':
                 if len(self.stack)!=0:
                    value1=self.pop()
                    value2=self.pop()
                    str=str+exp[i]+value2+value1
                    self.push(str)
                    str=""
    
            
            
    def  prefix_to_infix(self,exp): 
        exp=exp[::-1]
        str=""
        for i in range(len(exp)):
            
            if i==len(exp)-1:          
                while len(self.stack) != 0:
                        value1=self.pop()
                        value2=self.pop()
                        str=str+value1+exp[i]+value2
                        return str
        
            elif exp[i].isalpha():
                 self.push(exp[i])
                
            elif exp[i]=='/' or exp[i]=='+' or  exp[i]=='*' or exp[i]=='-':
                 if len(self.stack)!=0:
                    value1=self.pop()
                    value2=self.pop()
                    str=str+value1+exp[i]+value2
                    self.push(str)
                    str=""  

obj=Stack()
# POSTFIX TO PREFIX 

result=obj.postfix_to_prefix("ABC/-AK/L-*")
print("Prefix expression is =",result)

# PREFIX TO INFIX
print(obj.prefix_to_infix("+-*AB/CDE"))

