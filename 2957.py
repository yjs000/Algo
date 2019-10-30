class BinarySearchTree():
    def __init__(self):
        self.bst = []
        self.root = self.bst[0]
        self.C = 0
        self.left = None
        self.right = None

    def left(self, idx):
        self.left = idx*2
        return self.left

    def right(self, idx):
        self.right = idx*2 + 1
        return self.right

    def insert(self, X, idx):
        self.C += 1
        if X <= bst[idx]:
            if self.left() == None:
                self.left = self.left()
                self.left = X
            else:
                self.insert(X, self.left())
        else:
            if self.right() == None:
                self.right = self.right()
                self.right = X
            else:
                self.insert(X,self.right())

bst = BinarySearchTree()
N=9
Ns = [8,3,5,1,6,8,7,2,4]
for X in Ns :
    bst.insert(bst,X,N)
print(bst.C)