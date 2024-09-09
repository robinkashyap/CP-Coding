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

def isNodePresent(root, x):
    if root is None:
        return False
    
    if root.data == x:
        return True

    left_result = isNodePresent(root.left, x)
    if left_result:
        return True

    right_result =  isNodePresent(root.right, x)
    if right_result:
        return True
    
    return False

root = treeInput()
print(isNodePresent(root,8))