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


def numOfLeafNodes(root) :
	#Your code goes here
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    left = numOfLeafNodes(root.left)
    right = numOfLeafNodes(root.right)
    return left + right
    

root = treeInput()
print(numOfLeafNodes(root))