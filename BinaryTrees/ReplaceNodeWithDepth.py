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

def changeToDepthTree(root,k=0):
    if root is None:
        return
    root.data = k
    changeToDepthTree(root.left,k+1)
    changeToDepthTree(root.right, k+1)

def inOrderPrint(root):
    if root is None:
        return
    inOrderPrint(root.left)
    print(root.data, end = " ")
    inOrderPrint(root.right)

root = treeInput()
changeToDepthTree(root)
inOrderPrint(root)