#stack LIFO
"""
stack=[]

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)
"""
"""
stack=[]
def push(value):
    stack.append(value)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        print(stack.pop())
        print(stack)

while True:
    n=int(input("Enter the operation-1.Push 2.Pop 3.Quit"))
    if n==1:
        value=int(input())
        push(value)
    elif n==2:
        pop()
    elif n==3:
        break
    else:
        print("Enter correct option")
"""
"""
# using oops
class Stack:
    def __init__(self):
        self.__stack_list=[]
    def push(self,value):
        self.__stack_list.append(value)
        return self.__stack_list
    def pop(self):
        if not self.__stack_list:
            return "Stack is empty"
        else:
            print(self.__stack_list.pop())
            return self.__stack_list
class Adding_Stack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0
    def push(self,val):
        self.val=val
        self.__sum=self.__sum+self.val
        Stack.push(self,val)
    def pop(self):
        Stack.pop(self)
        self.__sum=self.__sum-self.val
        
    def getsum(self):
        return self.__sum

obj=Stack()
obj2=Adding_Stack()

for i in range(5):
    obj2.push(i)
print(obj2.getsum())
for j in range(5):
    obj2.pop()
    print(obj2.getsum())
"""
"""
#using collections
import collections
stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
"""
#using deque
import queue
stack=queue.LifoQueue()
stack.put(1)
stack.put(3)
print(stack)
stack.get()

