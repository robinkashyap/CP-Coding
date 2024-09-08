class PreOrder:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = PreOrder(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def preOrderPrint(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrderPrint(root.left)
    preOrderPrint(root.right)

root = treeInput()
preOrderPrint(root)