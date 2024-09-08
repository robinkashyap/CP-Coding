class PostOrder:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = PostOrder(rootdata)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def postOrderPrint(root):
    if root is None:
        return
    postOrderPrint(root.left)
    postOrderPrint(root.right)
    print(root.data, end =" ")

root = treeInput()
postOrderPrint(root)
