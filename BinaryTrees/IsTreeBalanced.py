class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data, end=" : ")
    if root.left != None:
        print("L",root.left.data, end = ", ")
    if root.right != None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)

def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right)) + 1

def isBalancedTree(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalancedTree(root.left)
    isRightBalanced = isBalancedTree(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False
root = treeInput()
# printTree(root)
print(isBalancedTree(root))