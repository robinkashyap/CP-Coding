class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = BinaryTreeNode(rootdata)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def height(root) :
	#Your code goes here
    if root is None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.right)
    return max(leftheight,rightheight) + 1
    

root = treeInput()
print(height(root))