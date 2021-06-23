class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head==None:
            print("linked list is empty")

        else:
            n=self.head
            while n is not None:
                print(n,"|",n.pref,"|",n.data,"|",n.nref)
                n=n.nref

    def print_llrev(self):
        if self.head==None:
            print("linked list is empty")

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref
    def insert_empty(self,data):
        if self.head is None:
            node0=Node(data)
            self.head=node0
        else:
            print("Linked List is not Empty")

    def add_beg(self,data):
        node1=Node(data)
        if self.head is None:           #To check linked list is empty or not
            self.head=node1
        else:
            node1.nref=self.head
            self.head.pref=node1
            self.head=node1

    def add_end(self,data):
        node2=Node(data)
        if self.head is None:           #To check linked list is empty or not
            self.head=node2
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=node2
            node2.pref=n

    def add_after(self,data,x):
        if self.head is None:
            print("Linked List is empty")

        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:          #To check if the node data is not present in Linked list
                print("Given Node is not present in DLL")
                
            node3=Node(data)
            node3.nref=n.nref
            node3.pref=n
            if n.nref is not None:  #To check the given Node x is not the last Node
                n.nref.pref=node3
            n.nref=node3

    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")

        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            if n is None:
                print("Given Node is not present in DLL")

            else:
                node4=Node(data)
                node4.nref=n
                node4.pref=n.pref
                if n.pref is not None:  #To check the given Node is the 1st Node
                    n.pref.nref=node4
                n.pref=node4

    def delete_beg(self):
        if self.head is None:
            print("Linked List is empty can't delete")
            return
        if self.head.nref is None:
            print("Doubly linked List has only one node ,after deleting Linked list becomes becomes empty")
            self.head=None
        else:
            self.head=self.head.nref
            self.head.pref= None

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty can't delete")
            return
        if self.head.nref is None:
            print("Doubly linked List has only one node ,after deleting Linked list becomes becomes empty")
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None

    def delete_byvalue(self,x):                        #x is node to delete
        if self.head is None:
            print("Linked List is empty can't delete")
            return
        if self.head.nref is None:                  #only one node
            if x==self.head.data:
                self.head=None
            else:
                print(x," is not present in doubly linked list")
        if self.head.data==x:                       #To check the data is in first node
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print(x," is not present in Linked List")
            
l=LinkedList()   # Object Creation

l.head=Node(10)
second=Node(20)
third=Node(30)

l.head.nref=second
second.pref=l.head
second.nref=third
third.pref=second

l.print_ll()
l.print_llrev()
"""
l.add_beg(0)

l.add_end(40)

l.add_after(25,20)

l.add_before(15,20)

l.delete_beg()

l.delete_end()
"""
l.delete_byvalue(10)
l.print_ll()


