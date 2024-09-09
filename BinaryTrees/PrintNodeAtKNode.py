class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = BinaryTreeNode(rootdata)
    left = treeInput()
    right = treeInput()
    root.left = left
    root.right = right
    return root

def printNodeAtK1(root,k):
    if root is None:
        return
    if k == 0:
        print(root.data,end =" ")
        return
    printNodeAtK1(root.left,k-1)
    printNodeAtK1(root.right, k-1)

def printNodeAtK2(root,k,d=0):
    if root is None:
        return
    if k == d:
        print(root.data, end =" ")
    printNodeAtK2(root.left,k,d+1)
    printNodeAtK2(root.right,k,d+1)

root = treeInput()
printNodeAtK1(root,2)
printNodeAtK2(root,2)