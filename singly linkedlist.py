class Node:
    def __init__(self,data):
        self.data= data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node2=Node(data)
        if self.head is None:
            self.head=new_node2
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node2
            
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        newnode=Node(data)
        newnode.ref=n.ref
        n.ref=newnode
        
    def add_before(self,data,x):
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        newnode=Node(data)
        newnode.ref=n.ref
        n.ref=newnode
               
    def delete_beg(self):
        n=self.head
        
        self.head=n.ref
        n.ref=None

    def delete_end(self):
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None


ll=LinkedList()

#creating 3 Nodes with data 10,20,30
ll.head=Node(10) 
second=Node(20)
third=Node(30)

#implementing references 2nd head to 1st ref and so on
ll.head.ref=second
second.ref=third

ll.print_ll()
"""
# ADD at beginning
ll.add_begin(100)
ll.print_ll()

# ADD at end
ll.add_end(200)
ll.print_ll()


ll.add_after(100,20)
ll.print_ll()

ll.add_before(100,20)
ll.print_ll()

ll.delete_beg()
ll.print_ll()
"""
ll.delete_end()
ll.print_ll()
