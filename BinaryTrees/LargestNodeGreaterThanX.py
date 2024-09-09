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


def countNodesGreaterThanX(root, x) :
	#Your code goes here
    if root is None:
        return 0
    left = countNodesGreaterThanX(root.left,x)
    right = countNodesGreaterThanX(root.right,x)
    count = 0
    if root.data>x:
        count += 1
    return count + left + right

root = treeInput()
print(countNodesGreaterThanX(root,1))