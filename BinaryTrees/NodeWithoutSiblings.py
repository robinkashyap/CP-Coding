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

def printNodesWithoutSibling(root) :
	# Your code goes here
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data, end=' ')
    if root.right is not None and root.left is None :
        print(root.right.data, end=' ')

    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)

root = treeInput()
printNodesWithoutSibling(root)