class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key > data:             # self.key >= data --In case of duplicates, to add on LST
            if self.lchild:             # still leaf node not found to insert 
                self.lchild.insert(data) # recursion to reach leaf node
            else:                       # if it reaches to leaf node to insert
                self.lchild=BST(data)

        else:
            if self.rchild:             #self.key <= data --In case of duplicates, to add on RST
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key==data:
            print("Node is found!")

        if data < self.key:
            if self.lchild is None:
                print("Node is not present in the tree")
            else:
                self.lchild.search(data)
        if data > self.key:
            if self.rchild is None:
                print("Node is not present in the tree")
            else:
                self.rchild.search(data)

    def preorder(self):
        print(self.key,end=" ")

        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):

        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):

        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def delete(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.lchild:             # self.lchild is not None
                self.lchild= self.lchild.delete(data)
            else:
                print("Given Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Given Node is not present in the tree")

#root=BST(None)                         #--for empty BST case
root=BST(10)
keys=[5,20,15,200]

for i in keys:
    root.insert(i)

root.search(100)

root.preorder()
print("Preorder")

root.inorder()
print("Inorder")

root.postorder()
print("PostOrder")
