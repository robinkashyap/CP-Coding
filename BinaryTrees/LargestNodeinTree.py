class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = BinaryTree(rootdata)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def findMax(root):
    if root is None:
        return -1
    leftlargest = findMax(root.left)
    rightlargest = findMax(root.right)
    if leftlargest > rightlargest and leftlargest > root.data:
        return leftlargest
    elif rightlargest > leftlargest and rightlargest > leftlargest:
        return rightlargest
    else:
        return root.data
    # return max(root.data, leftlargest, rightlargest)

root = treeInput()
print(findMax(root))

