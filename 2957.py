# class BinarySearchTree():
#     def __init__(self):
#         self.bst = []
#         self.root = self.bst[0]
#         self.C = 0
#         self.left = None
#         self.right = None

#     def left(self, idx):
#         self.left = idx*2
#         return self.left

#     def right(self, idx):
#         self.right = idx*2 + 1
#         return self.right

#     def insert(self, X, idx):
#         self.C += 1
#         if X <= bst[idx]:
#             if self.left() == None:
#                 self.left = self.left()
#                 self.left = X
#             else:
#                 self.insert(X, self.left())
#         else:
#             if self.right() == None:
#                 self.right = self.right()
#                 self.right = X
#             else:
#                 self.insert(X,self.right())

# bst = BinarySearchTree()
# N=9
# Ns = [8,3,5,1,6,8,7,2,4]
# for X in Ns :
#     bst.insert(bst,X,N)
# print(bst.C)

#2
class BinarySearchTree:
    class Node:
        def __init__(self, value, key, left, right):
            self.key = key
            self.value = [value]
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.value_count = 0

    def insert(self, value, key):
        self.root = self.__insert(self.root, value, key)

    def __insert(self, node, value, key):
        self.value_count += 1
        if node == None:
            return self.Node(value,key,None,None)
        elif node.key > key:
            if node.left == None:
                new = Node(value,key,None,None)
                node.left = new
            else :
                self.__insert(node.left, value, key)
        elif node.key < key:
            if node.right == None:
                new = Node(value,key,None,None)
                node.right = new
            else:
                node.right = self.__insert(node.right, value, key)
        else:
            node.value = value


bst = BinarySearchTree()
values = [8,3,5,1,6,8,7,2,4]
i = 0
print(bst.value_count)
for x in values :
    bst.insert(x,i)
    print(bst.value_count)
