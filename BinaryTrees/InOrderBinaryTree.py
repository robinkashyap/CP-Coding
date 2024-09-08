class InOrder:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = InOrder(rootdata)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def inOrderPrint(root):
    if root is None:
        return
    inOrderPrint(root.left)
    print(root.data, end =" ")
    inOrderPrint(root.right)

root = treeInput()
inOrderPrint(root)
